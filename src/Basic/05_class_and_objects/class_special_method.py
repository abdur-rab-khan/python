from app import main


class DB:
    def __init__(self, db_name):
        self.db_name = db_name
        print(f"Database {self.db_name} initialized.")

    def __enter__(self):
        print(f"Connecting to database {self.db_name}...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Disconnecting from database {self.db_name}...")
        if exc_type:
            print(f"An error occurred: {exc_value}")
        return True


if __name__ == "__main__":
    with DB("my_database") as db:
        main(db)
