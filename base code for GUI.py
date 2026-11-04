import tkinter as tk

root = tk.Tk()

root.title("My Tkinter App")

root.geometry("300x300")

root.mainloop()

label = tk.Label(root, text="Hello, Tkinter!")
label.place (x=100, y=150)

button = tk.Button(root, text="Click Me!", command=lambda: print("Button Clicked!"))    
button.place(x=100, y=200)

#start the main event loop
root.mainloop()