import data_akt
import tkinter
import Window_full_name
from tkinter import ttk
from tkinter import Toplevel
from tkinter import filedialog

x_data_akt = data_akt.Data_Akt()


class RootGUI:
    def __init__(self):
        # Создание и настройка основного окна
        self.root = tkinter.Tk()
        self.root.title('L.E.X.A.')
        self.root.geometry('700x700')

        # Создание МЕНЮ
        self.main_menu = tkinter.Menu(self.root)
        self.root.config(menu = self.main_menu)
        self.file_menu = tkinter.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label='Файл', menu=self.file_menu)
        self.file_menu.add_command(label='Новый', command=self.new_file)
        self.file_menu.add_command(label = 'Открыть', command=self.load_file)
        self.file_menu.add_command(label = 'Сохранить', command = self.save_file)

        # Создание вкладок
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand = True, fill = 'both')

        # Создание вкладки ОБЪЕКТ
        self.frame_object = tkinter.Frame(self.root)
        self.frame_object.pack(expand = True, fill = 'both')
        self.notebook.add(self.frame_object, text = 'Объект')

        # Создание группы виджетов ПОЛНОЕ НАИМЕНОВАНИЕ ОБЪЕКТА для вкладке ОБЪЕКТ
        self.frame_name_object = tkinter.LabelFrame(self.frame_object,
                                                    borderwidth = 1,
                                                    relief = 'solid',
                                                    text = 'Полное наименование объекта')
        self.frame_listbox_names = tkinter.Frame(self.frame_name_object)
        self.names_object = tkinter.Variable(value = x_data_akt.get_all_names_object())
        self.listbox_names = tkinter.Listbox(self.frame_listbox_names,
                                             listvariable =self.names_object,
                                             height = 5,
                                             width = 93)
        self.listbox_names.pack(side = 'left')
        self.listbox_names_scrollbar = tkinter.Scrollbar(self.frame_listbox_names,
                                                         command = self.listbox_names.yview)
        self.listbox_names_scrollbar.pack(side = 'right', fill = 'y')
        self.listbox_names.config(yscrollcommand = self.listbox_names_scrollbar.set)
        self.listbox_names.bind('<Button-3>', self.menu_names_object)
        self.frame_listbox_names.pack()
        self.frame_name_object.grid(row = 0, column = 0)#pack()

        # Создание группы виждетов КОРОТКОЕ НАИМЕНОВАНИЕ ОБЪЕКТА для вкладки ОБЪЕКТ
        self.frame_name_short = tkinter.LabelFrame(self.frame_object,
                                                    borderwidth=1,
                                                    relief='solid',
                                                    text='Короткое наименование объекта')
        self.frame_listbox_names_shorts = tkinter.Frame(self.frame_name_short)
        self.names_shorts = tkinter.Variable(value = x_data_akt.get_all_names_shorts())
        self.listbox_names_shorts = tkinter.Listbox(self.frame_listbox_names_shorts,
                                                    listvariable = self.names_shorts,
                                                    height=5,
                                                    width=93)
        self.listbox_names_shorts.pack(side='left')
        self.listbox_names_shorts_scrollbar = tkinter.Scrollbar(self.frame_listbox_names_shorts,
                                                         command=self.listbox_names_shorts.yview)
        self.listbox_names_shorts_scrollbar.pack(side='right', fill='y')
        self.listbox_names_shorts.config(yscrollcommand=self.listbox_names_shorts_scrollbar.set)
        self.listbox_names_shorts.bind('<Button-3>', self.menu_names_shorts)
        self.frame_listbox_names_shorts.pack()
        self.frame_name_short.grid(row = 1, column = 0)

        # Создание группы виджетов ОРГАНИЗАЦИИ для вкладки ОБЪЕКТ
        self.frame_organization = tkinter.LabelFrame(self.frame_object,
                                                   borderwidth=1,
                                                   relief='solid',
                                                   text='Огранизации учавствующие в строительстве')
        self.frame_listbox_organization = tkinter.Frame(self.frame_organization)
        #self.organizations = tkinter.Variable(value = x_data_akt.get_all_organizations())
        self.listbox_organization = tkinter.Listbox(self.frame_listbox_organization,
                                                    #listvariable=self.organizations,
                                                    height=5,
                                                    width=93)
        self.listbox_organization.pack(side='left')
        self.listbox_organization_scrollbar = tkinter.Scrollbar(self.frame_listbox_organization,
                                                                command=self.listbox_organization.yview)
        self.listbox_organization_scrollbar.pack(side='right', fill='y')
        self.listbox_organization.config(yscrollcommand=self.listbox_organization_scrollbar.set)
        self.listbox_organization.bind('<Button-3>', self.menu_organization)
        self.frame_listbox_organization.pack()
        self.frame_organization.grid(row = 2, column = 0)

        # Создание группы виджетов ПРЕДСТВАВИТЕЛИ для вкладки ОБЪЕКТ
        self.frame_representative = tkinter.LabelFrame(self.frame_object,
                                                     borderwidth=1,
                                                     relief='solid',
                                                     text='Представители')
        self.frame_listbox_representative = tkinter.Frame(self.frame_representative)
        self.representatives = tkinter.Variable(value= x_data_akt.get_all_representatives_names())
        self.listbox_representative = tkinter.Listbox(self.frame_listbox_representative,
                                                      listvariable=self.representatives,
                                                    height=5,
                                                    width=93)
        self.listbox_representative.pack(side='left')
        self.listbox_representative_scrollbar = tkinter.Scrollbar(self.frame_listbox_representative,
                                                                command=self.listbox_representative.yview)
        self.listbox_representative_scrollbar.pack(side='right', fill='y')
        self.listbox_representative.config(yscrollcommand=self.listbox_representative_scrollbar.set)
        self.listbox_representative.bind('<Button-3>', self.menu_representative)
        self.frame_listbox_representative.pack()
        self.frame_representative.grid(row = 3, column = 0)

        # Создание вкладки АКТЫ
        self.frame_akt = tkinter.Frame(self.root)
        self.frame_akt.pack()
        self.notebook.add(self.frame_akt, text='Акты')

        # Создание группы виджетов СПИСОК АКТОВ во вкладке АКТЫ
        self.frame_list_akts = tkinter.Frame(self.frame_akt)
        self.label_listbox_akts = tkinter.Label(self.frame_list_akts,
                                                text = 'Список актов')
        self.label_listbox_akts.pack()
        self.frame_listbox_akts = tkinter.Frame(self.frame_list_akts)
        self.akts = tkinter.Variable(value = x_data_akt.get_all_akts())
        self.listbox_akts = tkinter.Listbox(self.frame_listbox_akts,
                                            listvariable = self.akts,
                                            height=25,
                                            width=45)
        self.listbox_akts.pack(side = 'left')
        self.listbox_akts_scrollbar = tkinter.Scrollbar(self.frame_listbox_akts,
                                                        command=self.listbox_akts.yview)
        self.listbox_akts_scrollbar.pack(side = 'right', fill = 'y')
        self.listbox_akts.config(yscrollcommand = self.listbox_akts_scrollbar.set)
        self.listbox_akts.bind('<Button-3>', self.menu_listbox_akts)
        self.frame_listbox_akts.pack()
        self.frame_list_akts.grid(row = 0, column = 0)

        self.root.mainloop()

    # Функция ОТКРЫТЬ из МЕНЮ
    def new_file(self):
        x_data_akt = data_akt.Data_Akt()
        self.updater_list(self.listbox_names, x_data_akt.get_all_names_object())
        self.updater_list(self.listbox_names_shorts, x_data_akt.get_all_names_shorts())
        self.updater_list(self.listbox_organization, x_data_akt.get_all_organizations_names())
        self.updater_list(self.listbox_representative, x_data_akt.get_all_representatives_names())

    def load_file(self):
        global x_data_akt
        self.file = tkinter.filedialog.askopenfilename(defaultextension = 'dat')
        x_data_akt = data_akt.load(self.file)
        self.updater_list(self.listbox_names, x_data_akt.get_all_names_object())
        self.updater_list(self.listbox_names_shorts, x_data_akt.get_all_names_shorts())
        self.updater_list(self.listbox_organization, x_data_akt.get_all_organizations_names())
        self.updater_list(self.listbox_representative, x_data_akt.get_all_representatives_names())

    #self.names_object, self.names_shorts, self.organizations, self.representatives,

    def save_file(self):
        self.file = tkinter.filedialog.asksaveasfilename(defaultextension = 'dat')
        data_akt.save(self.file, x_data_akt)

    def updater_list(self, list_object, var):
        elements = tkinter.Variable(value = var)
        list_object.config(listvariable = elements)

    # Контекстное меню для ПОЛНОГО НАИМЕНОВАНИЯ ОБЪЕКТА вкладке ОБЪЕКТ
    def menu_names_object(self, event):
        menu = tkinter.Menu(tearoff = 0)
        menu.add_command(label = 'Добавить', command = self.add_name_object)
        menu.add_command(label = 'Изменить', command = self.change_name_object)
        menu.add_command(label = 'Удалить', command = self.delete_name_object)
        menu.post(event.x_root, event.y_root)

    def add_name_object(self):
        window = Window_name_object(self.root, self.listbox_names, self.names_object)

    def change_name_object(self):
        index = self.listbox_names.curselection()[0]
        window = Window_name_object(self.root, self.listbox_names, self.names_object, index)

    def delete_name_object(self):
        index = self.listbox_names.curselection()
        x_data_akt.delete_name_object(index[0])
        self.updater_list(self.listbox_names, x_data_akt.get_all_names_object())

    # Контекстное меню для КОРОТКОГО НАИМЕНОВАНИЯ ОБЪЕКТА вкладке ОБЪЕКТ
    def menu_names_shorts(self, event):
        menu = tkinter.Menu(tearoff = 0)
        menu.add_command(label = 'Добавить', command = self.add_name_short)
        menu.add_command(label = 'Изменить', command = self.change_name_short)
        menu.add_command(label = 'Удалить', command = self.delete_name_short)
        menu.post(event.x_root, event.y_root)

    def add_name_short(self):
        window = Window_name_short(self.root, self.listbox_names_shorts, self.names_shorts)

    def change_name_short(self):
        index = self.listbox_names_shorts.curselection()[0]
        window = Window_name_short(self.root, self.listbox_names_shorts, self.names_shorts, index)

    def delete_name_short(self):
        index = self.listbox_names_shorts.curselection()
        x_data_akt.delete_name_short(index[0])
        self.updater_list(self.listbox_names_shorts, x_data_akt.get_all_names_shorts())

    # Контекстное меню для ОРГАНИЗАЦИЙ вкладке ОБЪЕКТ
    def menu_organization(self, event):
        menu = tkinter.Menu(tearoff = 0)
        menu.add_command(label = 'Добавить', command = self.add_organization)
        menu.add_command(label = 'Изменить', command = self.change_organization)
        menu.add_command(label = 'Удалить', command = self.delete_organization)
        menu.post(event.x_root, event.y_root)

    def add_organization(self):
        window = Window_organization(self.root, self.listbox_organization) #self.organizations,

    def change_organization(self):
        index = self.listbox_organization.curselection()[0]
        window = Window_organization(self.root, self.listbox_organization, index) #self.organizations,

    def delete_organization(self):
        index = self.listbox_organization.curselection()
        x_data_akt.delete_organization(index[0])
        self.updater_list(self.listbox_organization, x_data_akt.get_all_organizations_names())

    # Контекстное меню для ПРЕДСТАВИТЕЛЕЙ вкладке ОБЪЕКТ
    def menu_representative(self, event):
        menu = tkinter.Menu(tearoff = 0)
        menu.add_command(label = 'Добавить', command = self.add_representative)
        menu.add_command(label = 'Изменить', command = self.change_representative)
        menu.add_command(label = 'Удалить', command = self.delete_representative)
        menu.post(event.x_root, event.y_root)

    def add_representative(self):
        window = Window_representative(self.root, self.listbox_representative, self.representatives)

    def change_representative(self):
        index = self.listbox_representative.curselection()[0]
        window = Window_representative(self.root, self.listbox_representative, self.representatives, index)

    def delete_representative(self):
        index = self.listbox_representative.curselection()
        x_data_akt.delete_representative(index[0])
        self.listbox_representative.delete(index[0])

    # Контекстное меню для СПИСКА АКТОВ вкладке АКТЫ
    def menu_listbox_akts(self, event):
        menu = tkinter.Menu(tearoff = 0)
        menu.add_command(label = 'Добавить', command = self.add_akt)
        menu.add_command(label = 'Изменить', command = self.change_akt)
        menu.add_command(label = 'Удалить', command = self.delete_akt)
        menu.post(event.x_root, event.y_root)

    def add_akt(self):
        window = Window_akt(self.root, self.listbox_akts)

    def change_akt(self):
        pass

    def delete_akt(self):
        index = self.listbox_akts.curselection()
        x_data_akt.delete_akt(index[0])
        self.listbox_akts.delete(index[0])


