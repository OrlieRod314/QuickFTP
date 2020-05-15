import tkinter as tk
from ftplib import FTP
import time

FIELD_LENGTH = 50
VALID_RUN = True

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Labels and entry fields
        
        # Domain name
        self.domain_label = tk.Label(self)
        self.domain_label["text"] = "Domain: "
        self.domain_label.pack(side="top")
        
        self.domain_name = tk.Entry(self)
        self.domain_name["width"] = FIELD_LENGTH
        self.domain_name.pack()
        
        # Subdomain
        self.sub_domain_label = tk.Label(self)
        self.sub_domain_label["text"] = "Specific domain or location: "
        self.sub_domain_label.pack(side="top")
        
        self.sub_domain_name = tk.Entry(self)
        self.sub_domain_name["width"] = FIELD_LENGTH
        self.sub_domain_name.pack()
        
        # Username
        self.uname_label = tk.Label(self)
        self.uname_label["text"] = "Username: "
        self.uname_label.pack(side="top")
        
        self.user_name = tk.Entry(self)
        self.user_name["width"] = FIELD_LENGTH
        self.user_name.pack()
        
        # Password
        self.pass_label = tk.Label(self)
        self.pass_label["text"] = "Password: "
        self.pass_label.pack(side="top")
        
        self.password = tk.Entry(self)
        self.password["width"] = FIELD_LENGTH
        self.password.pack()
        
        # Buttons for connecting and quitting
        self.connect = tk.Button(self)
        self.connect["text"] = "Connect"
        self.connect["command"] = self.transfer
        self.connect.pack(side="top")
        
        self.quit = tk.Button(self, text="QUIT", fg="red",
                                command=self.master.destroy)
        self.quit.pack(side="bottom")

    def transfer(self):
        domain = self.domain_name.get()
        subdomain = self.sub_domain_name.get()
        username = self.user_name.get()
        password = self.password.get()
        
        print("CONNECTING\n")

        try:
            ftp = FTP(domain)
            ftp.login(username, password)
            ftp.cwd(subdomain)
        except AttributeError:
            self.error_label = tk.Label(self)
            self.error_label["text"] = "Fields must be filled\nCLOSING APPLICATION IN 5 SECONDS"
            self.error_label.pack(side="top")
            self.after(5000, root.destroy)
            VALID_RUN = False
        
        if VALID_RUN:
            print("CONNECTED")
            # Connect button changed to reflect established connection
            self.connect["text"] = "Connected!"
            self.connect["fg"] = "green"
            
            # Input for file name
            self.file_name_label = tk.Label(self)
            self.file_name_label["text"] = "File name: "
            self.file_name_label.pack(side="top")
            
            self.file_name = tk.Entry(self)
            self.file_name["width"] = FIELD_LENGTH
            self.file_name.pack()
            
            # Buttons for storing and retrieving
            self.store = tk.Button(self)
            self.store["text"] = "STORE"
            self.store["command"] = self.store
            self.store.pack(side="top")
            
            self.retrieve = tk.Button(self)
            self.retrieve["text"] = "RETRIEVE"
            self.retrieve["command"] = self.retrieve
            self.retrieve.pack(side="top")
    
    def store():
        filename = self.file_name.get()
        local_file = open(filename, 'wb')
        ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
        ftp.quit()
        local_file.close()
    
    def retrieve():
        filename = self.file_name.get()
        ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
        ftp.quit()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
