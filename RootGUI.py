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
        self.listbox_akts.bind('<<ListboxSelect>>', self.view_akt)
        self.frame_listbox_akts.pack()
        self.frame_list_akts.grid(row=0, column=0)

        # Создание группы виджетов ПРОСМОТР АКТА
        self.frame_view_akt = tkinter.LabelFrame(self.frame_akt, text='Акт')
        self.frame_for_canvas = tkinter.Frame(self.frame_view_akt)
        self.canvas = tkinter.Canvas(self.frame_for_canvas, bg="white", width=720, height=750)
        self.frame_in_canvas = tkinter.Frame(self.frame_for_canvas, bg="white")

        self.label_object_name = tkinter.Label(self.frame_in_canvas,
                                               background='white',
                                               font=("Times new roman", 12, 'bold'),
                                               text='Объект капитального строительства:')
        self.text_object_name = tkinter.Text(self.frame_in_canvas,
                                             height=5,
                                             width=90,
                                             font=("Times new roman", 12),
                                             wrap='word')
        self.label_developer = tkinter.Label(self.frame_in_canvas,
                                             background='white',
                                             font=("Times new roman", 12, 'bold'),
                                             justify='left',
                                             text='Застройщик, технический заказчик, лицо, ответственное за ' +
                                             'эксплотацию здания, сооружения,\nили региональный оператор:')
        self.text_developer = tkinter.Text(self.frame_in_canvas,
                                           height=5,
                                           width=90,
                                           font=("Times new roman", 12),
                                           wrap='word')
        self.label_builder = tkinter.Label(self.frame_in_canvas,
                                           background='white',
                                           font=("Times new roman", 12, 'bold'),
                                           text='Лицо, осуществляющее строительство, реконструкцию, ' +
                                                'капитальный ремонт:')
        self.text_builder = tkinter.Text(self.frame_in_canvas,
                                         height=5,
                                         width=90,
                                         font=("Times new roman", 12),
                                         wrap='word')
        self.label_designer = tkinter.Label(self.frame_in_canvas,
                                            background='white',
                                            font=("Times new roman", 12, 'bold'),
                                            text='Лицо, осуществляющее подготовку проектной документации:')
        self.text_designer = tkinter.Text(self.frame_in_canvas,
                                          height=5,
                                          width=90,
                                          font=("Times new roman", 12),
                                          wrap='word')
        self.label_doc1 = tkinter.Label(self.frame_in_canvas,
                                        background='white',
                                        font=("Times new roman", 12, 'bold'),
                                        text='АКТ\nосвидетельствования скрытых работ')
        self.frame_number_and_date = tkinter.Frame(self.frame_in_canvas, background='white')
        self.label_act_number = tkinter.Label(self.frame_number_and_date,
                                              background='white',
                                              font=("Times new roman", 12),
                                              text='№')
        self.entry_act_number = tkinter.Entry(self.frame_number_and_date,
                                              background='white',
                                              font=("Times new roman", 12),
                                              width=5)
        self.entry_act_date = tkinter.Entry(self.frame_number_and_date,
                                              background='white',
                                              font=("Times new roman", 12))
        self.label_developer_name = tkinter.Label(self.frame_in_canvas,
                                              background='white',
                                              font=("Times new roman", 12, 'bold'),
                                              justify='left',
                                              text='\nПредставитель застройщика, технического заказчика, ' +
                                                  'лица ответственного за эксплуатацию здания,\nсооружения,' +
                                                  'или регионального оператора по вопросам строительного контроля:')
        self.text_developer_name = tkinter.Text(self.frame_in_canvas,
                                                height=5,
                                                width=90,
                                                font=("Times new roman", 12),
                                                wrap='word')
        self.label_builder_name = tkinter.Label(self.frame_in_canvas,
                                                background='white',
                                                font=("Times new roman", 12, 'bold'),
                                                justify='left',
                                                text='Представитель лица, осуществляющего строительство, ' +
                                                     'реконструкцию, капитальный ремонт:')
        self.text_builder_name = tkinter.Text(self.frame_in_canvas,
                                                height=5,
                                                width=90,
                                                font=("Times new roman", 12),
                                                wrap='word')
        self.label_builder_control_name = tkinter.Label(self.frame_in_canvas,
                                                background='white',
                                                font=("Times new roman", 12, 'bold'),
                                                justify='left',
                                                text='Представитель лица, осуществляющего строительство, ' +
                                                     'реконструкцию, капитальный ремонт,\nпо вопросам ' +
                                                     'строительного контроля')
        self.text_builder_control_name = tkinter.Text(self.frame_in_canvas,
                                                height=5,
                                                width=90,
                                                font=("Times new roman", 12),
                                                wrap='word')
        self.label_designer_name = tkinter.Label(self.frame_in_canvas,
                                                 background='white',
                                                 font=("Times new roman", 12, 'bold'),
                                                 justify='left',
                                                 text='Представитель лица, осуществляющего подготовку проектной' +
                                                 'документации (в случае\nпривлечения застройщиком лица,' +
                                                 'осуществляющего подготовку строительной документации, для\nпроверки' +
                                                 'соответсвия выполняемых работ проектной документации согласно' +
                                                 'части 2 статьи 53\n'
                                                 'Градостроительного кодекса Российской Федирации:')
        self.text_designer_name = tkinter.Text(self.frame_in_canvas,
                                               height=5,
                                               width=90,
                                               font=("Times new roman", 12),
                                               wrap='word')
        self.label_contractor_name = tkinter.Label(self.frame_in_canvas,
                                                 background='white',
                                                 font=("Times new roman", 12, 'bold'),
                                                 justify='left',
                                                 text='Представитель лица, выполнявщего работы, подлежащие ' +
                                                      'освидетельствованию (в случае\nвыполнения работы по договорам о' +
                                                      'строительстве, реконструкции, капитальном ремонте\nобъектов' +
                                                      'капитального строительства, заключенным с иными лицами):')
        self.text_contractor_name = tkinter.Text(self.frame_in_canvas,
                                               height=5,
                                               width=90,
                                               font=("Times new roman", 12),
                                               wrap='word')
        self.label_another_person = tkinter.Label(self.frame_in_canvas,
                                                 background='white',
                                                 font=("Times new roman", 12, 'bold'),
                                                 justify='left',
                                                 text='а также иные представители лиц, учавствующих в ' +
                                                      'освидетельствовании:')
        self.text_another_person = tkinter.Text(self.frame_in_canvas,
                                                height=5,
                                                width=90,
                                                font=("Times new roman", 12),
                                                wrap='word')
        self.frame_contractor = tkinter.Frame(self.frame_in_canvas, background='white')
        self.label_contractor = tkinter.Label(self.frame_contractor,
                                                 background='white',
                                                 font=("Times new roman", 12, 'bold'),
                                                 justify='left',
                                                 text='приозвели осмотр работ, выполненных: ')
        self.text_contractor = tkinter.Text(self.frame_contractor,
                                            height=1,
                                            width=52,
                                            font=("Times new roman", 12),
                                            wrap='word')
        self.label_doc2 = tkinter.Label(self.frame_in_canvas,
                                        background='white',
                                        font=("Times new roman", 12, 'bold'),
                                        text='и составили настоящий акт о нижеследующем:')
        self.label_work = tkinter.Label(self.frame_in_canvas,
                                        background='white',
                                        font=("Times new roman", 12, 'bold'),
                                        text='1. К освидетельствованию предъявлены следующие работы:')
        self.text_work = tkinter.Text(self.frame_in_canvas,
                                    height=3,
                                    width=90,
                                    font=("Times new roman", 12),
                                    wrap='word')
        self.label_documentation = tkinter.Label(self.frame_in_canvas,
                                        background='white',
                                        font=("Times new roman", 12, 'bold'),
                                        text='2. Работы выполнены по проектно-сметной документации:')
        self.text_documentation = tkinter.Text(self.frame_in_canvas,
                                               height=3,
                                               width=90,
                                               font=("Times new roman", 12),
                                               wrap='word')

        self.label_object_name.grid(row=0, column=0, columnspan=1, sticky='w')
        self.text_object_name.grid(row=1, column=0, columnspan=1, sticky='w')
        self.label_developer.grid(row=2, column=0, columnspan=1, sticky='w')
        self.text_developer.grid(row=3, column=0, columnspan=1, sticky='w')
        self.label_builder.grid(row=5, column=0, columnspan=1, sticky='w')
        self.text_builder.grid(row=6, column=0, columnspan=1, sticky='w')
        self.label_designer.grid(row=7, column=0, columnspan=1, sticky='w')
        self.text_designer.grid(row=8, column=0, columnspan=1, sticky='w')
        self.label_doc1.grid(row=9, column=0, columnspan=1)
        self.frame_number_and_date.grid(row=10, column=0, columnspan=1, sticky='we')
        self.label_act_number.pack(side='left')
        self.entry_act_number.pack(side='left')
        self.entry_act_date.pack(side='right')
        self.label_developer_name.grid(row=11, column=0, columnspan=1, sticky='w')
        self.text_developer_name.grid(row=12, column=0, columnspan=1, sticky='w')
        self.label_builder_name.grid(row=13, column=0, columnspan=1, sticky='w')
        self.text_builder_name.grid(row=14, column=0, columnspan=1, sticky='w')
        self.label_builder_control_name.grid(row=15, column=0, columnspan=1, sticky='w')
        self.text_builder_control_name.grid(row=16, column=0, columnspan=1, sticky='w')
        self.label_designer_name.grid(row=17, column=0, columnspan=1, sticky='w')
        self.text_designer_name.grid(row=18, column=0, columnspan=1, sticky='w')
        self.label_contractor_name.grid(row=19, column=0, columnspan=1, sticky='w')
        self.text_contractor_name.grid(row=20, column=0, columnspan=1, sticky='w')
        self.label_another_person.grid(row=21, column=0, columnspan=1, sticky='w')
        self.text_another_person.grid(row=22, column=0, columnspan=1, sticky='w')
        self.frame_contractor.grid(row=23, column=0, columnspan=1, sticky='w')
        self.label_contractor.pack(side='left')
        self.text_contractor.pack(side='left')
        self.label_doc2.grid(row=24, column=0, columnspan=1, sticky='w')
        self.label_work.grid(row=25, column=0, columnspan=1, sticky='w')
        self.text_work.grid(row=26, column=0, columnspan=1, sticky='w')
        self.label_documentation.grid(row=27, column=0, columnspan=1, sticky='w')
        self.text_documentation.grid(row=28, column=0, columnspan=1, sticky='w')

        self.canvas.create_window(0, 0, anchor='nw', window=self.frame_in_canvas)

        self.canvas_scrollbar = tkinter.Scrollbar(self.frame_for_canvas, command=self.canvas.yview)
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"), yscrollcommand=self.canvas_scrollbar.set)
        self.canvas.pack(side='left')
        self.canvas_scrollbar.pack(side='right', fill='y')
        self.frame_for_canvas.pack()
        self.frame_view_akt.grid(row=0, column=1)

        self.root.mainloop()

    # Функция ОТКРЫТЬ из МЕНЮ
    def new_file(self):
        x_data_akt = data_akt.Data_Akt()
        self.updater_list(self.listbox_names, x_data_akt.get_all_name_object_names())
        self.updater_list(self.listbox_organization, x_data_akt.get_all_organizations_names())
        self.updater_list(self.listbox_representative, x_data_akt.get_all_representatives_names())
        self.updater_list(self.listbox_akts, x_data_akt.get_all_akts_names())

    def load_file(self):
        global x_data_akt
        self.file = tkinter.filedialog.askopenfilename(defaultextension='dat')
        x_data_akt = data_akt.load(self.file)
        self.updater_list(self.listbox_names, x_data_akt.get_all_name_object_names())
        self.updater_list(self.listbox_organization, x_data_akt.get_all_organizations_names())
        self.updater_list(self.listbox_representative, x_data_akt.get_all_representatives_names())
        self.updater_list(self.listbox_akts, x_data_akt.get_all_akts_names())

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
        window = Window_object_element(self.root, self.listbox_organization, 'организации')

    def change_organization(self):
        index = self.listbox_organization.curselection()[0]
        window = Window_object_element(self.root, self.listbox_organization, 'организации', index)

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
        menu.add_command(label='Создать новый акт', command=self.add_akt)
        menu.add_command(label='Создать акт на основе выбранного', command=self.add_akt_based_on)
        menu.add_command(label='Изменить', command=self.change_akt)
        menu.add_command(label='Удалить', command=self.delete_akt)
        menu.post(event.x_root, event.y_root)

    def add_akt(self):
        window = Window_akt(self.root, self.listbox_akts, 'новый')

    def add_akt_based_on(self):
        index = self.listbox_akts.curselection()[0]
        window = Window_akt(self.root, self.listbox_akts, 'на основе другого', index)

    def change_akt(self):
        index = self.listbox_akts.curselection()[0]
        window = Window_akt(self.root, self.listbox_akts, 'изменить', index)

    def delete_akt(self):
        index = self.listbox_akts.curselection()
        x_data_akt.delete_akt(index[0])
        self.listbox_akts.delete(index[0])

    def view_akt(self, event):
        self.text_object_name.delete(0.0, 'end')
        self.text_developer.delete(0.0, 'end')
        self.text_builder.delete(0.0, 'end')
        self.text_designer.delete(0.0, 'end')
        self.entry_act_number.delete(0, 'end')
        self.entry_act_date.delete(0, 'end')
        self.text_developer_name.delete(0.0, 'end')
        self.text_builder_name.delete(0.0, 'end')
        self.text_builder_control_name.delete(0.0, 'end')
        self.text_designer_name.delete(0.0, 'end')
        self.text_contractor_name.delete(0.0, 'end')
        self.text_another_person.delete(0.0, 'end')
        self.text_contractor.delete(0.0, 'end')
        self.text_work.delete(0.0, 'end')
        self.text_documentation.delete(0.0, 'end')
        index = self.listbox_akts.curselection()
        self.text_object_name.insert('end', x_data_akt.get_akt(index[0]).get_name_object().get_text())
        self.text_developer.insert('end', x_data_akt.get_akt(index[0]).get_developer().get_text())
        self.text_builder.insert('end', x_data_akt.get_akt(index[0]).get_builder().get_text())
        self.text_designer.insert('end', x_data_akt.get_akt(index[0]).get_designer().get_text())
        # self.entry_act_number.insert('end', )
        self.entry_act_date.insert('end', x_data_akt.get_akt(index[0]).get_str_finish_date())
        self.text_developer_name.insert('end', x_data_akt.get_akt(index[0]).get_developer_name().get_text())
        self.text_builder_name.insert('end', x_data_akt.get_akt(index[0]).get_builder_name().get_text())
        self.text_builder_control_name.insert('end', x_data_akt.get_akt(index[0]).get_builder_control_name().get_text())
        self.text_designer_name.insert('end', x_data_akt.get_akt(index[0]).get_designer_name().get_text())
        self.text_contractor_name.insert('end', x_data_akt.get_akt(index[0]).get_contractor_name().get_text())
        self.text_another_person.insert('end', x_data_akt.get_akt(index[0]).get_another_person().get_text())
        self.text_contractor.insert('end', x_data_akt.get_akt(index[0]).get_contractor().get_text())

        self.text_work.insert('end', x_data_akt.get_akt(index[0]).get_name_work())
        self.text_documentation.insert('end',x_data_akt.get_akt(index[0]).get_text_of_documentation())



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
    def __init__(self, root, listbox, action, index=None):
        self.__root = root
        self.__listbox = listbox
        self.__indicator = ''
        if index is None:
            self.__index = None
            self.__name_object = None
            self.__developer = None
            self.__builder = None
            self.__designer = None
            self.__developer_name = None
            self.__builder_name = None
            self.__builder_control_name = None
            self.__designer_name = None
            self.__contractor_name = None
            self.__another_person = None
            self.__contractor = None
            self.__start_date = None
            self.__finish_date = None
            self.__work = None
            self.__documentation = None
        else:
            self.__index = index
            self.__name_object = self.old_elements(x_data_akt.get_akt(index).get_name_object())
            self.__developer = self.old_elements(x_data_akt.get_akt(index).get_developer())
            self.__builder = self.old_elements(x_data_akt.get_akt(index).get_builder())
            self.__designer = self.old_elements(x_data_akt.get_akt(index).get_designer())
            self.__developer_name = self.old_elements(x_data_akt.get_akt(index).get_developer_name())
            self.__builder_name = self.old_elements(x_data_akt.get_akt(index).get_builder_name())
            self.__builder_control_name = self.old_elements(x_data_akt.get_akt(index).get_builder_control_name())
            self.__designer_name = self.old_elements(x_data_akt.get_akt(index).get_designer_name())
            self.__contractor_name = self.old_elements(x_data_akt.get_akt(index).get_contractor_name())
            self.__another_person = self.old_elements(x_data_akt.get_akt(index).get_another_person())
            self.__contractor = self.old_elements(x_data_akt.get_akt(index).get_contractor())
            self.__start_date = x_data_akt.get_akt(index).get_str_start_date()
            self.__finish_date = x_data_akt.get_akt(index).get_str_finish_date()
            self.__work = x_data_akt.get_akt(index).get_name_work()
            self.__documentation = x_data_akt.get_akt(index).get_documentation()

        if action == 'новый':
            self.__action = action
            self.__heading = 'Создание акта'
            self.__text_button = 'Создать акт'
        elif action == 'на основе другого':
            self.__action = action
            self.__heading = f'Создание акта на основе "{self.__work}"'
            self.__text_button = 'Создать акт'
        elif action == 'изменить':
            self.__action = action
            self.__heading = f'Изменение акта "{self.__work}"'
            self.__text_button = 'Изменить акт'

        self.window_creat_akt = Toplevel(self.__root)
        self.window_creat_akt.title(self.__heading)
        self.window_creat_akt.geometry('700x900')
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

        self.frame_work = tkinter.LabelFrame(self.frame_window_akt, text='Наименование работ')
        self.label_work = tkinter.Label(self.frame_work, text='Введите наименование работ:')
        self.label_work.grid(row=0, column=0)
        self.entry_work = tkinter.Entry(self.frame_work, width=50)
        self.entry_work.grid(row=0, column=1)

        self.frame_date = tkinter.LabelFrame(self.frame_window_akt, text='Дата начала и окончания работ')
        self.label_start_date = tkinter.Label(self.frame_date, text='Начала работ:')
        self.label_start_date.pack(side='left')
        self.entry_start_date = tkinter.Entry(self.frame_date, width=20)
        self.entry_start_date.pack(side='left')
        self.entry_finish_date = tkinter.Entry(self.frame_date, width=20)
        self.entry_finish_date.pack(side='right')
        self.label_finis_date = tkinter.Label(self.frame_date, text='Окончание работ:')
        self.label_finis_date.pack(side='right')

        self.frame_documentation = tkinter.LabelFrame(self.frame_window_akt, text='Проектно-сметная документация')
        self.label_org = tkinter.Label(self.frame_documentation, text='Организация')
        self.label_doc = tkinter.Label(self.frame_documentation, text='Документация')
        self.label_page = tkinter.Label(self.frame_documentation, text='Страница/Листы')
        self.button_add_org = tkinter.Button(self.frame_documentation, text='>>', command=self.add_widget_from_doc)
        self.label_org.grid(row=0, column=1, rowspan=1, stick='ns')
        self.label_doc.grid(row=0, column=2, rowspan=1, stick='ns')
        self.label_page.grid(row=0, column=3, rowspan=1, stick='ns')
        self.button_add_org.grid(row=1, column=0, rowspan=1, stick='ns')

        self.list_documentation = []
        self.list_documentation.append(ttk.Combobox(self.frame_documentation,
                                                    width=30,
                                                    values=x_data_akt.get_all_organizations_names()))
        self.list_documentation.append(ttk.Combobox(self.frame_documentation,
                                                    width=30))
        self.list_documentation.append(tkinter.Entry(self.frame_documentation, width=30))
        self.list_documentation[0].grid(row=1, column=1, stick='we')
        self.list_documentation[1].grid(row=1, column=2, stick='we')
        self.list_documentation[2].grid(row=1, column=3, stick='we')

        if index is not None:
            self.combobox_object.set(self.__name_object)
            self.combobox_developer.set(self.__developer)
            self.combobox_builder.set(self.__builder)
            self.combobox_designer.set(self.__designer)
            self.combobox_developer_name.set(self.__developer_name)
            self.combobox_builder_name.set(self.__builder_name)
            self.combobox_builder_control_name.set(self.__builder_control_name)
            self.combobox_designer_name.set(self.__designer_name)
            self.combobox_contractor_name.set(self.__contractor_name)
            self.combobox_another_person.set(self.__another_person)
            self.combobox_contractor.set(self.__contractor)
            self.entry_start_date.insert('end', self.__start_date)
            self.entry_finish_date.insert('end', self.__finish_date)
            self.entry_work.insert('end', self.__work)
            self.old_doc(self.__documentation)


        self.frame_object.grid(row=0, column=0)
        self.frame_work.grid(row=1, column=0, stick='we')
        self.frame_date.grid(row=2, column=0, stick='we')
        self.frame_documentation.grid(row=3, column=0, stick='we')

        self.button_akt = tkinter.Button(self.window_creat_akt, text=self.__text_button, command=self.akt)
        self.label_indicator = tkinter.Label(self.window_creat_akt, foreground='red')

        self.frame_window_akt.pack()
        self.button_akt.pack()
        self.label_indicator.pack()

    def old_elements(self, elements_of_akt):
        if elements_of_akt is None:
            return ''
        elif elements_of_akt.get_name() is None:
            return elements_of_akt.get_text()
        else:
            return elements_of_akt.get_name()

    def add_widget_from_doc(self):
        if self.list_documentation[-2].get() != '':
            self.list_documentation.append(ttk.Combobox(self.frame_documentation,
                                                        width=30,
                                                        values=x_data_akt.get_all_organizations_names()))
            self.list_documentation.append(ttk.Combobox(self.frame_documentation,
                                                        width=30))
            self.list_documentation.append(tkinter.Entry(self.frame_documentation, width=30))
            self.list_documentation[-3].grid(row=int(len(self.list_documentation)/3), column=1, stick='we')
            self.list_documentation[-2].grid(row=int(len(self.list_documentation)/3), column=2, stick='we')
            self.list_documentation[-1].grid(row=int(len(self.list_documentation)/3), column=3, stick='we')
            self.button_add_org.grid(row=1, column=0, rowspan=int(len(self.list_documentation)/3)+1, stick='ns')

    def old_doc(self, documentation):
        for component in documentation:
            self.list_documentation[-3].set(self.old_elements(component.get_organization()))
            self.list_documentation[-2].set(component.get_name_doc().get_text())
            self.list_documentation[-1].insert('end', component.get_page())
            self.add_widget_from_doc()

    def akt(self):

        # функция для получения данный из полей
        def insert_data(combobox, data_tuple):
            index = combobox.current()
            if index == -1:
                return data_akt.Object_element(combobox.get(), None)
            else:
                return data_tuple[index]

        # функция для получения данный из группы виджетов Проектно-сметная документация
        def insert_data_documentation():
            documents_list = []
            for iteration in range(int(len(self.list_documentation) / 3)):
                org = insert_data(self.list_documentation[iteration * 3 + 0], x_data_akt.get_all_organizations())
                doc_name = insert_data(self.list_documentation[iteration * 3 + 1], None)
                page = self.list_documentation[iteration * 3 + 2].get()
                if org.get_text() == '' and doc_name.get_text() == '' and page == '':
                    pass
                else:
                    if page == '' or page[0] == '"':
                        doc = data_akt.Doc(org, doc_name, page)
                        documents_list.append(doc)
                    else:
                        page = data_akt.page_modification(page)
                        if page is None:
                            self.__indicator += 'Некорректно введен список листов'
                            return
                        else:
                            doc = data_akt.Doc(org, doc_name, page)
                    documents_list.append(doc)
            documents_list = tuple(documents_list)
            return documents_list

        # получение элементов акта
        self.__name_object = insert_data(self.combobox_object, x_data_akt.get_all_names_object())
        self.__developer = insert_data(self.combobox_developer, x_data_akt.get_all_organizations())
        self.__builder = insert_data(self.combobox_builder, x_data_akt.get_all_organizations())
        self.__designer = insert_data(self.combobox_designer, x_data_akt.get_all_organizations())
        self.__developer_name = insert_data(self.combobox_developer_name, x_data_akt.get_all_representatives())
        self.__builder_name = insert_data(self.combobox_builder_name, x_data_akt.get_all_representatives())
        self.__builder_control_name = insert_data(self.combobox_builder_control_name, x_data_akt.get_all_representatives())
        self.__designer_name = insert_data(self.combobox_designer_name, x_data_akt.get_all_representatives())
        self.__contractor_name = insert_data(self.combobox_contractor_name, x_data_akt.get_all_representatives())
        self.__another_person = insert_data(self.combobox_another_person, x_data_akt.get_all_representatives())
        self.__contractor = insert_data(self.combobox_contractor, x_data_akt.get_all_organizations())
        self.__start_date = self.entry_start_date.get()
        self.__finish_date = self.entry_finish_date.get()
        self.__work = self.entry_work.get()
        if self.__work == '':
            self.__indicator += 'Наименование работ не может быть пустым\n'
        self.__documentation = insert_data_documentation()

        akt = data_akt.Akt()
        akt.set_name_object(self.__name_object)
        akt.set_developer(self.__developer)
        akt.set_builder(self.__builder)
        akt.set_designer(self.__designer)
        akt.set_developer_name(self.__developer_name)
        akt.set_builder_name(self.__builder_name)
        akt.set_builder_control_name(self.__builder_control_name)
        akt.set_designer_name(self.__designer_name)
        akt.set_contractor_name(self.__contractor_name)
        akt.set_another_person(self.__another_person)
        akt.set_contractor(self.__contractor)
        indicator_date = akt.add_deadlines(self.__start_date, self.__finish_date)
        if indicator_date is not None:
            self.__indicator += indicator_date
        akt.set_name_work(self.__work)
        akt.set_documentation(self.__documentation)

        if self.__indicator != '':
            self.label_indicator.config(text=self.__indicator)
            return

        if self.__action == 'новый' or self.__action == 'на основе другого':
            x_data_akt.set_akt(akt)
        elif self.__action == 'изменить':
            x_data_akt.change_akt(akt, self.__index)

        elements = tkinter.Variable(value=x_data_akt.get_all_akts_names())
        self.__listbox.config(listvariable=elements)
        self.window_creat_akt.destroy()

if __name__ == '__main__':
    window = RootGUI()