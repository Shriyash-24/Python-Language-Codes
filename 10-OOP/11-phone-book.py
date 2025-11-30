class PhoneBook:
    phone_directory = []
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        PhoneBook.phone_directory.append(self)

    def show_contact(self):
        return f"Name: {self.name}, Contact Number: {self.phone_number}"

    @classmethod
    def show_all_contact(cls):
        if len(cls.phone_directory) == 0:
            print("No contacts available.")
        else:
            for contact in cls.phone_directory:
                print(contact.show_contact())

    @classmethod
    def search_contact(cls, search_name):
        for contact in cls.phone_directory:
            if contact.name.lower() == search_name.lower():
                return contact.phone_number
        return f"No contact for {search_name} found."

    @staticmethod
    def validate_phone_number(number):
        if len(number) > 8 and number.isdigit():
            return True
        else:
            return False



n_contacts = int(input("How many contacts do you want to add?: "))
for i in range(n_contacts):
    name = input("Enter name of the contact: ")
    phone_number = input("Enter phone number: ")
    if PhoneBook.validate_phone_number(phone_number):
        PhoneBook(name,phone_number)
    else:
        print(f"Invalid Phone Number for {name}, phone number should be atleast 8 digits and should only contain numbers in it.")

PhoneBook.show_all_contact()
