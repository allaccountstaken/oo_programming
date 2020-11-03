import datetime

# Store the next id
last_id = 0

class Note:
    """Represents a note in a notebook. Match agains a 
    string in searches and stores tags for each note"""

    def __init__(self, memo, tags=""):
        """Initializes a note woth memo and optional space-separeated tags. 
        Automatically set the notes's creation date and a unique id"""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """Determine if this note matches the filter text. 
        Return True if matches and False otherwise. 
        Search is case sensitive and matches both text and tags"""
        return filter in self.memo or filter in self.tags

    
class Notebook:
    """Represents a collection of notes that can be tagged, 
    modified, and searched."""
    def __init__(self):
        """Initializes a notebook with an empty list."""
        self.notes = []
    
    def new_note(self, memo, tags=""):
        """Create a new note and add it to the list"""
        self.notes.append(Note(memo, tags))
        
    def modify_memo(self, note_id, memo):
        """Find the note with the given id and change its 
        memo to a given value"""
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False
    
    def modify_tags(self, note_id, tags):
        """Find the note with the given id and change its 
        tags to a given value."""
        tags = self._find_note(note_id)
        if tags:
            note.tags = tags
            return True
        return False
                
    def search(self, filter):
        """Find all notes that match the given filter string."""
        return [note for note in self.notes if note.match(filter)]
    
    def _find_note(self, note_id):
        """Locate the note with the given id."""
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None