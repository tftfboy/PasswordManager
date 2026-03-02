from tkinter import *
from tkinter import messagebox
import random
from tkinter import ttk
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8,10)
nr_symbols = random.randint(2,4)
nr_numbers = random.randint(2,4)

def generate_password():
    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    random.shuffle(password_list)

    password = "".join(password_list)
    enter_email_pass.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = enter_website.get()
    email = enter_email_user.get()
    password = enter_email_pass.get()
    if website == "" or email == "" or password == "":
        messagebox.showerror(title = "Oops",message="Please Don't leave any fields empty")
        return
    is_ok = messagebox.askokcancel(title=website,message=f"These are the details enterd : \n Email : {email} \n Password : {password} is it okay to save?")
    if is_ok:
        openfile = open("password.txt","a")
        openfile.write(website +  " | " + email + " | " + password + "\n")
        enter_website.delete(0, END)
        enter_email_pass.delete(0, END)
        openfile.close()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
window.configure(bg="white")
window.columnconfigure(0, weight=0)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=0)

style = ttk.Style(window)
style.theme_use("clam")
style.configure("TLabel", font=("Segoe UI", 11), background="white")
style.configure("TEntry", font=("Segoe UI", 11))
style.configure("Accent.TButton", font=("Segoe UI", 11, "bold"), padding=(10, 6))
style.configure("TButton", font=("Segoe UI", 10), padding=(8, 5))

canvas = Canvas(window,width=200, height=200, bg="white", highlightthickness=0)

#load Img
img = PhotoImage(file="logo.png")
#add IMG to canvas
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=0, columnspan=3, pady=(0, 16))


#Labels

web_name = ttk.Label(window,text="Website:")
web_name.grid(row=1, column=0, sticky="e", padx=(0, 10), pady=6)
email_user = ttk.Label(window,text="Email/Username:")
email_user.grid(row=2, column=0, sticky="e", padx=(0, 10), pady=6)
email_pass = ttk.Label(window,text="Password:")
email_pass.grid(row=3, column=0, sticky="e", padx=(0, 10), pady=6)

#Enteries
enter_website = ttk.Entry(width=35)
enter_website.grid(row=1, column=1, columnspan=2, sticky="ew", pady=6)
enter_website.focus()
enter_email_user = ttk.Entry(width=35)
enter_email_user.grid(row=2, column=1, columnspan=2, sticky="ew", pady=6)
enter_email_user.insert(0,"example@gmail.com")
enter_email_pass = ttk.Entry(width=35)
enter_email_pass.grid(row=3, column=1, sticky="ew", pady=6)
#Buttons
generate_password_button = ttk.Button(window,text="Generate Password",width=21,command=generate_password, style="TButton")
generate_password_button.grid(row=3, column=2, sticky="ew", padx=(8, 0), pady=6)
add_password = ttk.Button(text="Add",width=35,command=save_pass, style="Accent.TButton")
add_password.grid(row=4, column=1, columnspan=2, sticky="ew", pady=(10, 0))


window.mainloop()