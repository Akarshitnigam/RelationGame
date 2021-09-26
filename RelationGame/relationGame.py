print("Welcome to Relation Game!")
import random
from tkinter import *
rel = ["father", "mother", "sister", "brother", "grandfather","friend"]

def cal():
     choice = random.choice(rel)
     l.configure(text=f'Your friend was your {choice}')


root = Tk()
root.title("Relation Game")
root.geometry('400x300')
root['bg'] = 'black'
name1 = StringVar()
e1 = Entry(root, textvariable=name1)
e1.place(x=20, y=40)
e2= Entry(root)
e2.place(x=250, y=40)

l = Label(text="Find relation with  your friends", fg='white', bg='black', font=('verdana',10,'bold'))
l.place(x=20, y=80)

b= Button(text='Find', command = cal, bg ='yellow', fg = 'black')
b.place(x=185,y=180)


root.mainloop()






root.mainloop()
