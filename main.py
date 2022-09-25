from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from password_generator import Password_Generator


def generate_pass():
    password_gen = Password_Generator().password
    pass_textbox.insert(0, password_gen)
    pyperclip.copy(password_gen)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    global website_name, username_textbox, pass_textbox
    website = website_name.get()
    username = username_textbox.get()
    password = pass_textbox.get()
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="You have left some fields empty!")
    else:
        try:
            with open("data.json", mode="r") as file:
                # reading old data
                data = json.load(file)
                # updating old data
                data.update(new_data)

        except FileNotFoundError:
            data = new_data

        finally:
            with open("data.json", "w") as file:
                # saving new data
                json.dump(data, file, indent=4)
                website_name.delete(0, END)
                pass_textbox.delete(0, END)


# ---------------------------- SEARCH FUNCTIONALITY ------------------------------- #

def search():
    global website_name, username_textbox, pass_textbox

    try:
        with open("data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showwarning(title="Oops", message="Please insert some data first.")

    else:
        try:
            website = data[website_name.get()]
            email = website["email"]
            password = website["password"]
        except KeyError:
            messagebox.showwarning(title="Oops", message="No data found or enter correct data!")
        else:
            messagebox.showinfo(title=website, message=f"email: {email}\npassword: {password}")

    finally:
        website_name.delete(0, END)
        pass_textbox.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20, bg="white")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 110, image=lock_image)

label1 = Label(text="Website:", bg="white")
label1.grid(row=1, column=0)
website_name = Entry(width=32)
website_name.focus()
website_name.grid(row=1, column=1)

label2 = Label(text="Email/Username:", bg="white")
label2.grid(row=2, column=0)
username_textbox = Entry(width=39, background="white")
username_textbox.insert(0, "example@gmail.com")
username_textbox.grid(row=2, column=1, columnspan=2, sticky="EW")

label3 = Label(text="Password:", bg="white")
label3.grid(row=3, column=0)
pass_textbox = Entry(width=19, background="white")
pass_textbox.grid(row=3, column=1, sticky="EW")

search_button = Button(text="Search", bg="white", width=14, command=search)
search_button.grid(row=1, column=2, sticky="EW")
gen_pass_button = Button(text="Generate Password", bg="white", width=14, command=generate_pass)
gen_pass_button.grid(row=3, column=2, sticky="EW")
add_button = Button(text="Add", width=35, background="white", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


canvas.grid(row=0, column=1)
window.mainloop()
