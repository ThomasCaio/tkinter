import tkinter as tk
import time


class Menubar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self,parent, *args, **kwargs)
        self.menubar = tk.Menu(parent)
        self.master.config(menu=self.menubar)
        self.file = tk.Menu(self.menubar, tearoff=0)
        self.edit = tk.Menu(self.menubar, tearoff=0)
        self.access_value = parent.access_value
        self.access(self.access_value)

    def default_buttons(self):
        """Usuarios com acesso inicial"""
        self.menubar.add_cascade(label='File', menu=self.file)
        self.file.add_separator()
        self.file.add_command(label='Exit', command=quit)

    def access_one(self):
        self.default_buttons()
        self.menubar.add_cascade(label='Edit', menu=self.edit)
        self.edit.add_command(label='New')

    def access_two(self):
        self.access_one()
        self.edit.add_command(label='New2')

    def access_three(self):
        self.access_two()
        self.edit.add_command(label='New3')

    def access_four(self):
        self.access_three()
        self.edit.add_command(label='New4')

    def access_five(self):
        """Acesso máximo ao programa"""
        self.access_four()
        self.edit.add_command(label='New5')

    def access(self, access):
        if access is 0:
            self.default_buttons()
        elif access is 1:
            self.access_one()
        elif access is 2:
            self.access_two()
        elif access is 3:
            self.access_three()
        elif access is 4:
            self.access_four()
        elif access is 5:
            self.access_five()

class Statusbar(tk.Frame):
    def __init__(self, parent, **kw):
        tk.Frame.__init__(self,**kw)
        # TODO: Preciso colocar as duas statusbar se dividam igualmente na parte de baixo do programa.
        statusbar1 = tk.Label(self, text='Statusbar', bd=1, relief='sunken', anchor='w')
        self.statusbar2 = tk.Label(self, bd=1, relief='sunken', anchor='w')

        self.statusbar2.pack(side='right', fill='x')
        statusbar1.pack(side='bottom', fill='x')

        self.after(1000, self.clock_tick())
        self.pack(side='bottom', fill='x')

    def clock_tick(self, delay=1000):
        time_string = time.strftime("%H:%M:%S")
        self.statusbar2['text'] = time_string
        self.statusbar2.after(delay ,self.clock_tick)

if __name__ == '__main__':
    pass