"""
SQLITE      -->     sqlite:///relative/path/to/database.db
POSTGRES    -->     postgresql://[user[:password]@][host][:port][/dbname][?param1=value1&...]
"""

from sqlmodel import Session, SQLModel, col, create_engine, or_, select

from .schema.hero import Hero, User  # noqa: I001

# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"

postgres_url = "postgresql://postgres:abdul@localhost:5432"

engine = create_engine(postgres_url, echo=True)

# 🟡 Drop everything before creating any database tables
# SQLModel.metadata.drop_all(engine)

# 🟡 It's use to create all the tables, and it must run after the code "create tables"
SQLModel.metadata.create_all(engine)


# 👉 This is how we create table using SQLModel
def create_db_and_tables():
    with Session(engine) as session:
        # 🟡 Let's add all the users into the database first
        user_1 = User(first_name="John", last_name="Doe", age=21)
        user_2 = User(first_name="Charlie", last_name="Jacob", age=25)
        user_3 = User(first_name="Abraham", last_name="Lincon", age=50)

        session.add(user_1)
        session.add(user_2)
        session.add(user_3)
        session.commit()

        # 🟡 Let's add all the heroes into the database with users as well
        hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson", user_id=user_1.id)
        hero_2 = Hero(
            name="Spider-Boy", secret_name="Pedro Parqueador", user_id=user_1.id
        )
        hero_3 = Hero(
            name="Rusty-Man", secret_name="Tommy Sharp", age=48, user_id=user_1.id
        )
        hero_4 = Hero(
            name="Tarantula", secret_name="Natalia Roman-on", age=32, user_id=user_2.id
        )
        hero_5 = Hero(
            name="Black Lion", secret_name="Trevor Challa", age=35, user_id=user_1.id
        )
        hero_6 = Hero(
            name="Dr. Weird", secret_name="Steve Weird", age=36, user_id=user_3.id
        )
        hero_7 = Hero(
            name="Captain North America",
            secret_name="Esteban Rogelios",
            age=93,
        )

        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        session.add(hero_4)
        session.add(hero_5)
        session.add(hero_6)
        session.add(hero_7)

        session.commit()

        session.refresh(hero_1)
        session.refresh(hero_2)
        session.refresh(hero_3)
        session.refresh(hero_4)
        session.refresh(hero_5)
        session.refresh(hero_6)
        session.refresh(hero_7)

        print("Hero 1 is created: ", hero_1)
        print("Hero 2 is created: ", hero_2)
        print("Hero 3 is created: ", hero_3)
        print("Hero 4 is created: ", hero_4)
        print("Hero 5 is created: ", hero_5)
        print("Hero 6 is created: ", hero_6)
        print("Hero 7 is created: ", hero_7)


# 👉 This is how we select data from the table
def select_heros():
    # 🟡 For Selecting the "Hero" from the database, we need to pass the model directly to select
    #    function.
    # 🟡 It will automatically know where i need to select, it's just a query for running that
    #    query it needs "database engine" for that we need to use "session" that uses to query from
    #    the database.
    # 🟡 The result it provides after running the ".exec" is an """Iterable Object""" and we can
    #     iterate using "for" loop.
    # 🟡 But for getting full result instead of an """Iterable Object""" we need to use
    #    "result.all()" similar to "result.all()" we also have "result.first()" for getting the
    #    first result.
    # 🟡 There might be a case where we just need to have only single row for that case we use
    #     ".one()" in this case more than one row exists than it don't return anything
    # 🟡 We can use "offset()" and "limit()" for pagination
    with Session(engine) as session:
        # result = session.exec(select(Hero.name, Hero.age)) 👉 For Selecting particular column from the table
        result = session.exec(select(Hero))

        # Printing result as list of Hero
        print("Result is: ", result.all())

        # Looping to each item of the result
        for hero in result:
            print("Hero is: ", hero)


# 👉 This is how we filter the data from the table
def filter_heros():
    # 🟡 For filtering something we need to use ".where()" and in the return it again return ".where()"
    #    which is use to write multiple ".where" that become "AND" like "name = 'Deapond' and age >= 45'
    # 🟡 For having "OR" operation between two condition we need to use "or_" function for all pass
    #    all the condition required
    # 🟡 For comparison in sql model we can simply use, ">=", "<=", "==", "!=" and "in_"
    #    ".where(col(Hero.name).in_(['Deadpond', 'Ratman']))"
    # 🟡 We use "col()" method so that the editor simply understand what we are doing and it simply
    #    infer it.
    with Session(engine) as session:
        result = session.exec(
            select(Hero)
            .where(col(Hero.name).in_(["Deadpond", "Rusty-Man", "Black Lion"]))
            .where(col(Hero.age).is_not(None))
            .where(or_(col(Hero.age) >= 35, col(Hero.age) <= 100))
        ).all()
        print("Filter Result is: ", [res.model_dump() for res in result])


# 👉 This is how we handle update using SQLModel
def update_date():
    with Session(engine) as session:
        # 🟡 To update first we need to fetch the data and than directly update to the hero object
        #     after that we just commit it
        hero = session.exec(select(Hero).where(Hero.name == "Spider-Boy")).one()
        print("Before Update: ", hero.model_dump(), end="\n\n")

        hero.age = 22

        # 🟡 After adding this hero SQLModel will simply update it
        session.add(hero)
        session.commit()

        # 🟡 After updating ("committing") if you want to get the data that begin updated you need to
        #    refresh it.
        session.refresh(hero)

        print("After Updating: ", hero.model_dump())


# 👉 This is how we delete the data using SQLModel
def delete_data():
    # 🟡 To delete first we need to fetch the data and than using "session.delete(hero)" we just delete
    #     it and than commit it.
    with Session(engine) as session:
        hero = session.exec(select(Hero).where(Hero.name == "Spider-Boy")).one()
        print("Before Deleting it: ", hero.model_dump(), end="\n\n")

        session.delete(hero)
        session.commit()


# 👉 This is how we connect two tables using SQLModel
def connect_tables():
    with Session(engine) as session:
        # 🟡 Simple query for connecting two tables using ".join()" method
        # 🟡 "DOSE 1": When joining a table it make imaginary table at right side and by default joins
        #               in SQL are "right-join" mean only data will show that have
        # 🟡 "DOSE 2": In "left-join" it includes everything even they don't have any right matching
        #               row, it just give null to each field
        heroes = session.exec(select(Hero, User).join(User)).all()
        print(
            "Heroes are: ",
            [
                {**(hero.model_dump(exclude={"user_id"})), "user": user.model_dump()}
                for hero, user in heroes
            ],
            end="\n\n",
        )


# 🟡 Let's how """Relationship""" is working:
def auto_connect():
    with Session(engine) as session:
        hero = session.exec(select(Hero)).first()
        print(
            "Hero are: ",
            hero.model_dump(include={"secret_name", "name", "age", "user"})
            if hero
            else None,
        )


if __name__ == "__main__":
    # create_db_and_tables()
    # select_heros()
    # filter_heros()
    # update_date()
    # delete_data()
    # connect_tables()
    auto_connect()