class Window_name_object:
    def __init__(self, root, listbox, elements, index = None):
        self.__root = root
        self.__listbox_names = listbox
        self.__elements = elements
        if index == None:
            self.__name = 'Введите полное наименование объекта'
            self.__index = None
            self.__text_button = 'Добавить полное наименование объекта'
        else:
            self.__name = x_data_akt.get_name_object(index)
            self.__index = index
            self.__text_button = 'Изменить полное наименование объекта'
        self.window_name_object = Toplevel(self.__root)
        self.window_name_object.title('Полное имя объекта')
        self.window_name_object.geometry('500x500')
        self.window_name_object.grab_set()

        self.frame_name_object = tkinter.Frame(self.window_name_object)
        self.label_name_object = tkinter.Label(self.frame_name_object,
                                               text='Введите полное имя объекта')
        self.text_name_object = tkinter.Text(self.frame_name_object,
                                             height=5,
                                             width=80,
                                             wrap='word')
        self.text_name_object.insert('end', self.__name)
        self.label_indicator = tkinter.Label(self.frame_name_object,
                                             foreground = 'red')
        self.button_name_object = tkinter.Button(self.frame_name_object,
                                                 text = self.__text_button,
                                                 command = self.set_name_object)
        self.label_name_object.pack()
        self.text_name_object.pack()
        self.label_indicator.pack()
        self.button_name_object.pack()
        self.frame_name_object.pack()

    def set_name_object(self):
        name = self.text_name_object.get('0.1', 'end')[0:-1]
        def set_name(name):
            if self.__index == None:
                x_data_akt.set_name_object(name)
                self.__elements = tkinter.Variable(value = x_data_akt.get_all_names_object())
                self.__listbox_names.config(listvariable = self.__elements)
                self.window_name_object.destroy()
            else:
                x_data_akt.change_name_object(name, self.__index)
                self.__elements = tkinter.Variable(value = x_data_akt.get_all_names_object())
                self.__listbox_names.config(listvariable = self.__elements)
                self.window_name_object.destroy()
        if name == '':
            self.label_indicator.config(text = 'Введенное имя не должно быть пустым')
        elif name == self.__name:
            self.label_indicator.config(text='Введенное имя должно отличаться от предыдущего')
        else:
            set_name(name)

