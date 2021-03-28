from tkinter import *
import csv


file = open('nflroster.csv', 'r')
reader = csv.reader(file)
player = {}
for row in reader:
    player[row[0]] = {'first':row[1], 'last':row[2],'COB':row[3], 'SOB':row[4],'DOB': row[6],                                             'COL':row[7],'TEAM':row[8],
                      'DRFTYR':row[11], 'POS':row[12],'WEIGHT':row[14] }
 
root = Tk()
HEIGHT = 500
WIDTH = 950      
def format_response(name):
    first = name['first']
    last = name["last"]
    dob = name['DOB']
    cob = name['COB']
    sob = name['SOB']
    col = name['COL']
    team = name['TEAM']
    year = name['DRFTYR']
    pos = name ['POS']
    weight = name["WEIGHT"]
    return(first +" "+ last +" was born in " + str(cob) + ","+ str(sob)+ " "+ str(dob)+'.\n'
         + " He attended college at " + col +" and was\n drafted by the " + team + " in " + year +
         ".\n He played as " + pos + " and weighed " + weight + "lbs.")
      
def get_player(entry):
    name = player[entry]
    
    label['text'] = format_response(name)
    
canvas = Canvas(root, height = HEIGHT , width=WIDTH)
canvas.pack()

bg_image = PhotoImage(file = "feild.png")
bg_label = Label(root, image=bg_image)
bg_label.place(x=0,y=0,relwidth=1, relheight=1)

#Frame
frame = Frame(root, bg="brown", bd=5)
frame.place(relx = 0.5, rely=0.1, relwidth=0.75, relheight = 0.1, anchor = 'n')

entry = Entry(frame,bg = "grey", font =('Courier', 16))
entry.place(relwidth=0.65, relheight = 1)

button = Button(frame, text = "Your Pick!",bg = "grey", fg = "black", font =('Courier', 16),command=lambda: get_player(entry.get()))
button.place(relx = 0.7, relheight =1,relwidth=0.3)

lower_frame = Frame(root, bg="brown", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = Label(lower_frame, bg = "grey", font =('Courier', 16) )
label.place(relwidth=1, relheight = 1)



root.mainloop()
