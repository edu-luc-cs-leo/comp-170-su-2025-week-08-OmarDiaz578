from datetime import datetime

class Birthday:

    # Some data for this object: the number of days in each month.
    # For simplicity, we ignore leap years and keep February at 28.
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, month, day):
        """Basic constructor. It validates the arguments past to it
        and if they are out of range, it assigns a default value of
        January 1."""
        # Protect month value
        if month >= 1 and month <= 12:
            self.__month = month
        else:
            # In case of out of range month, default to January
            self.__month = 1
        # At this point we have a legit month value 1-12.
        # Protect day value; use -1 in array to synchronize months
        if day >= 1 and day <= Birthday.days_in_month[month - 1]:
            self.__day = day
        else:
            # In case of out of range day, default is 1st of month
            self.__day = 1
    # end basic constructor

    def set_day(self, day):
        """Mutator for day. It only changes the day value if the
        passed argument is within a valid range for the given month."""
        if day > 0 and day <= Birthday.days_in_month[self.__month-1]:
            self.__day = day
    # end set_day

    # Accessor for __month
    def get_month(self):
        return self.__month

    # Accessor for __day
    def get_day(self):
        return self.__day

    # Compute days to birthday
    def days_until(self):
        # Gets today's date using datetime module
        today = datetime.today()
        # Gets numeric month and date
        today_month = today.month
        today_day = today.day
        # Uses day_in_year to calculate what day of the year today is
        # and what day the birthday falls on
        today_day_number = self.day_in_year(today_month, today_day)
        birthday_day_number = self.day_in_year(self.__month, self.__day)
        # Calculates how many days until the birthday:
        # If birthday is still coming just subtract
        if birthday_day_number >= today_day_number:
            days_remaining = birthday_day_number - today_day_number
        else:
        # If birthday passed, calculates number of day until it comes
            days_remaining = 365 - today_day_number + birthday_day_number
        return days_remaining
        
    def day_in_year(self, month, day):
        """calculates the day number within the year corresponding to a given 
        date (month, day), assuming that February has 28 days always."""
        count = 0
        for i in range(month-1):
            count += Birthday.days_in_month[i]
        return count + day

    def __str__(self):
        """String representation for the object"""
        return f"[ {self.get_month()}/{self.get_day()} ]"
    
    def set_month(self, month):
        # Checks if the month is a valid calendar month
        # If it's false the method does nothing
        if 1 <= month <= 12:
            # If check passes, this line updates 
            self.__month = month
    

    

demo = Birthday(6,29)

print(demo.day_in_year(6,29)) # d_b
print(demo.day_in_year(4,29)) # d_t

b = Birthday(2, 15)
print(f"Days until birthday: {b.days_until()}")