class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def get_person_details(self):
        return f"Name:: {self._name} and Age:: {self._age}"

    @property
    def name(self):
        raise ValueError("You can't access it.")

    @name.setter
    def name(self,value):
        if isinstance(value,str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")


person1 = Person("Abdur Rab Khan",12)

person1.name = "Babu Bhai"

print(person1.get_person_details())