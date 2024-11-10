import tkinter as tk
from tkinter import messagebox
import requests
import json
import admin

class LogIn(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        tk.Label(self, text='Username:').pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()
        tk.Label(self, text='Password:').pack()
        self.password_entry = tk.Entry(self)
        self.password_entry.pack()
        self.login_btn = tk.Button(self, text='Log in', command=self.login)
        self.login_btn.pack()
        self.session = requests.Session()
        self.res_lb = tk.Label(self)
        self.res_lb.pack()
        self.mainloop()
    
    def login(self):
        url = "https://127.0.0.1:5000/api/auth/login"

        payload = json.dumps({
        "username": self.username_entry.get(),
        "password": self.password_entry.get()
        })
        headers = {
        'Content-Type': 'application/json',
        'Cookie': 'session=eyJhY2NvdW50SWQiOjJ9.ZzCzww.fwI0lJsZtaOV5ACoq1vGkF2NU1Q'
        }

        response = self.session.request("POST", url, headers=headers, data=payload, verify=False)

        res_json = json.loads(response.text)
        if res_json['success'] == True:
            messagebox.showinfo(title='Info', message=res_json['message'])
            self.withdraw()
            admin_window = admin.Admin(self.session)
        else:
            messagebox.showerror(title='Error', message=res_json['message'])

a = LogIn()