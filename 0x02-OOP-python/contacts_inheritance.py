#!/usr/bin/python3
"""This module contains a contaxt class
    and a supplier class that extends
    the contacts class as a subclass
    simple demonstration of OOP
    inheritance in python3
"""


class Contact:
    """Contact class with an all_contacts list as class attribute"""
    all_contacts = []

    def __init__(self, name, email):
        """Initializer for the contact class
            each contact gets a name and an email
            after instantiation, the newly created
            contact gets added to the all_contacts list
        """
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Supplier(Contact):
    """This Supplier class extends the Contact class
        meaning it has the all_contact class variable
        and shares same init method as the parent class
    """
    def order(self, order):
        """This method is unique to Supplier
            which is a subclass of Contact
            meaning only Suppliers within our 
            all_contacts list can take orders
        """
        print("In a real system, I'd send "
                "{} order to {}".format(order, self.name))




