from abc import ABC, abstractmethod


class UserInterface(ABC):

    @abstractmethod
    def print_contacts(self, contacts):
        pass

    @abstractmethod
    def print_notes(self, notes):
        pass

    @abstractmethod
    def print_help(self, commands):
        pass

    @abstractmethod
    def print_info(self, message):
        pass


class ConsoleUI(UserInterface):

    def __init__(self, commands):
        self.commands = commands

    def print_contacts(self, contact):
        print("===CONTACTS===\n")
        # for contact in contacts:
        print(contact)

    def print_notes(self, notes):
        print("===NOTES===\n")
        for note in notes:
            print(note)

    def print_help(self, commands):
        format_str = str('{:%s%d}' % ('^', 20))
        print("===Available Commands===\n")
        for command in self.commands:
            print(format_str.format(command))

    def print_info(self, message):
        print(message)
