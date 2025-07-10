# booking.py
import tkinter as tk
from tkinter import messagebox
import database

class BookingPage(tk.Frame):
    def __init__(self, parent, navigate_callback):
        super().__init__(parent)
        self.navigate_callback = navigate_callback
        tk.Label(self, text="Book a Flight", font=("Arial", 16)).pack(pady=10)

        self.entries = {}
        fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        for field in fields:
            frame = tk.Frame(self)
            frame.pack(pady=2)
            tk.Label(frame, text=field, width=15, anchor="w").pack(side="left")
            entry = tk.Entry(frame)
            entry.pack(side="left")
            self.entries[field] = entry

        tk.Button(self, text="Submit", command=self.submit_booking).pack(pady=10)
        tk.Button(self, text="Back", command=lambda: self.navigate_callback("HomePage")).pack(pady=5)

    def set_navigation(self, callback):
        self.navigate_callback = callback

    def submit_booking(self):
        values = [self.entries[field].get().strip() for field in self.entries]
        if any(not v for v in values):
            messagebox.showerror("Error", "All fields are required.")
            return
        try:
            database.add_reservation(*values)
            messagebox.showinfo("Success", "Reservation Successful!")
            for entry in self.entries.values():
                entry.delete(0, tk.END)
            self.navigate_callback("HomePage")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to make reservation. {e}")

