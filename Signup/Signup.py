from pathlib import Path
import bcrypt

# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import mysql.connector

class UserManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.configure(bg="#FFFFFF")

        self.ASSETS_PATH = Path(r"C:\Users\hp\OneDrive\Desktop\⠀\py\py\Sign up\assets1\frame0")

        self.canvas = Canvas(
            self.root,
            bg="#FFFFFF",
            height=768,
            width=1366,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            1085.9999694824219,
            497.99999734533776,
            1199.9999694824219,
            558.9999973453378,
            fill="#FFFFFF",
            outline=""
        )

        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(
            938.0000076293945,
            62.99999800082878,
            image=self.image_image_1
        )

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.canvas.create_image(
            937.5000152587891,
            362.9999820865487,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#F2F4F7",
            fg="#000716",
            highlightthickness=0,
            font=('Helevetica', 14)
        )
        self.entry_1.place(
            x=769.0000152587891,
            y=346.9999820865487,
            width=337.0,
            height=30.0
        )

        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.canvas.create_image(
            937.4999980926514,
            457.99999734533776,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#F2F4F7",
            fg="#000716",
            highlightthickness=0,
            font=('Helevetica', 14)
        )
        self.entry_2.place(
            x=768.9999980926514,
            y=441.99999734533776,
            width=337.0,
            height=30.0
        )

        self.entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.canvas.create_image(
            937.5000133514404,
            271.99999734533776,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#F2F4F7",
            fg="#000716",
            highlightthickness=0,
            font=('Helevetica', 14),
            show="*"
        )
        self.entry_3.place(
            x=769.0000133514404,
            y=255.99999734533776,
            width=337.0,
            height=30.0
        )

        self.entry_image_4 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        self.canvas.create_image(
            937.5000228881836,
            179.99999734533776,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#F2F4F7",
            fg="#000716",
            highlightthickness=0,
            font=('Helevetica', 14)
        )
        self.entry_4.place(
            x=769.0000228881836,
            y=162.99999734533776,
            width=337.0,
            height=32.0
        )

        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.canvas.create_image(
            959.0000152587891,
            171.00000649660836,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.canvas.create_image(
            959.0,
            356.99999037143425,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))
        self.canvas.create_image(
            958.9999847412109,
            452.0000056302233,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(file=self.relative_to_assets("image_5.png"))
        self.canvas.create_image(
            958.0000076293945,
            262.99999331974647,
            image=self.image_image_5
        )

        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.save_data(self.connect_to_mysql()),
            relief="flat"
        )
        self.button_1.place(
            x=1142.9999389648438,
            y=558.9999818165961,
            width=114.00704327787389,
            height=60.01338222796039
        )

        self.canvas.create_text(
            719.9999771118164,
            655.00002781691,
            anchor="nw",
            text="Already have an account",
            fill="#475466",
            font=("Inter Medium", 16 * -1)
        )

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=930.9999847412109,
            y=654.9999952051076,
            width=169.00281731114956,
            height=24.019838566011458
        )

        self.image_image_6 = PhotoImage(file=self.relative_to_assets("image_6.png"))
        self.canvas.create_image(
            327.0,
            383.0834734252045,
            image=self.image_image_6
        )

        self.root.resizable(False, False)

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def connect_to_mysql(self, host="localhost", user="your_username", password="your_password", database="your_database_name"):
        try:
            mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                password='abdoSAOUF2004@',
                database='gestion_labo',
                auth_plugin='mysql_native_password'  # Add this if using an older MySQL version
            )
            print("Connected to MySQL database")
            return mydb  # Return the connection object
        except mysql.connector.Error as err:
            print(f"Error connecting to database: {err}")
            return None  # Return None if connection fails
    def hash_password(self, password):
        # Convert the password to bytes
        password_bytes = password.encode('utf-8')
        # Generate a salt and hash the password
        hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        return hashed
    def save_data(self, db):
        if db is None:
            print("Database connection failed. Cannot save data.")
            return

        cursor = db.cursor()
        user_name = self.entry_4.get()
        user_password = self.hash_password(self.entry_3.get())
        user_role = self.entry_1.get()
        employee_id = self.entry_2.get()

        sql = "INSERT INTO users (user_name, user_password, user_role, employee_id) VALUES (%s, %s, %s,%s)"
        values = (user_name, user_password, user_role, employee_id)
        try:
            cursor.execute(sql, values)
            db.commit()
            print("Data inserted successfully")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

if __name__ == "__main__":
    root = Tk()
    app = UserManagementApp(root)
    root.mainloop()
