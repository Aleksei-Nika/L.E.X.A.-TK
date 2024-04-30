import data_akt
import tkinter
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
        self.root.config(menu=self.main_menu)
        self.file_menu = tkinter.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label='Файл', menu=self.file_menu)
        self.file_menu.add_command(label='Новый', command=self.new_file)
        self.file_menu.add_command(label='Открыть', command=self.load_file)
        self.file_menu.add_command(label='Сохранить', command=self.save_file)

        # Создание вкладок
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        # Создание вкладки ОБЪЕКТ
        self.frame_object = tkinter.Frame(self.root)
        self.frame_object.pack(expand=True, fill='both')
        self.notebook.add(self.frame_object, text='Объект')

        # Создание группы виджетов НАИМЕНОВАНИЕ ОБЪЕКТА для вкладке ОБЪЕКТ
        self.frame_name_object = tkinter.LabelFrame(self.frame_object,
                                                    borderwidth=1,
                                                    relief='solid',
                                                    text='Наименование объекта')
        self.frame_listbox_names = tkinter.Frame(self.frame_name_object)
        self.names_object = tkinter.Variable(value=x_data_akt.get_all_name_object_names())
        self.listbox_names = tkinter.Listbox(self.frame_listbox_names,
                                             listvariable=self.names_object,
                                             height=5,
                                             width=93)
        self.listbox_names.pack(side='left')
        self.listbox_names_scrollbar = tkinter.Scrollbar(self.frame_listbox_names,
                                                         command=self.listbox_names.yview)
        self.listbox_names_scrollbar.pack(side='right', fill='y')
        self.listbox_names.config(yscrollcommand=self.listbox_names_scrollbar.set)
        self.listbox_names.bind('<Button-3>', self.menu_names_object)
        self.frame_listbox_names.pack()
        self.frame_name_object.grid(row=0, column=0)  # pack()

        # Создание группы виджетов ОРГАНИЗАЦИИ для вкладки ОБЪЕКТ
        self.frame_organization = tkinter.LabelFrame(self.frame_object,
                                                     borderwidth=1,
                                                     relief='solid',
                                                     text='Огранизации учавствующие в строительстве')
        self.frame_listbox_organization = tkinter.Frame(self.frame_organization)
        # self.organizations = tkinter.Variable(value = x_data_akt.get_all_organizations())
        self.listbox_organization = tkinter.Listbox(self.frame_listbox_organization,
                                                    # listvariable=self.organizations,
                                                    height=5,
                                                    width=93)
        self.listbox_organization.pack(side='left')
        self.listbox_organization_scrollbar = tkinter.Scrollbar(self.frame_listbox_organization,
                                                                command=self.listbox_organization.yview)
        self.listbox_organization_scrollbar.pack(side='right', fill='y')
        self.listbox_organization.config(yscrollcommand=self.listbox_organization_scrollbar.set)
        self.listbox_organization.bind('<Button-3>', self.menu_organization)
        self.frame_listbox_organization.pack()
        self.frame_organization.grid(row=2, column=0)

        # Создание группы виджетов ПРЕДСТВАВИТЕЛИ для вкладки ОБЪЕКТ
        self.frame_representative = tkinter.LabelFrame(self.frame_object,
                                                       borderwidth=1,
                                                       relief='solid',
                                                       text='Представители')
        self.frame_listbox_representative = tkinter.Frame(self.frame_representative)
        self.representatives = tkinter.Variable(value=x_data_akt.get_all_representatives_names())
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
        self.frame_representative.grid(row=3, column=0)

        # Создание вкладки АКТЫ
        self.frame_akt = tkinter.Frame(self.root)
        self.frame_akt.pack()
        self.notebook.add(self.frame_akt, text='Акты')

        # Создание группы виджетов СПИСОК АКТОВ во вкладке АКТЫ
        self.frame_list_akts = tkinter.Frame(self.frame_akt)
        self.label_listbox_akts = tkinter.Label(self.frame_list_akts,
                                                text='Список актов')
        self.label_listbox_akts.pack()
        self.frame_listbox_akts = tkinter.Frame(self.frame_list_akts)
        self.akts = tkinter.Variable(value=x_data_akt.get_all_akts())
        self.listbox_akts = tkinter.Listbox(self.frame_listbox_akts,
                                            listvariable=self.akts,
                                            height=25,
                                            width=45)
        self.listbox_akts.pack(side='left')
        self.listbox_akts_scrollbar = tkinter.Scrollbar(self.frame_listbox_akts,
                                                        command=self.listbox_akts.yview)
        self.listbox_akts_scrollbar.pack(side='right', fill='y')
        self.listbox_akts.config(yscrollcommand=self.listbox_akts_scrollbar.set)
        self.listbox_akts.bind('<Button-3>', self.menu_listbox_akts)
        self.frame_listbox_akts.pack()
        self.frame_list_akts.grid(row=0, column=0)

        self.root.mainloop()

    # Функция ОТКРЫТЬ из МЕНЮ
    def new_file(self):
        x_data_akt = data_akt.Data_Akt()
        self.updater_list(self.listbox_names, x_data_akt.get_all_name_object_names())
        self.updater_list(self.listbox_organization, x_data_akt.get_all_organizations_names())
        self.updater_list(self.listbox_representative, x_data_akt.get_all_representatives_names())

    def load_file(self):
        global x_data_akt
        self.file = tkinter.filedialog.askopenfilename(defaultextension='dat')
        x_data_akt = data_akt.load(self.file)
        self.updater_list(self.listbox_names, x_data_akt.get_all_name_object_names())
        self.updater_list(self.listbox_organization, x_data_akt.get_all_organizations_names())
        self.updater_list(self.listbox_representative, x_data_akt.get_all_representatives_names())

    def save_file(self):
        self.file = tkinter.filedialog.asksaveasfilename(defaultextension='dat')
        data_akt.save(self.file, x_data_akt)

    def updater_list(self, list_object, var):
        elements = tkinter.Variable(value=var)
        list_object.config(listvariable=elements)

    # Контекстное меню для НАИМЕНОВАНИЯ ОБЪЕКТА во вкладке ОБЪЕКТ
    def menu_names_object(self, event):
        menu = tkinter.Menu(tearoff=0)
        menu.add_command(label='Добавить', command=self.add_name_object)
        menu.add_command(label='Изменить', command=self.change_name_object)
        menu.add_command(label='Удалить', command=self.delete_name_object)
        menu.post(event.x_root, event.y_root)

    def add_name_object(self):
        window = Window_object_element(self.root, self.listbox_names, 'имена')

    def change_name_object(self):
        index = self.listbox_names.curselection()[0]
        window = Window_object_element(self.root, self.listbox_names, 'имена', index)

    def delete_name_object(self):
        index = self.listbox_names.curselection()
        x_data_akt.delete_name_object(index[0])
        self.updater_list(self.listbox_names, x_data_akt.get_all_names_object())

    # Контекстное меню для ОРГАНИЗАЦИЙ вкладке ОБЪЕКТ
    def menu_organization(self, event):
        menu = tkinter.Menu(tearoff=0)
        menu.add_command(label='Добавить', command=self.add_organization)
        menu.add_command(label='Изменить', command=self.change_organization)
        menu.add_command(label='Удалить', command=self.delete_organization)
        menu.post(event.x_root, event.y_root)

    def add_organization(self):
        window = Window_object_element(self.root, self.listbox_organization, 'организации')  # self.organizations,

    def change_organization(self):
        index = self.listbox_organization.curselection()[0]
        window = Window_object_element(self.root, self.listbox_organization, 'организации', index)  # self.organizations,

    def delete_organization(self):
        index = self.listbox_organization.curselection()
        x_data_akt.delete_organization(index[0])
        self.updater_list(self.listbox_organization, x_data_akt.get_all_organizations_names())

    # Контекстное меню для ПРЕДСТАВИТЕЛЕЙ вкладке ОБЪЕКТ
    def menu_representative(self, event):
        menu = tkinter.Menu(tearoff=0)
        menu.add_command(label='Добавить', command=self.add_representative)
        menu.add_command(label='Изменить', command=self.change_representative)
        menu.add_command(label='Удалить', command=self.delete_representative)
        menu.post(event.x_root, event.y_root)

    def add_representative(self):
        window = Window_object_element(self.root, self.listbox_representative, 'представители')

    def change_representative(self):
        index = self.listbox_representative.curselection()[0]
        window = Window_object_element(self.root, self.listbox_representative, 'представители', index)

    def delete_representative(self):
        index = self.listbox_representative.curselection()
        x_data_akt.delete_representative(index[0])
        self.listbox_representative.delete(index[0])

    # Контекстное меню для СПИСКА АКТОВ вкладке АКТЫ
    def menu_listbox_akts(self, event):
        menu = tkinter.Menu(tearoff=0)
        menu.add_command(label='Добавить', command=self.add_akt)
        menu.add_command(label='Изменить', command=self.change_akt)
        menu.add_command(label='Удалить', command=self.delete_akt)
        menu.post(event.x_root, event.y_root)

    def add_akt(self):
        window = Window_akt(self.root, self.listbox_akts)

    def change_akt(self):
        pass

    def delete_akt(self):
        index = self.listbox_akts.curselection()
        x_data_akt.delete_akt(index[0])
        self.listbox_akts.delete(index[0])


