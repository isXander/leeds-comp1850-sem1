# Worksheet 1.5: Person class

from datetime import date


class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self, name, birth):
        if type(name) != str:
            raise TypeError("name must be a string")

        if not name:
            raise ValueError("name must not be empty string")

        if type(birth) != date:
            raise TypeError("birth must be a date")

        self.name = name
        self.birth = birth

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)


    def initials(self):
        """
        returns initials
        """
        return "".join([x[0].upper() for x in self.name.split(" ")])

    def is_birthday(self):
        """
        returns true if today is the person's birthday
        """
        today = date.today()
        return today.day == self.birth.day \
            and today.month == self.birth.month
