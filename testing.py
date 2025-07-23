from Birthday import Birthday
from Person import Person

p1 = Person("Bob", "Marley")
p2 = Person("Jimmi", "Hendrix")
p1.set_birthday(2, 6)
print(p1.say_birthday())
print(p1 < p2)
b = Birthday(2, 15)
print(f"Days until birthday: {b.days_until()}")