class Window_name_short:
    def __init__(self, root, listbox, elements, index = None):
        self.__root = root
        self.__listbox_names_shorts = listbox
        self.__elements = elements
        if index == None:
            self.__name = 'Введите короткое наименование объекта'
            self.__index = None
            self.__text_button = 'Добавить короткое наименование объекта'
        else:
            self.__name = x_data_akt.get_name_short(index)
            self.__index = index
            self.__text_button = 'Изменить короткое наименование объекта'
        self.window_name_short = Toplevel(self.__root)
        self.window_name_short.title('Короткое имя объекта')
        self.window_name_short.geometry('500x500')
        self.window_name_short.grab_set()

        self.frame_name_short = tkinter.Frame(self.window_name_short)
        self.label_name_short = tkinter.Label(self.frame_name_short,
                                               text = 'Введите короткое имя объекта')
        self.entry_name_short = tkinter.Entry(self.frame_name_short,
                                             width = 80)
        self.entry_name_short.insert('end', self.__name)
        self.label_indicator = tkinter.Label(self.frame_name_short,
                                             foreground='red')
        self.button_name_short = tkinter.Button(self.frame_name_short,
                                                 text = self.__text_button,
                                                 command = self.set_name_short)
        self.label_name_short.pack()
        self.entry_name_short.pack()
        self.label_indicator.pack()
        self.button_name_short.pack()
        self.frame_name_short.pack()

    def set_name_short(self):
        name = self.entry_name_short.get()

        def set_name(name):
            if self.__index == None:
                x_data_akt.set_name_short(name)
                self.__elements = tkinter.Variable(value = x_data_akt.get_all_names_shorts())
                self.__listbox_names_shorts.config(listvariable = self.__elements)
                self.window_name_short.destroy()
            else:
                x_data_akt.change_name_short(name, self.__index)
                self.__elements = tkinter.Variable(value = x_data_akt.get_all_names_shorts())
                self.__listbox_names_shorts.config(listvariable = self.__elements)
                self.window_name_short.destroy()

        if name == '':
            self.label_indicator.config(text='Введенное имя не должно быть пустым')
        elif name == self.__name:
            self.label_indicator.config(text='Введенное имя должно отличаться от предыдущего')
        else:
            set_name(name)

