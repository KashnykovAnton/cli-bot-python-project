class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.tags = []
    
    def edit(self, new_content):
        self.content = new_content

    def add_tags(self, tags):
        if isinstance(tags, list):
            for tag in tags:
                if tag not in self.tags:
                    self.tags.append(tag)
        elif isinstance(tags, str):
            self.tags.append(tags)
        else:
            print(Fore.RED + "Invalid tags format.")
    
    def __str__(self):
        tags_str = ", ".join(self.tags) if self.tags else "No tags"
        return f"Title: {self.title}\nContent: {self.content}\nTags: {tags_str}"