import tkinter as tk

root = tk.Tk()
root.wm_geometry("400x400")

frameOne = tk.Frame(root, bg = "blue", width = 250, height = 200)
frameTwo = tk.Frame(root, bg = "green", width = 150, height = 200)
frameThree = tk.Frame(root, bg = "red", width = 250, height = 200)
frameFour = tk.Frame(root, bg = "yellow", width = 150, height = 200)

frameOne.grid(row=0, column=0)
frameTwo.grid(row=0, column=1)
frameThree.grid(row=1, column=0)
frameFour.grid(row=1, column=1)

root.mainloop()