class Window_object_element:
    def __init__(self, root, listbox, type_elenemt, index = None):
        self.__root = root
        self.__listbox_organization = listbox
        self.__type_element = type_elenemt
        if index == None:
            self.__text = 'Введите необходимую информацию'
            self.__name = 'Введите наименование'
            self.__index = None
            self.__text_button = 'Добавить'
        else:
            self.__text = x_data_akt.get_organization_text(index)
            self.__name = x_data_akt.get_organization_name(index)
            self.__index = index
            self.__text_button = 'Изменить'

        self.window = Toplevel(self.__root)
        self.window.title('Данные об объекте')
        self.window.geometry('500x500')
        self.window.grab_set()

        self.frame = tkinter.Frame(self.window)
        self.label = tkinter.Label(self.frame, text='Введите информацию')
        self.text = tkinter.Text(self.frame, height=5, width=80, wrap='word')
        self.text.insert('end', self.__text)
        self.label_indicator_text = tkinter.Label(self.frame, foreground='red')
        self.entry = tkinter.Entry(self.frame, width=80)
        self.entry.insert('end', self.__name)
        self.label_indicator_entry = tkinter.Label(self.frame, foreground='red')
        self.button = tkinter.Button(self.frame, text=self.__text_button, command=self.set)
        self.label.pack()
        self.text.pack()
        self.label_indicator_text.pack()
        self.entry.pack()
        self.label_indicator_entry.pack()
        self.button.pack()
        self.frame.pack()

    def set(self):
        self.label_indicator_text.config(text='')
        self.label_indicator_entry.config(text='')
        text = self.text.get('0.1', 'end')[0:-1]
        name = self.entry.get()
        def set_name(text, name):
            if self.__index == None:
                self.set_element_data_akt(self.__type_element, text, name)
                elements = tkinter.Variable(value = x_data_akt.get_all_organizations_names())
                self.__listbox_organization.config(listvariable = elements)
                self.window_organization.destroy()
            else:
                self.change_element_data_akt(self.__type_element, text, name)
                elements = tkinter.Variable(value = x_data_akt.get_all_organizations_names())
                self.__listbox_organization.config(listvariable = elements)
                self.window_organization.destroy()
        if text == '' and name == '':
            self.label_indicator_text.config(text='Введенная информация не может быть пустой')
            self.label_indicator_entry.config(text='Наменование не может быть пустым')
        elif text == '':
            self.label_indicator_text.config(text = 'Введенная информация не может быть пустой')
        elif name == '':
            self.label_indicator_entry.config(text = 'Наменование не может быть пустым')
        elif text == self.__text and name == self.__name:
            self.label_indicator_text.config(text = 'Изменений не обнаруженно')
            self.label_indicator_entry.config(text = 'Введенная информация должна отличаться от предыдущей')
        else:
            set_name(text, name)

    def get_name(self):
        pass

    def get_names(self):
        pass

    def set_element_data_akt(self, type_elenemt, text, name):
        if type_elenemt == 'имена':
            pass
        elif type_elenemt == 'организации':
            x_data_akt.set_organization(text, name)
        elif type_elenemt == 'представители':
            x_data_akt.set_representative(text, name)

    def change_element_data_akt(self, type_elenemt, text, name):
        if type_elenemt == 'имена':
            pass
        elif type_elenemt == 'организации':
            x_data_akt.change_organization(text, name, self.__index)
        elif type_elenemt == 'представители':
            x_data_akt.change_representative(text, name, self.__index)


