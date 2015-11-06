from Tkinter import *
from morse import *

window = Tk()

l = Label(window, text = "Enter text to listen to Morse code of: ")

var = StringVar()

messages = Frame(window)                         #separate Frame that gets destroyed and repacked

e = Entry(window, textvariable = var)


def butFunc(arg = None):                        #event manager
    
    for widget in messages.winfo_children():     #destroys already packed labels
        widget.destroy()
        messages.pack()
    try:
        trans = morsify(var.get())              #sounds Morse code
        ans = Label(messages, text = trans, bg = "orange")
        ans.pack(fill=X)                        #packs transcript label
    except KeyError:                            #handles foreign characters with error message
        err = Label(messages, text="You have entered a character that may not have a Morse equivalent.", bg="crimson")
        err.pack()    

def more():
    global s
    s+=1
    print s

def less():
    global s
    s-=1
    print s

b = Button(window, text = "Go!", bg = "brown", fg = "gray", command = butFunc)
b.bind('<Return>', butFunc)                     #binds <Return> to butFunc

plus = Button(window, text="+", bg = "brown", fg = 'gray', command = more)
minus = Button(window, text="-", bg = "brown", fg = 'gray', command = less)

l.pack(fill=X)
e.pack(fill=X)
plus.pack(side=RIGHT, padx = 50)
minus.pack(side=LEFT, padx = 50)
b.pack(pady = 5)
e.focus()

window.mainloop() 
