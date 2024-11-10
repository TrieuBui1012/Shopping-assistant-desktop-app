import tkinter as tk
from tkinter import messagebox
import requests
import json

class Admin(tk.Toplevel):
    def __init__(self, session = requests.Session()):
        super().__init__()
        self.title('Admin')
        self.geometry('720x720')
        self.session = session
        self.res_lb = tk.Label(self)
        self.res_lb.pack()

        url = "https://127.0.0.1:5000/api/admin/manage_users"

        payload = {}
        headers = {}

        response = self.session.request("GET", url, headers=headers, data=payload, verify=False)

        res_json = json.loads(response.text)
        if res_json['success'] == True:
            self.res_lb.config(text=res_json['data'])
        else:
            self.res_lb.config(text='You are not an admin')