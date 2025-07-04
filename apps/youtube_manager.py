import json
from json import loads,dumps

"""
In this is app we have
🔘 We add youtube name with youtube link and we have to decide how many minutes you want to learn it.
🔘 And all save into the file
"""

PATH = "data/youtube.json"


def load_data():
    try:
        with open(PATH,"r") as file:
            file_data = json.load(file)
            return file_data
    except (FileNotFoundError, FileExistsError):
        return []

def check_valid_index(operation):
        def decorator(func):
            def wrapper(self):
                self.get_all_data()

                if len(self.video_data) <= 0:
                    return

                video_index = input(f"Choose the video that you want to {operation}:: ")

                if video_index.isdigit():
                    video_index = int(video_index) - 1

                    if len(self.video_data) > video_index >= 0:
                        result = func(self,video_index)
                        print(f"Video is {operation} successfully")
                        self.add_data()
                        return result
                    else:
                        print("\nOut of range\n")
                else:
                    print("\nInvalid Choice\n")
            return wrapper
        return decorator


class DatabaseManager:
    def __init__(self):
        self.video_data = load_data()

    def add_data(self):
        try:
            with open(PATH, "w") as file:
                file.write(dumps(self.video_data,indent=4))
        except Exception as e:
            print(f"Error:: {e}")

    def insert_data(self):
        video_name = input("Enter video name:: ")
        time = input("Enter video duration:: ")

        if video_name and time:
            self.video_data.append({"video_name":video_name,"time":time})
            self.add_data()
        else:
            raise ValueError("Video name and video duration are required")

    @check_valid_index("delete")
    def delete_data(self,video_index):
        self.video_data.pop(video_index)
        self.add_data()

    @check_valid_index("update")
    def update_data(self,video_index):
        print("\nChoose the option what you want to update\n")
        print("1. Update the video name")
        print("2. Update the video duration")
        print("3. Update both video name and duration")
        choice = input("Enter you choice:: ")

        match choice:
            case '1':
                video_name = input("Enter new video name:: ")

                if video_name is not None:
                    self.video_data[video_index] = {**self.video_data[video_index],"video_name":video_name}
                else:
                    print("Video name is required")
            case '2':
                time = input("Enter new video duration:: ")

                if time is not None:
                    self.video_data[video_index] = {**self.video_data[video_index], "time": time}
                else:
                    print("Video duration is required")
            case '3':
                video_name = input("Enter new video name:: ")
                time = input("Enter video duration:: ")

                if all([video_name,time]):
                    self.video_data[video_index] = {"video_name":video_name, "time": time}
                else:
                    print("Video name and video duration are required")
            case _:
                print("Invalid choice try again")

    def get_all_data(self):
        if len(self.video_data) > 0:
            print(f"Sr No.    |  Name   |  Duration |")
            for index, data in enumerate(self.video_data,start=1):
                print(f"{index}.   |  {data['video_name']} | {data['time']} ")
        else:
            print("\nNO VIDEO FOUND 404\n")

def main():
    db_manager = DatabaseManager()
    while True:
        print("\n--------------- YOUTUBE MANAGER | CHOOSE AN OPTIONS -------------------\n")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")

        choice = input("Enter your choice:: ")

        match choice:
            case '1':
                db_manager.get_all_data()
            case '2':
                db_manager.insert_data()
            case '3':
                db_manager.update_data()
            case '4':
                db_manager.delete_data()
            case '5':
                break
            case _:
                print("Invalid choice please try again!")


if __name__ == "__main__":
    main()
