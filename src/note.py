class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    def edit(self, new_content):
        self.content = new_content
    
    def __str__(self):
        return f"Title: {self.title}, Content: {self.content}"