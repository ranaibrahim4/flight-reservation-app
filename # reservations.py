# reservations.py
import tkinter as tk
from tkinter import ttk, messagebox
import database

class ReservationsPage(tk.Frame):
    def __init__(self, parent, navigate_callback):
        super().__init__(parent)
        self.navigate_callback = navigate_callback
        tk.Label(self, text="All Reservations", font=("Arial", 16)).pack(pady=10)
        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Flight", "From", "To", "Date", "Seat"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(expand=True, fill="both")
        self.refresh_tree()
        tk.Button(self, text="Edit", command=self.edit_selected).pack(pady=5)
        tk.Button(self, text="Delete", command=self.delete_selected).pack(pady=5)
        tk.Button(self, text="Back", command=lambda: self.navigate_callback("HomePage")).pack(pady=10)

    def set_navigation(self, callback):
        self.navigate_callback = callback

    def refresh_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in database.get_all_reservations():
            self.tree.insert("", "end", values=row)

    def get_selected(self):
        selected = self.tree.focus()
        if selected:
            return self.tree.item(selected)["values"]
        return None

    def delete_selected(self):
        item = self.get_selected()
        if item:
            if messagebox.askyesno("Confirm", "Delete this reservation?"):
                database.delete_reservation(item[0])
                self.refresh_tree()

    def edit_selected(self):
        item = self.get_selected()
        if item:
            self.navigate_callback("EditReservationPage", item)
