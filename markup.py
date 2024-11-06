from tabulate import tabulate
from colorama import Fore, Back, Style

header = [
    f"{Back.LIGHTBLACK_EX}{Fore.WHITE} Command {Style.RESET_ALL}",
    f"{Back.LIGHTBLACK_EX}{Fore.WHITE} Description {Style.RESET_ALL}"
]


table_data = [
    [f"{Fore.LIGHTCYAN_EX}hello{Style.RESET_ALL}", "greeting"],
    [f"{Fore.LIGHTCYAN_EX}help{Style.RESET_ALL}", "Displays a table with tips"],
    ["--------------", "----------------------------"],
    [f"{Fore.LIGHTCYAN_EX}add{Style.RESET_ALL}", "Adds a new contact"],
    [f"{Fore.LIGHTCYAN_EX}rm_contact{Style.RESET_ALL}", "Remove a contact"],
    [f"{Fore.LIGHTCYAN_EX}rm_phone{Style.RESET_ALL}", "Remove a phone number"],
    [f"{Fore.LIGHTCYAN_EX}change{Style.RESET_ALL}", "Update contact details"],
    [f"{Fore.LIGHTCYAN_EX}find_phone{Style.RESET_ALL}", "Finds a number by name"],
    ["--------------", "----------------------------"],
    [f"{Fore.LIGHTCYAN_EX}all{Style.RESET_ALL}", "View book"],
    [f"{Fore.LIGHTCYAN_EX}add_email{Style.RESET_ALL}", "Adds email to contact"],
    [f"{Fore.LIGHTCYAN_EX}add_birthday{Style.RESET_ALL}", "Adds birthday to contact"],
    [f"{Fore.LIGHTCYAN_EX}show_birthday{Style.RESET_ALL}", "Finds a birthday by name"],
    [f"{Fore.LIGHTCYAN_EX}reminder{Style.RESET_ALL}", "Birthdays for the next week"],
    ["--------------", "----------------------------"],
    [f"{Fore.LIGHTCYAN_EX}close, exit{Style.RESET_ALL}", "Close and exit"],
]


def create_markup(header: list, table_data: list):
    '''
    Function for creating a table
    '''
    return tabulate(table_data, headers=header, tablefmt="mixed_outline")


markup = create_markup(header, table_data)
