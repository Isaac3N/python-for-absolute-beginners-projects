
from tkinter import*

class Application(Frame):
    """ Gui application for favorite movie"""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        """ create widgets for movie type choices """
        # create description label
        Label(self,
              text = "choose your favorite movie").grid(row = 0, column = 0, sticky = W)

        Label(self,
              text = "choose as follows").grid(row = 1, column = 0, sticky = W)

        # creates drama check button
        self.likesDrama = BooleanVar()
        Checkbutton(self,
                    text = "Drama" ,
                    variable = self.likesDrama,
                    command = self.upadateText
                    ).grid(row = 2, column = 0, sticky = W)

        # creates comedy check button
        self.likesComedy = BooleanVar()
        Checkbutton(self,
                    text = "Comedy" ,
                    variable = self.likesComedy,
                    command = self.upadateText
                    ).grid(row = 3, column = 0, sticky = W)

        # creates romance check button
        self.likesRom = BooleanVar()
        Checkbutton(self,
                    text = "Romance" ,
                    variable = self.likesRom,
                    command = self.upadateText
                    ).grid(row = 4, column = 0, sticky = W)
        self.result_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.result_txt.grid(row = 5, column = 0, columnspan = 3)


    def upadateText(self):
        """ update text and display users favorite movie"""
        likes = ""

        if self.likesComedy.get():
            likes = "you like comedic movies \n"
        if self.likesRom.get():
            likes = "you like romantic movies \n"
        if self.likesDrama.get():
            likes = "you like dramatic movies \n"

            self.result_txt.delete(0.0, END)
            self.result_txt.insert(0.0, likes)

 # main
root = Tk()
root.title("Movie Chooser")
app = Application(root)
root.mainloop()             
                            
            
              




































              
