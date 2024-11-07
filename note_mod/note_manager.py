import pickle
from colorama import Fore, Style
from .note import Note


class NotesManager:
    def __init__(self):
        self.notes = []

    def add_note(self, author, title, text, tags=None):
        note = Note(author, title, text, tags)
        self.notes.append(note)
        return f"✅   {Fore.GREEN}Note added successfully.{Style.RESET_ALL}"

    def show_all_notes(self):
        if not self.notes:
            return f"⛔️   {Fore.RED}No notes found.{Style.RESET_ALL}"

        result = ["\nNOTES"]
        result.append(
            f"{'#':<4} {'Author':<15} {'Title':<20} {'Description':<40} {'Tags':<15} {'Created'}")
        result.append("-" * 100)

        for idx, note in enumerate(self.notes, 1):
            result.append(
                f"{idx:<4} {note.author:<15} {note.title:<20} {note.text:<40} {note.tags:<15} {note.created}")

        return "\n".join(result)

    def search_notes(self, search_term):
        found_notes = []
        search_term = search_term.lower()

        for note in self.notes:
            if (search_term in note.title.lower() or
                search_term in note.text.lower() or
                search_term in note.author.lower() or
                    search_term in note.tags.lower()):
                found_notes.append(note)

        if not found_notes:
            return f"⛔️   {Fore.RED}No matching notes found.{Style.RESET_ALL}"

        result = ["\nFound Notes:"]
        result.append(
            f"{'#':<4} {'Author':<15} {'Title':<20} {'Description':<40} {'Tags':<15} {'Created'}")
        result.append("-" * 100)

        for idx, note in enumerate(found_notes, 1):
            result.append(
                f"{idx:<4} {note.author:<15} {note.title:<20} {note.text:<40} {note.tags:<15} {note.created}")

        return "\n".join(result)

    def delete_note(self, idx):
        try:
            idx = int(idx) - 1
            if 0 <= idx < len(self.notes):
                deleted_note = self.notes.pop(idx)
                return f"✅   {Fore.GREEN}Deleted note: {deleted_note.title}{Style.RESET_ALL}"
            else:
                return f"⛔️   {Fore.RED}Invalid note number.{Style.RESET_ALL}"
        except ValueError:
            return f"⛔️   {Fore.RED}Please enter a valid number.{Style.RESET_ALL}"


def save_notes(notes_manager, filename="notes.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(notes_manager, f)


def load_notes(filename="notes.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return NotesManager()
