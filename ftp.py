import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.connect = tk.Button(self)
        self.connect["text"] = "Connect"
        self.connect["command"] = self.transfer
        self.connect.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                                command=self.master.destroy)
        self.quit.pack(side="bottom")

    def transfer(self):
        print("CONNECTING\n")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
