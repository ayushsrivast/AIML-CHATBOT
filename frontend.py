import tkinter as tk
from tkinter import font
import aiml
import os


#to define the height and width of the UI window
HEIGHT = 479
WIDTH = 479

#AIML usage to obtain reply from the bot
kernel = aiml.Kernel()


#to not have to train AIML files everytime we run the program, this if-else statements overpasses the creation of .brn file if already exists
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
 else:
    kernel.bootstrap(learnFiles = "startup.xml", commands = "LOAD AIML B")
    kernel.saveBrain("bot_brain.brn")


#function created to obtain bot reply by input of message string, bot reply is returned which is shown on label on UI, this funcion is called everytime the get repy button is pressed and the string in entry is passed as input
def main(message):
	bot_response = kernel.respond(message)
	res=str(bot_response)
	label['text']= res


#using tkinter library the window components is put under root and root.mainloop
root = tk.Tk()

canvas = tk.Canvas(root,height=HEIGHT, width=WIDTH)
canvas.pack()


#to put a background image
background_image = tk.PhotoImage(file='me.png')
background_label = tk.Label(root, image= background_image)
background_label.place(relwidth=1, relheight=1)


#frame for uper part
frame = tk.Frame(root, bg='grey', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75,relheight=0.1, anchor='n')


#entry box for passing input
entry = tk.Entry(frame,bg='#59b659', font = ('Modern',12,'bold'))
entry.place(relwidth=0.65, relheight=1)


#button to be pressed to call function
button = tk.Button(frame, text="Get Reply", font = ('Modern',13), command=lambda : main(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)


#lower frame
lower_frame = tk.Frame(root, bg='#e58377', bd=10)
lower_frame.place(relx=0.5,rely=0.25, relwidth=0.75, relheight=0.6, anchor= 'n')

#label to show bot answer
label = tk.Label(lower_frame, font = ('Modern',11), anchor = 'nw', justify='left', bd=4, wraplength = 300)
label.place(relwidth=1, relheight=1)


root.mainloop()
