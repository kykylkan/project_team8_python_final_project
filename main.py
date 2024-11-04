from functionality import parse_input, remove_record, add_contact, change_number, show_phones, remove_phone, show_all, add_birthday, show_birthday, show_reminder, save_data, load_data, add_email


def main(): 
    '''
    The main function for launching an assistant bot.

    Accepts commands from the user and executes them.
    '''

    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break


        elif command == "hello":
            print("How can I help you?")        


        elif command == "add":                  
            print(add_contact(args, book))  

        elif command == "rm_contact":                  
            print(remove_record(args, book))  


        elif command == "rm_phone":                  
            print(remove_phone(args, book))  


        elif command == "change":               
            print(change_number(args, book))  

        elif command == "phone":               
            print(show_phones(args[0], book))

        elif command == "all":                  
            print(show_all(book))


        elif command == 'add_email':
            print(add_email(args, book))

        elif command == "add-birthday":         
            print(add_birthday(args, book))

        elif command == "show-birthday":        
            print(show_birthday(args[0], book))

        elif command == "birthdays":         
            print(show_reminder(book))


        else:
            print("Invalid command.")



if __name__ == "__main__":
    main()

#   add_email roman rstrizhko1994@gmail.comad


