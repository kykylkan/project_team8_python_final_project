import pickle
from colorama import Fore, Style
from .note import Note
from functionality import input_error


class NotesManager:
    def __init__(self):
        self.notes = []

    @input_error
    def add_note(self, author, title, text, tags=None):
        if not author.strip():
            raise ValueError("Author field cannot be empty")
        if not title.strip():
            raise ValueError("Title field cannot be empty")
        if not text.strip():
            raise ValueError("Note text field cannot be empty")

        note = Note(author, title, text, tags)
        self.notes.append(note)
        return f"✅   {Fore.GREEN}Note \"{title}\" successfully added{Style.RESET_ALL}"

    @input_error
    def show_all_notes(self):
        if not self.notes:
            raise ValueError("No notes found")

        result = ["\nNOTES"]
        result.append(
            f"{'#':<4} {'Author':<15} {'Title':<20} {'Description':<40} {'Tags':<15} {'Created'}")
        result.append("-" * 100)

        for idx, note in enumerate(self.notes, 1):
            result.append(
                f"{idx:<4} {note.author:<15} {note.title:<20} {note.text:<40} {note.tags:<15} {note.created}")

        return "\n".join(result)

    @input_error
    def search_notes(self, search_term):
        if not search_term.strip():
            raise ValueError("Search term cannot be empty")

        found_notes = []
        search_term = search_term.lower()

        for note in self.notes:
            if (search_term in note.title.lower() or
                search_term in note.text.lower() or
                search_term in note.author.lower() or
                    search_term in note.tags.lower()):
                found_notes.append(note)

        if not found_notes:
            raise KeyError(f"No notes found matching: {search_term}")

        result = ["\nFound Notes:"]
        result.append(
            f"{'#':<4} {'Author':<15} {'Title':<20} {'Description':<40} {'Tags':<15} {'Created'}")
        result.append("-" * 100)

        for idx, note in enumerate(found_notes, 1):
            result.append(
                f"{idx:<4} {note.author:<15} {note.title:<20} {note.text:<40} {note.tags:<15} {note.created}")

        return "\n".join(result)

    @input_error
    def delete_note(self, idx):
        if not str(idx).strip():
            raise ValueError("Note number cannot be empty")

        try:
            idx = int(idx) - 1
        except ValueError:
            raise ValueError("Note number must be a number")

        if not 0 <= idx < len(self.notes):
            raise IndexError(f"Note number {idx + 1} not found")

        deleted_note = self.notes.pop(idx)
        return f"✅   {Fore.GREEN}Note \"{deleted_note.title}\" successfully deleted{Style.RESET_ALL}"


@input_error
def save_notes(notes_manager, filename="notes.pkl"):
    try:
        with open(filename, "wb") as f:
            pickle.dump(notes_manager, f)
    except Exception as e:
        raise ValueError(f"Failed to save notes: {str(e)}")


@input_error
def load_notes(filename="notes.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return NotesManager()
    except Exception as e:
        raise ValueError(f"Failed to load notes: {str(e)}")