class Window_object_element:
    def __init__(self, root, listbox, type_element, index=None):
        self.__root = root
        self.__listbox = listbox
        self.__type_element = type_element
        if index is None:
            self.__index = None
            self.__text = 'Введите необходимую информацию'
            self.__name = 'Введите наименование'
            self.__text_button = 'Добавить'
        else:
            self.__index = index
            self.__name, self.__text = self.get_name_and_text()
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
            if self.__index is None:
                self.set_element_data_akt(text, name)
                elements = tkinter.Variable(value=self.get_names())
                self.__listbox.config(listvariable=elements)
                self.window.destroy()
            else:
                self.change_element_data_akt(text, name)
                elements = tkinter.Variable(value=self.get_names())
                self.__listbox.config(listvariable=elements)
                self.window.destroy()

        if text == '' and name == '':
            self.label_indicator_text.config(text='Введенная информация не может быть пустой')
            self.label_indicator_entry.config(text='Наменование не может быть пустым')
        elif text == '':
            self.label_indicator_text.config(text='Введенная информация не может быть пустой')
        elif name == '':
            self.label_indicator_entry.config(text='Наменование не может быть пустым')
        elif text == self.__text and name == self.__name:
            self.label_indicator_text.config(text='Изменений не обнаруженно')
            self.label_indicator_entry.config(text='Введенная информация должна отличаться от предыдущей')
        else:
            set_name(text, name)

    def get_name_and_text(self):
        if self.__type_element == 'имена':
            return x_data_akt.get_name_object_name(self.__index), x_data_akt.get_name_object_text(self.__index)
        elif self.__type_element == 'организации':
            return x_data_akt.get_organization_name(self.__index), x_data_akt.get_organization_text(self.__index)
        elif self.__type_element == 'представители':
            return x_data_akt.get_representative_name(self.__index), x_data_akt.get_representative_text(self.__index)

    def get_names(self):
        if self.__type_element == 'имена':
            return x_data_akt.get_all_name_object_names()
        elif self.__type_element == 'организации':
            return x_data_akt.get_all_organizations_names()
        elif self.__type_element == 'представители':
            return x_data_akt.get_all_representatives_names()

    def set_element_data_akt(self, text, name):
        if self.__type_element == 'имена':
            x_data_akt.set_name_object(text, name)
        elif self.__type_element == 'организации':
            x_data_akt.set_organization(text, name)
        elif self.__type_element == 'представители':
            x_data_akt.set_representative(text, name)

    def change_element_data_akt(self, text, name):
        if self.__type_element == 'имена':
            x_data_akt.change_name_object(text, name, self.__index)
        elif self.__type_element == 'организации':
            x_data_akt.change_organization(text, name, self.__index)
        elif self.__type_element == 'представители':
            x_data_akt.change_representative(text, name, self.__index)


