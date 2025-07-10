import tkinter as tk
from tkinter import messagebox
import database

# Import page modules
from booking import BookingPage
from reservations import ReservationsPage
from edit_reservation import EditReservationPage

def show_frame(frame):
    frame.tkraise()

def main():
    # Initialize database
    database.create_table()

    root = tk.Tk()
    root.title("Flight Reservation System")
    root.geometry("500x500")
    root.resizable(False, False)

    # Create a container for all frames
    container = tk.Frame(root)
    container.pack(fill="both", expand=True)

    # Dictionary to hold references to frames
    frames = {}

    # Home Page
    class HomePage(tk.Frame):
        def __init__(self, parent, controller):
            super().__init__(parent)
            tk.Label(self, text="Flight Reservation System", font=("Arial", 18)).pack(pady=30)
            tk.Button(self, text="Book Flight", width=20, command=lambda: show_frame(frames["BookingPage"])).pack(pady=10)
            tk.Button(self, text="View Reservations", width=20, command=lambda: show_frame(frames["ReservationsPage"])).pack(pady=10)
            tk.Button(self, text="Exit", width=20, command=root.destroy).pack(pady=30)

    # Instantiate all frames
    for F, name in zip([HomePage, BookingPage, ReservationsPage, EditReservationPage],
                       ["HomePage", "BookingPage", "ReservationsPage", "EditReservationPage"]):
        frame = F(container, lambda page: show_frame(frames[page]))
        frames[name] = frame
        frame.grid(row=0, column=0, sticky="nsew")

    # Set up navigation callbacks for reservations and edit pages
    frames["ReservationsPage"].set_navigation(lambda page: show_frame(frames[page]))
    frames["EditReservationPage"].set_navigation(lambda page: show_frame(frames[page]))
    frames["BookingPage"].set_navigation(lambda page: show_frame(frames[page]))

    show_frame(frames["HomePage"])
    root.mainloop()

if __name__ == "__main__":
    main()


