from Birthday import Birthday



class Person:

    def __init__(self, first_name, last_name):
        """A person is defined by a first and last name, a birthday in the 
        form (month, day), and a city they live in. Additional fields may 
        be added here later. A new object requires only a first and last 
        name to instatiate. The remaining fields can be set later using 
        the corresponding mutator methods."""
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = None
        self.city = None

    def introduce(self):
        """Simple way for a person object to introduce itself."""
        print(
            f"Hello, my name is {self.first_name} and my birthday is on {self.say_birthday()}"
        )

    def set_birthday(self, month, day):
        """Mutator for birthday. Uses our very own Birthday class."""
        self._birthday = Birthday(month, day)

    def set_city(self, city):
        """Mutator for city."""
        self.city = city

    def get_first_name(self):
        """Accessor for first name"""
        return self.first_name

    def get_last_name(self):
        """Accessor for last name"""
        return self.last_name

    def __str__(self):
        """String representation for the object"""
        return f"[ {self.first_name} {self.last_name}]"
    
    def say_birthday(self) -> str:
     """
     - Returns a conversation string of a person's birthday
     """
    # Goes into the Person object, accesses birthday attribute, then accesses the day inside the Birthday object
     day: int = self._birthday.get_day()
    # Determines the suffix for the day
     suffix: str = "th"
     if day in [1, 21, 31]:
        suffix = "st"
     elif day in [2, 22]:
        suffix = "nd"
     elif day in [3, 23]:
        suffix = "rd"
     # List of month names
     month_names = ["January", "February", "March", "April", "May", "June", "july", "August", "September", "October", "November", "December"]
     # Gets numeric month from Birthday object
     month_index = self._birthday.get_month()
     # Converts numeric month to full name using the list of month names
     month_name = month_names[month_index - 1]
     return f"{day}{suffix} of {month_name}"
    
    def __lt__(self, other) -> bool:
        # Compares first names alphabetically and returns true if first name of self is less alphabetically than other.
        return self.first_name < other.first_name
    


    

# Testing Code
 
p1 = Person("Bob", "Marley")
p2 = Person("Jimmi", "Hendrix")
p1.set_birthday(2, 6)
print(p1.say_birthday())
print(p1 < p2)