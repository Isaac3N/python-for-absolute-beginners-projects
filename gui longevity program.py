# gui longevity program
# demmonstrates text and entry widgets

from tkinter import*

class Application(Frame):
    """ gui application which can reveal the secret of a long life """
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        """ cretes buttons, text and entry widgets. """
        # creates instruction label
        self.instr_lbl = Label(self, text = "enter the password for the secret of longevity")
        self.instr_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # create label for password
        self.psw_lbl =  Label(self, text = "password: ")
        self.psw_lbl.grid(row = 1, column = 0, sticky = W)

        # create entry widget to accept password
        self.psw_entry = Entry(self)
        self.psw_entry.grid(row = 1, column = 1, sticky = W)

        # create submit button
        self.sumbitBttn = Button(self, text = "submit", command = self.reveal)
        self.sumbitBttn.grid(row = 2, column = 0, sticky = W)

        # create text widget to display message
        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD )
        self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)

    def reveal(self):
        """ reveal message based on password """
        contents = self.psw_entry.get()

        if contents == "secret":
           message = "Here's the secret to living to 100: live to 99 " \
                     "and then be VERY careful. "
           print (message)
        else:
            message ="That's not the correct password, so I can't share " \
                     "the secret with you."
            self.secret_txt.delete(0.0, END)
            self.secret_txt.insert(0.0, message)
            
# main
root = Tk()
root.title("Longevity")
root.geometry("300x150")
app = Application(root)
root.mainloop()

        
    
