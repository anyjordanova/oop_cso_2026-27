
from people import Person


if __name__ == "__main__":
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    age = int(input("Enter age: "))

    left_handed = input("Are you left-handed? (y/Y for yes, any other key for no)")
    if left_handed.lower() == "y":
        is_lefty = True
    else:
        is_lefty = False

    person_with_constructor = Person(
        first_name=first,
        last_name=last,
        age=age,
        is_left=is_lefty
    )

    print("------------------------------\n MY PERSON DETAILS: ")
    person_with_constructor.display_details()