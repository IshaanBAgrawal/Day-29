from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    password_entry.delete(0, END)
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    rand_alpha = [choice(letters) for _ in range(randint(8, 10))]
    rand_num = [choice(numbers) for _ in range(randint(2, 4))]
    rand_char = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = rand_num + rand_char + rand_alpha
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(f"{password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def password_add():
    url_of_website = website_name.get()
    email_of_registration = email_or_username_entry.get()
    my_password = password_entry.get()

    if url_of_website != "" and my_password != "":
        is_ok = messagebox.askokcancel(title="Alert!", message=f"These are the details entered: \nEmail: "
                                                               f"{email_of_registration} \nPassword: "
                                                               f"{my_password} \nWebsite: {url_of_website}"
                                                               f"\nIs it ok to save?")

        password_info = f"{url_of_website} | {email_of_registration} | {my_password}\n"

        if is_ok:
            with open("data.txt", mode="a") as password:
                if my_password != '' or email_of_registration != '' or url_of_website != '':
                    password.writelines(f"{password_info}")

        website_name.delete(0, END)
        password_entry.delete(0, END)
        email_or_username_entry.delete(0, END)
        email_or_username_entry.insert(0, '@gmail.com')
    else:
        messagebox.showinfo(title="Error!", message="You've left some fields empty. Please fill them up!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_name = Entry(width=35)
website_name.grid(row=1, column=1, columnspan=2)
website_name.focus()

# email/user id
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

email_or_username_entry = Entry(width=35)
email_or_username_entry.grid(row=2, column=1, columnspan=2)
email_or_username_entry.insert(0, '@gmail.com')

# password
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

password_generator = Button(text="Generate Password", command=password_generate)
password_generator.grid(row=3, column=2)

# adding data
add_button = Button(width=36, text="Add", command=password_add)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
