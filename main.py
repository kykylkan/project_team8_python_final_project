from functionality import parse_input, input_error, remove_record, add_contact, change_number, show_phones, remove_phone, show_all, add_birthday, show_birthday, show_reminder, save_data, load_data, add_email
from markup import create_markup, table_data, header
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style as prompt_style
from colorama import Fore, Back, Style
from note_mod import NotesManager, save_notes, load_notes

style = prompt_style.from_dict({
    'prompt': 'fg:#003366  bold',            
    'completion-menu': 'bg:#045160',                    
    'completion-menu.selected': 'bg:#E0F7FA fg:#003366',  
    'completion-menu.completions': 'fg:#003366',        
})



def main(): 
    '''
    The main function for launching an assistant bot.

    Accepts commands from the user and executes them.
    '''
    commands = ['help', 'hello', 'add_contact', 'del_contact', 'del_phone', 'change_number', 'find_phone', 'all_contacts', 'add_email', 'add_birthday', 'show_birthday', 'reminder', 'add-note', 'all-notes', 'search-notes', 'delete-note', 'close', 'exit', ]
    command_completer = WordCompleter(commands, ignore_case=True)
    book = load_data()
    notes_manager = load_notes()
    print(f"\nWelcome to the ASSISTANT BOT! 🤖")

    while True:
        print(f"\n " * 2)               
        user_input = prompt('Enter a command: >>> ', style=style, completer=command_completer)


        print("\n " * 2)               

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            save_notes(notes_manager)
            print("Good bye!")
            break


        elif command == "hello":
            print("How can I help you?")        


        elif command == "help":   
            print("\n")               
            print(create_markup(header, table_data))

        elif command == "add_contact":                  
            print(add_contact(args, book))  

        elif command == "del_contact":                  
            print(remove_record(args, book))  


        elif command == "del_phone":                  
            print(remove_phone(args, book))  


        elif command == "change_number":               
            print(change_number(args, book))  

        elif command == "find_phone":               
            print(show_phones(args[0], book))
            break

        elif command == "all_contacts":                  
            print(show_all(book))


        elif command == 'add_email':
            print(add_email(args, book))

        elif command == "add_birthday":         
            print(add_birthday(args, book))

        elif command == "show_birthday":        
            print(show_birthday(args[0], book))

        elif command == "reminder":         
            print(show_reminder(book))

        # Notes commands
        elif command == "add-note":
            author = input("Enter author of the note: ")
            title = input("Enter note title: ")
            text = input("Enter note text: ")
            tags = input("Enter tags (comma-separated) or press enter to skip: ")
            print(notes_manager.add_note(author, title, text, tags))
            save_notes(notes_manager)

        elif command == "all-notes":
            print(notes_manager.show_all_notes())

        elif command == "search-notes":
            search_term = input("Enter search term: ")
            print(notes_manager.search_notes(search_term))

        elif command == "delete-note":
            print(notes_manager.show_all_notes())
            idx = input("Enter the number of the note to delete: ")
            print(notes_manager.delete_note(idx))
            save_notes(notes_manager)

        else:
            print(f"⛔️   {Fore.RED}Invalid command.{Style.RESET_ALL}")



if __name__ == "__main__":
    main()




