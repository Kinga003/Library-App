# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 20:12:53 2024

@author: kinga
"""
# import packages
import tkinter as tk
from tkinter import messagebox

class LibraryApp:
    """Klasa służąca do tworzenia interface'u do zarządzania biblioteką"""
    def __init__(self, root):
        """
        konstruktor klasy LibraryApp

        Parameters
        ----------
        root : 
            instancja klasy tkinter - główne okno aplikacji.

        Returns
        -------
        None.

        """
        self.root = root
        root.title("myapp")
        root.geometry("590x250+0+0")

        self.labelAuthor = tk.Label(root, text="Autor")
        self.labelAuthor.grid(row=0, column=0, padx=5)

        self.entryAuthor = tk.Entry(root)
        self.entryAuthor.grid(row=0, column=1, padx=5)

        self.labelTitle = tk.Label(root, text="Tytuł")
        self.labelTitle.grid(row=0, column=2, padx=5)

        self.entryTitle = tk.Entry(root)
        self.entryTitle.grid(row=0, column=3, padx=5)

        self.buttonAdd = tk.Button(root, text="Dodaj Książkę", command=self.addBook)
        self.buttonAdd.grid(row=0, column=4, padx=5)

        self.listBox = tk.Listbox(root, width=50, height=10)
        self.listBox.grid(row=1, columnspan=5, padx=5, pady=5)

        self.buttonBorrow = tk.Button(root, text="Wypożycz Książkę", command=self.borrowBook)
        self.buttonBorrow.grid(row=2, column=0, padx=5, pady=5)

        self.buttonSave = tk.Button(root, text="Zapisz baze", command=self.saveBase)
        self.buttonSave.grid(row=2, column=1, padx=5, pady=5)

        self.buttonLoadLibrary = tk.Button(root, text="Załaduj biblioteke", command=self.loadLibrary)
        self.buttonLoadLibrary.grid(row=2, column=2, padx=5, pady=5)
        
        self.books = []
# add book
    def addBook(self):
        """
        funkcja dodająca książkę do listy

        Returns
        -------
        None.

        """
        author = self.entryAuthor.get()
        title = self.entryTitle.get()
        if title and author:
            self.books.append({"title":title, "author":author})
            self.entryAuthor.delete(0,tk.END)
            self.entryTitle.delete(0,tk.END)
            messagebox.showinfo("Sukces", "Poprawnie dodano książkę")
            self.updateListBox()
        else:
            messagebox.showwarning("Uwaga", "proszę podać autora i tytuł")
            
    def updateListBox(self):
        """
        Funkcja aktualizująca listbox

        Returns
        -------
        None.

        """
        self.listBox.delete(0, tk.END)
        for book in self.books:
            self.listBox.insert(tk.END, f"author: {book['author']}, title: {book['title']}")
    # borrow book
    def borrowBook(self):
        """
        Funkcja wypożyczania książki

        Returns
        -------
        None.

        """
        borrowedBook = self.listBox.curselection()
        if borrowedBook:
            index = borrowedBook[0]
            title = self.books[index]["title"]
            author = self.books[index]["author"]
            messagebox.showinfo("Wypożyczono", f"Udało się wypożyczyć: {title} {author}")
            del self.books[index]
            self.updateListBox()
        else:
            messagebox.showwarning("Uwaga", "Wybierz ksiązkę")
            
    def saveBase(self):
        """
        Zapis bazy książek z listy do pliku tekstowego

        Returns
        -------
        None.

        """
        try:
            with open("library.txt", "w") as file:
                for book in self.books:
                    file.write(f"{book['title']},{book['author']}\n")
                messagebox.showinfo("sukces", "poprawnie zapisano biblioteke")
        except Exception as e:
            messagebox.showerror("Błąd", f"Błąd podczas zapisu {e}")
   # library         
    def loadLibrary(self):
        """
        Wczystywaie bazy z pliku tekstowego do listy

        Returns
        -------
        None.

        """
        try:
            with open("library.txt", "r") as file:
                for line in file:
                    title, author = line.strip().split(",")
                    self.books.append({"title":title, "author":author})
                self.updateListBox()
        except Exception as e:
            messagebox.showerror("Błąd", f"Błąd podczas wczytywania {e}")
    
def main():
    root = tk.Tk()
    _ = LibraryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
