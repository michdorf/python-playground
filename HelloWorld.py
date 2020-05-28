import tkinter as Tk
import requests as req

ALLAN = "et navn"

class App:

    def __init__(self, master):

        frame = Tk.Frame(master)
        frame.pack()

        self.button = Tk.Button(
            frame, text="CHIUDI", fg="red", command=frame.quit
        )
        self.button.pack(side=Tk.LEFT)

        self.hiThere = Tk.Button(frame, text="Ciao", command=self.richiedi)
        self.hiThere.pack(side=Tk.LEFT)
        
        self.w = Tk.Spinbox(frame, values=(1, 2, 4, 8))
        self.w.pack(side=Tk.RIGHT)

    def sayHi(self):
        print ("Ciao ragazzi!")

    def richiedi(self):
        r = req.get("https://dechiffre.dk/webApp/api/onlinefile.txt")
        print (r.text)
    
root = Tk.Tk()

app = App(root)

root.mainloop()
root.destroy() # optional