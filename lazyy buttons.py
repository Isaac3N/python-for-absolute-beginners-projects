from tkinter import*

# creating a root window
root = Tk()

# modifyin the root window
root.title("Lazy buttons")
root.geometry("200x85")

# create the frame on the windows for other widgets
app = Frame(root)
app.grid()

# create the first button
button1 = Button(app, text = "I do nothing")
button1.grid()

# create the second button
button2 = Button(app)
button2.grid()
button2.configure(text = "me too")

root.mainloop()
