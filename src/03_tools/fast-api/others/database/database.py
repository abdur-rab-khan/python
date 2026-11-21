"""
SQLITE      -->     sqlite:///relative/path/to/database.db
POSTGRES    -->     postgresql://[user[:password]@][host][:port][/dbname][?param1=value1&...]
"""

from sqlmodel import Session, SQLModel, col, create_engine, or_, select

from .schema.hero import Hero  # noqa: I001

# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"

postgres_url = "postgresql://postgres:abdul@localhost:5432"

engine = create_engine(postgres_url, echo=True)

# It's use to create all the tables, and it must run after the code "create tables"
SQLModel.metadata.create_all(engine)


# 👉 This is how we create table using SQLModel
def create_db_and_tables():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson", age=48)
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    with Session(engine) as session:
        session.add(hero_1)
        # session.add(hero_2)
        # session.add(hero_3)
        session.commit()


# 👉 This is how we select data from the table
def select_heros():
    # 🟡 For Selecting the "Hero" from the database, we need to pass the model directly to select function.
    # 🟡 It will automatically know where i need to select, it's just a query for running that query it needs "database engine" for that we need to use "session" that uses to query from the database.
    # 🟡 The result it provides after running the ".exec" is an """Iterable Object""" and we can iterate using "for" loop.
    # 🟡 But for getting full result instead of an """Iterable Object""" we need to use "result.all()"
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
    with Session(engine) as session:
        result = session.exec(
            select(Hero)
            .where(Hero.name == "Deadpond")
            .where(col(Hero.age).is_not(None))
            .where(or_(col(Hero.age) >= 45, col(Hero.age) <= 100))
        ).all()
        print("Filter Result is: ", [res.model_dump() for res in result])


if __name__ == "__main__":
    # create_db_and_tables()
    # select_heros()
    filter_heros()
