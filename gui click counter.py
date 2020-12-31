from tkinter import*

class Application(Frame):
    """ A gui application with two buttons"""

    def __init__(self, master):
        """ initialize the frame """
        super(Application, self).__init__(master)
        self.grid()
        self.buttonClicks = 0 # the number of button clicks
        self.createWidgets()


    def createWidgets(self):
        """ create a button which displays the number of clicks """
        self.button = Button(self,text = "Total clicks: 0")
        #self.button["text"] = "Total Clicks: 0"
        self.button["command"] = self.updateCount
        self.button.grid()

    def updateCount(self):
         """ increase the click count and the display the number"""
         self.buttonClicks += 1
         self.button["text"] = "Total Clicks: " + str(self.buttonClicks)


 # main
root = Tk()
root.title("Click Counter")
root.geometry("200x50")
app = Application(root)
root.mainloop()       
        
    
