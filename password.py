from tkinter import *
import random
import string
from random import randint
import tkinter.messagebox as tmsg
import tkinter as tk

root = Tk()
try:
    root.iconbitmap('password.ico')  
except tk.TclError as e:
        print(f"Error: {e}. Icon not found or invalid.")
        
maxwidth = 760
maxheight = 680
root.minsize(maxwidth, maxheight)
root.maxsize(maxwidth, maxheight)
root.title("Password Generator")
frame = Frame(root)
Label(frame, text="Password generator", anchor=N, font=("bear", 30), fg="#239B56").pack(side=TOP)
frame.pack(pady=10)
password = None

# Logic of password generator- so there will be many levels
# Level-1 (basic) - only numbers
# Level-2 () - only alphabets() either uppercase or lowercase each time
# Level-3 () - uppercase_lowercase alphabets + numbers
# Level-4 () - special characters + UC_LC alphabets
# Level-5 () - special characters + UC_LC alphabets + Numbers
frame2 = Frame(root)
Label(frame2, text="#Choose difficulty level for your Password (:)", fg="#28B463", anchor=W, font=("bear", 20)).pack(side=TOP)
frame2.pack(pady=10, fill=X)

frame3 = Frame(root)
frame3.pack()

special_characters = ['@', '#', '$', '&', '-', '_', '*']

def l1():
    global b1, password
    b1 = True
    length = myslider.get()
    password = ""
    while(len(password)!=length):
        p = randint(0,9)
        password += str(p)
        
def l2():
    global b2, password
    b2 = True
    length = myslider.get()
    password = ""
    upcase_locase = randint(0,1)
    if upcase_locase == 0:
        while(len(password)!=length):
            random_char = (random.choice(string.ascii_letters))
            password+=random_char.upper()
    else:
        while(len(password)!=length):
            random_char = (random.choice(string.ascii_letters))
            password+=random_char.lower()
            
def l3():
    global b3, password
    b3 = True
    length = myslider.get()
    password = ""
    while (len(password)!=length):
        num = randint(0, 9)
        if num>=8:
            num2 = str(randint(0,9))
            password+=num2
        else:
            random_char = (random.choice(string.ascii_letters))
            password+=random_char

def l4():
    global b4, password
    b4 = True
    length = myslider.get()
    password = ""
    while (len(password)!=length):
        num = randint(0, 9)
        if num>=7:
            num2 = randint(0, len(special_characters)-1)
            special_char = special_characters[num2]
            password+=special_char
        else:
            random_char = random.choice(string.ascii_letters)
            password+=random_char
        
def l5():
    global b5, password
    b5 = True
    length = myslider.get()
    password = ""
    while (len(password)!=length):
        num = randint(0,9)
        if num>=7:
            num2 = randint(0, len(special_characters)-1)
            password+=special_characters[num2]
        elif(num>=5 and num<7):
            num2 = str(randint(0, 9))
            password+=num2
        else:
            random_char = random.choice(string.ascii_letters)
            password+=random_char
            
def otp():
    global otps
    otps = ""
    while len(otps) != 4:
        num = str(randint(0,9))
        otps+=num
    
def show_password():
    if password:
        text = texts.get(1.0, END)
        if len(text)>0:
            texts.delete(1.0, END)
            texts.insert(1.0, password)
        else:
            texts.insert(1.0, password)
    else:
        l3()
        text = texts.get(1.0, END)
        if len(text)>0:
            texts.delete(1.0, END)
            texts.insert(1.0, password)
        else:
            texts.insert(1.0, password)
        
    
def show_otp():
    otp()
    tmsg.showinfo("OTP generated", f"{otps}")
    
Button(frame3, text="Level-1", font="bear 20", borderwidth=15, padx=3, pady=3, fg="#3498DB", command=l1).grid(row=3, column=1, padx=20, pady=3)
Button(frame3, text="Level-2", font="bear 20", borderwidth=15, padx=3, pady=3, fg="#2E86C1", command=l2).grid(row=3, column=2, padx=20, pady=3)
Button(frame3, text="Level-3", font="bear 20", borderwidth=15, padx=3, pady=3, fg="#2874A6", command=l3).grid(row=3, column=3, padx=20, pady=3)

frame4 = Frame(root)
frame4.pack()
Button(frame4, text="Level-4", font="bear 20", borderwidth=15, padx=3, pady=3, fg="#21618C",  command=l4).grid(row=4, column=2, padx=20, pady=7)
Button(frame4, text="Level-5", font="bear 20", borderwidth=15, padx=3, pady=3, fg="#1B4F72", command=l5).grid(row=4, column=3, padx=20, pady=7)

frame5 = Frame(root)
frame5.pack(pady=10)
Label(frame5, text="#Choose the length of Password (:)", fg="#28B463", anchor=N, font=("bear", 20)).pack()

myslider = Scale(frame5, from_=4, to=16, orient=HORIZONTAL, fg="#28B463", tickinterval=4, width=25, font="bear 15", length=200)
myslider.set(6)
myslider.pack()

frame5 = Frame(root)
frame5.pack(pady=10)
Button(frame5, text="Generate Password", font="bear 20", fg="#DE3163", borderwidth=20,  padx=5, pady=5, command=show_password).grid(row=0, column=1, padx=10)
Button(frame5, text="Generate OTP", font="bear 20", fg="#E74C3C", borderwidth=20,  padx=5, pady=5,   command=show_otp).grid(row=0, column=0, padx=10)

frame6 = Frame(root)
frame6.pack(pady=10)
texts = Text(frame6, height=5, fg="#DE3163", font="bear 26", padx=290, pady=23)
texts.pack(expand=True)

root.mainloop()