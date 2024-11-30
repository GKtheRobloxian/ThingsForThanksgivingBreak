import tkinter

root = tkinter.Tk()

def PrintName():
    print("Hello my name is Abida")

buttonOne = tkinter.Button(root, text = "Print my name", command = PrintName)
buttonOne.pack()

root.mainloop()