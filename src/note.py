class Note:
    def __init__(self, title, content, tags=None):
        self.title = title
        self.content = content
        self.tags = tags if tags else []
    
    def edit(self, new_content, new_tags):
        self.content = new_content
        self.tags = new_tags
    
    def __str__(self):
        return f"Title: {self.title}, Content: {self.content}"
    
    def add_tags(self, note, new_tags):
        if not new_tags:
            return
        note.tags = [str(tag).strip() for tag in note.tags.split(",")]
        for tag in new_tags.split(","):
            if tag not in note.tags:
                note.tags.append(tag)
        return f"Tags added to note with title: '{note.title.value}'."