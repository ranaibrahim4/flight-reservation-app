
import sqlite3

def connect_db():
    return sqlite3.connect('flights.db')

def create_table():
    """Create the reservations table if it doesn't exist."""
    try:
        conn = connect_db()
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS reservations
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT,
                      flight_number TEXT,
                      departure TEXT,
                      destination TEXT,
                      date TEXT,
                      seat_number TEXT)''')
        conn.commit()
        conn.close()
        return True
    except Exception:
        return False

def add_reservation(name, flight_number, departure, destination, date, seat):
    """Add a new reservation to the database."""
    try:
        conn = connect_db()
        c = conn.cursor()
        c.execute('''INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
                     VALUES (?, ?, ?, ?, ?, ?)''', (name, flight_number, departure, destination, date, seat))
        conn.commit()
        conn.close()
        return True
    except Exception:
        return False

def get_all_reservations():
    """Retrieve all reservations from the database."""
    try:
        conn = connect_db()
        c = conn.cursor()
        c.execute("SELECT * FROM reservations")
        reservations = c.fetchall()
        conn.close()
        return reservations
    except Exception:
        return []

def update_reservation(reservation_id, name, flight_number, departure, destination, date, seat):
    """Update an existing reservation."""
    try:
        conn = connect_db()
        c = conn.cursor()
        c.execute('''UPDATE reservations SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=?
                     WHERE id=?''', (name, flight_number, departure, destination, date, seat, reservation_id))
        conn.commit()
        conn.close()
        return True
    except Exception:
        return False

def delete_reservation(reservation_id):
    """Delete a reservation by ID."""
    try:
        conn = connect_db()
        c = conn.cursor()
        c.execute("DELETE FROM reservations WHERE id=?", (reservation_id,))
        conn.commit()
        conn.close()
        return True
    except Exception:
        return False
