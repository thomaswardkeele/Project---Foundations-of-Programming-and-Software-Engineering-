import tkinter as tk
from tkinter import messagebox
import csv
import os
import math

#main window
root = tk.Tk()
root.geometry("350x350")
root.title("Budget Tracker")

#clearing a preivous menu

def menuclear():    
    for widget in root.winfo_children():
        widget.destroy()

#creating headings

def heading(text):
    tk.Label(root, text=text, font=("Arial", 16)).pack(pady=15)

#creating buttons

def button(text,function):
    tk.Button
    (   root,
    
        font = ("Arial, 12"),
        width=25
        command = function 
    ).pack (pady = 5)

#main menu

def menu_1():
    menuclear()

    heading("Welcome to Bidget Tracker")

    button("Add Income" ,




root.mainloop()