class Window_akt:
    def __init__(self, root, listbox, index=None):
        self.__root = root
        self.__listbox = listbox

        self.window_creat_akt = Toplevel(self.__root)
        self.window_creat_akt.title('Акт')
        self.window_creat_akt.geometry('500x500')
        self.frame_window_akt = tkinter.Frame(self.window_creat_akt)

        self.frame_object = tkinter.LabelFrame(self.frame_window_akt, text='Объект, организации, представители')
        self.label_object = tkinter.Label(self.frame_object, text='Выберите наименование объекта')
        self.label_object.grid(row=0, column=0, stick='e')  # pack(side = 'left')
        # Combobox наименование объекта
        self.combobox_object = ttk.Combobox(self.frame_object,
                                            width=50,
                                            values=x_data_akt.get_all_name_object_names())
        self.combobox_object.grid(row=0, column=1)  # pack(side = 'right')

        self.label_developer = tkinter.Label(self.frame_object, text='Выберите застройщика')
        self.label_developer.grid(row=1, column=0, stick='e')  # pack(side='left')
        # Combobox застройщик
        self.combobox_developer = ttk.Combobox(self.frame_object,
                                               width=50,
                                               values=x_data_akt.get_all_organizations_names())
        self.combobox_developer.grid(row=1, column=1)  # pack(side='right')

        self.label_builder = tkinter.Label(self.frame_object, text='Выберите лицо осуществляющее строительство')
        self.label_builder.grid(row=2, column=0, stick='e')  # pack(side='left')
        # Combobox лицо осуществляющее строительство
        self.combobox_builder = ttk.Combobox(self.frame_object,
                                             width=50,
                                             values=x_data_akt.get_all_organizations_names())
        self.combobox_builder.grid(row=2, column=1)  # pack(side='right')

        self.label_designer = tkinter.Label(self.frame_object, text='Выберите проектировщика')
        self.label_designer.grid(row=3, column=0, stick='e')  # pack(side='left')
        # Combobox проектировщик
        self.combobox_designer = ttk.Combobox(self.frame_object,
                                              width=50,
                                              values=x_data_akt.get_all_organizations_names())
        self.combobox_designer.grid(row=3, column=1)  # pack(side='right')

        self.label_developer_name = tkinter.Label(self.frame_object,
                                                  text='Выберите представителя застройщика\n' +
                                                       'по вопросам строительного контроля')
        self.label_developer_name.grid(row=4, column=0, stick='e')
        # Combobox представитель застройщика по вопросам строительства
        self.combobox_developer_name = ttk.Combobox(self.frame_object,
                                                    width=50,
                                                    values=x_data_akt.get_all_representatives_names())
        self.combobox_developer_name.grid(row=4, column=1, stick='ns')

        self.label_builder_name = tkinter.Label(self.frame_object,
                                                text='Выберите представителя\n' +
                                                     'лица осуществляющего строительство')
        self.label_builder_name.grid(row=5, column=0, stick='e')
        # Combobox представитель лица осуществляющего строительство
        self.combobox_builder_name = ttk.Combobox(self.frame_object,
                                                  width=50,
                                                  values=x_data_akt.get_all_representatives_names())
        self.combobox_builder_name.grid(row=5, column=1, stick='ns')

        self.label_builder_control_name = tkinter.Label(self.frame_object,
                                                        text='Выберите представителя строителя\n' +
                                                             'по вопросам строительного контроля')
        self.label_builder_control_name.grid(row=6, column=0, stick='e')
        # Combobox представитель строителя по вопросам строительного контроля
        self.combobox_builder_control_name = ttk.Combobox(self.frame_object,
                                                          width=50,
                                                          values=x_data_akt.get_all_representatives_names())
        self.combobox_builder_control_name.grid(row=6, column=1, stick='ns')

        self.label_designer_name = tkinter.Label(self.frame_object,
                                                 text='Выберите представителя осуществляющего\n' +
                                                      'подготовку проектной документации')
        self.label_designer_name.grid(row=7, column=0, stick='e')
        # Combobox представитель осуществляющей подготовку строительной документации
        self.combobox_designer_name = ttk.Combobox(self.frame_object,
                                                   width=50,
                                                   values=x_data_akt.get_all_representatives_names())
        self.combobox_designer_name.grid(row=7, column=1, stick='ns')

        self.label_contractor_name = tkinter.Label(self.frame_object,
                                                   text='Выберите представителя\n' +
                                                        'выполнившего работы')
        self.label_contractor_name.grid(row=8, column=0, stick='e')
        # Combobox представитель выполняющий работы
        self.combobox_contractor_name = ttk.Combobox(self.frame_object,
                                                     width=50,
                                                     values=x_data_akt.get_all_representatives_names())
        self.combobox_contractor_name.grid(row=8, column=1, stick='ns')

        self.label_another_person = tkinter.Label(self.frame_object,
                                                  text='Выберите иного представителя\n' +
                                                       'учавствующего в осведетельствовании')
        self.label_another_person.grid(row=9, column=0, stick='e')
        # Combobox представитель учавствующий в осведетельствовании
        self.combobox_another_person = ttk.Combobox(self.frame_object,
                                                    width=50,
                                                    values=x_data_akt.get_all_representatives_names())
        self.combobox_another_person.grid(row=9, column=1, stick='ns')

        self.label_contractor = tkinter.Label(self.frame_object,
                                              text='Выберите организацию выполняющую работы')
        self.label_contractor.grid(row=10, column=0, stick='e')
        # Combobox организация выполняющая работы
        self.combobox_contractor = ttk.Combobox(self.frame_object,
                                                width=50,
                                                values=x_data_akt.get_all_organizations_names())
        self.combobox_contractor.grid(row=10, column=1, stick='ns')

        self.frame_date = tkinter.LabelFrame(self.frame_window_akt, text='Дата начала и окончания работ')
        self.label_start_date = tkinter.Label(self.frame_date, text='Начала работ:')
        self.label_start_date.grid(row=0, column=0)
        self.entry_start_date = tkinter.Entry(self.frame_date, width=10)
        self.entry_start_date.grid(row=0, column=1, padx=[0, 10])
        self.label_start_date = tkinter.Label(self.frame_date, text='Окончание работ:')
        self.label_start_date.grid(row=0, column=2, padx=[10, 0])
        self.entry_start_date = tkinter.Entry(self.frame_date, width=10)
        self.entry_start_date.grid(row=0, column=3)

        self.frame_work = tkinter.LabelFrame(self.frame_window_akt, text='Наименование работ')
        self.label_work = tkinter.Label(self.frame_work, text='Введите наименование работ:')
        self.label_work.grid(row=0, column=0)
        self.entry_work = tkinter.Entry(self.frame_work, width=50)
        self.entry_work.grid(row=0, column=1)

        self.frame_object.grid(row=0, column=0)
        self.frame_date.grid(row=1, column=0, stick='we')
        self.frame_work.grid(row=2, column=0, stick='we')

        self.button_akt = tkinter.Button(self.window_creat_akt, text='Создать акт', command=self.akt)

        self.frame_window_akt.pack()
        self.button_akt.pack()

    def akt(self):
        # функция для получения данный из полей
        def insert_data(index, data_from_combobox, data_tuple):
            if index == -1:
                return data_akt.Object_element(data_from_combobox, '')
            else:
                return data_tuple[index]
        # получение имени объекта
        name_object = insert_data(self.combobox_object.current(), self.combobox_object.get(), x_data_akt.get_all_names_object())
        developer = insert_data(self.combobox_developer.current(), self.combobox_developer.get(), x_data_akt.get_all_organizations())
        builder = insert_data(self.combobox_builder.current(), self.combobox_builder.get(), x_data_akt.get_all_organizations())
        designer = insert_data(self.combobox_designer.current(), self.combobox_designer.get(), x_data_akt.get_all_organizations())
        developer_name = insert_data(self.combobox_developer_name.current(), self.combobox_developer_name.get(), x_data_akt.get_all_representatives())
        builder_name = insert_data(self.combobox_builder_name.current(), self.combobox_builder_name.get(), x_data_akt.get_all_representatives())
        builder_control_name = insert_data(self.combobox_builder_control_name.current(), self.combobox_builder_control_name.get(), x_data_akt.get_all_representatives())
        designer_name = insert_data(self.combobox_designer_name.current(), self.combobox_designer_name.get(), x_data_akt.get_all_representatives())
        contractor_name = insert_data(self.combobox_contractor_name.current(), self.combobox_contractor_name.get(), x_data_akt.get_all_representatives())
        another_person = insert_data(self.combobox_another_person.current(), self.combobox_another_person.get(), x_data_akt.get_all_representatives())
        contractor = insert_data(self.combobox_contractor.current(), self.combobox_contractor.get(), x_data_akt.get_all_organizations())
        work = self.entry_work.get()

        akt = data_akt.Akt()
        akt.set_name_object(name_object)
        akt.set_developer(developer)
        akt.set_builder(builder)
        akt.set_designer(designer)
        akt.set_developer_name(developer_name)
        akt.set_builder_name(builder_name)
        akt.set_builder_control_name(builder_control_name)
        akt.set_designer_name(designer_name)
        akt.set_contractor_name(contractor_name)
        akt.set_another_person(another_person)
        akt.set_contractor(contractor)
        akt.set_name_work(work)

        x_data_akt.set_akt(akt)
        elements = tkinter.Variable(value=tuple(element.get_name_work() for element in x_data_akt.get_all_akts()))
        self.__listbox.config(listvariable=elements)
        self.window_creat_akt.destroy()

if __name__ == '__main__':
    window = RootGUI()