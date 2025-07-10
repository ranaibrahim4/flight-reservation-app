# edit_reservation.py
import tkinter as tk
from tkinter import messagebox
import database

class EditReservationPage(tk.Frame):
    def __init__(self, parent, navigate_callback):
        super().__init__(parent)
        self.navigate_callback = navigate_callback
        self.data = None
        self.entries = {}
        self.fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        tk.Label(self, text="Edit Reservation", font=("Arial", 16)).pack(pady=10)
        self.form_frame = tk.Frame(self)
        self.form_frame.pack(pady=10)
        for i, field in enumerate(self.fields):
            frame = tk.Frame(self.form_frame)
            frame.pack(pady=2)
            tk.Label(frame, text=field, width=15, anchor="w").pack(side="left")
            entry = tk.Entry(frame)
            entry.pack(side="left")
            self.entries[field] = entry
        tk.Button(self, text="Update", command=self.submit).pack(pady=10)
        tk.Button(self, text="Back", command=lambda: self.navigate_callback("ReservationsPage")).pack()

    def set_navigation(self, callback):
        self.navigate_callback = callback

    def set_data(self, data):
        self.data = data
        for i, field in enumerate(self.fields):
            self.entries[field].delete(0, tk.END)
            self.entries[field].insert(0, data[i+1])

    def submit(self):
        if not self.data:
            return
        values = [self.entries[field].get().strip() for field in self.fields]
        if any(not v for v in values):
            messagebox.showerror("Error", "All fields are required.")
            return
        try:
            database.update_reservation(self.data[0], *values)
            messagebox.showinfo("Success", "Reservation updated!")
            self.navigate_callback("ReservationsPage")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update reservation. {e}")
