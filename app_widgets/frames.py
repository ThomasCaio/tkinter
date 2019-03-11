import tkinter as tk
from tkinter import ttk
import sys, inspect
import time
import sqlite3 as sql

conn = sql.connect('data.db')
c = conn.cursor()

NOW = [time.strftime('%d/%m/%Y'), time.strftime('%H:%M')]

class MainFrame(tk.Frame):
    def __init__(self, parent, controller, frame_list=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        self.frames = frame_list

        top_frame = tk.Frame(self); top_frame.pack(side='top')
        value_label = tk.Label(top_frame, text='Insira o valor')
        value_label.pack(side='left')
        self.value_entry = ttk.Entry(top_frame)
        self.value_entry.pack(side='left',padx=10)
        info_label = tk.Label(top_frame, text='Informações')
        info_label.pack(side='left',padx=10)
        self.info_entry = ttk.Entry(top_frame)
        self.info_entry.pack(side='left')

        add_but = ttk.Button(self,text='Adicionar', command=self.insert_value)
        add_but.pack(pady=30)

        button_frame = tk.Frame(self)
        graph_button = ttk.Button(button_frame, text='Gráficos', command=lambda: self.controller.show_frame(GraphFrame))
        graph_button.pack()
        data_button = ttk.Button(button_frame, text='Checar dados', command=lambda: self.controller.show_frame(DataFrame))
        data_button.pack()
        button_frame.pack(side='bottom',pady=20)
        self.value_entry.focus()

    def insert_value(self):
        c.execute('INSERT INTO value(value, info, date, time) VALUES(?,?,?,?)', (self.value_entry.get(), self.info_entry.get(), NOW[0], NOW[1]))
        conn.commit()
        self.value_entry.delete(0, 'end')
        self.info_entry.delete(0, 'end')
        self.value_entry.focus()

class GraphFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Você está no GraphFrame')
        but = ttk.Button(self, text='Ir para MainFrame', command=lambda: controller.show_frame(MainFrame))
        label.pack()
        but.pack()

class DataFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Listagem de dados'); label.pack()

        ######## TREEVIEW #########
        treeview_frame = tk.Frame(self); treeview_frame.pack()
        self.treeview = ttk.Treeview(treeview_frame, selectmode='extended'); self.treeview.pack(side='left')
        scrollbar = ttk.Scrollbar(treeview_frame, orient='vertical', command=self.treeview.yview); scrollbar.pack(side='right', fill='y')
        self.treeview.configure(yscrollcommand=scrollbar.set)
        self.treeview['columns'] = ['1','2','3','4']
        self.treeview['show'] = 'headings'
        self.treeview.heading('1', text='ID')
        self.treeview.heading('2', text='Valor')
        self.treeview.heading('3', text='Informações')
        self.treeview.heading('4', text='Data')
        self.treeview.column('1', width=50, anchor='c')
        self.treeview.column('2', width=100,anchor='c')
        self.treeview.column('3', width=250,anchor='c')
        self.treeview.column('4', width=150,anchor='c')
        ###########################

        button_frame = tk.Frame(self); button_frame.pack()
        check_button = ttk.Button(button_frame, text='Checar',command=self.check_item); check_button.pack(side='left')
        delete_button = ttk.Button(button_frame, text='Deletar',command=self.delete_item); delete_button.pack(side='right')
        but = ttk.Button(self, text='Ir para a tela inicial', command=lambda: controller.show_frame(MainFrame)); but.pack(side='bottom',pady=30)
        self.treeview_update()

    def treeview_update(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        c.execute("SELECT * FROM value")
        result = c.fetchall()
        for item in result:
            ID,value,info,date = item[0],item[1],item[2],item[3]+' - '+item[4]
            self.treeview.insert('','end',values=[ID,value,info,date])

    def selected_item(self):
        item_list = self.treeview.selection()
        id_list = []
        for i in item_list:
            item_list = self.treeview.item(i)
            item = item_list['values'][0]
            id_list.append(item)
        return id_list

    def check_item(self):
        # TODO: Função que exibe mais informações sobre o item selecionado
        pass

    def delete_item(self):
        item_list = self.selected_item()
        if len(item_list) > 1:
            for item in item_list:
                c.execute("DELETE FROM value WHERE id = %s" %item)
        else:
            c.execute("DELETE FROM value WHERE id = %s" % item_list[0])
        conn.commit()
        self.treeview_update()

FRAMES = inspect.getmembers(sys.modules[__name__], inspect.isclass)