import ipdb

class Human:

    species = "Homo sapiens"

    def __init__(self, age):
        self.age = age

    def get_age(self):
        print("Retrieving age.")
        return self._age

    def set_age(self, age):
        if (type(age) in (int, float)) and (0 <= age <= 120):
            print(f"Setting age to { age }.")
            self._age = age

        else:
            print("Age must be a number between 0 and 120.")

    age = property(get_age, set_age)

#guido = Human("Guido")
guido = Human(age= 67)

guido.species
guido.name

#changing species and name using dot notation
guido.name = "Guido van Rossum"
guido.species = "Python programmer"

#adding new attributes using dot notation
guido.nationality = "Dutch"
guido.nationality

#another way get the attribute:
guido.name
getattr(guido, "name")

#another way to set an attribute:
guido.nationality = "Dutch"
setattr(guido, "nationality", "Dutch")

ipdb.set_trace()