from functionality import parse_input, remove_record, add_contact, change_number, show_phones, remove_phone, show_all, add_birthday, show_birthday, show_reminder, save_data, load_data, add_email
from markup import create_markup, table_data, header
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

def main(): 
    '''
    The main function for launching an assistant bot.

    Accepts commands from the user and executes them.
    '''
    commands = ['close', 'close', 'hello', 'help', 'add', 'rm_contact', 'rm_phone', 'change', 'find_phone', 'all', 'add_email', 'add_birthday', 'show_birthday', 'reminder']
    command_completer = WordCompleter(commands, ignore_case=True)
    book = load_data()
    print("\nWelcome to the assistant bot!")
    while True:
        user_input = prompt("\nEnter a command: ", completer=command_completer)

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break


        elif command == "hello":
            print("How can I help you?")        


        elif command == "help":   
            print("\n" * 1)               
            print(create_markup(header, table_data))

        elif command == "add":                  
            print(add_contact(args, book))  

        elif command == "rm_contact":                  
            print(remove_record(args, book))  


        elif command == "rm_phone":                  
            print(remove_phone(args, book))  


        elif command == "change":               
            print(change_number(args, book))  

        elif command == "find_phone":               
            print(show_phones(args[0], book))

        elif command == "all":                  
            print(show_all(book))


        elif command == 'add_email':
            print(add_email(args, book))

        elif command == "add_birthday":         
            print(add_birthday(args, book))

        elif command == "show_birthday":        
            print(show_birthday(args[0], book))

        elif command == "reminder":         
            print(show_reminder(book))


        else:
            print("Invalid command.")



if __name__ == "__main__":
    main()

#   add_email roman rstrizhko1994@gmail.comad


