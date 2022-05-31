# database.py
import sys, shelve


def store_person(db):
    pid = input("Enter unique ID number:")
    person = {'name': input("Enter name: "), 'age': input("Enter age: "), 'phone': input("Enter phone number:")}
    db[pid] = person


def lookup_person(db):
    pid = input("Enter ID number:")
    field = input("What would you like to know?(name, age, phone):")
    field = field.strip().lower()

    print(field.capitalize() + ":", db[pid][field])


def print_help():
    print("The available commands are:")
    print("store : Stores information about a person")
    print("lookup: Looks up a person from ID number")
    print("quit: Save changes and exit")
    print("? :Prints this message")


def enter_command():
    cmd = input("Enter command(? for help):")
    cmd = cmd.strip().lower()
    return cmd


def main():
    database = shelve.open('database.dat')
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            if cmd == 'lookup':
                lookup_person(database)
            if cmd == 'quit':
                return
            if cmd == '?':
                print_help()
    finally:
        database.close()


if __name__ == '__main__':
    main()