class Window_organization:
    def __init__(self, root, listbox, index = None):
        self.__root = root
        self.__listbox_organization = listbox
        self.__elements = None
        if index == None:
            self.__organization_text = 'Введите необходимую информацию об организации'
            self.__organization_name = 'Введите наименование организации'
            self.__index = None
            self.__text_button = 'Добавить организацию'
        else:
            self.__organization_text = x_data_akt.get_organization_text(index)
            self.__organization_name = x_data_akt.get_organization_name(index)
            self.__index = index
            self.__text_button = 'Изменить организацию'
        self.window_organization = Toplevel(self.__root)
        self.window_organization.title('Организация учавствующия в строительстве')
        self.window_organization.geometry('500x500')
        self.window_organization.grab_set()

        self.frame_organization = tkinter.Frame(self.window_organization)
        self.label_organization = tkinter.Label(self.frame_organization,
                                               text='Введите информацию об организации')
        self.text_organization = tkinter.Text(self.frame_organization,
                                             height = 5,
                                             width = 80,
                                             wrap = 'word')
        self.text_organization.insert('end', self.__organization_text)
        self.label_indicator_text = tkinter.Label(self.frame_organization,
                                             foreground = 'red')
        self.entry_organization = tkinter.Entry(self.frame_organization,
                                                width=80)
        self.entry_organization.insert('end', self.__organization_name)
        self.label_indicator_entry = tkinter.Label(self.frame_organization,
                                                   foreground= 'red')
        self.button_organization = tkinter.Button(self.frame_organization,
                                                 text = self.__text_button,
                                                 command = self.set_organization)
        self.label_organization.pack()
        self.text_organization.pack()
        self.label_indicator_text.pack()
        self.entry_organization.pack()
        self.label_indicator_entry.pack()
        self.button_organization.pack()
        self.frame_organization.pack()

    def set_organization(self):
        self.label_indicator_text.config(text='')
        self.label_indicator_entry.config(text='')
        organization_text = self.text_organization.get('0.1', 'end')[0:-1]
        organization_name = self.entry_organization.get()
        def set_name(organization_text, organization_name):
            if self.__index == None:
                x_data_akt.set_organization(organization_text, organization_name)
                self.__elements = tkinter.Variable(value = x_data_akt.get_all_organizations_names())
                self.__listbox_organization.config(listvariable = self.__elements)
                self.window_organization.destroy()
            else:
                x_data_akt.change_organization(organization_text, organization_name, self.__index)
                self.__elements = tkinter.Variable(value = x_data_akt.get_all_organizations_names())
                self.__listbox_organization.config(listvariable = self.__elements)
                self.window_organization.destroy()
        if organization_text == '' and organization_name == '':
            self.label_indicator_text.config(text='Введенная информация об организации не должна быть пустой')
            self.label_indicator_entry.config(text='Наменование организации не должно быть пустым')
        elif organization_text == '':
            self.label_indicator_text.config(text = 'Введенная информация об организации не должна быть пустой')
        elif organization_name == '':
            self.label_indicator_entry.config(text = 'Наменование организации не должно быть пустым')
        elif organization_text == self.__organization_text and organization_name == self.__organization_name:
            self.label_indicator_text.config(text = 'Изменений не обнаруженно')
            self.label_indicator_entry.config(text = 'Введенная информация должна отличаться от предыдущей')
        else:
            set_name(organization_text, organization_name)

