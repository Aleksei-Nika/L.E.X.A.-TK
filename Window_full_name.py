import tkinter
from tkinter import ttk
from tkinter import Toplevel

class Window_name:
    def __init__(self, root, listbox_names, name = ''):
        self.__listbox_names = listbox_names
        self.__name_object = name
        self.window_name_object = Toplevel(root)
        self.window_name_object.title('Добавление нового полного имени объекта')
        self.window_name_object.geometry('500x500')
        self.window_name_object.grab_set()

        self.frame_name_object = tkinter.Frame(self.window_name_object)
        self.label_name_object = tkinter.Label(self.frame_name_object,
                                                   text='Введите полное имя объекта')
        self.text_name_object = tkinter.Text(self.frame_name_object,
                                                 height=5, width=80,
                                                 wrap='word', )
        self.text_name_object.insert('end', 'Введите наименование объекта')
        self.button_name_object = tkinter.Button(self.frame_name_object,
                                                 text = 'Добавить полное наименование объекта',
                                                 command = self.set_name_object)
        self.label_name_object.pack()
        self.text_name_object.pack()
        self.button_name_object.pack()
        self.frame_name_object.pack()

    def set_name_object(self):
        self.__name_object = self.text_name_object.get('0.1', 'end')[0:-1]
        self.__listbox_names.insert('end', self.__name_object)
        self.window_name_object.destroy()