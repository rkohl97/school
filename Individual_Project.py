import tkinter as tk
import sqlite3
from datetime import date
from tkinter import messagebox
from PIL import Image, ImageTk

class FitnessTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fitness Tracker")

        # Connect to the database with a specific date adapter
        self.conn = sqlite3.connect("fitness_tracker.db", detect_types=sqlite3.PARSE_DECLTYPES)
        self.cur = self.conn.cursor()

        # Create exercise table if not exists
        self.cur.execute('''CREATE TABLE IF NOT EXISTS exercise (
                            date DATE,
                            pushups INTEGER,
                            crunches INTEGER,
                            pullups INTEGER,
                            running_miles REAL
                            )''')
        self.conn.commit()

        # Create calorie intake table if not exists
        self.cur.execute('''CREATE TABLE IF NOT EXISTS calorie_intake (
                            date DATE,
                            calories INTEGER
                            )''')
        self.conn.commit()

        # Create weight table if not exists
        self.cur.execute('''CREATE TABLE IF NOT EXISTS weight (
                            date DATE,
                            weight_pounds REAL
                            )''')
        self.conn.commit()

        # Load logo image
        self.logo_image = Image.open("fitness.jpg")
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)

        # Create GUI components
        self.logo_label = tk.Label(root, image=self.logo_photo)
        self.logo_label.pack()

        # Rest of the GUI components
        self.label_pushups = tk.Label(root, text="Pushups:")
        self.label_pushups.pack()
        self.entry_pushups = tk.Entry(root)
        self.entry_pushups.pack()

        self.label_crunches = tk.Label(root, text="Crunches:")
        self.label_crunches.pack()
        self.entry_crunches = tk.Entry(root)
        self.entry_crunches.pack()

        self.label_pullups = tk.Label(root, text="Pullups:")
        self.label_pullups.pack()
        self.entry_pullups = tk.Entry(root)
        self.entry_pullups.pack()

        self.label_running = tk.Label(root, text="Running (miles):")
        self.label_running.pack()
        self.entry_running = tk.Entry(root)
        self.entry_running.pack()

        self.btn_track_exercise = tk.Button(root, text="Track Exercise", command=self.track_exercise)
        self.btn_track_exercise.pack()

        self.label_calories = tk.Label(root, text="Calories Eaten Today:")
        self.label_calories.pack()
        self.entry_calories = tk.Entry(root)
        self.entry_calories.pack()

        self.btn_track_calories = tk.Button(root, text="Track Calories", command=self.track_calories)
        self.btn_track_calories.pack()

        self.label_weight = tk.Label(root, text="Weight (pounds):")
        self.label_weight.pack()
        self.entry_weight = tk.Entry(root)
        self.entry_weight.pack()

        self.btn_track_weight = tk.Button(root, text="Track Weight", command=self.track_weight)
        self.btn_track_weight.pack()

        self.btn_view_saved_data = tk.Button(root, text="View Saved Data", command=self.view_saved_data)
        self.btn_view_saved_data.pack()

    def track_exercise(self):
        pushups = int(self.entry_pushups.get())
        crunches = int(self.entry_crunches.get())
        pullups = int(self.entry_pullups.get())
        running_miles = float(self.entry_running.get())

        # Insert exercise data into database
        self.cur.execute("INSERT INTO exercise (date, pushups, crunches, pullups, running_miles) "
                         "VALUES (?, ?, ?, ?, ?)",
                         (date.today(), pushups, crunches, pullups, running_miles))
        self.conn.commit()
        messagebox.showinfo("Success", "Exercise tracked successfully!")

    def track_calories(self):
        calories = int(self.entry_calories.get())

        # Insert calorie intake data into database
        self.cur.execute("INSERT INTO calorie_intake (date, calories) VALUES (?, ?)",
                         (date.today(), calories))
        self.conn.commit()
        self.check_calorie_intake(calories)

    def track_weight(self):
        weight_pounds = float(self.entry_weight.get())

        # Insert weight data into database
        self.cur.execute("INSERT INTO weight (date, weight_pounds) VALUES (?, ?)",
                         (date.today(), weight_pounds))
        self.conn.commit()
        messagebox.showinfo("Success", "Weight tracked successfully!")

    def check_calorie_intake(self, calories):
        if calories < 2000:
            messagebox.showwarning("Reminder", "You've consumed less than 2000 calories today. Remember to eat more!")
        elif 2000 <= calories <= 3000:
            messagebox.showinfo("Recommended", "You've consumed a healthy amount of calories today.")
        else:
            messagebox.showwarning("Warning", "You've consumed more than 3000 calories today. Consider reducing your intake.")

    def view_saved_data(self):
        # Retrieve saved data from the database
        self.cur.execute("SELECT * FROM exercise")
        exercise_data = self.cur.fetchall()

        self.cur.execute("SELECT * FROM calorie_intake")
        calorie_intake_data = self.cur.fetchall()

        self.cur.execute("SELECT * FROM weight")
        weight_data = self.cur.fetchall()

        # Display saved data in a new window
        saved_data_window = tk.Toplevel(self.root)
        saved_data_window.title("Saved Data")

        tk.Label(saved_data_window, text="Exercise Data").pack()
        for data in exercise_data:
            tk.Label(saved_data_window, text=data).pack()

        tk.Label(saved_data_window, text="\nCalorie Intake Data").pack()
        for data in calorie_intake_data:
            tk.Label(saved_data_window, text=data).pack()

        tk.Label(saved_data_window, text="\nWeight Data").pack()
        for data in weight_data:
            tk.Label(saved_data_window, text=data).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessTrackerApp(root)
    root.mainloop()
