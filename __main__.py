from Bot import Bot
from user_interface import ConsoleUI
from AddressBook import AddressBook

if __name__ == "__main__":
    commands = ['Add', 'Search', 'Edit', 'Load',
                'Remove', 'Save', 'Congratulate', 'View', 'Exit']
    ui = ConsoleUI(commands)
    bot = Bot(ui, commands)
    bot.book.load("auto_save")

    ui.print_info(
        'Hello. I am your contact-assistant. What should I do with your contacts?')

    while True:
        action = input(
            'Type help for list of commands or enter your command\n').strip().lower()
        if action == 'help':
            ui.print_help(commands)
            action = input().strip().lower()
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")

        if action == 'exit':
            break
