from tkinter import *
from backend import Database

database = Database("books.db")


class Window(object):
    def __init__(self, window):
        self.window = window
        self.window.wm_title("Bookstore")


        # Create labels
        l1 = Label(window, text="Title")
        l1.grid(row=0, column=0)

        l2 = Label(window, text="Author")
        l2.grid(row=0, column=2)

        l3 = Label(window, text="Year")
        l3.grid(row=1, column=0)

        l4 = Label(window, text="ISBN")
        l4.grid(row=1, column=2)


        # Create entry fields/boxes
        self.title_text = StringVar()
        self.e1=Entry(window, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)

        self.author_text = StringVar()
        self.e2=Entry(window, textvariable=self.author_text)
        self.e2.grid(row=0, column=3)

        self.year_text = StringVar()
        self.e3=Entry(window, textvariable=self.year_text)
        self.e3.grid(row=1, column=1)

        self.isbn_text = StringVar()
        self.e4=Entry(window, textvariable=self.isbn_text)
        self.e4.grid(row=1, column=3)


        #Create listbox
        self.list1 = Listbox(window, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)


        # Create scrollbar
        sb1 = Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)


        # Configure listbox and scrollbar to interact
        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)


        # Create buttons
        # After "backend.py" created, button commands can reference backend functions
        b1 = Button(window, text="View All", width=12, command=self.view_command)
        b1.grid(row=2, column=3)

        b2 = Button(window, text="Search Entry", width=12, command=self.search_command)
        b2.grid(row=3, column=3)

        b3 = Button(window, text="Add Entry", width=12, command=self.add_command)
        b3.grid(row=4, column=3)

        b4 = Button(window, text="Update Selected", width=12, command=self.update_command)
        b4.grid(row=5, column=3)

        b5 = Button(window, text="Delete Selected", width=12, command=self.delete_command)
        b5.grid(row=6, column=3)

        b6 = Button(window, text="Close", width=12, command=window.destroy)
        b6.grid(row=7, column=3)


    # Creates function to get information from selecting items in listbox
    # Also populates entry fields with selected listbox item's information
    def get_selected_row(self, event):
        try: 
            global selected_tuple
            index = self.list1.curselection()[0]
            selected_tuple = self.list1.get(index)
            # Inserts tuple index items into desired entry fields
            self.e1.delete(0, END)
            self.e1.insert(END, selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END, selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END, selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END, selected_tuple[4])
        except:
            pass


    # Wrapper functions for buttons:
    # Creates wrapper function for "View All" button
    def view_command(self):
        self.list1.delete(0, END)
        for row in database.view():
            self.list1.insert(END, row)


    # Creates wrapper function for "Search Entry" button
    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.list1.insert(END, row)


    # Creates wrapper function for "Add Entry" button
    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))


    # Creates wrapper function for "Delete Selected" button
    def delete_command(self):
        database.delete(selected_tuple[0])
        self.list1.delete(0, END)
        for row in database.view():
            self.list1.insert(END, row)

    # Creates wrapper function for "Update Selected" button
    def update_command(self):
        database.update(selected_tuple[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.list1.delete(0, END)
        for row in database.view():
            self.list1.insert(END, row)


# Create window
window = Tk()

# Calls class
Window(window)

# Mainloop window
window.mainloop()