class Window_representative:
    def __init__(self, root, listbox, elements, index = None):
        self.__root = root
        self.__listbox_representative = listbox
        self.__elements = elements
        if index == None:
            self.__representative = 'Введите необходимую информацию о представителе'
            self.__representative_name = 'Введите имя представителя'
            self.__index = None
            self.__text_button = 'Добавить представителя'
        else:
            self.__representative = x_data_akt.get_representative_text(index)
            self.__representative_name = x_data_akt.get_representative_name(index)
            self.__index = index
            self.__text_button = 'Изменить представителя'
        self.window_representative = Toplevel(self.__root)
        self.window_representative.title('Представитель')
        self.window_representative.geometry('500x500')
        self.window_representative.grab_set()

        self.frame_representative = tkinter.Frame(self.window_representative)
        self.label_representative = tkinter.Label(self.frame_representative,
                                               text='Введите информацию об представителе')
        self.text_representative = tkinter.Text(self.frame_representative,
                                             height = 5,
                                             width = 80,
                                             wrap = 'word')
        self.text_representative.insert('end', self.__representative)
        self.label_indicator_text = tkinter.Label(self.frame_representative,
                                             foreground = 'red')
        self.entry_representative = tkinter.Entry(self.frame_representative,
                                                   width = 80)
        self.entry_representative.insert('end', self.__representative_name)
        self.label_indicator_entry = tkinter.Label(self.frame_representative,
                                                  foreground='red')
        self.button_representative = tkinter.Button(self.frame_representative,
                                                 text = self.__text_button,
                                                 command = self.set_representative)
        self.label_representative.pack()
        self.text_representative.pack()
        self.label_indicator_text.pack()
        self.entry_representative.pack()
        self.label_indicator_entry.pack()
        self.button_representative.pack()
        self.frame_representative.pack()

    def set_representative(self):
        self.label_indicator_text.config(text='')
        self.label_indicator_entry.config(text='')
        representative = self.text_representative.get('0.1', 'end')[0:-1]
        representative_name = self.entry_representative.get()
        def set_name(representative, representative_name):
            if self.__index == None:
                x_data_akt.set_representative(representative, representative_name)
                self.__elements = tkinter.Variable(value = x_data_akt.get_all_representatives_names())
                self.__listbox_representative.config(listvariable = self.__elements)
                self.window_representative.destroy()
            else:
                x_data_akt.change_representative(representative, representative_name, self.__index)
                self.__elements = tkinter.Variable(value = x_data_akt.get_all_representatives_names())
                self.__listbox_representative.config(listvariable = self.__elements)
                self.window_representative.destroy()
        if representative == '' and representative_name == '':
            self.label_indicator_text.config(text='Введенная информация о представителе не должна быть пустой')
            self.label_indicator_entry.config(text='Имя представителя не должно быть пустом')
        elif representative == '':
            self.label_indicator_text.config(text = 'Введенная информация о представителе не должна быть пустой')
        elif representative_name == '':
            self.label_indicator_entry.config(text = 'Имя представителя не должно быть пустом')
        elif representative == self.__representative and representative_name == self.__representative_name:
            self.label_indicator_text.config(text = 'Изменений не обнаруженно')
            self.label_indicator_entry.config(text = 'Введенная информация должна отличаться от предыдущей')
        else:
            set_name(representative, representative_name)

