class Book():
    def __init__(self, title, author, genre, available):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
    
    def toggle_check_out(self, available):
        self.available = available
