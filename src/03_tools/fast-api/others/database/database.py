from .schema.hero import Hero  # noqa: I001
from sqlmodel import SQLModel, Session, create_engine, select

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

# It's use to create all the tables, and it must run after the code "create tables"
SQLModel.metadata.create_all(engine)


# 👉 This is how we create table using SQLModel
def create_db_and_tables():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        session.commit()


# 👉 This is how we select data from the table
def select_heros():
    with Session(engine) as session:
        result = session.exec(select(Hero))

        # Printing result as list of Hero
        print("Result is: ", result.all())

        # Looping to each item of the result
        for hero in result:
            print("Hero is: ", hero)


# 👉 This is how we filter the data from the table
def filter_heros():
    pass


if __name__ == "__main__":
    create_db_and_tables()
    select_heros()
    filter_heros()
