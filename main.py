import tkinter as tk

class Library:
    def __init__(self):
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")
    
    def __del__(self):
        self.file.close()
    
    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        book_info_str = ""
        for book in books:
            book_info = book.strip().split(',')
            book_info_str += f"Book: {book_info[0]}, Author: {book_info[1]}\n"
        return book_info_str
    
    def add_book(self, title, author, release_year, num_pages):
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
    
    def remove_book(self, title):
        if not title.strip():
            return  # Boş girişi kontrol et
        self.file.seek(0)
        books = self.file.readlines()
        updated_books = [book for book in books if title not in book]
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(updated_books)


def list_books():
    book_info_text.set(lib.list_books())

def add_book():
    title = entry_title.get()
    author = entry_author.get()
    release_year = entry_release_year.get()
    num_pages = entry_num_pages.get()
    lib.add_book(title, author, release_year, num_pages)
    list_books()

def remove_book():
    title = entry_remove_title.get()
    lib.remove_book(title)
    list_books()

lib = Library()

root = tk.Tk()
root.title("Library Management System")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_title = tk.Label(frame, text="Title:")
label_title.grid(row=0, column=0, sticky="e")
entry_title = tk.Entry(frame)
entry_title.grid(row=0, column=1)

label_author = tk.Label(frame, text="Author:")
label_author.grid(row=1, column=0, sticky="e")
entry_author = tk.Entry(frame)
entry_author.grid(row=1, column=1)

label_release_year = tk.Label(frame, text="Release Year:")
label_release_year.grid(row=2, column=0, sticky="e")
entry_release_year = tk.Entry(frame)
entry_release_year.grid(row=2, column=1)

label_num_pages = tk.Label(frame, text="Number of Pages:")
label_num_pages.grid(row=3, column=0, sticky="e")
entry_num_pages = tk.Entry(frame)
entry_num_pages.grid(row=3, column=1)

button_add = tk.Button(frame, text="Add Book", command=add_book)
button_add.grid(row=4, column=0, columnspan=2, pady=5)

button_list = tk.Button(frame, text="List Books", command=list_books)
button_list.grid(row=5, column=0, columnspan=2, pady=5)

label_remove_title = tk.Label(frame, text="Title to Remove:")
label_remove_title.grid(row=6, column=0, sticky="e")
entry_remove_title = tk.Entry(frame)
entry_remove_title.grid(row=6, column=1)

button_remove = tk.Button(frame, text="Remove Book", command=remove_book)
button_remove.grid(row=7, column=0, columnspan=2, pady=5)

book_info_text = tk.StringVar()
label_books_info = tk.Label(frame, textvariable=book_info_text, justify="left")
label_books_info.grid(row=8, column=0, columnspan=2, pady=5)

root.configure(background="purple")
root.mainloop()