class Window_akt:
    def __init__(self, root, listbox, index = None):
        self.__root = root
        self.__listbox = listbox

        self.window_creat_akt = Toplevel(self.__root)
        self.window_creat_akt.title('Акт')
        self.window_creat_akt.geometry('500x500')
        self.frame_window_akt = tkinter.Frame(self.window_creat_akt)

        self.frame_object = tkinter.LabelFrame(self.frame_window_akt, text='Объект, организации, представители')
        self.label_object = tkinter.Label(self.frame_object, text = 'Выберите наименование объекта')
        self.label_object.grid(row = 0, column = 0, stick = 'e')#pack(side = 'left')
        self.combobox_object = ttk.Combobox(self.frame_object,
                                            width = 50,
                                            values = x_data_akt.get_all_names_object())
        self.combobox_object.grid(row = 0, column = 1)#pack(side = 'right')

        self.label_developer = tkinter.Label(self.frame_object, text = 'Выберите застройщика')
        self.label_developer.grid(row = 1, column = 0, stick = 'e')#pack(side='left')
        self.combobox_developer = ttk.Combobox(self.frame_object,
                                                  width=50,
                                                  values=x_data_akt.get_all_organizations_names())
        self.combobox_developer.grid(row = 1, column = 1)#pack(side='right')

        self.label_builder = tkinter.Label(self.frame_object, text = 'Выберите лицо осуществляющее строительство')
        self.label_builder.grid(row = 2, column = 0, stick = 'e')#pack(side='left')
        self.combobox_builder = ttk.Combobox(self.frame_object,
                                               width=50,
                                               values=x_data_akt.get_all_organizations_names())
        self.combobox_builder.grid(row = 2, column = 1)#pack(side='right')

        self.label_designer = tkinter.Label(self.frame_object, text = 'Выберите проектировщика')
        self.label_designer.grid(row = 3, column = 0, stick = 'e')#pack(side='left')
        self.combobox_designer = ttk.Combobox(self.frame_object,
                                             width=50,
                                             values=x_data_akt.get_all_organizations_names())
        self.combobox_designer.grid(row = 3, column = 1)#pack(side='right')

        self.label_developer_name = tkinter.Label(self.frame_object,
                                                  text = 'Выберите представителя застройщика\n'+
                                                  'по вопросам строительного контроля')
        self.label_developer_name.grid(row = 4, column = 0, stick = 'e')
        self.combobox_developer_name = ttk.Combobox(self.frame_object,
                                                    width=50,
                                                    values=x_data_akt.get_all_representatives_names())
        self.combobox_developer_name.grid(row = 4, column = 1, stick='ns')

        self.label_builder_name = tkinter.Label(self.frame_object,
                                                text='Выберите представителя\n'+
                                                'лица осуществляющего строительство')
        self.label_builder_name.grid(row=5, column=0, stick='e')
        self.combobox_builder_name = ttk.Combobox(self.frame_object,
                                                    width=50,
                                                    values=x_data_akt.get_all_representatives_names())
        self.combobox_builder_name.grid(row=5, column=1, stick='ns')

        self.label_builder_control_name = tkinter.Label(self.frame_object,
                                                        text='Выберите представителя строителя\n'+
                                                        'по вопросам строительного контроля')
        self.label_builder_control_name.grid(row=6, column=0, stick='e')
        self.combobox_builder_control_name = ttk.Combobox(self.frame_object,
                                                  width=50,
                                                  values=x_data_akt.get_all_representatives_names())
        self.combobox_builder_control_name.grid(row=6, column=1, stick='ns')

        self.label_designer_name = tkinter.Label(self.frame_object,
                                                 text='Выберите представителя осуществляющего\n' +
                                                      'подготовку проектной документации')
        self.label_designer_name.grid(row=7, column=0, stick='e')
        self.combobox_designer_name = ttk.Combobox(self.frame_object,
                                                          width=50,
                                                          values=x_data_akt.get_all_representatives_names())
        self.combobox_designer_name.grid(row=7, column=1, stick='ns')

        self.label_contractor_name = tkinter.Label(self.frame_object,
                                                 text='Выберите представителя\n' +
                                                      'выполнившего работы')
        self.label_contractor_name.grid(row=8, column=0, stick='e')
        self.combobox_contractor_name = ttk.Combobox(self.frame_object,
                                                   width=50,
                                                   values=x_data_akt.get_all_representatives_names())
        self.combobox_contractor_name.grid(row=8, column=1, stick='ns')

        self.label_another_person = tkinter.Label(self.frame_object,
                                                   text='Выберите иного представителя\n' +
                                                        'учавствающего в осведетельствовании')
        self.label_another_person.grid(row=9, column=0, stick='e')
        self.combobox_another_person = ttk.Combobox(self.frame_object,
                                                     width=50,
                                                     values=x_data_akt.get_all_representatives_names())
        self.combobox_another_person.grid(row=9, column=1, stick='ns')

        self.label_contractor = tkinter.Label(self.frame_object,
                                                  text='Выберите организацию выполняющую работы')
        self.label_contractor.grid(row=10, column=0, stick='e')
        self.combobox_contractor = ttk.Combobox(self.frame_object,
                                                    width=50,
                                                    values=x_data_akt.get_all_organizations_names())
        self.combobox_contractor.grid(row=10, column=1, stick='ns')

        self.frame_date = tkinter.LabelFrame(self.frame_window_akt, text='Дата начала и окончания работ')
        self.leble_start_date = tkinter.Label(self.frame_date, text='Начала работ:')
        self.leble_start_date.grid(row=0, column=0)
        self.entry_start_date = tkinter.Entry(self.frame_date, width=10)
        self.entry_start_date.grid(row=0, column=1, padx=[0, 10])
        self.leble_start_date = tkinter.Label(self.frame_date, text='Окончание работ:')
        self.leble_start_date.grid(row=0, column=2, padx=[10, 0])
        self.entry_start_date = tkinter.Entry(self.frame_date, width=10)
        self.entry_start_date.grid(row=0, column=3)

        self.frame_work = tkinter.LabelFrame(self.frame_window_akt, text='Наименование работ')
        self.leble_work = tkinter.Label(self.frame_work, text='Введите наименование работ:')
        self.leble_work.grid(row=0, column=0)
        self.entry_work = tkinter.Entry(self.frame_work, width=50)
        self.entry_work.grid(row=0, column=1)

        self.frame_object.grid(row=0, column=0)
        self.frame_date.grid(row=1, column=0, stick='we')
        self.frame_work.grid(row=2, column=0, stick='we')

        self.button_akt = tkinter.Button(self.window_creat_akt, text='Создать акт', command=self.akt)


        self.frame_window_akt.pack()
        self.button_akt.pack()

    def akt(self):
        index_name_object = self.combobox_object.current()
        if index_name_object == -1:
            name_object = self.combobox_object.get()
        else:
            name_object = x_data_akt.get_name_object(index_name_object)

        x_data_akt.set_akt(name_object)

if __name__ == '__main__':
    window = RootGUI()