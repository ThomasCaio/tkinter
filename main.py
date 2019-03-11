from app_widgets.main_widgets import Statusbar, Menubar
from app_widgets.frames import *
from content.login import Login
from content import database
database.load_database()

FRAMES = [i[1] for i in FRAMES]

fonte = ('helvetica',12)

class Root(tk.Tk):
    """Janela principal no qual o programa inteiro está contido."""
    def __init__(self,*args,**kwargs):
        """Aqui estão todos os atributos e características que a janela recebe."""
        tk.Tk.__init__(self,*args,**kwargs)
        self.title('Main Window')
        self.minsize(640,400)
        self.args = args
        self.kwargs = kwargs

        main_frame = tk.Canvas(self)
        main_frame.pack(side='top', fill='both', expand=True)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in FRAMES:
            frame = F(main_frame, self)
            frame.grid(row=0, column=0, sticky='nsew')
            self.frames[F] = frame

        MainFrame.access = DataFrame
        self.show_frame(MainFrame)
        self.init_window()
        from content.center import center
        center(self)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.focus_force()

    def init_window(self):
        """Widgets que estão na janela principal."""
        Menubar(self)
        Statusbar(self)

    def show_frame(self, content):
        """Função que muda as frames da janela principal"""
        self.frames[content].tkraise()

    def on_closing(self):
        """Funções que serão executadas ao sair do programa."""
        self.quit()
        self.destroy()

if __name__ == '__main__':
    Root.access_value = 5
    Root().mainloop()
    #Login().mainloop()