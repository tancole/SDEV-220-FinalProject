"""
SDEV-220 Final Project
Flashcard Learning App

The intention of our project is to design a learning 
tool that can be used by schools or any type of 
educational organizations to use to help create
study materials for their students. We are going to 
use programming terms as our example for this proposal.

Authors:
Tanner Cole
Lamarana Diallo
Roan Campbell
"""
#tkinter gui set up
from tkinter import *
from random import randint

root =Tk()
root.title('Computer Programming Flashcard')
root.geometry("550x410")
#word list for flashcards
words = [
      (("HTML"), ("Hyper Text Markup Language")),
      (("Algorithm"), ("A set of instructions used to solve a problem")),
      (("API"), ("Application programming interface")),
      (("Boolean"), ("True or False")),
      (("Class"), ("Set of related objects with common characteristics")),
      (("Data Type"), ("What a variable or object can hold in computer programming.")),
      (("EOF"), ("End of file")),
      (("Bit"), ("The individual 1's and 0's you see in binary are called bits. ")),
      (("Else Statements"), ("Else statements are used to do something else when the condition in the if statement isn't true.")),
      (("Input"), ("Input is any interaction from the user to the program. In video games, this includes using the keyboard to move or using the mouse to look around.")),
      (("Strings"), ("Variables can hold data besides numbers, including words. Programmers refer to variables holding words as strings.")),
      (("Terminal"), ("Terminal is a text-based interface for sending commands to a computer."))
      ]

#creating a count
count = len(words)

def next():
    #clear screen
    answer_label.config(text="")
    entry_box.delete(0, END)
    
    #random word selection
    global random_word
    random_word = randint(0, count-1)
    #Vocab word configuration
    vocab_word.config(text=words[random_word][0])

def answer():
    if entry_box.get().capitalize == words[random_word][1]:
        answer_label.config(text=f"That's Correct!{words[random_word][0]} is {words[random_word][1]}")
    else:
        answer_label.config(text=f"Incorrect, try again!{words[random_word][0]} is not {entry_box.get().capitalize}")

#vocab word 
vocab_word = Label(root, text="", font=("Helvetica", 36))
vocab_word.pack(pady=50)

#answer display
answer_label = Label(root, text="")
answer_label.pack(pady=20)

#entry box
entry_box = Entry(root, font=("Helvetica", 18))
entry_box.pack(pady=20)

#button creation
button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row="0", column="0", padx=20)

next_button = Button(button_frame, text="Next", command=next)
next_button.grid(row="0", column="1")

help_button = Button(button_frame, text="Need help?")
help_button.grid(row="0", column="2", padx=20)

#Create Hint Label
help_label = Label(root, text="")
help_label.pack(pady=20)

# Run next function when studying begins 
next()





root.mainloop()