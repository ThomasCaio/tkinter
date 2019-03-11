import tkinter as tk
from app_widgets.main_widgets import Menubar
from tkinter import ttk
import sqlite3 as sql

conn = sql.connect(database='data.db')
c = conn.cursor()

class Login(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        from content.center import center

        self.geometry('300x200')
        self.title('Login')
        self.access_value = 0
        userlabel = tk.Label(self, text='Usuário')
        passwlabel= tk.Label(self, text='Senha')
        userentry = ttk.Entry(self)
        passwentry = ttk.Entry(self, show='*')
        but = ttk.Button(self, text='Validar', command=lambda: self.password_check([userentry.get(),passwentry.get()]))

        userlabel.pack()
        userentry.pack()
        passwlabel.pack()
        passwentry.pack()
        userentry.focus()
        but.pack(pady=20)

        self.init_window()
        center(self)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.focus_force()

    def init_window(self):
        Menubar(self)

    def password_check(self, data):
        try:
            user, passw = data
            c.execute("SELECT username, password, access FROM users WHERE username = ? AND password = ?",(user, passw))
            result = list(c.fetchone())
            if result is not None:
                if result[2] is None or result[2] is '':
                    result[2] = 0
                self.start_program(result[2])
        except TypeError:
            pass

    def on_closing(self):
        self.quit()
        self.destroy()

    def start_program(self,access):
        import main
        self.destroy()
        main.Root.access_value = access
        main.Root().focus_force()

if __name__ == '__main__':
    pass
