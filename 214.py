import tkinter as tk
import multifactorgui

def TestMyButton():
    frameAuth.tkraise()
    passwordGet = ent_password.get()
    authLabel.config(text = passwordGet)

# main window
root = tk.Tk()
root.wm_geometry("400x400")
root.title("Authorization")
frameLogin = tk.Frame(root)
frameLogin.grid(row = 0, column = 0, sticky = "news")
frameAuth = tk.Frame(root)
frameAuth.grid(row = 0, column = 0, sticky = "news")
authLabel = tk.Label(frameAuth, text = "lol")
authLabel.pack()
lblUsername = tk.Label(frameLogin, text="Username:")
lblUsername.pack()
ent_username = tk.Entry(frameLogin, bd=3)
ent_username.pack(pady=5)
labeel = tk.Label(frameLogin, text = "Password:", font = "Courier")
labeel.pack()
ent_password = tk.Entry(frameLogin, bd=3, show = "*")
ent_password.pack(pady=5)
loginButton = tk.Button(frameLogin, text = "Login", command = TestMyButton)
loginButton.pack()
frameLogin.tkraise()
root.mainloop()