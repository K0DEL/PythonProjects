import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- SEARCH ------------------------------- # noqa : E501


def search():
    website = web_entry.get()
    if website != "":
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror(
                title="Oops", message="No Passwords saved currently!")
        else:
            try:
                print(data[website])
                username = data[website]["username"]
                password = data[website]["password"]
            except KeyError:
                messagebox.showerror(
                    title="Oops",
                    message="No Passwords saved for this website!")
            else:
                messagebox.showinfo(
                    title=f"{website}",
                    message=f"These are the details that you saved earlier:"
                    f" \nEmail: {username} \nPassword: {password}")
    else:
        messagebox.showerror(
            title="Oops", message="Please don't leave website feild empty!")


# ---------------------------- PASSWORD GENERATOR ------------------------------- # noqa : E501


def password_generator():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
               'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    letter_list = [random.choice(letters)
                   for char in range(random.randint(8, 10))]

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    symbol_list = [random.choice(symbols)
                   for char in range(random.randint(2, 4))]

    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    number_list = [random.choice(numbers)
                   for char in range(random.randint(2, 4))]

    password_list.extend(letter_list)
    password_list.extend(symbol_list)
    password_list.extend(number_list)
    print(password_list)

    random.shuffle(password_list)

    password = ("").join(password_list)
    # password = ""
    # for char in password_list:
    #     password += char
    pyperclip.copy(password)

    print(f"Your password is: {password}")
    pass_entry.delete(0, tkinter.END)
    pass_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- # noqa : E501


def save_password():
    website = web_entry.get()
    username = user_entry.get()
    password = pass_entry.get()

    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if website == "" or username == "" or password == "":
        messagebox.showerror(
            title="Oops", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(
            title=f"{website}",
            message=f"These are the details that you entered:"
            f" \nEmail: {username} \nPassword: {password}")

        if is_ok:

            data = website + " | " + username + " | " + password + " \n"
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                web_entry.delete(0, tkinter.END)
                pass_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- # noqa : E501
window = tkinter.Tk()
window.title("Password Manager")
# window.minsize(width=600, height=300)
window.config(padx=50, pady=50)

# Canvas
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website Label~
web_label = tkinter.Label(text="Website:")
web_label.grid(column=0, row=1)

# Username/Email Label
user_label = tkinter.Label(text="Username/Email:")
user_label.grid(column=0, row=2)

# Password Label
pass_label = tkinter.Label(text="Password:")
pass_label.grid(column=0, row=3)

# Website Entry
web_entry = tkinter.Entry(width=20)
web_entry.grid(column=1, row=1, sticky="nsew")
web_entry.focus()

# Username/Email Entry
user_entry = tkinter.Entry(width=40)
user_entry.grid(column=1, row=2, columnspan=2, sticky="nsew")
user_entry.insert(0, "techinfinity10@gmail.com")

# Password Entry
pass_entry = tkinter.Entry(width=20)
pass_entry.grid(column=1, row=3, sticky="nsew")

# Generate Password Button
gen_pass = tkinter.Button(text="Generate Password",
                          width=20,
                          highlightthickness=0,
                          command=password_generator)
gen_pass.grid(column=2, row=3, sticky="nsew")

# Add Button
add_button = tkinter.Button(text="Add", width=40, command=save_password,)
add_button.grid(column=1, row=4, columnspan=2, sticky="nsew")

# Search Button
search_button = tkinter.Button(text="Search", width=20, command=search)
search_button.grid(column=2, row=1)


window.mainloop()
