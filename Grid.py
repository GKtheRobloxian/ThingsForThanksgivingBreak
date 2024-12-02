import tkinter as tk

root = tk.Tk()
root.wm_geometry("400x400")

frameOne = tk.Frame(root, bg = "blue", width = 250)
frameTwo = tk.Frame(root, bg = "green", width = 150)

frameOne.grid(row = 0, column = 0, rowspan = 200, sticky=tk.W+tk.N+tk.E)
frameTwo.grid(row = 0, column = 1, rowspan = 200, sticky=tk.W+tk.N+tk.E)

root.mainloop()