import Export_Akt_Word
import data_akt
import tkinter
from tkinter import ttk, Toplevel, filedialog, messagebox

x_data_akt = data_akt.Data_Akt()


class RootGUI:
    def __init__(self):
        # Создание и настройка основного окна
        self.root = tkinter.Tk()
        self.root.title('L.E.X.A.')
        # self.root.attributes('-fullscreen', True)
        # self.root.attributes("-alpha", 0.5)
        # self.root.attributes("-toolwindow", True)
        self.root.geometry('700x700')
        # self.root.geometry(f'{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}')

        self.root.bind('<Control-KeyPress>', key_rus)

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

        # Создание группы виджетов ПРОЕКТНО-СМЕТНАЯ ДОКУМЕНТАЦИЯ для вкладки ОБЪЕКТ
        self.frame_project_documentation = tkinter.LabelFrame(self.frame_object,
                                                              borderwidth=1,
                                                              relief='solid',
                                                              text='Проектно-сметная документация')
        self.frame_listbox_project_documentation = tkinter.Frame(self.frame_project_documentation)
        self.project_documentation = tkinter.Variable(value=x_data_akt.get_all_project_documentations_names())
        self.listbox_project_documentation = tkinter.Listbox(self.frame_listbox_project_documentation,
                                                             listvariable=self.project_documentation,
                                                             height=5,
                                                             width=93)
        self.listbox_project_documentation.pack(side='left')
        self.listbox_project_documentation_scrollbar = tkinter.Scrollbar(self.frame_listbox_project_documentation,
                                                                         command=self.listbox_project_documentation.yview)
        self.listbox_project_documentation_scrollbar.pack(side='right', fill='y')
        self.listbox_project_documentation.config(yscrollcommand=self.listbox_project_documentation_scrollbar.set)
        self.listbox_project_documentation.bind('<Button-3>', self.menu_project_documentation)
        self.frame_listbox_project_documentation.pack()
        self.frame_project_documentation.grid(row=4, column=0)

        # Создание группы виджетов ТЕХНИЧЕСКИЕ РЕГЛАМЕНТЫ для вкладки ОБЪЕКТ
        self.frame_regulation = tkinter.LabelFrame(self.frame_object,
                                                   borderwidth=1,
                                                   relief='solid',
                                                   text='Технические регламенты, нормативные документы')
        self.frame_listbox_regulation = tkinter.Frame(self.frame_regulation)
        self.regulations = tkinter.Variable(value=x_data_akt.get_all_regulations_names())
        self.listbox_regulation = tkinter.Listbox(self.frame_listbox_regulation,
                                                  listvariable=self.regulations,
                                                  height=5,
                                                  width=93)
        self.listbox_regulation.pack(side='left')
        self.listbox_regulation_scrollbar = tkinter.Scrollbar(self.frame_listbox_regulation,
                                                              command=self.listbox_regulation.yview)
        self.listbox_regulation_scrollbar.pack(side='right', fill='y')
        self.listbox_regulation.config(yscrollcommand=self.listbox_regulation_scrollbar.set)
        self.listbox_regulation.bind('<Button-3>', self.menu_regulation)
        self.frame_listbox_regulation.pack()
        self.frame_regulation.grid(row=5, column=0)

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
                                                  'эксплуатацию здания, сооружения,\nили региональный оператор:')
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
        self.tuple_widget_canvas = (
            self.label_object_name, self.text_object_name, self.label_developer, self.text_developer,
            self.label_builder, self.text_builder, self.label_designer, self.text_designer,
            self.label_doc1, self.frame_number_and_date, self.label_act_number, self.entry_act_number,
            self.entry_act_date, self.label_developer_name, self.text_developer_name,
            self.label_builder_name, self.text_builder_name, self.label_builder_control_name,
            self.text_builder_control_name, self.label_designer_name, self.text_designer_name,
            self.label_contractor_name, self.text_contractor_name, self.label_another_person,
            self.text_another_person, self.frame_contractor, self.label_contractor,
            self.text_contractor, self.label_doc2, self.label_work, self.text_work,
            self.label_documentation, self.text_documentation)

        self.canvas.create_window(0, 0, anchor='nw', window=self.frame_in_canvas)

        self.canvas_scrollbar = tkinter.Scrollbar(self.frame_for_canvas, orient=tkinter.VERTICAL,
                                                  command=self.canvas.yview)
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"), yscrollcommand=self.canvas_scrollbar.set)
        self.canvas.pack(side='left')
        # Прокрутка canvas просмотр акта
        self.canvas.bind_all('<MouseWheel>', self.scrolling_canvas)
        self.canvas_scrollbar.pack(side='right', fill='y')
        self.frame_for_canvas.pack()
        self.frame_view_akt.grid(row=0, column=1)

        # Создание вкладки МАТЕРИАЛЫ
        self.frame_material = tkinter.Frame(self.root)
        self.frame_material.pack()
        self.notebook.add(self.frame_material, text='Материалы')

        # Создание группы виджетов РАБОТА С МАТЕРИАЛАМИ
        self.frame_materials_of_akt = ttk.LabelFrame(self.frame_material, text='Материалы')
        self.frame_table_materials = tkinter.Frame(self.frame_materials_of_akt)
        self.table_material = ttk.Treeview(self.frame_table_materials,
                                           columns=('id', 'type', 'material', 'document', 'date', 'file'),
                                           show='headings',
                                           height=5)
        self.table_material_scrollbar = ttk.Scrollbar(self.frame_table_materials, orient='vertical',
                                                      command=self.table_material.yview)
        self.table_material.config(yscrollcommand=self.table_material_scrollbar.set)
        self.table_material.heading('id', text='id')
        self.table_material.heading('type', text='Вид')
        self.table_material.heading('material', text='Материал')
        self.table_material.heading('document', text='Документ')
        self.table_material.heading('date', text='Дата')
        self.table_material.heading('file', text='Изображения')
        self.table_material.column('#1', width=30)
        self.table_material.column('#2', width=100)
        self.table_material.column('#3', width=300)
        self.table_material.column('#4', width=300)
        self.table_material.column('#5', width=200)
        self.table_material.column('#6', width=100)
        self.table_material.bind('<Button-3>', self.menu_table_material)

        self.frame_materials_of_akt.pack()
        self.frame_table_materials.pack()
        self.table_material_scrollbar.pack(side='right', fill='y')
        self.table_material.pack(side='left')

        self.frame_base_data = ttk.LabelFrame(self.frame_material, text='База данных материалов')
        self.entry_base_data = tkinter.Entry(self.frame_base_data, width=161)
        self.entry_base_data.bind('<Button-3>', self.menu_base_data)
        self.button_base_data = tkinter.Button(self.frame_base_data, text='Подключить', command=self.connect_database)
        self.frame_base_data.pack()
        self.entry_base_data.pack(side='left')
        self.button_base_data.pack(side='right', fill='y')

        # Создание вкладки ДОКУМЕНТЫ
        self.frame_document = tkinter.Frame(self.root)
        self.frame_document.pack()
        self.notebook.add(self.frame_document, text='Документы')

        # Создание группы виджетов РАБОТА С ДОКУМЕНТАМИ СООТВЕТСВИЯ
        self.frame_documents_of_akt = ttk.LabelFrame(self.frame_document, text='Документы соответствия работ')
        self.frame_table_documents = tkinter.Frame(self.frame_documents_of_akt)
        self.table_document = ttk.Treeview(self.frame_table_documents,
                                           columns=('id', 'document', 'date', 'file'),
                                           show='headings',
                                           height=5)
        self.table_document_scrollbar = ttk.Scrollbar(self.frame_table_documents, orient='vertical',
                                                      command=self.table_document.yview)
        self.table_document.config(yscrollcommand=self.table_document_scrollbar.set)
        self.table_document.heading('id', text='id')
        self.table_document.heading('document', text='Документ')
        self.table_document.heading('date', text='Дата')
        self.table_document.heading('file', text='Изображения')
        self.table_document.column('#1', width=30)
        self.table_document.column('#2', width=100)
        self.table_document.column('#3', width=300)
        self.table_document.column('#4', width=300)
        self.table_document.bind('<Button-3>', self.menu_table_document)

        self.frame_documents_of_akt.pack()
        self.frame_table_documents.pack()
        self.table_document_scrollbar.pack(side='right', fill='y')
        self.table_document.pack(side='left')

        self.root.mainloop()

    # Функция ОТКРЫТЬ из МЕНЮ
    def new_file(self):
        global x_data_akt
        x_data_akt = data_akt.Data_Akt()
        self.updater_list(self.listbox_names, x_data_akt.get_all_name_object_names())
        self.updater_list(self.listbox_organization, x_data_akt.get_all_organizations_names())
        self.updater_list(self.listbox_regulation, x_data_akt.get_all_representatives_names())
        self.updater_list(self.listbox_akts, x_data_akt.get_all_akts_names_text())
        self.updater_table_materials()

    def load_file(self):
        global x_data_akt
        self.file = tkinter.filedialog.askopenfilename(defaultextension='lexa')
        x_data_akt = data_akt.load(self.file)
        self.updater_list(self.listbox_names, x_data_akt.get_all_name_object_names())
        self.updater_list(self.listbox_organization, x_data_akt.get_all_organizations_names())
        self.updater_list(self.listbox_regulation, x_data_akt.get_all_representatives_names())
        self.updater_list(self.listbox_akts, x_data_akt.get_all_akts_names_text())
        self.updater_table_materials()

    def save_file(self):
        self.file = tkinter.filedialog.asksaveasfilename(confirmoverwrite=True, defaultextension='lexa')
        data_akt.save(self.file, x_data_akt)

    def updater_list(self, list_object, var):
        elements = tkinter.Variable(value=var)
        list_object.config(listvariable=elements)

    def updater_table_materials(self):
        for item in self.table_material.get_children():
            self.table_material.delete(item)
        for material in x_data_akt.get_all_text_materials_table():
            self.table_material.insert('', 'end', values=material)

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

    # Контекстное меню для ТЕХНИЧЕСКИХ РЕГЛАМЕНТОВ вкладке ОБЪЕКТ
    def menu_regulation(self, event):
        menu = tkinter.Menu(tearoff=0)
        menu.add_command(label='Добавить', command=self.add_regulation)
        menu.add_command(label='Изменить', command=self.change_regulation)
        menu.add_command(label='Удалить', command=self.delete_regulation)
        menu.post(event.x_root, event.y_root)

    def add_regulation(self):
        window = Window_object_element(self.root, self.listbox_regulation, 'регламенты')

    def change_regulation(self):
        index = self.listbox_regulation.curselection()[0]
        window = Window_object_element(self.root, self.listbox_regulation, 'регламенты', index)

    def delete_regulation(self):
        index = self.listbox_regulation.curselection()
        x_data_akt.delete_regulation(index[0])
        self.listbox_regulation.delete(index[0])

    # Контекстное меню для ПРОЕКТНО-СМЕТНОЙ ДОКУМЕНТАЦИИ
    def menu_project_documentation(self, event):
        menu = tkinter.Menu(tearoff=0)
        menu.add_command(label='Добавить', command=self.add_project_documentation)
        menu.add_command(label='Изменить', command=self.change_project_documentation)
        menu.add_command(label='Удалить', command=self.delete_project_documentation)
        menu.post(event.x_root, event.y_root)

    def add_project_documentation(self):
        window = Window_object_element(self.root, self.listbox_project_documentation,
                                       'проектно-сметная документация')

    def change_project_documentation(self):
        index = self.listbox_project_documentation.curselection()[0]
        window = Window_object_element(self.root, self.listbox_project_documentation,
                                       'проектно-сметная документация', index)

    def delete_project_documentation(self):
        index = self.listbox_project_documentation.curselection()
        x_data_akt.delete_project_documentation(index[0])
        self.listbox_project_documentation.delete(index[0])

    # Контекстное меню для СПИСКА АКТОВ вкладке АКТЫ
    def menu_listbox_akts(self, event):
        menu = tkinter.Menu(tearoff=0)
        menu.add_command(label='Создать новый акт', command=self.add_akt)
        menu.add_command(label='Создать акт на основе выбранного', command=self.add_akt_based_on)
        menu.add_command(label='Изменить', command=self.change_akt)
        cascade_export = tkinter.Menu(tearoff=0)
        cascade_export.add_command(label='в Word', command=self.export_to_Word)
        menu.add_cascade(label='Импорт', menu=cascade_export)
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

    def export_to_Word(self):
        index = self.listbox_akts.curselection()[0]
        window = Window_export_to_word(self.root, index)

    def delete_akt(self):
        index = self.listbox_akts.curselection()
        x_data_akt.delete_akt(index[0])
        self.listbox_akts.delete(index[0])

    # Скролинг ГРУППЫ виджетов canvas
    def scrolling_canvas(self, event):
        if self.root.focus_get() in self.tuple_widget_canvas:
            self.canvas.yview_scroll(int(-1 * event.delta / 120), 'units')

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

        self.text_work.insert('end', x_data_akt.get_akt(index[0]).get_name_work().get_text())
        self.text_documentation.insert('end', x_data_akt.get_akt(index[0]).get_text_of_documentation())

    # Функции меню для таблицы материалов
    def menu_table_material(self, event):
        menu = tkinter.Menu(tearoff=0)
        menu.add_command(label='Cоздать новый', command=self.create_material)
        menu.add_command(label='Добавить материал из БД', command=self.add_from_database)
        menu.add_command(label='Установить порядок материалов', command=self.order_material)
        if self.table_material.selection() != ():
            menu.add_command(label='Изменить', command=self.change_material)
            menu.add_command(label='Удалить', command=self.delete_material)
            menu.add_separator()
            menu.add_command(label='Просмотр документа', command=self.view_file_material)
            menu.add_command(label='Удаление документа', command=self.del_file_material)
        menu.post(event.x_root, event.y_root)

    def view_file_material(self):
        line = self.table_material.selection()[0]
        id = self.table_material.item(line)['values'][0]
        index_material = x_data_akt.get_all_id_materials().index(id)
        images = x_data_akt.get_material(index_material).get_bin_images()
        if images is not None:
            window = Window_veiw_doc(self.root, images)
        else:
            return None

    def del_file_material(self):
        for line in self.table_material.selection():
            id = self.table_material.item(line)['values'][0]
            index_material = x_data_akt.get_all_id_materials().index(id)
            x_data_akt.get_material(index_material).del_bin_images()
            self.table_material.set(line, 5, '<Файл не загружен>')

    def create_material(self):
        window = Window_material(self.root, self.table_material)

    def add_from_database(self):
        print(self.table_material.selection())

    def order_material(self):
        window = Window_order_material(self.root, x_data_akt.get_all_text_materials_list(), 'material')

    def change_material(self):
        line = self.table_material.selection()[0]
        id = self.table_material.item(line)['values'][0]
        index_material = x_data_akt.get_all_id_materials().index(id)
        window = Window_material(self.root, self.table_material, index_material, line)

    def delete_material(self):
        for line in self.table_material.selection():
            id = self.table_material.item(line)['values'][0]
            x_data_akt.delete_material(x_data_akt.get_all_id_materials().index(id))
            self.table_material.delete(line)

    # Функции для БД материалов
    def connect_database(self):
        object_base_materials = data_akt.connection_base_data(self.entry_base_data.get())
        Window = Window_data_base(self.root, object_base_materials, self.table_material)

    def menu_base_data(self, event):
        menu = tkinter.Menu(tearoff=0)
        menu.add_command(label='Cоздать новую БД', command=self.create_base_data)
        menu.add_command(label='Загрузить БД', command=self.load_base_data)
        menu.post(self.entry_base_data.winfo_rootx(), self.entry_base_data.winfo_rooty() + 20)
        # menu.post(event.x_root, event.y_root)

    def create_base_data(self):
        self.entry_base_data.delete(0, 'end')
        self.file_db = tkinter.filedialog.asksaveasfilename(confirmoverwrite=True, defaultextension='db',
                                                            initialfile='new_date_base_material.db')
        self.entry_base_data.insert('end', self.file_db)

    def load_base_data(self):
        self.entry_base_data.delete(0, 'end')
        self.file_db = tkinter.filedialog.askopenfilename(defaultextension='db')
        self.entry_base_data.insert('end', self.file_db)

    # функции меню для таблицы документов
    def menu_table_document(self, event):
        menu = tkinter.Menu(tearoff=0)
        menu.add_command(label='Cоздать новый', command=self.create_document)
        menu.add_command(label='Установить порядок материалов', command=self.order_document)
        if self.table_document.selection() != ():
            menu.add_command(label='Изменить', command=self.change_document)
            menu.add_command(label='Удалить', command=self.delete_document)
            menu.add_separator()
            menu.add_command(label='Просмотр документа', command=self.view_file_document)
            menu.add_command(label='Удаление документа', command=self.del_file_document)
        menu.post(event.x_root, event.y_root)

    def create_document(self):
        window = Window_document(self.root, self.table_document)

    def order_document(self):
        window = Window_order_material(self.root, x_data_akt.get_all_text_documents_list(), 'document')

    def change_document(self):
        line = self.table_document.selection()[0]
        id = self.table_document.item(line)['values'][0]
        index_documents = x_data_akt.get_all_id_documents().index(id)
        window = Window_document(self.root, self.table_document, index_documents, line)

    def delete_document(self):
        for line in self.table_document.selection():
            id = self.table_document.item(line)['values'][0]
            x_data_akt.delete_document(x_data_akt.get_all_id_documents().index(id))
            self.table_document.delete(line)

    def view_file_document(self):
        line = self.table_document.selection()[0]
        id = self.table_document.item(line)['values'][0]
        index_document = x_data_akt.get_all_id_documents().index(id)
        images = x_data_akt.get_document(index_document).get_bin_images()
        if images is not None:
            window = Window_veiw_doc(self.root, images)
        else:
            return None

    def del_file_document(self):
        for line in self.table_document.selection():
            id = self.table_document.item(line)['values'][0]
            index_document = x_data_akt.get_all_id_documents().index(id)
            x_data_akt.get_document(index_document).del_bin_images()
            self.table_document.set(line, 3, '<Файл не загружен>')


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

        self.window.bind('<Control-KeyPress>', key_rus)

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
        elif self.__type_element == 'проектно-сметная документация':
            print(self.__index)
            return x_data_akt.get_project_documentation_name(self.__index), x_data_akt.get_project_documentation_text(
                self.__index)
        elif self.__type_element == 'регламенты':
            return x_data_akt.get_regulation_name(self.__index), x_data_akt.get_regulation_text(self.__index)

    def get_names(self):
        if self.__type_element == 'имена':
            return x_data_akt.get_all_name_object_names()
        elif self.__type_element == 'организации':
            return x_data_akt.get_all_organizations_names()
        elif self.__type_element == 'представители':
            return x_data_akt.get_all_representatives_names()
        elif self.__type_element == 'проектно-сметная документация':
            return x_data_akt.get_all_project_documentations_names()
        elif self.__type_element == 'регламенты':
            return x_data_akt.get_all_regulations_names()

    def set_element_data_akt(self, text, name):
        if self.__type_element == 'имена':
            x_data_akt.set_name_object(text, name)
        elif self.__type_element == 'организации':
            x_data_akt.set_organization(text, name)
        elif self.__type_element == 'представители':
            x_data_akt.set_representative(text, name)
        elif self.__type_element == 'проектно-сметная документация':
            x_data_akt.set_project_documentation(text, name)
        elif self.__type_element == 'регламенты':
            x_data_akt.set_regulation(text, name)

    def change_element_data_akt(self, text, name):
        if self.__type_element == 'имена':
            x_data_akt.change_name_object(text, name, self.__index)
        elif self.__type_element == 'организации':
            x_data_akt.change_organization(text, name, self.__index)
        elif self.__type_element == 'представители':
            x_data_akt.change_representative(text, name, self.__index)
        elif self.__type_element == 'проектно-сметная документация':
            x_data_akt.change_project_documentation(text, name, self.__index)
        elif self.__type_element == 'регламенты':
            x_data_akt.change_regulation(text, name, self.__index)


class Window_akt:
    def __init__(self, root, listbox, action, index=None):
        self.__root = root
        self.__listbox = listbox
        self.__indicator = ''
        self.__list_text_all_materials = x_data_akt.get_all_text_materials_list()
        self.__static_all_materials = x_data_akt.get_all_text_materials_list()
        self.__list_text_all_documents = x_data_akt.get_all_text_documents_list()
        self.__static_all_documents = x_data_akt.get_all_text_documents_list()
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
            self.__list_text_materials_akt = tuple()
            self.__list_text_documents_akt = tuple()
            self.__list_regulations_akt = tuple()
            self.__previous_work = tuple()
            self.__next_work = tuple()
            self.__additional_information = None
            self.__number_of_copies = None
            self.__classifications = None
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
            self.__work = self.old_elements(x_data_akt.get_akt(index).get_name_work())
            self.__documentation = x_data_akt.get_akt(index).get_documentation()
            self.__list_text_materials_akt = x_data_akt.get_akt(index).get_text_all_materials_of_akt()
            self.__list_text_documents_akt = x_data_akt.get_akt(index).get_text_all_documents_of_akt()
            self.__list_regulations_akt = x_data_akt.get_akt(index).get_regulations()
            self.__previous_work = x_data_akt.get_names_previous_works(index)
            self.__next_work = x_data_akt.get_akt(index).get_next_work()
            self.__additional_information = x_data_akt.get_akt(index).get_additional_information()
            self.__number_of_copies = x_data_akt.get_akt(index).get_number_of_copies()
            self.__classifications = x_data_akt.get_akt(index).get_dict_classifications()

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

        self.window_create_akt = Toplevel(self.__root)
        self.window_create_akt.title(self.__heading)
        self.window_create_akt.geometry('700x900')
        self.window_create_akt.grab_set()
        self.frame_window_akt = tkinter.Frame(self.window_create_akt)
        self.window_create_akt.bind('<Control-KeyPress>', key_rus)

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

        # группа виджетов ПРОЕКТНО-СМЕТНОЙ ДОКУМЕНТАЦИИ
        self.frame_documentation = tkinter.LabelFrame(self.frame_window_akt, text='Проектно-сметная документация')
        self.label_org = tkinter.Label(self.frame_documentation, text='Организация')
        self.label_doc = tkinter.Label(self.frame_documentation, text='Наименование документация')
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
                                                    width=30,
                                                    values=x_data_akt.get_all_project_documentations_names()))
        self.list_documentation.append(tkinter.Entry(self.frame_documentation, width=30))
        self.list_documentation[0].grid(row=1, column=1, stick='we')
        self.list_documentation[1].grid(row=1, column=2, stick='we')
        self.list_documentation[2].grid(row=1, column=3, stick='we')

        # группа виджетов МАТЕРИАЛЫ
        self.frame_material = tkinter.LabelFrame(self.frame_window_akt, text='Материалы/Оснастка')
        self.frame_listbox_materials_akt = tkinter.Frame(self.frame_material)
        self.label_materials_akt = tkinter.Label(self.frame_material, text='Используемые материалы')
        self.listbox_materials_akt = tkinter.Listbox(self.frame_listbox_materials_akt, width=75, height=10,
                                                     selectmode='extended')
        self.listbox_materials_akt_scrollbar = tkinter.Scrollbar(self.frame_listbox_materials_akt,
                                                                 command=self.listbox_materials_akt.yview)
        self.listbox_materials_akt.config(yscrollcommand=self.listbox_materials_akt_scrollbar.set)
        self.listbox_materials_akt_scrollbar.pack(side='left', fill='y')
        self.listbox_materials_akt.pack(side='right')
        self.label_symbol_document = tkinter.Label(self.frame_material, text='<-')
        self.label_all_materials = tkinter.Label(self.frame_material, text='Все материалы')
        self.frame_listbox_all_materials = tkinter.Frame(self.frame_material)
        self.listbox_all_materials = tkinter.Listbox(self.frame_listbox_all_materials, width=75, height=10,
                                                     selectmode='extended',
                                                     listvariable=tkinter.Variable(
                                                         value=x_data_akt.get_all_text_materials_list()))
        self.listbox_all_materials_scrollbar = tkinter.Scrollbar(self.frame_listbox_all_materials,
                                                                 command=self.listbox_all_materials.yview)
        self.listbox_all_materials.config(yscrollcommand=self.listbox_all_materials_scrollbar.set)
        self.listbox_all_materials.pack(side='left')
        self.listbox_all_materials_scrollbar.pack(side='right', fill='y')

        self.listbox_all_materials.bind('<Double-ButtonPress-1>', self.transfer_to_listbox_materials_akt)
        self.listbox_materials_akt.bind('<Double-ButtonPress-1>', self.cancellation_transfer_materials)
        self.listbox_all_materials.bind('<ButtonPress-3>', self.menu_listbox_all_materials)
        self.listbox_materials_akt.bind('<ButtonPress-3>', self.menu_listbox_materials_akt)

        self.label_materials_akt.grid(row=0, column=0)
        self.frame_listbox_materials_akt.grid(row=1, column=0)
        self.label_symbol_document.grid(row=0, column=1, rowspan=2, padx=5)
        self.label_all_materials.grid(row=0, column=2)
        self.frame_listbox_all_materials.grid(row=1, column=2)

        # группа виджетов ДОКУМЕНТЫ СООТВЕТСТВИЯ
        self.frame_document = tkinter.LabelFrame(self.frame_window_akt, text='Документы соответствия работ')
        self.frame_listbox_documents_akt = tkinter.Frame(self.frame_document)
        self.label_documents_akt = tkinter.Label(self.frame_document, text='Документы соответствия работ акта')
        self.listbox_documents_akt = tkinter.Listbox(self.frame_listbox_documents_akt, width=75, height=10,
                                                     selectmode='extended')
        self.listbox_documents_akt_scrollbar = tkinter.Scrollbar(self.frame_listbox_documents_akt,
                                                                 command=self.listbox_documents_akt.yview)
        self.listbox_documents_akt.config(yscrollcommand=self.listbox_documents_akt_scrollbar.set)
        self.listbox_documents_akt_scrollbar.pack(side='left', fill='y')
        self.listbox_documents_akt.pack(side='right')
        self.label_symbol_document = tkinter.Label(self.frame_document, text='<-')
        self.label_all_documents = tkinter.Label(self.frame_document, text='Все документы соответствия работ')
        self.frame_listbox_all_documents = tkinter.Frame(self.frame_document)
        self.listbox_all_documents = tkinter.Listbox(self.frame_listbox_all_documents, width=75, height=10,
                                                     selectmode='extended',
                                                     listvariable=tkinter.Variable(
                                                         value=x_data_akt.get_all_text_documents_list()))
        self.listbox_all_documents_scrollbar = tkinter.Scrollbar(self.frame_listbox_all_documents,
                                                                 command=self.listbox_all_documents.yview)
        self.listbox_all_documents.config(yscrollcommand=self.listbox_all_documents_scrollbar.set)
        self.listbox_all_documents.pack(side='left')
        self.listbox_all_documents_scrollbar.pack(side='right', fill='y')

        self.listbox_all_documents.bind('<Double-ButtonPress-1>', self.transfer_to_listbox_documents_akt)
        self.listbox_documents_akt.bind('<Double-ButtonPress-1>', self.cancellation_transfer_documents)
        self.listbox_all_documents.bind('<ButtonPress-3>', self.menu_listbox_all_documents)
        self.listbox_documents_akt.bind('<ButtonPress-3>', self.menu_listbox_documents_akt)

        self.label_documents_akt.grid(row=0, column=0)
        self.frame_listbox_documents_akt.grid(row=1, column=0)
        self.label_symbol_document.grid(row=0, column=1, rowspan=2, padx=5)
        self.label_all_documents.grid(row=0, column=2)
        self.frame_listbox_all_documents.grid(row=1, column=2)

        # Группа виджетов ТЕХНИЧЕСКИЕ РЕГЛАМЕНТЫ
        self.frame_regulations = tkinter.LabelFrame(self.frame_window_akt,
                                                    text='Технические регламенты, нормативные документы')
        self.button_add_regulations = tkinter.Button(self.frame_regulations, text='>>',
                                                     command=self.add_widget_from_regulation)
        self.button_add_regulations.grid(row=0, column=0, rowspan=1, stick='ns')
        self.list_widget_regulations = []
        self.list_widget_regulations.append(ttk.Combobox(self.frame_regulations,
                                                         width=50,
                                                         values=x_data_akt.get_all_regulations_names()))
        self.list_widget_regulations[-1].grid(row=0, column=1, stick='we')

        # Группа виджетов ПОСЛЕДОВАТЕЛЬНОСТЬ РАБОТ
        self.frame_order_work = tkinter.LabelFrame(self.frame_window_akt,
                                                   text='Последовательность производства работ')
        self.label_previous_work = tkinter.Label(self.frame_order_work, text='Предыдущая работа')
        self.label_next_work = tkinter.Label(self.frame_order_work, text='Последующая работа')
        self.button_add_order_work = tkinter.Button(self.frame_order_work, text='>>',
                                                    command=self.add_widget_from_order_work)
        self.label_previous_work.grid(row=0, column=1, rowspan=1, stick='ns')
        self.label_next_work.grid(row=0, column=2, rowspan=1, stick='ns')
        self.button_add_order_work.grid(row=1, column=0, rowspan=1, stick='ns')

        self.list_widget_order_work = []
        self.list_widget_order_work.append(ttk.Combobox(self.frame_order_work,
                                                        width=50,
                                                        state="readonly",
                                                        values=x_data_akt.get_all_akts_names_text()))
        self.list_widget_order_work.append(ttk.Combobox(self.frame_order_work,
                                                        width=50,
                                                        values=x_data_akt.get_all_akts_names_text()))
        self.list_widget_order_work[-2].grid(row=1, column=1, rowspan=1, stick='ns')
        self.list_widget_order_work[-1].grid(row=1, column=2, rowspan=1, stick='ns')

        # Группа виджетов ДОПОЛНИТЕЛЬНЫЕ СВЕДЕНИЯ
        self.frame_additional_information = tkinter.LabelFrame(self.frame_window_akt,
                                                               text='Дополнительные сведения')
        self.text_additional_information = tkinter.Text(self.frame_additional_information,
                                                        wrap='word', height=5, width=120)
        self.text_additional_information.pack()

        # Группа виджетов КОЛИЧЕСТВО ЭКЗЕМПЛЯРОВ
        self.frame_number_of_copies = tkinter.LabelFrame(self.frame_window_akt, text='Количество экземпляров')
        self.label_number_of_copies1 = tkinter.Label(self.frame_number_of_copies, text='Акт составлен в ')
        self.snipbox_number_of_copies = ttk.Spinbox(self.frame_number_of_copies, width=5, from_=0.0, to=999.0)
        self.snipbox_number_of_copies.set(3)
        self.label_number_of_copies2 = tkinter.Label(self.frame_number_of_copies, text=' экземплярах')
        self.label_number_of_copies1.grid(row=0, column=0)
        self.snipbox_number_of_copies.grid(row=0, column=1)
        self.label_number_of_copies2.grid(row=0, column=2)

        # Группа виджетов КЛАССИФИКАЦИЯ АКТОВ
        self.frame_classifications = tkinter.LabelFrame(self.frame_window_akt, text='Классификация')
        self.label_name_classification = tkinter.Label(self.frame_classifications, text='Наименование классификации')
        self.label_classification = tkinter.Label(self.frame_classifications, text='Класс')
        self.button_add_classification = tkinter.Button(self.frame_classifications, text='>>',
                                                        command=self.add_widget_from_classification)
        self.label_name_classification.grid(row=0, column=1, rowspan=1, stick='ns')
        self.label_classification.grid(row=0, column=2, rowspan=1, stick='ns')
        self.button_add_classification.grid(row=1, column=0, rowspan=1, stick='ns')

        self.list_widget_classifications = []
        self.list_widget_classifications.append(ttk.Combobox(self.frame_classifications,
                                                             width=50,
                                                             values=x_data_akt.get_all_names_classifications()))
        combobox_name_classification = self.list_widget_classifications[-1]
        combobox_name_classification.bind('<<ComboboxSelected>>',
                                          lambda x: self.set_variant_in_combobox_classification(
                                              combobox_name_classification))
        self.list_widget_classifications.append(ttk.Combobox(self.frame_classifications, width=50))
        self.list_widget_classifications[-2].grid(row=1, column=1, rowspan=1, stick='we')
        self.list_widget_classifications[-1].grid(row=1, column=2, rowspan=1, stick='we')

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
            self.old_doc()
            self.old_materials()
            self.old_documents()
            self.old_regulations()
            self.old_next_and_previous_work()
            self.text_additional_information.insert('end', self.__additional_information)
            self.snipbox_number_of_copies.set(self.__number_of_copies)
            self.old_classifications()

        self.frame_object.grid(row=0, column=0, stick='we')
        self.frame_work.grid(row=1, column=0, stick='we')
        self.frame_date.grid(row=2, column=0, stick='we')
        self.frame_documentation.grid(row=3, column=0, stick='we')
        self.frame_material.grid(row=4, column=0, stick='we')
        self.frame_document.grid(row=5, column=0, stick='we')
        self.frame_regulations.grid(row=6, column=0, stick='we')
        self.frame_order_work.grid(row=7, column=0, stick='we')
        self.frame_additional_information.grid(row=8, column=0, stick='we')
        self.frame_number_of_copies.grid(row=9, column=0)
        self.frame_classifications.grid(row=10, column=0, stick='we')

        self.button_akt = tkinter.Button(self.window_create_akt, text=self.__text_button, command=self.akt)
        self.label_indicator = tkinter.Label(self.window_create_akt, foreground='red')

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
                                                        width=30,
                                                        values=x_data_akt.get_all_project_documentations_names()))
            self.list_documentation.append(tkinter.Entry(self.frame_documentation, width=30))
            self.list_documentation[-3].grid(row=int(len(self.list_documentation) / 3), column=1, stick='we')
            self.list_documentation[-2].grid(row=int(len(self.list_documentation) / 3), column=2, stick='we')
            self.list_documentation[-1].grid(row=int(len(self.list_documentation) / 3), column=3, stick='we')
            self.button_add_org.grid(row=1, column=0, rowspan=int(len(self.list_documentation) / 3) + 1, stick='ns')

    def add_widget_from_regulation(self):
        if self.list_widget_regulations[-1].get() != '':
            self.list_widget_regulations.append(ttk.Combobox(self.frame_regulations,
                                                             width=50,
                                                             values=x_data_akt.get_all_regulations_names()))
            self.list_widget_regulations[-1].grid(row=len(self.list_widget_regulations), column=1, stick='we')
            self.button_add_regulations.grid(row=0, column=0, rowspan=int(len(self.list_widget_regulations) / 2 + 1),
                                             stick='ns')

    def add_widget_from_order_work(self):
        if self.list_widget_order_work[-1].get() != '' or self.list_widget_order_work[-2].get() != '':
            self.list_widget_order_work.append(ttk.Combobox(self.frame_order_work,
                                                            width=50,
                                                            state="readonly",
                                                            values=x_data_akt.get_all_akts_names_text()))
            self.list_widget_order_work.append(ttk.Combobox(self.frame_order_work,
                                                            width=50,
                                                            values=x_data_akt.get_all_akts_names_text()))
            self.list_widget_order_work[-2].grid(row=int(len(self.list_widget_order_work) / 2),
                                                 column=1, stick='we')
            self.list_widget_order_work[-1].grid(row=int(len(self.list_widget_order_work) / 2),
                                                 column=2, stick='we')
            self.button_add_order_work.grid(row=1, column=0, rowspan=int(len(self.list_widget_order_work) / 2 + 1),
                                            stick='ns')

    def add_widget_from_classification(self):
        if self.list_widget_classifications[-1].get() != '' and self.list_widget_classifications[-2].get() != '':
            self.list_widget_classifications.append(ttk.Combobox(self.frame_classifications, width=50,
                                                                 values=self.set_list_selected_names_classifications()))
            combobox_name_classification = self.list_widget_classifications[-1]
            combobox_name_classification.bind('<<ComboboxSelected>>',
                                              lambda x: self.set_variant_in_combobox_classification(
                                                  combobox_name_classification))
            self.list_widget_classifications.append(ttk.Combobox(self.frame_classifications, width=50))
            self.list_widget_classifications[-2].grid(row=int(len(self.list_widget_classifications) / 2),
                                                      column=1, stick='we')
            self.list_widget_classifications[-1].grid(row=int(len(self.list_widget_classifications) / 2),
                                                      column=2, stick='we')
            self.button_add_classification.grid(row=1, column=0,
                                                rowspan=int(len(self.list_widget_classifications) / 2 + 1),
                                                stick='ns')

    def old_doc(self):
        for component in self.__documentation:
            self.list_documentation[-3].set(self.old_elements(component.get_organization()))
            self.list_documentation[-2].set(component.get_name_doc().get_text())
            self.list_documentation[-1].insert('end', component.get_page())
            self.add_widget_from_doc()

    def old_materials(self):
        self.listbox_materials_akt.config(listvariable=tkinter.Variable(value=self.__list_text_materials_akt))
        self.__list_text_all_materials = list(self.__list_text_all_materials)
        for material_of_akt in self.__list_text_materials_akt:
            self.__list_text_all_materials.remove(material_of_akt)
        self.__list_text_all_materials = tuple(self.__list_text_all_materials)
        self.listbox_all_materials.config(listvariable=tkinter.Variable(value=self.__list_text_all_materials))

    def old_documents(self):
        self.listbox_documents_akt.config(listvariable=tkinter.Variable(value=self.__list_text_documents_akt))
        self.__list_text_all_documents = list(self.__list_text_all_documents)
        for document_of_akt in self.__list_text_documents_akt:
            self.__list_text_all_documents.remove(document_of_akt)
        self.__list_text_all_documents = tuple(self.__list_text_all_documents)
        self.listbox_all_documents.config(listvariable=tkinter.Variable(value=self.__list_text_all_documents))

    def old_regulations(self):
        for regulation in self.__list_regulations_akt:
            self.list_widget_regulations[-1].set(self.old_elements(regulation))
            self.add_widget_from_regulation()

    def old_next_and_previous_work(self):
        if len(self.__next_work) >= len(self.__previous_work):
            number_cycles = len(self.__next_work)
        else:
            number_cycles = len(self.__previous_work)
        for cycle_number in range(number_cycles):
            if cycle_number < len(self.__next_work):
                self.list_widget_order_work[-1].set(self.__next_work[cycle_number].get_text())
            if cycle_number < len(self.__previous_work):
                self.list_widget_order_work[-2].set(self.__previous_work[cycle_number].get_text())
            self.add_widget_from_order_work()

    def old_classifications(self):
        keys_classifications = x_data_akt.get_keys_classifications_akt(self.__index)
        for name_classification in keys_classifications:
            self.list_widget_classifications[-2].set(name_classification)
            self.list_widget_classifications[-1].set(self.__classifications[name_classification])
            self.list_widget_classifications[-1].config(
                values=x_data_akt.get_all_classifications_by_key(name_classification))
            self.add_widget_from_classification()
        self.setting_variant_in_combobox_name_classification()

    def transfer_to_listbox_materials_akt(self, event=None):
        self.__list_text_all_materials = list(self.__list_text_all_materials)
        separator_list = []
        for index_row in self.listbox_all_materials.curselection():
            row = self.listbox_all_materials.get(index_row)
            separator_list.append(row)
            self.__list_text_all_materials.remove(row)

        self.listbox_all_materials.config(listvariable=tkinter.Variable(value=self.__list_text_all_materials))
        self.__list_text_materials_akt = list(self.__list_text_materials_akt) + separator_list
        self.__list_text_materials_akt.sort(key=lambda x: self.__static_all_materials.index(x))
        self.listbox_materials_akt.config(listvariable=tkinter.Variable(value=self.__list_text_materials_akt))
        self.__list_text_all_materials = tuple(self.__list_text_all_materials)
        self.__list_text_materials_akt = tuple(self.__list_text_materials_akt)

    def cancellation_transfer_materials(self, event=None):
        self.__list_text_materials_akt = list(self.__list_text_materials_akt)
        self.__list_text_all_materials = list(self.__list_text_all_materials)

        separator_list = []
        for index_row in self.listbox_materials_akt.curselection():
            row = self.listbox_materials_akt.get(index_row)
            separator_list.append(row)
            self.__list_text_materials_akt.remove(row)

        self.__list_text_all_materials += separator_list

        self.__list_text_all_materials.sort(key=lambda x: x_data_akt.get_all_text_materials_list().index(x))
        self.listbox_all_materials.config(listvariable=tkinter.Variable(value=self.__list_text_all_materials))
        self.listbox_materials_akt.config(listvariable=tkinter.Variable(value=self.__list_text_materials_akt))
        self.__list_text_materials_akt = tuple(self.__list_text_materials_akt)
        self.__list_text_all_materials = tuple(self.__list_text_all_materials)

    def menu_listbox_all_materials(self, event):
        menu = tkinter.Menu(tearoff=0)
        menu.add_command(label='Добавить', command=self.transfer_to_listbox_materials_akt)
        menu.post(self.window_create_akt.winfo_pointerx(), self.window_create_akt.winfo_pointery())

    def menu_listbox_materials_akt(self, event):
        menu = tkinter.Menu(tearoff=0)
        menu.add_command(label='Убрать', command=self.cancellation_transfer_materials)
        menu.post(self.window_create_akt.winfo_pointerx(), self.window_create_akt.winfo_pointery())

    def transfer_to_listbox_documents_akt(self, event=None):
        self.__list_text_all_documents = list(self.__list_text_all_documents)
        separator_list = []
        for index_row in self.listbox_all_documents.curselection():
            row = self.listbox_all_documents.get(index_row)
            separator_list.append(row)
            self.__list_text_all_documents.remove(row)

        self.listbox_all_documents.config(listvariable=tkinter.Variable(value=self.__list_text_all_documents))
        self.__list_text_documents_akt = list(self.__list_text_documents_akt) + separator_list
        self.__list_text_documents_akt.sort(key=lambda x: self.__static_all_documents.index(x))
        self.listbox_documents_akt.config(listvariable=tkinter.Variable(value=self.__list_text_documents_akt))
        self.__list_text_all_documents = tuple(self.__list_text_all_documents)
        self.__list_text_documents_akt = tuple(self.__list_text_documents_akt)

    def cancellation_transfer_documents(self, event=None):
        self.__list_text_documents_akt = list(self.__list_text_documents_akt)
        self.__list_text_all_documents = list(self.__list_text_all_documents)

        separator_list = []
        for index_row in self.listbox_documents_akt.curselection():
            row = self.listbox_documents_akt.get(index_row)
            separator_list.append(row)
            self.__list_text_documents_akt.remove(row)

        self.__list_text_all_documents += separator_list

        self.__list_text_all_documents.sort(key=lambda x: x_data_akt.get_all_text_documents_list().index(x))
        self.listbox_all_documents.config(listvariable=tkinter.Variable(value=self.__list_text_all_documents))
        self.listbox_documents_akt.config(listvariable=tkinter.Variable(value=self.__list_text_documents_akt))
        self.__list_text_documents_akt = tuple(self.__list_text_documents_akt)
        self.__list_text_all_documents = tuple(self.__list_text_all_documents)

    def menu_listbox_all_documents(self, event):
        menu = tkinter.Menu(tearoff=0)
        menu.add_command(label='Добавить', command=self.transfer_to_listbox_documents_akt)
        menu.post(self.window_create_akt.winfo_pointerx(), self.window_create_akt.winfo_pointery())

    def menu_listbox_documents_akt(self, event):
        menu = tkinter.Menu(tearoff=0)
        menu.add_command(label='Убрать', command=self.cancellation_transfer_documents)
        menu.post(self.window_create_akt.winfo_pointerx(), self.window_create_akt.winfo_pointery())

    def set_variant_in_combobox_classification(self, combobox_classification):
        index_widget = self.list_widget_classifications.index(combobox_classification) + 1
        key = combobox_classification.get()
        self.list_widget_classifications[index_widget].config(values=x_data_akt.get_all_classifications_by_key(key))
        self.setting_variant_in_combobox_name_classification()

    def set_list_selected_names_classifications(self):
        list_selected_names_classifications = []
        new_list_names_classifications = []
        for iteration_widget in range(int(len(self.list_widget_classifications) / 2)):
            list_selected_names_classifications.append(self.list_widget_classifications[iteration_widget * 2].get())
        list_selected_names_classifications = tuple(list_selected_names_classifications)
        for name_classification in x_data_akt.get_all_names_classifications():
            if name_classification not in list_selected_names_classifications:
                new_list_names_classifications.append(name_classification)
        return tuple(new_list_names_classifications)

    def setting_variant_in_combobox_name_classification(self):
        for iteration_widget in range(int(len(self.list_widget_classifications) / 2)):
            self.list_widget_classifications[iteration_widget * 2].config(
                values=self.set_list_selected_names_classifications())

    def akt(self):

        # Функция для проверки корректности введенных дат и перевод их в объект класса Date
        def checking_deadline():
            good_data_date = True
            if self.__start_date is not None:
                try:
                    self.__start_date = data_akt.Date(self.__start_date)
                except (KeyError, IndexError, ValueError):
                    self.__indicator += 'В поле "Дата начала" введеные некоректные данные\n'
                    good_data_date = False
            if self.__finish_date is not None:
                try:
                    self.__finish_date = data_akt.Date(self.__finish_date)
                except (KeyError, IndexError, ValueError):
                    self.__indicator += 'В поле "Дата окончания" введеные некоректные данные\n'
                    good_data_date = False
            if self.__start_date is not None and self.__finish_date is not None and good_data_date:
                if data_akt.date_comparison(self.__start_date, self.__finish_date):
                    self.__indicator += '"Дата начала" не может быть позднее "Даты окончания"\n'

        # функция для получения данный из полей
        def insert_data(combobox, data_tuple):
            index = combobox.current()
            if index == -1:
                return data_akt.Object_element(combobox.get(), combobox.get())
            else:
                return data_tuple[index]

        # функция для получения данный из группы виджетов Проектно-сметная документация
        def insert_data_documentation():
            documents_list = []
            for iteration in range(int(len(self.list_documentation) / 3)):
                org = insert_data(self.list_documentation[iteration * 3 + 0], x_data_akt.get_all_organizations())
                doc_name = insert_data(self.list_documentation[iteration * 3 + 1],
                                       x_data_akt.get_all_project_documentation())
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
                            self.__indicator += 'Некорректно введен список листов\n'
                            return
                        else:
                            doc = data_akt.Doc(org, doc_name, page)
                            documents_list.append(doc)
            documents_list = tuple(documents_list)
            return documents_list

        # Получение кортежа выбранных материалов
        def set_materials_object():
            index_materials = []
            for text_material in self.__list_text_materials_akt:
                index_materials.append(self.__static_all_materials.index(text_material))
            materials = []
            for index_material in index_materials:
                materials.append(x_data_akt.get_material(index_material))
            return tuple(materials)

        def set_documents_object():
            index_documents = []
            for text_document in self.__list_text_documents_akt:
                index_documents.append(self.__static_all_documents.index(text_document))
            documents = []
            for index_document in index_documents:
                documents.append(x_data_akt.get_document(index_document))
            return tuple(documents)

        def set_list_regulations_akt():
            list_regulations_akt = []
            for iteration in self.list_widget_regulations:
                list_regulations_akt.append(insert_data(iteration, x_data_akt.get_all_regulations()))
            return tuple(list_regulations_akt)

        def set_list_next_work():
            list_next_work = []
            for iteration in range(int(len(self.list_widget_order_work) / 2)):
                if self.list_widget_order_work[iteration * 2 + 1].get() != '':
                    list_next_work.append(insert_data(self.list_widget_order_work[iteration * 2 + 1],
                                                      x_data_akt.get_all_akts_names_object()))
                if self.list_widget_order_work[iteration * 2].get() != '':
                    previous_akt_work = self.list_widget_order_work[iteration * 2].get()
                    index_previous_akt_work = x_data_akt.get_all_akts_names_text().index(previous_akt_work)
                    x_data_akt.get_akt(index_previous_akt_work).add_next_work(self.__work)
            return tuple(list_next_work)

        def set_classifications():
            dict_classifications = dict()
            for iteration in range(int(len(self.list_widget_classifications) / 2)):
                key = self.list_widget_classifications[iteration * 2].get()
                value = self.list_widget_classifications[iteration * 2 + 1].get()
                if key in dict_classifications:
                    self.__indicator += 'Акта не должен содержать несколько классов в одной классификации\n'
                if key != '' and value != '':
                    dict_classifications[key] = value
                    if key not in x_data_akt.get_all_names_classifications():
                        x_data_akt.set_name_classification(key)
                elif key == '' and value != '':
                    self.__indicator += 'Наименование классификации не должно быть пустым, если класс заполнен\n'
            return dict_classifications

        # Обновление переменной "Индикатор" (необходимо в случае, если индикатор уже горел)
        self.__indicator = ''

        # получение элементов акта
        self.__name_object = insert_data(self.combobox_object, x_data_akt.get_all_names_object())
        self.__developer = insert_data(self.combobox_developer, x_data_akt.get_all_organizations())
        self.__builder = insert_data(self.combobox_builder, x_data_akt.get_all_organizations())
        self.__designer = insert_data(self.combobox_designer, x_data_akt.get_all_organizations())
        self.__developer_name = insert_data(self.combobox_developer_name, x_data_akt.get_all_representatives())
        self.__builder_name = insert_data(self.combobox_builder_name, x_data_akt.get_all_representatives())
        self.__builder_control_name = insert_data(self.combobox_builder_control_name,
                                                  x_data_akt.get_all_representatives())
        self.__designer_name = insert_data(self.combobox_designer_name, x_data_akt.get_all_representatives())
        self.__contractor_name = insert_data(self.combobox_contractor_name, x_data_akt.get_all_representatives())
        self.__another_person = insert_data(self.combobox_another_person, x_data_akt.get_all_representatives())
        self.__contractor = insert_data(self.combobox_contractor, x_data_akt.get_all_organizations())
        self.__start_date = self.entry_start_date.get() if self.entry_start_date.get() != '' else None
        self.__finish_date = self.entry_finish_date.get() if self.entry_finish_date.get() != '' else None
        self.__work = data_akt.Object_element(self.entry_work.get(), None)
        self.__documentation = insert_data_documentation()
        self.__list_regulations_akt = set_list_regulations_akt()
        self.__next_work = set_list_next_work()
        self.__additional_information = self.text_additional_information.get('1.0', 'end')
        self.__number_of_copies = self.snipbox_number_of_copies.get() if self.snipbox_number_of_copies.get() != '0' else ''
        self.__classifications = set_classifications()

        # проверка корректности введенных данный
        if self.__work.get_text() == '':
            self.__indicator = 'Наименование работ не должно быть пустым\n' + self.__indicator
        checking_deadline()

        if self.__indicator != '':
            self.label_indicator.config(text=self.__indicator)
            return

        if self.__action == 'новый' or self.__action == 'на основе другого':
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
            akt.set_object_start_date(self.__start_date)
            akt.set_object_finish_date(self.__finish_date)
            akt.set_name_work(self.__work)
            akt.set_documentation(self.__documentation)
            akt.set_materials_of_akt(set_materials_object())
            akt.set_documents_of_akt(set_documents_object())
            akt.set_regulations(self.__list_regulations_akt)
            akt.set_next_work(self.__next_work)
            akt.set_additional_information(self.__additional_information)
            akt.set_number_of_copies(self.__number_of_copies)
            akt.set_classification(self.__classifications)
            x_data_akt.set_akt(akt)
        elif self.__action == 'изменить':
            x_data_akt.get_akt(self.__index).set_name_object(self.__name_object)
            x_data_akt.get_akt(self.__index).set_developer(self.__developer)
            x_data_akt.get_akt(self.__index).set_builder(self.__builder)
            x_data_akt.get_akt(self.__index).set_designer(self.__designer)
            x_data_akt.get_akt(self.__index).set_developer_name(self.__developer_name)
            x_data_akt.get_akt(self.__index).set_builder_name(self.__builder_name)
            x_data_akt.get_akt(self.__index).set_builder_control_name(self.__builder_control_name)
            x_data_akt.get_akt(self.__index).set_designer_name(self.__designer_name)
            x_data_akt.get_akt(self.__index).set_contractor_name(self.__contractor_name)
            x_data_akt.get_akt(self.__index).set_another_person(self.__another_person)
            x_data_akt.get_akt(self.__index).set_contractor(self.__contractor)
            x_data_akt.get_akt(self.__index).set_object_start_date(self.__start_date)
            x_data_akt.get_akt(self.__index).set_object_finish_date(self.__finish_date)
            x_data_akt.get_akt(self.__index).set_name_work(self.__work)
            x_data_akt.get_akt(self.__index).set_documentation(self.__documentation)
            x_data_akt.get_akt(self.__index).set_materials_of_akt(set_materials_object())
            x_data_akt.get_akt(self.__index).set_documents_of_akt(set_documents_object())
            x_data_akt.get_akt(self.__index).set_regulations(self.__list_regulations_akt)
            x_data_akt.get_akt(self.__index).set_additional_information(self.__additional_information)
            x_data_akt.get_akt(self.__index).set_next_work(self.__next_work)
            x_data_akt.get_akt(self.__index).set_number_of_copies(self.__number_of_copies)
            x_data_akt.get_akt(self.__index).set_classification(self.__classifications)

        elements = tkinter.Variable(value=x_data_akt.get_all_akts_names_text())
        self.__listbox.config(listvariable=elements)
        self.window_create_akt.destroy()


class Window_material:
    def __init__(self, root, table, index=None, item=None):
        self.__root = root
        self.__table = table
        self.__indicator = ''
        if index is None:
            self.__index = None
            self.__type = None
            self.__material = None
            self.__document_name = None
            self.__documents_name = None
            self.__document_number = None
            self.__start_date = None
            self.__finish_date = None
            self.__file = None
            self.__order_material = 'поставить в конец списка'
            self.__heading = 'Добавление материала'
            self.__text_button = 'Добавить материал'
        else:
            self.__index = index
            self.__item = item
            self.__type = x_data_akt.get_material(index).get_type()
            self.__material = x_data_akt.get_material(index).get_material()
            self.__document_name = x_data_akt.get_material(index).get_document_name()
            self.__documents_name = x_data_akt.get_material(index).get_documents_name()
            self.__document_number = x_data_akt.get_material(index).get_document_number()
            self.__start_date = x_data_akt.get_material(index).get_str_start_date()
            self.__finish_date = x_data_akt.get_material(index).get_str_finish_date()
            if x_data_akt.get_material(index).get_bin_images() is None:
                self.__file = '<Файл не загружен>'
            else:
                self.__file = '<Есть загруженный файл>'
            self.__order_material = index + 1
            self.__heading = 'Изменение материала'
            self.__text_button = 'Изменить материал'

        self.window = Toplevel(self.__root)
        self.window.title(self.__heading)
        self.window.geometry('500x500')
        self.window.grab_set()
        self.window.bind('<Control-KeyPress>', key_rus)

        self.frame_root = tkinter.Frame(self.window)
        self.frame_material = ttk.LabelFrame(self.frame_root, text='Данные о материале')
        self.label_type = tkinter.Label(self.frame_material, text='Вид')
        self.combobox_type = ttk.Combobox(self.frame_material,
                                          width=35,
                                          values=x_data_akt.get_all_unique_type_materials())
        self.label_material = tkinter.Label(self.frame_material, text='Наименование')
        self.combobox_material = ttk.Combobox(self.frame_material,
                                              width=35,
                                              values=x_data_akt.get_all_unique_material_materials())
        self.label_document_name = tkinter.Label(self.frame_material, text='Наименование документа')
        self.combobox_document_name = ttk.Combobox(self.frame_material,
                                                   width=35,
                                                   values=x_data_akt.get_all_unique_document_names_materials())
        self.label_documents_name = tkinter.Label(self.frame_material, text='Наименование документов')
        self.combobox_documents_name = ttk.Combobox(self.frame_material,
                                                    width=35,
                                                    values=x_data_akt.get_all_unique_documents_names_materials())
        self.label_document_number = tkinter.Label(self.frame_material, text='Номер документа')
        self.entry_document_number = tkinter.Entry(self.frame_material, width=35)
        self.label_start_date = tkinter.Label(self.frame_material, text='Дата начала')
        self.entry_start_date = tkinter.Entry(self.frame_material, width=35)
        self.label_finish_date = tkinter.Label(self.frame_material, text='Дата окончания')
        self.entry_finish_date = tkinter.Entry(self.frame_material, width=35)
        self.label_file = tkinter.Label(self.frame_material, text='Файл документа')
        self.entry_file = tkinter.Entry(self.frame_material, width=35)

        self.label_type.grid(row=0, column=0, stick='we', sticky='e')
        self.label_material.grid(row=1, column=0, stick='we', sticky='e')
        self.label_document_name.grid(row=2, column=0, stick='we', sticky='e')
        self.label_documents_name.grid(row=3, column=0, stick='we', sticky='e')
        self.label_document_number.grid(row=4, column=0, stick='we', sticky='e')
        self.label_start_date.grid(row=5, column=0, stick='we', sticky='e')
        self.label_finish_date.grid(row=6, column=0, stick='we', sticky='e')
        self.label_file.grid(row=7, column=0, stick='we', sticky='e')

        self.combobox_type.grid(row=0, column=1, stick='we')
        self.combobox_material.grid(row=1, column=1, stick='we')
        self.combobox_document_name.grid(row=2, column=1, stick='we')
        self.combobox_documents_name.grid(row=3, column=1, stick='we')
        self.entry_document_number.grid(row=4, column=1, stick='we')
        self.entry_start_date.grid(row=5, column=1, stick='we')
        self.entry_finish_date.grid(row=6, column=1, stick='we')
        self.entry_file.grid(row=7, column=1, stick='we')

        self.frame_order_material = ttk.LabelFrame(self.frame_root, text='Порядок материала')

        numbers_order = len(x_data_akt.get_all_text_materials_list())
        if numbers_order == 0:
            combobox_var = tuple(['поставить в конец списка'])
        else:
            combobox_var = ['поставить последним материалом этого типа']
            combobox_var += list(range(1, numbers_order + 2))
        self.combobox_order_material = ttk.Combobox(self.frame_order_material, width=61,
                                                    values=combobox_var)
        self.combobox_order_material.set(self.__order_material)
        languages_var = []
        for iteration in range(len(x_data_akt.get_all_text_materials_list())):
            languages_var.append(f'{iteration + 1}. {x_data_akt.get_all_text_materials_list()[iteration]}')
        languages_var.append(f'{len(x_data_akt.get_all_text_materials_list()) + 1}. в конце списка')
        languages_var = tkinter.Variable(value=languages_var)
        self.frame_listbox = tkinter.Frame(self.frame_order_material)
        self.listbox_order_material = tkinter.Listbox(self.frame_listbox, width=61,
                                                      listvariable=languages_var)
        self.listbox_order_material_scrollbar = tkinter.Scrollbar(self.frame_listbox,
                                                                  command=self.listbox_order_material.yview)
        self.listbox_order_material.config(yscrollcommand=self.listbox_order_material_scrollbar.set)

        self.combobox_order_material.grid(row=0, column=0)
        self.frame_listbox.grid(row=1, column=0)
        self.listbox_order_material.pack(side='left')
        self.listbox_order_material_scrollbar.pack(side='right', fill='y')

        # self.combobox_documents_name.config(state='disabled')
        # self.entry_finish_date.config(state='disabled')FocusOut

        self.combobox_document_name.bind('<FocusOut>', self.corresponding_documents_name)
        self.entry_file.bind('<Double-ButtonPress-3>', self.get_file_path_file_material)
        self.listbox_order_material.bind('<<ListboxSelect>>', self.setting_combobox_order_material)
        self.combobox_order_material.bind('<<ComboboxSelected>>', self.setting_listbox_order_material)

        if self.__index is not None:
            self.combobox_type.set(self.__type if self.__type is not None else '')
            self.combobox_material.set(self.__material if self.__material is not None else '')
            self.combobox_document_name.set(self.__document_name if self.__document_name is not None else '')
            self.combobox_documents_name.set(self.__documents_name if self.__documents_name is not None else '')
            self.entry_document_number.insert('end',
                                              self.__document_number if self.__document_number is not None else '')
            self.entry_start_date.insert('end', self.__start_date if self.__start_date is not None else '')
            self.entry_finish_date.insert('end', self.__finish_date if self.__finish_date is not None else '')
            self.entry_file.insert('end', self.__file)

        self.frame_indicator_and_button = tkinter.Frame(self.frame_root)
        self.button_material = tkinter.Button(self.frame_indicator_and_button, text=self.__text_button,
                                              command=self.material)
        self.label_indicator = tkinter.Label(self.frame_indicator_and_button, foreground='red')

        self.button_material.pack()
        self.label_indicator.pack()

        self.frame_material.grid(row=0, column=0, sticky='n')
        self.frame_order_material.grid(row=1, column=0)
        self.frame_indicator_and_button.grid(row=2, column=0)

        self.frame_root.pack()

        # Автозаполнение combobox_documents_name

    def corresponding_documents_name(self, event):
        documents_name = x_data_akt.get_corresponding_documents_name_materials(self.combobox_document_name.get())
        if documents_name is not None:
            self.combobox_documents_name.set(documents_name)

        # Функция для получения пути до файла документа

    def get_file_path_file_material(self, event):
        self.entry_file.delete(0, 'end')
        path_file_material = tkinter.filedialog.askopenfilename(title='Загрузка файл документа')
        self.entry_file.insert('end', path_file_material)

        # Функции для установки значения в combobox порядка материалов

    def setting_combobox_order_material(self, event):
        index_order = self.listbox_order_material.curselection()[0]
        self.combobox_order_material.set(index_order + 1)

        # Функция для выделения материала в listbox порядка материалов

    def setting_listbox_order_material(self, event):
        index_order = self.combobox_order_material.get()
        if index_order != 'поставить в конец списка' and index_order != 'поставить последним материалом этого типа':
            self.listbox_order_material.select_set(int(index_order) - 1)

    def material(self):

        # Функция для проверки корректности введенных дат и перевод их в объект класса Date
        def checking_deadline():
            if self.__start_date is None and self.__finish_date is not None:
                self.__indicator += 'Поле "Дата начала" не может быть пустым, если поле "Дата окончания" заполнено\n'
                return
            good_data_date = True
            if self.__start_date is not None:
                try:
                    self.__start_date = data_akt.Date(self.__start_date)
                except (KeyError, IndexError, ValueError):
                    self.__indicator += 'В поле "Дата начала" введеные некоректные данные\n'
                    good_data_date = False
            if self.__finish_date is not None:
                try:
                    self.__finish_date = data_akt.Date(self.__finish_date)
                except (KeyError, IndexError, ValueError):
                    self.__indicator += 'В поле "Дата окончания" введеные некоректные данные\n'
                    good_data_date = False
            if self.__start_date is not None and self.__finish_date is not None and good_data_date:
                if data_akt.date_comparison(self.__start_date, self.__finish_date):
                    self.__indicator += '"Дата начала" не может быть позднее "Даты окончания"\n'

        # Обновление переменной "Индикатор" (необходимо в случае, если индикатор уже горел)
        self.__indicator = ''

        # Получение данный с полей ввода
        self.__type = self.combobox_type.get() if self.combobox_type.get() != '' else None
        self.__material = self.combobox_material.get()
        self.__document_name = self.combobox_document_name.get() if self.combobox_document_name.get() != '' else None
        self.__documents_name = self.combobox_documents_name.get() if self.combobox_documents_name.get() != '' else None
        self.__document_number = self.entry_document_number.get() if self.entry_document_number.get() != '' else None
        self.__start_date = self.entry_start_date.get() if self.entry_start_date.get() != '' else None
        self.__finish_date = self.entry_finish_date.get() if self.entry_finish_date.get() != '' else None
        if self.entry_file.get() == '<Файл не загружен>' or self.entry_file.get() == '<Есть загруженный файл>' or self.entry_file.get() == '':
            self.__file = None
        else:
            self.__file = self.entry_file.get()
        if self.combobox_order_material.get() == 'поставить в конец списка' or self.combobox_order_material.get() == 'поставить последним материалом этого типа' or self.combobox_order_material.get() == '':
            self.__order_material = None
        else:
            self.__order_material = int(self.combobox_order_material.get()) - 1

        # проверка корректности введенных данный
        if self.__material == '':
            self.__indicator += 'Поле "Наименование" не может быть пустым\n'
        if self.__document_name is None and self.__documents_name is not None:
            self.__indicator += ('Поле "Наименование документа" не может быть пустым, ' +
                                 'если поле "Наименование документов" заполнено\n')
        checking_deadline()

        # Если данные введены некорректно выводит ошибки в веденных данных
        if self.__indicator != '':
            self.label_indicator.config(text=self.__indicator)
        else:
            # Создание нового материала, назначение его атрибутов и добавление в таблицу
            if self.__index is None:
                material = data_akt.Material()

                material.set_type(self.__type)
                material.set_material(self.__material)
                material.set_document_name(self.__document_name)
                material.set_documents_name(self.__documents_name)
                material.set_document_number(self.__document_number)
                material.set_object_start_date(self.__start_date)
                material.set_object_finish_date(self.__finish_date)
                material.load_bin_images(self.__file)

                x_data_akt.set_material(material, self.__order_material)

                for item in self.__table.get_children():
                    self.__table.delete(item)
                for material in x_data_akt.get_all_text_materials_table():
                    self.__table.insert('', 'end', values=material)

                self.window.destroy()
            # Изменение атрибутов ранее созданного объекта класса "Материалы"
            else:
                x_data_akt.get_material(self.__index).set_type(self.__type)
                x_data_akt.get_material(self.__index).set_material(self.__material)
                x_data_akt.get_material(self.__index).set_document_name(self.__document_name)
                x_data_akt.get_material(self.__index).set_documents_name(self.__documents_name)
                x_data_akt.get_material(self.__index).set_document_number(self.__document_number)
                x_data_akt.get_material(self.__index).set_object_start_date(self.__start_date)
                x_data_akt.get_material(self.__index).set_object_finish_date(self.__finish_date)
                x_data_akt.get_material(self.__index).load_bin_images(self.__file)

                x_data_akt.change_order_of_material(x_data_akt.get_material(self.__index), self.__order_material)

                for item in self.__table.get_children():
                    self.__table.delete(item)
                for material in x_data_akt.get_all_text_materials_table():
                    self.__table.insert('', 'end', values=material)

                self.window.destroy()


class Window_order_material:
    def __init__(self, root, list_old_order, subject_of_order):
        self.__root = root

        self.list_old_order_materials = list_old_order
        self.static_list_old_order_materials = self.numbering_list(list_old_order)
        self.list_new_order_materials = tuple()
        self.subject_of_order = subject_of_order
        self.__indicator = ''

        self.window = Toplevel(self.__root)
        self.window.title('Порядок отображения позиций')
        self.window.geometry('1000x500')
        self.window.grab_set()
        self.window.bind('<Control-KeyPress>', key_rus)
        self.frame_root = tkinter.Frame(self.window)
        self.frame_listbox_old_order = tkinter.Frame(self.frame_root)
        self.label_old_order = tkinter.Label(self.frame_root, text='Старый порядок позиций')
        self.listbox_old_order = tkinter.Listbox(self.frame_listbox_old_order, width=75, height=25,
                                                 selectmode='extended',
                                                 listvariable=tkinter.Variable(
                                                     value=self.static_list_old_order_materials))
        self.listbox_old_order_scrollbar = tkinter.Scrollbar(self.frame_listbox_old_order,
                                                             command=self.listbox_old_order.yview)
        self.listbox_old_order.config(yscrollcommand=self.listbox_old_order_scrollbar.set)
        self.listbox_old_order_scrollbar.pack(side='left', fill='y')
        self.listbox_old_order.pack(side='right')

        self.label_symbol = tkinter.Label(self.frame_root, text='->')

        self.label_new_order = tkinter.Label(self.frame_root, text='Новый порядок позиций')
        self.frame_listbox_new_order = tkinter.Frame(self.frame_root)
        self.listbox_new_order = tkinter.Listbox(self.frame_listbox_new_order, width=75, height=25,
                                                 selectmode='extended')
        self.listbox_new_order_scrollbar = tkinter.Scrollbar(self.frame_listbox_new_order,
                                                             command=self.listbox_new_order.yview)
        self.listbox_new_order.config(yscrollcommand=self.listbox_new_order_scrollbar.set)
        self.listbox_new_order.pack(side='left')
        self.listbox_new_order_scrollbar.pack(side='right', fill='y')

        self.button_setting_order = tkinter.Button(self.window, text='Установить новый порядок позиций',
                                                   command=self.setting_new_material_order)
        self.label_indicator = tkinter.Label(self.window, foreground='red')

        self.label_old_order.grid(row=0, column=0)
        self.frame_listbox_old_order.grid(row=1, column=0)
        self.label_symbol.grid(row=0, column=1, rowspan=2, padx=5)
        self.label_new_order.grid(row=0, column=2)
        self.frame_listbox_new_order.grid(row=1, column=2)

        self.frame_root.pack()
        self.button_setting_order.pack(pady=5)
        self.label_indicator.pack()

        self.listbox_old_order.bind('<Double-ButtonPress-1>', self.transfer_to_listbox_new_order)
        self.listbox_new_order.bind('<Double-ButtonPress-1>', self.cancellation_transfer)
        self.listbox_old_order.bind('<ButtonPress-3>', self.menu_listbox_old_order)
        self.listbox_new_order.bind('<ButtonPress-3>', self.menu_listbox_new_order)

    def menu_listbox_old_order(self, event):
        menu = tkinter.Menu(tearoff=0)
        menu.add_command(label='Добавить', command=self.transfer_to_listbox_new_order)
        menu.post(self.window.winfo_pointerx(), self.window.winfo_pointery())

    def menu_listbox_new_order(self, event):
        menu = tkinter.Menu(tearoff=0)
        menu.add_command(label='Убрать', command=self.cancellation_transfer)
        menu.post(self.window.winfo_pointerx(), self.window.winfo_pointery())

        # Перемещение Материалов из сторого списка в новый

    def transfer_to_listbox_new_order(self, event=None):
        self.list_old_order_materials = list(self.list_old_order_materials)
        separator_list = []
        for index_row in self.listbox_old_order.curselection():
            row = self.listbox_old_order.get(index_row)
            separator_index = row.find('.')
            separator_list.append(row[separator_index + 2:])
            self.list_old_order_materials.remove(row[separator_index + 2:])

        old_list = []
        for row in self.static_list_old_order_materials:
            separator_index = row.find('.')
            if row[separator_index + 2:] in self.list_old_order_materials:
                old_list.append(row)
        self.listbox_old_order.config(listvariable=tkinter.Variable(value=old_list))

        self.list_new_order_materials += tuple(separator_list)
        list_material = self.numbering_list(self.list_new_order_materials)
        self.listbox_new_order.config(listvariable=tkinter.Variable(value=list_material))
        self.list_old_order_materials = tuple(self.list_old_order_materials)

        # Отмена перемещения материала в новый список

    def cancellation_transfer(self, event=None):
        self.list_new_order_materials = list(self.list_new_order_materials)
        self.list_old_order_materials = list(self.list_old_order_materials)

        separator_list = []
        for index_row in self.listbox_new_order.curselection():
            row = self.listbox_new_order.get(index_row)
            separator_index = row.find('.')
            separator_list.append(row[separator_index + 2:])
            self.list_new_order_materials.remove(row[separator_index + 2:])

        self.list_old_order_materials += separator_list

        old_list = []
        for row in self.static_list_old_order_materials:
            separator_index = row.find('.')
            if row[separator_index + 2:] in self.list_old_order_materials:
                old_list.append(row)
        self.listbox_old_order.config(listvariable=tkinter.Variable(value=old_list))

        new_list = self.numbering_list(self.list_new_order_materials)
        self.listbox_new_order.config(listvariable=tkinter.Variable(value=new_list))
        self.list_old_order_materials.sort(key=lambda x: x_data_akt.get_all_text_materials_list().index(x))
        self.list_new_order_materials = tuple(self.list_new_order_materials)
        self.list_old_order_materials = tuple(self.list_old_order_materials)

        # Установка полного списка материалов в новом порядке

    def setting_new_material_order(self):
        self.__indicator = ''
        self.label_indicator.config(text='')
        if len(self.list_old_order_materials) != 0:
            self.__indicator += 'Не все позиции добавленый в новый список'
            self.label_indicator.config(text=self.__indicator)
            return
        if self.subject_of_order == 'material':
            x_data_akt.setting_complete_material_order(self.list_new_order_materials)
        elif self.subject_of_order == 'document':
            x_data_akt.setting_complete_document_order(self.list_new_order_materials)
        self.window.destroy()

        # Нуменрация списка

    def numbering_list(self, list_material):
        list_selected_material = []
        for iter in range(len(list_material)):
            list_selected_material.append(f'{iter + 1}. {list_material[iter]}')
        return tuple(list_selected_material)


class Window_data_base:
    def __init__(self, root, object_data_base, material_executive_documentation):
        self.__root = root
        self.__object_data_base = object_data_base
        self.__root_table = material_executive_documentation
        self.__indicator = ''

        self.window = Toplevel(self.__root)
        self.window.title('База данный материалов')
        self.window.geometry('500x500')
        self.window.grab_set()
        self.window.bind('<Control-KeyPress>', key_rus)
        self.window.protocol("WM_DELETE_WINDOW", self.close_window)

        # МЕНЮ окна
        self.main_menu = tkinter.Menu(self.window)
        self.window.config(menu=self.main_menu)
        self.file_menu = tkinter.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label='Файл', menu=self.file_menu)
        self.file_menu.add_command(label='Новый', command=self.new_db)
        self.file_menu.add_command(label='Открыть', command=self.load_db)
        self.file_menu.add_command(label='Сохранить', command=self.data_base_commit)

        self.frame_table_materials = tkinter.Frame(self.window)
        self.table_material_db = ttk.Treeview(self.frame_table_materials,
                                              columns=('id', 'type', 'material', 'document', 'date'),
                                              show='headings',
                                              height=25)
        self.table_material_scrollbar_y = ttk.Scrollbar(self.frame_table_materials, orient='vertical',
                                                        command=self.table_material_db.yview)
        self.table_material_scrollbar_x = ttk.Scrollbar(self.frame_table_materials, orient='horizontal',
                                                        command=self.table_material_db.xview)
        self.table_material_db.config(yscrollcommand=self.table_material_scrollbar_y.set)
        self.table_material_db.config(xscrollcommand=self.table_material_scrollbar_x.set)

        self.table_material_db.heading('id', text='id', command=self.menu_sorting_by_id_materials)
        self.table_material_db.heading('type', text='Вид',
                                       command=self.menu_sorting_by_type)
        self.type_sort = {}
        self.table_material_db.heading('material', text='Материал', command=self.menu_sorting_by_name_materials)
        self.material_sort = {}
        self.table_material_db.heading('document', text='Документ', command=self.menu_sorting_by_document_name)
        self.document_name_sort = {}
        self.document_number_sort = {}
        self.table_material_db.heading('date', text='Дата', command=self.menu_sorting_by_date)
        self.start_date_sort = {}
        self.finish_date_sort = {}
        self.table_material_db.column('#1', width=30)
        self.table_material_db.column('#2', width=100)
        self.table_material_db.column('#3', width=300)
        self.table_material_db.column('#4', width=300)
        self.table_material_db.column('#5', width=200)
        self.table_material_db.grid(row=0, column=0)
        self.table_material_scrollbar_y.grid(row=0, column=1, sticky='ns')
        self.table_material_scrollbar_x.grid(row=1, column=0, rowspan=2, sticky='we')

        self.frame_search_materials = ttk.LabelFrame(self.window, text='Поиск материалов')
        self.entry_search = tkinter.Entry(self.frame_search_materials, width=150)
        self.button_search = tkinter.Button(self.frame_search_materials, text='Поиск',
                                            command=lambda: self.search_materials(None))
        self.entry_search.grid(row=0, column=0, sticky='ns')
        self.button_search.grid(row=0, column=1, sticky='we')

        self.frame_material = ttk.LabelFrame(self.window, text='Материал')
        self.label_id = tkinter.Label(self.frame_material, text='ID в базе')
        self.combobox_id = ttk.Combobox(self.frame_material,
                                        state="readonly",
                                        width=50)
        self.label_type = tkinter.Label(self.frame_material, text='Вид')
        self.combobox_type = ttk.Combobox(self.frame_material,
                                          width=50)
        self.label_material = tkinter.Label(self.frame_material, text='Наименование')
        self.combobox_material = ttk.Combobox(self.frame_material,
                                              width=50)
        self.label_document_name = tkinter.Label(self.frame_material, text='Наименование документа')
        self.combobox_document_name = ttk.Combobox(self.frame_material,
                                                   width=50,
                                                   values=x_data_akt.get_all_unique_document_names_materials())
        self.label_documents_name = tkinter.Label(self.frame_material, text='Наименование документов')
        self.combobox_documents_name = ttk.Combobox(self.frame_material,
                                                    width=50,
                                                    values=x_data_akt.get_all_unique_documents_names_materials())
        self.label_document_number = tkinter.Label(self.frame_material, text='Номер документа')
        self.entry_document_number = tkinter.Entry(self.frame_material, width=50)
        self.label_start_date = tkinter.Label(self.frame_material, text='Дата начала')
        self.entry_start_date = tkinter.Entry(self.frame_material, width=50)
        self.label_finish_date = tkinter.Label(self.frame_material, text='Дата окончания')
        self.entry_finish_date = tkinter.Entry(self.frame_material, width=50)
        self.label_file = tkinter.Label(self.frame_material, text='Файл документа')
        self.entry_file = tkinter.Entry(self.frame_material, width=50)

        self.label_id.grid(row=0, column=0, stick='we', sticky='e')
        self.label_type.grid(row=1, column=0, stick='we', sticky='e')
        self.label_material.grid(row=2, column=0, stick='we', sticky='e')
        self.label_document_name.grid(row=3, column=0, stick='we', sticky='e')
        self.label_documents_name.grid(row=4, column=0, stick='we', sticky='e')
        self.label_document_number.grid(row=5, column=0, stick='we', sticky='e')
        self.label_start_date.grid(row=6, column=0, stick='we', sticky='e')
        self.label_finish_date.grid(row=7, column=0, stick='we', sticky='e')
        self.label_file.grid(row=8, column=0, stick='we', sticky='e')

        self.combobox_id.grid(row=0, column=1, stick='we')
        self.combobox_type.grid(row=1, column=1, stick='we')
        self.combobox_material.grid(row=2, column=1, stick='we')
        self.combobox_document_name.grid(row=3, column=1, stick='we')
        self.combobox_documents_name.grid(row=4, column=1, stick='we')
        self.entry_document_number.grid(row=5, column=1, stick='we')
        self.entry_start_date.grid(row=6, column=1, stick='we')
        self.entry_finish_date.grid(row=7, column=1, stick='we')
        self.entry_file.grid(row=8, column=1, stick='we')

        self.frame_button = tkinter.Frame(self.frame_material)
        self.but_add = tkinter.Button(self.frame_button, text='добавить', command=self.add_material)
        self.but_del = tkinter.Button(self.frame_button, text='удалить', command=self.delete_material)
        self.but_view = tkinter.Button(self.frame_button, text='просмотр', command=self.view_file)
        self.but_del_file = tkinter.Button(self.frame_button, text='удалить файл', command=self.delete_file)
        self.but_add.grid(row=0, column=0, stick='ns')
        self.but_del.grid(row=0, column=1, stick='ns')
        self.but_view.grid(row=0, column=2, stick='ns')
        self.but_del_file.grid(row=0, column=3, stick='ns')
        self.frame_button.grid(row=9, column=0, columnspan=2, sticky='w')

        self.label_indicator = tkinter.Label(self.frame_material, foreground='red')
        self.label_indicator.grid(row=10, column=0, columnspan=2, sticky='w')

        self.frame_material.grid(row=0, column=0, stick='we')
        self.frame_search_materials.grid(row=1, column=0, stick='we')
        self.frame_table_materials.grid(row=2, column=0, stick='ns')

        self.table_material_db.bind('<<TreeviewSelect>>', self.select_material_via_tabel)
        self.table_material_db.bind('<ButtonPress-3>', self.menu_table_material)
        self.combobox_id.bind('<<ComboboxSelected>>', self.select_material_via_combobox_id)
        self.entry_file.bind('<Double-ButtonPress-3>', self.get_file_path_file_material)
        self.entry_search.bind('<Return>', self.search_materials)

        self.update_table_material()

        # функция для новой база данных

    def new_db(self):
        path_file = tkinter.filedialog.asksaveasfilename(confirmoverwrite=True,
                                                         defaultextension='db',
                                                         initialfile='new_date_base_material.db',
                                                         title='Создание базы данных')
        self.__object_data_base = data_akt.connection_new_base_data(path_file, self.__object_data_base)
        self.update_table_material()

        # функция для загрузки база данных

    def load_db(self):
        path_file = tkinter.filedialog.askopenfilename(defaultextension='db',
                                                       initialfile='new_date_base_material.db',
                                                       title='Загрузка базы данных')
        self.__object_data_base = data_akt.connection_base_data(path_file)
        self.update_table_material()

    def menu_table_material(self, event):
        if self.table_material_db.selection() != ():
            menu = tkinter.Menu(tearoff=0)
            menu.add_command(label='Добавить в исполнительную документацию', command=self.export_data_akt)
            menu.add_separator()
            menu.add_command(label='Просмотр документа', command=self.view_file)
            menu.add_command(label='Удалить документ', command=self.delete_file)
            menu.add_separator()
            menu.add_command(label='Удалить запись из БД', command=self.delete_material)
            menu.post(self.window.winfo_pointerx(), self.window.winfo_pointery())

        # функции для контекстного меню столбца "ID"

    def menu_sorting_by_id_materials(self):
        menu = tkinter.Menu(tearoff=0)
        menu.add_command(label='Сбросить сортировку', command=self.update_table_material)
        menu.add_separator()
        menu.add_command(label='Сортировать А-Я', command=lambda: self.sort_material('ItemID'))
        menu.add_command(label='Сортировать Я-A', command=lambda: self.sort_material('ItemID DESC'))
        menu.post(self.window.winfo_pointerx(), self.window.winfo_pointery())

    def menu_sorting_by_type(self):
        menu = tkinter.Menu(tearoff=0)
        menu.add_command(label='Сбросить сортировку', command=self.update_table_material)
        menu.add_separator()
        menu.add_command(label='Сортировать А-Я',
                         command=lambda: self.sort_material('type'))
        menu.add_command(label='Сортировать Я-A',
                         command=lambda: self.sort_material('type DESC'))
        menu.add_separator()
        for el_type in self.__object_data_base.all_type_material():
            var_type = self.type_sort[el_type]
            menu.add_checkbutton(label=el_type, onvalue=True, offvalue=False, variable=var_type,
                                 command=self.switching_by_type)
        menu.post(self.window.winfo_pointerx(), self.window.winfo_pointery())

        # функции для контекстного меню столбца "МАТЕРИАЛ"

    def menu_sorting_by_name_materials(self):
        menu = tkinter.Menu(tearoff=0)
        menu.add_command(label='Сбросить сортировку', command=self.update_table_material)
        menu.add_separator()
        menu.add_command(label='Сортировать А-Я',
                         command=lambda: self.sort_material('material'))
        menu.add_command(label='Сортировать Я-A',
                         command=lambda: self.sort_material('material DESC'))
        menu.add_separator()
        list_menu_materials = []
        for el_type in self.__object_data_base.all_type_material():
            list_menu_materials.append(tkinter.Menu(tearoff=0))
            for el_material in self.__object_data_base.all_name_material(el_type):
                var_material = self.material_sort[el_material]
                list_menu_materials[-1].add_checkbutton(label=el_material, onvalue=True, offvalue=False,
                                                        variable=var_material, command=self.switching_by_materials)
            menu.add_cascade(label=el_type, menu=list_menu_materials[-1])
        menu.post(self.window.winfo_pointerx(), self.window.winfo_pointery())

        # функции для контекстного меню столбца "ДОКУМЕНТЫ"

    def menu_sorting_by_document_name(self):
        menu = tkinter.Menu(tearoff=0)
        menu.add_command(label='Сбросить сортировку', command=self.update_table_material)
        menu.add_separator()
        menu.add_command(label='Сортировать А-Я',
                         command=lambda: self.sort_material('document_name'))
        menu.add_command(label='Сортировать Я-A',
                         command=lambda: self.sort_material('document_name DESC'))
        menu.add_separator()
        list_menu_document_name = []
        for el_document_name in self.__object_data_base.all_document_name():
            list_menu_document_name.append(tkinter.Menu(tearoff=0))
            var_document_name = self.document_name_sort[el_document_name]
            menu.add_checkbutton(label=el_document_name, onvalue=True, offvalue=False, variable=var_document_name,
                                 command=self.switching_by_document_name)
            for el_document_number in self.__object_data_base.all_document_number(el_document_name):
                var_document_number = self.document_number_sort[el_document_number]
                list_menu_document_name[-1].add_checkbutton(label=el_document_number, onvalue=True, offvalue=False,
                                                            variable=var_document_number,
                                                            command=self.switching_by_document_number)
            menu.add_cascade(label=el_document_name, menu=list_menu_document_name[-1])
            menu.add_separator()
        menu.post(self.window.winfo_pointerx(), self.window.winfo_pointery())

        # функции для контекстного меню столбца "ДАТА"

    def menu_sorting_by_date(self):
        menu = tkinter.Menu(tearoff=0)
        menu_start_date = tkinter.Menu(tearoff=0)
        menu.add_command(label='Сбросить сортировку', command=self.update_table_material)
        menu_start_date.add_command(label='Сортировать А-Я', command=lambda: self.sort_material('start_date'))
        menu_start_date.add_command(label='Сортировать Я-A', command=lambda: self.sort_material('start_date DESC'))
        menu.add_cascade(label='Сортировка даты начала', menu=menu_start_date)
        menu_finish_date = tkinter.Menu(tearoff=0)
        menu_finish_date.add_command(label='Сортировать А-Я', command=lambda: self.sort_material('finish_date'))
        menu_finish_date.add_command(label='Сортировать Я-A', command=lambda: self.sort_material('finish_date DESC'))
        menu.add_cascade(label='Сортировка даты окончания', menu=menu_finish_date)

        menu.post(self.window.winfo_pointerx(), self.window.winfo_pointery())

        # Сортировка материалов

    def sort_material(self, column_for_order=None):
        def sort_finish_date(list_data, revers):
            list_none_date = []
            list_finish_date = []
            for row in list_data:
                if row[7] is None:
                    list_none_date.append(row)
                else:
                    list_finish_date.append(row)
            if revers:
                list_finish_date.sort(key=lambda row: data_akt.Date(row[7]).get_date(), reverse=True)
            else:
                list_finish_date.sort(key=lambda row: data_akt.Date(row[7]).get_date())
            return tuple(list_finish_date + list_none_date)

        material_names = []
        for key_0 in self.material_sort:
            if not self.material_sort[key_0].get():
                material_names.append(key_0)
        document_number = []
        for key_1 in self.document_number_sort:
            if not self.document_number_sort[key_1].get():
                document_number.append(key_1)
        result = self.__object_data_base.selection_materials_for_table(material_names, document_number,
                                                                       column_for_order)
        if column_for_order == 'start_date':
            result.sort(key=lambda row: data_akt.Date(row[6]).get_date())
        elif column_for_order == 'start_date DESC':
            result.sort(key=lambda row: data_akt.Date(row[6]).get_date(), reverse=True)
        elif column_for_order == 'finish_date':
            result = sort_finish_date(result, False)
        elif column_for_order == 'finish_date DESC':
            result = sort_finish_date(result, True)

        for row in self.table_material_db.get_children():
            self.table_material_db.delete(row)
        self.show_in_table(result)

        # Переключатель типа по материалу:

    def switching_by_materials(self):
        for key in self.type_sort:
            self.type_sort[key].set(True)
            for el in self.__object_data_base.all_name_material(key):
                if not self.material_sort[el].get():
                    self.type_sort[key].set(False)
                    for row in self.__object_data_base.selection_materials('material', el):
                        self.document_number_sort[row[5]].set(False)
                else:
                    for row in self.__object_data_base.selection_materials('material', el):
                        self.document_number_sort[row[5]].set(True)
        self.sort_material()

        # Переключение материалов по типу:

    def switching_by_type(self):
        for key in self.document_name_sort:
            self.document_name_sort[key].set(True)
        for key in self.type_sort:
            if self.type_sort[key].get():
                for el in self.__object_data_base.all_name_material(key):
                    self.material_sort[el].set(True)
                for row in self.__object_data_base.selection_materials('type', key):
                    self.document_number_sort[row[5]].set(True)
            else:
                for el in self.__object_data_base.all_name_material(key):
                    self.material_sort[el].set(False)
                for row in self.__object_data_base.selection_materials('type', key):
                    self.document_number_sort[row[5]].set(False)
                    self.document_name_sort[row[3]].set(False)
        self.sort_material()

        # Переключатель типа по номеру документов:

    def switching_by_document_number(self):
        for key in self.document_name_sort:
            self.document_name_sort[key].set(True)
            for el in self.__object_data_base.all_document_number(key):
                if not self.document_number_sort[el].get():
                    self.document_name_sort[key].set(False)
                    for row in self.__object_data_base.selection_materials('document_number', el):
                        self.material_sort[row[2]].set(False)
                else:
                    for row in self.__object_data_base.selection_materials('document_number', el):
                        self.material_sort[row[2]].set(True)
        self.sort_material()

        # Переключатель типа по наименованию документов:

    def switching_by_document_name(self):
        for key in self.type_sort:
            self.type_sort[key].set(True)
        for key in self.document_name_sort:
            if self.document_name_sort[key].get():
                for el in self.__object_data_base.all_document_number(key):
                    self.document_number_sort[el].set(True)
                for row in self.__object_data_base.selection_materials('document_name', key):
                    self.material_sort[row[2]].set(True)
            else:
                for el in self.__object_data_base.all_document_number(key):
                    self.document_number_sort[el].set(False)
                for row in self.__object_data_base.selection_materials('document_name', key):
                    self.material_sort[row[2]].set(False)
                    self.type_sort[row[1]].set(False)
        self.sort_material()

        # функция для поиска материалов в базе данных

    def search_materials(self, event):
        search = self.entry_search.get()
        result = self.__object_data_base.selection_materials_for_search(search)
        for row in self.table_material_db.get_children():
            self.table_material_db.delete(row)
        self.show_in_table(result)

        # функция для добавления и изменения материала

    def add_material(self):
        self.__indicator = ''
        self.label_indicator.config(text=self.__indicator)

        def checking_deadline(start_date, finish_date):
            if start_date is None and finish_date is not None:
                self.__indicator += 'Поле "Дата начала" не может быть пустым, если поле "Дата окончания" заполнено\n'
                return
            good_data_date = True
            if start_date is not None:
                try:
                    start_date = data_akt.Date(start_date)
                except (KeyError, IndexError, ValueError):
                    self.__indicator += 'В поле "Дата начала" введеные некоректные данные\n'
                    good_data_date = False
            if finish_date is not None:
                try:
                    finish_date = data_akt.Date(finish_date)
                except (KeyError, IndexError, ValueError):
                    self.__indicator += 'В поле "Дата окончания" введеные некоректные данные\n'
                    good_data_date = False
            if start_date is not None and finish_date is not None and good_data_date:
                if data_akt.date_comparison(start_date, finish_date):
                    self.__indicator += '"Дата начала" не может быть позднее "Даты окончания"\n'

        type_material = self.combobox_type.get() if self.combobox_type.get() != '' else None
        material = self.combobox_material.get() if self.combobox_material.get() != '' else None
        document_name = self.combobox_document_name.get() if self.combobox_document_name.get() != '' else None
        documents_name = self.combobox_documents_name.get() if self.combobox_documents_name.get() != '' else None
        document_number = self.entry_document_number.get() if self.entry_document_number.get() != '' else None
        start_date = self.entry_start_date.get() if self.entry_start_date.get() != '' else None
        finish_date = self.entry_finish_date.get() if self.entry_finish_date.get() != '' else None
        if self.entry_file.get() == '' or self.entry_file.get() == '<Файл не загружен>' or self.entry_file.get() == '<Есть загруженный файл>':
            path_file_material = None
        else:
            path_file_material = self.entry_file.get() if self.entry_file.get() != '' else None
        material_id = self.combobox_id.get()

        if type_material is None:
            self.__indicator += 'Поле "Вид" не должно быть пустым\n'
        if material is None:
            self.__indicator += 'Поле "Наименование" не должно быть пустым\n'
        if document_name is None:
            self.__indicator += 'Поле "Наименование документа" не должно быть пустым\n'
        if documents_name is None:
            self.__indicator += 'Поле "Наименование документов" не должно быть пустым\n'
        if document_number is None:
            self.__indicator += 'Поле "Номер документа" не должно быть пустым\n'
        checking_deadline(start_date, finish_date)

        if self.__indicator != '':
            self.label_indicator.config(text=self.__indicator[:-1])
            return

        if material_id == '<Добавить материал>':
            self.__object_data_base.insert_data(type_material, material, document_name, documents_name, document_number,
                                                start_date, finish_date, path_file_material)
        else:
            self.__object_data_base.change_data(material_id, type_material, material, document_name, documents_name,
                                                document_number, start_date, finish_date, path_file_material)
        self.update_table_material()
        self.clear_input()

    # функция для получения пути до файла документа
    def get_file_path_file_material(self, event):
        self.entry_file.delete(0, 'end')
        path_file_material = tkinter.filedialog.askopenfilename(defaultextension='db',
                                                                initialfile='new_date_base_material.db',
                                                                title='Загрузка файл документа в базу данных')
        self.entry_file.insert('end', path_file_material)

    # функция для просмотра файла
    def view_file(self):
        row = self.table_material_db.selection()[0]
        id = self.table_material_db.item(row)['values'][0]
        images = self.__object_data_base.get_file_material(id)
        window_PDF = Window_veiw_doc(self.window, images)

    # функция для удаления файла
    def delete_file(self):
        row = self.table_material_db.selection()[0]
        id = self.table_material_db.item(row)['values'][0]
        self.__object_data_base.del_file_material(id)
        self.update_table_material()
        self.clear_input()

    # функция для обновления таблицы материалов
    def update_table_material(self):
        for row in self.table_material_db.get_children():
            self.table_material_db.delete(row)
        self.show_in_table(self.__object_data_base.extract_all_data_from_database())
        self.combobox_id.config(values=('<Добавить материал>',) + self.__object_data_base.all_id_material())
        self.combobox_id.current(0)
        self.combobox_type.config(values=self.__object_data_base.all_type_material())
        self.combobox_material.config(values=self.__object_data_base.all_name_material())
        for el in self.__object_data_base.all_type_material():
            self.type_sort[el] = tkinter.BooleanVar()
            self.type_sort[el].set(True)
        for el in self.__object_data_base.all_name_material():
            self.material_sort[el] = tkinter.BooleanVar()
            self.material_sort[el].set(True)
        for el in self.__object_data_base.all_document_number():
            self.document_number_sort[el] = tkinter.BooleanVar()
            self.document_number_sort[el].set(True)
        for el in self.__object_data_base.all_document_name():
            self.document_name_sort[el] = tkinter.BooleanVar()
            self.document_name_sort[el].set(True)
        for el in self.__object_data_base.all_start_date():
            self.start_date_sort[data_akt.Date(el)] = el
        for el in self.__object_data_base.all_finish_date():
            if el is not None:
                self.finish_date_sort[data_akt.Date(el)] = el

    # показать базу данных в таблице
    def show_in_table(self, selection):
        for row_db in selection:
            material = []
            material.append(row_db[0])
            material.append(row_db[1])
            material.append(row_db[2])
            material.append(f'{row_db[3]} {row_db[5]}')
            if row_db[7] is not None:
                material.append(f'с {row_db[6]} до {row_db[7]}')
            else:
                material.append(f'от {row_db[6]}')
            self.table_material_db.insert('', 'end', values=material)

    # выбор материала
    def select_material(self, material_id):
        self.clear_input()
        self.but_add.config(text='изменить')
        material = self.__object_data_base.material_selection_by_id(material_id)
        self.combobox_id.set(material[0])
        self.combobox_type.set(material[1] if material[1] is not None else '')
        self.combobox_material.set(material[2] if material[2] is not None else '')
        self.combobox_document_name.set(material[3] if material[3] is not None else '')
        self.combobox_documents_name.set(material[4] if material[4] is not None else '')
        self.entry_document_number.insert('end', material[5] if material[5] is not None else '')
        self.entry_start_date.insert('end', material[6] if material[6] is not None else '')
        self.entry_finish_date.insert('end', material[7] if material[7] is not None else '')
        if material[8] is None:
            self.entry_file.insert('end', '<Файл не загружен>')
        elif material[8] is not None:
            self.entry_file.insert('end', '<Есть загруженный файл>')

    # удаление материала
    def delete_material(self):
        for row in self.table_material_db.selection():
            material_id = self.table_material_db.item(row)['values'][0]
            self.__object_data_base.delete_data(material_id)
            self.table_material_db.delete(row)
            self.clear_input()

    # выбор материала через combobox id
    def select_material_via_combobox_id(self, event):
        material_id = self.combobox_id.get()
        if material_id == '<Добавить материал>':
            self.but_add.config(text='добавить')
            return
        self.select_material(material_id)
        for row in self.table_material_db.get_children(''):
            if self.table_material_db.item(row)['values'][0] == int(material_id):
                self.table_material_db.selection_set(row)
                break

    # выбор материала через таблицу материалов
    def select_material_via_tabel(self, event):
        row = self.table_material_db.selection()[0]
        id = self.table_material_db.item(row)['values'][0]
        self.select_material(id)

    # отчистка полей ввода материалов
    def clear_input(self):
        self.combobox_id.set('<Добавить материал>')
        self.combobox_type.set('')
        self.combobox_material.set('')
        self.combobox_document_name.set('')
        self.combobox_documents_name.set('')
        self.entry_document_number.delete(0, 'end')
        self.entry_start_date.delete(0, 'end')
        self.entry_finish_date.delete(0, 'end')
        self.entry_file.delete(0, 'end')

    # Добавление материал в исполнительную документацию
    def export_data_akt(self):
        row = self.table_material_db.selection()[0]
        id = self.table_material_db.item(row)['values'][0]
        data_material = self.__object_data_base.material_export(id)
        material = data_akt.Material()
        material.set_type(data_material[1])
        material.set_material(data_material[2])
        material.set_document_name(data_material[3])
        material.set_documents_name(data_material[4])
        material.set_document_number(data_material[5])
        material.set_object_start_date(data_material[6])
        material.set_object_finish_date(data_material[7])
        material.set_bin_images(data_material[8])
        x_data_akt.set_material(material)
        self.__root_table.insert('', 'end', values=material.get_in_tabel())

    # вызов окна с предложением сохранить БЗ бри закрытии окна
    def close_window(self):
        result = tkinter.messagebox.askyesnocancel(title='Закрыть базу данных материалов',
                                                   message='Сохранить базу данных перед закрытием?')
        if result:
            self.data_base_commit()
            self.data_base_close()
        elif result is None:
            return
        elif not result:
            self.data_base_close()

    # сохранение базы данных
    def data_base_commit(self):
        self.__object_data_base.commit_data_base()

    # закрытие окна
    def data_base_close(self):
        self.__object_data_base.close_date_base()
        self.window.destroy()


class Window_veiw_doc:
    def __init__(self, window, images):
        self.__window = Toplevel(window)
        self.__window.geometry('700x900')
        self.__window.bind('<Control-KeyPress>', key_rus)
        self.images = images
        self.num_page = 1
        self.frame_page = tkinter.Frame(self.__window)
        self.but_left = tkinter.Button(self.frame_page, text='<', command=lambda: self.next_page(-1))
        self.but_right = tkinter.Button(self.frame_page, text='>', command=lambda: self.next_page(1))
        self.label_page = tkinter.Label(self.frame_page, text=f'{self.num_page}/{len(self.images)}')
        self.label = tkinter.Label(self.__window)

        self.frame_page.pack()
        self.but_left.grid(row=0, column=0)
        self.label_page.grid(row=0, column=1)
        self.but_right.grid(row=0, column=2)
        self.label.pack()

        self.next_page(0)

        self.__window.bind('<Left>', lambda a: self.next_page(-1))
        self.__window.bind('<Right>', lambda a: self.next_page(1))

    def next_page(self, page):
        if (self.num_page + page) <= 0:
            self.num_page = 1
        elif (self.num_page + page) > len(self.images):
            self.num_page = len(self.images)
        else:
            self.num_page += page
        self.label_page.config(text=f'{self.num_page}/{len(self.images)}')
        image_tk = tkinter.PhotoImage(data=self.images[self.num_page - 1])
        # self.__window.geometry(f'{image_tk.width()}x{image_tk.height()}')
        self.label.config(image=image_tk)
        self.label.photo = image_tk


class Window_document:
    def __init__(self, root, table, index=None, item=None):
        self.__root = root
        self.__table = table
        self.__indicator = ''
        if index is None:
            self.__index = None
            self.__document_name = None
            self.__documents_name = None
            self.__document_number = None
            self.__start_date = None
            self.__finish_date = None
            self.__file = None
            self.__order_document = 'поставить в конец списка'
            self.__heading = 'Добавление документа'
            self.__text_button = 'Добавить документ'
        else:
            self.__index = index
            self.__item = item
            self.__document_name = x_data_akt.get_document(index).get_document_name()
            self.__documents_name = x_data_akt.get_document(index).get_documents_name()
            self.__document_number = x_data_akt.get_document(index).get_document_number()
            self.__start_date = x_data_akt.get_document(index).get_str_start_date()
            self.__finish_date = x_data_akt.get_document(index).get_str_finish_date()
            if x_data_akt.get_document(index).get_bin_images() is None:
                self.__file = '<Файл не загружен>'
            else:
                self.__file = '<Есть загруженный файл>'
            self.__order_document = index + 1
            self.__heading = 'Изменение документа'
            self.__text_button = 'Изменить документ'

        self.window = Toplevel(self.__root)
        self.window.title(self.__heading)
        self.window.geometry('500x500')
        self.window.grab_set()
        self.window.bind('<Control-KeyPress>', key_rus)

        self.frame_root = tkinter.Frame(self.window)
        self.frame_document = ttk.LabelFrame(self.frame_root, text='Данные о документе')
        self.label_document_name = tkinter.Label(self.frame_document, text='Наименование документа')
        self.combobox_document_name = ttk.Combobox(self.frame_document,
                                                   width=35,
                                                   values=x_data_akt.get_all_unique_document_names_documents())
        self.label_documents_name = tkinter.Label(self.frame_document, text='Наименование документов')
        self.combobox_documents_name = ttk.Combobox(self.frame_document,
                                                    width=35,
                                                    values=x_data_akt.get_all_unique_documents_names_documents())
        self.label_document_number = tkinter.Label(self.frame_document, text='Номер документа')
        self.entry_document_number = tkinter.Entry(self.frame_document, width=35)
        self.label_start_date = tkinter.Label(self.frame_document, text='Дата начала')
        self.entry_start_date = tkinter.Entry(self.frame_document, width=35)
        self.label_finish_date = tkinter.Label(self.frame_document, text='Дата окончания')
        self.entry_finish_date = tkinter.Entry(self.frame_document, width=35)
        self.label_file = tkinter.Label(self.frame_document, text='Файл документа')
        self.entry_file = tkinter.Entry(self.frame_document, width=35)

        self.label_document_name.grid(row=0, column=0, stick='we', sticky='e')
        self.label_documents_name.grid(row=1, column=0, stick='we', sticky='e')
        self.label_document_number.grid(row=2, column=0, stick='we', sticky='e')
        self.label_start_date.grid(row=3, column=0, stick='we', sticky='e')
        self.label_finish_date.grid(row=4, column=0, stick='we', sticky='e')
        self.label_file.grid(row=5, column=0, stick='we', sticky='e')

        self.combobox_document_name.grid(row=0, column=1, stick='we')
        self.combobox_documents_name.grid(row=1, column=1, stick='we')
        self.entry_document_number.grid(row=2, column=1, stick='we')
        self.entry_start_date.grid(row=3, column=1, stick='we')
        self.entry_finish_date.grid(row=4, column=1, stick='we')
        self.entry_file.grid(row=5, column=1, stick='we')

        self.frame_order_document = ttk.LabelFrame(self.frame_root, text='Порядок документов')

        numbers_order = len(x_data_akt.get_all_text_materials_list())
        if numbers_order == 0:
            combobox_var = tuple(['поставить в конец списка'])
        else:
            combobox_var = ['поставить последним документом этого наименования']
            combobox_var += list(range(1, numbers_order + 2))
        self.combobox_order_document = ttk.Combobox(self.frame_order_document, width=61,
                                                    values=combobox_var)
        self.combobox_order_document.set(self.__order_document)
        languages_var = []
        for iteration in range(len(x_data_akt.get_all_text_documents_list())):
            languages_var.append(f'{iteration + 1}. {x_data_akt.get_all_text_documents_list()[iteration]}')
        languages_var.append(f'{len(x_data_akt.get_all_text_documents_list()) + 1}. в конце списка')
        languages_var = tkinter.Variable(value=languages_var)
        self.frame_listbox = tkinter.Frame(self.frame_order_document)
        self.listbox_order_document = tkinter.Listbox(self.frame_listbox, width=61,
                                                      listvariable=languages_var)
        self.listbox_order_document_scrollbar = tkinter.Scrollbar(self.frame_listbox,
                                                                  command=self.listbox_order_document.yview)
        self.listbox_order_document.config(yscrollcommand=self.listbox_order_document_scrollbar.set)

        self.combobox_order_document.grid(row=0, column=0)
        self.frame_listbox.grid(row=1, column=0)
        self.listbox_order_document.pack(side='left')
        self.listbox_order_document_scrollbar.pack(side='right', fill='y')

        self.combobox_document_name.bind('<FocusOut>', self.corresponding_documents_name)
        self.entry_file.bind('<Double-ButtonPress-3>', self.get_file_path_file_document)
        self.listbox_order_document.bind('<<ListboxSelect>>', self.setting_combobox_order_document)
        self.combobox_order_document.bind('<<ComboboxSelected>>', self.setting_listbox_order_document)

        if self.__index is not None:
            self.combobox_document_name.set(self.__document_name if self.__document_name is not None else '')
            self.combobox_documents_name.set(self.__documents_name if self.__documents_name is not None else '')
            self.entry_document_number.insert('end',
                                              self.__document_number if self.__document_number is not None else '')
            self.entry_start_date.insert('end', self.__start_date if self.__start_date is not None else '')
            self.entry_finish_date.insert('end', self.__finish_date if self.__finish_date is not None else '')
            self.entry_file.insert('end', self.__file)

        self.frame_indicator_and_button = tkinter.Frame(self.frame_root)
        self.button_material = tkinter.Button(self.frame_indicator_and_button, text=self.__text_button,
                                              command=self.document)
        self.label_indicator = tkinter.Label(self.frame_indicator_and_button, foreground='red')

        self.button_material.pack()
        self.label_indicator.pack()

        self.frame_document.grid(row=0, column=0, sticky='n')
        self.frame_order_document.grid(row=1, column=0)
        self.frame_indicator_and_button.grid(row=2, column=0)

        self.frame_root.pack()

        # Автозаполнение combobox_documents_name

    def corresponding_documents_name(self, event):
        documents_name = x_data_akt.get_corresponding_documents_name_documents(self.combobox_document_name.get())
        if documents_name is not None:
            self.combobox_documents_name.set(documents_name)

        # Функция для получения пути до файла документа

    def get_file_path_file_document(self, event):
        self.entry_file.delete(0, 'end')
        path_file_document = tkinter.filedialog.askopenfilename(title='Загрузка файл документа')
        self.entry_file.insert('end', path_file_document)

        # Функции для установки значения в combobox порядка материалов

    def setting_combobox_order_document(self, event):
        index_order = self.listbox_order_document.curselection()[0]
        self.combobox_order_document.set(index_order + 1)

        # Функция для выделения материала в listbox порядка материалов

    def setting_listbox_order_document(self, event):
        index_order = self.combobox_order_document.get()
        if index_order != 'поставить в конец списка' and index_order != 'поставить последним материалом этого типа':
            self.listbox_order_document.select_set(int(index_order) - 1)

    def document(self):

        # Функция для проверки корректности введенных дат и перевод их в объект класса Date
        def checking_deadline():
            if self.__start_date is None and self.__finish_date is not None:
                self.__indicator += 'Поле "Дата начала" не может быть пустым, если поле "Дата окончания" заполнено\n'
                return
            good_data_date = True
            if self.__start_date is not None:
                try:
                    self.__start_date = data_akt.Date(self.__start_date)
                except (KeyError, IndexError, ValueError):
                    self.__indicator += 'В поле "Дата начала" введеные некоректные данные\n'
                    good_data_date = False
            if self.__finish_date is not None:
                try:
                    self.__finish_date = data_akt.Date(self.__finish_date)
                except (KeyError, IndexError, ValueError):
                    self.__indicator += 'В поле "Дата окончания" введеные некоректные данные\n'
                    good_data_date = False
            if self.__start_date is not None and self.__finish_date is not None and good_data_date:
                if data_akt.date_comparison(self.__start_date, self.__finish_date):
                    self.__indicator += '"Дата начала" не может быть позднее "Даты окончания"\n'

        # Обновление переменной "Индикатор" (необходимо в случае, если индикатор уже горел)
        self.__indicator = ''

        # Получение данный с полей ввода
        self.__document_name = self.combobox_document_name.get() if self.combobox_document_name.get() != '' else None
        self.__documents_name = self.combobox_documents_name.get() if self.combobox_documents_name.get() != '' else None
        self.__document_number = self.entry_document_number.get() if self.entry_document_number.get() != '' else None
        self.__start_date = self.entry_start_date.get() if self.entry_start_date.get() != '' else None
        self.__finish_date = self.entry_finish_date.get() if self.entry_finish_date.get() != '' else None
        if self.entry_file.get() == '<Файл не загружен>' or self.entry_file.get() == '<Есть загруженный файл>' or self.entry_file.get() == '':
            self.__file = None
        else:
            self.__file = self.entry_file.get()
        if self.combobox_order_document.get() == 'поставить в конец списка' or self.combobox_order_document.get() == 'поставить последним материалом этого типа' or self.combobox_order_document.get() == '':
            self.__order_document = None
        else:
            self.__order_document = int(self.combobox_order_document.get()) - 1

        # проверка корректности введенных данный
        if self.__document_name is None:
            self.__indicator += 'Поле "Наименование" не может быть пустым\n'
        if self.__documents_name is None:
            self.__indicator += 'Поле "Наименование документов" не может быть пустым'
        checking_deadline()

        # Если данные введены некорректно выводит ошибки в веденных данных
        if self.__indicator != '':
            self.label_indicator.config(text=self.__indicator)
        else:
            # Создание нового материала, назначение его атрибутов и добавление в таблицу
            if self.__index is None:
                document = data_akt.Document()

                document.set_document_name(self.__document_name)
                document.set_documents_name(self.__documents_name)
                document.set_document_number(self.__document_number)
                document.set_object_start_date(self.__start_date)
                document.set_object_finish_date(self.__finish_date)
                document.load_bin_images(self.__file)

                x_data_akt.set_document(document, self.__order_document)

                for item in self.__table.get_children():
                    self.__table.delete(item)
                for document in x_data_akt.get_all_text_documents_table():
                    self.__table.insert('', 'end', values=document)

                self.window.destroy()
            # Изменение атрибутов ранее созданного объекта класса "Материалы"
            else:
                x_data_akt.get_document(self.__index).set_document_name(self.__document_name)
                x_data_akt.get_document(self.__index).set_documents_name(self.__documents_name)
                x_data_akt.get_document(self.__index).set_document_number(self.__document_number)
                x_data_akt.get_document(self.__index).set_object_start_date(self.__start_date)
                x_data_akt.get_document(self.__index).set_object_finish_date(self.__finish_date)
                x_data_akt.get_document(self.__index).load_bin_images(self.__file)

                x_data_akt.change_order_of_document(x_data_akt.get_document(self.__index), self.__order_document)

                for item in self.__table.get_children():
                    self.__table.delete(item)
                for document in x_data_akt.get_all_text_documents_table():
                    self.__table.insert('', 'end', values=document)

                self.window.destroy()


class Window_export_to_word:
    def __init__(self, root, index_akt):
        self.__root = root
        self.__index_akt = index_akt
        self.__point = None
        self.__font = ('Times New Roman', 'Calibri', 'Arial')
        self.__format_day = ('01', '1')
        self.__format_month = ('1', '01', 'декабрь', 'декабря')
        self.__format_year = ('2024', '24')

        self.window = Toplevel(self.__root)
        self.window.title('Экспорт в Word')
        self.window.geometry('500x500')
        self.window.grab_set()
        self.window.bind('<Control-KeyPress>', key_rus)
        self.Export = data_akt.Export()

        self.frame_pattern_akt = tkinter.LabelFrame(self.window, text='Шаблоны')
        self.button_load_pattern = tkinter.Button(self.frame_pattern_akt, text='Загрузить', width=15,
                                                  command=self.load_pattern)
        self.button_add_pattern = tkinter.Button(self.frame_pattern_akt, text='Новый', width=15,
                                                 command=self.add_pattern)
        self.button_change_pattern = tkinter.Button(self.frame_pattern_akt, text='Изменить', width=15,
                                                    command=self.change_pattern)
        self.button_delete_pattern = tkinter.Button(self.frame_pattern_akt, text='Удалить', width=15,
                                                    command=self.delete_pattern)
        self.patterns_names = tkinter.Variable(value=self.Export.list_patterns())
        self.listbox_pattern = tkinter.Listbox(self.frame_pattern_akt, listvariable=self.patterns_names, width=25,
                                               height=4)
        self.button_load_pattern.grid(row=1, column=0)
        self.button_add_pattern.grid(row=2, column=0)
        self.button_change_pattern.grid(row=3, column=0)
        self.button_delete_pattern.grid(row=4, column=0)
        self.listbox_pattern.grid(row=1, rowspan=4, column=1)

        self.frame_pattern_name = tkinter.Frame(self.window)
        self.label_pattern_name = tkinter.Label(self.frame_pattern_name, text='Наименование шаблона: ')
        self.entry_pattern_name = tkinter.Entry(self.frame_pattern_name, width=93)
        self.label_pattern_name.grid(row=0, column=0)
        self.entry_pattern_name.grid(row=0, column=1)

        '''
        def object_grid_remove(self):
            self.frame.grid_remove()
        '''

        class Point_format:
            def __init__(self, root, labelframe_text, heading, fonts, paragraph_var, alignment, bold_var, bold_italic,
                         bold_underline):

                self.frame = tkinter.LabelFrame(root, text=labelframe_text)
                self.frame_text = tkinter.Frame(self.frame)
                self.label_text = tkinter.Label(self.frame_text, text=f'{heading}')
                self.text_content = tkinter.Text(self.frame_text, height=8, width=50, wrap='word')
                self.label_text.grid(row=0, column=0)
                self.text_content.grid(row=1, column=0)

                self.frame_customization = tkinter.Frame(self.frame)

                self.frame_font = tkinter.Frame(self.frame_customization)
                self.label_font = tkinter.Label(self.frame_font, text='Шрифт:')
                self.combobox_font = ttk.Combobox(self.frame_font, width=25, values=fonts)
                self.label_font.grid(row=0, column=0)
                self.combobox_font.grid(row=0, column=1)

                self.frame_size = tkinter.Frame(self.frame_customization)
                self.label_size = tkinter.Label(self.frame_size, text='Размер:')
                self.spinbox_size = ttk.Spinbox(self.frame_size, width=3, from_=0.0, to=999.0)
                self.label_size.grid(row=0, column=0)
                self.spinbox_size.grid(row=0, column=1)

                self.frame_checkbutton = tkinter.Frame(self.frame_customization)
                self.bold_var = tkinter.BooleanVar(value=bold_var)
                self.checkbutton_bold = tkinter.Checkbutton(self.frame_checkbutton, text='Полужирный',
                                                            offvalue=False, onvalue=True, variable=self.bold_var)
                self.italic_var = tkinter.BooleanVar(value=bold_italic)
                self.checkbutton_italic = tkinter.Checkbutton(self.frame_checkbutton, text='Курсив',
                                                              offvalue=False, onvalue=True, variable=self.italic_var)
                self.underline_var = tkinter.BooleanVar(value=bold_underline)
                self.checkbutton_underline = tkinter.Checkbutton(self.frame_checkbutton, text='Подчеркнутый',
                                                                 offvalue=False, onvalue=True,
                                                                 variable=self.underline_var)
                self.checkbutton_bold.grid(row=0, column=0)
                self.checkbutton_italic.grid(row=0, column=1)
                self.checkbutton_underline.grid(row=0, column=2)

                self.paragraph_frame = tkinter.Frame(self.frame_customization)
                self.paragraph_var = tkinter.BooleanVar(value=paragraph_var)
                self.checkbutton_paragraph = tkinter.Checkbutton(self.paragraph_frame,
                                                                 text='Поместить в отдельный абзац',
                                                                 offvalue=False, onvalue=True,
                                                                 variable=self.paragraph_var)
                self.checkbutton_paragraph.grid(row=0, column=0)

                self.frame_alignment = tkinter.Frame(self.frame_customization)
                self.label_alignment = tkinter.Label(self.frame_alignment, text='Выравнивание:')
                self.alignment = tkinter.StringVar(value=alignment)
                self.left_radiobutton = tkinter.Radiobutton(self.frame_alignment, text='по левому краю',
                                                            value='LEFT', variable=self.alignment)
                self.right_radiobutton = tkinter.Radiobutton(self.frame_alignment, text='по правому краю',
                                                             value='RIGHT', variable=self.alignment)
                self.cent_radiobutton = tkinter.Radiobutton(self.frame_alignment, text='по центру',
                                                            value='CENTER', variable=self.alignment)
                self.width_radiobutton = tkinter.Radiobutton(self.frame_alignment, text='по ширине',
                                                             value='JUSTIFY', variable=self.alignment)
                self.all_width_radiobutton = tkinter.Radiobutton(self.frame_alignment, text='по абзацу',
                                                                 value='DISTRIBUTE', variable=self.alignment)
                self.label_alignment.grid(row=0, column=0, columnspan=2, sticky='w')
                self.left_radiobutton.grid(row=1, column=0, sticky='w')
                self.right_radiobutton.grid(row=1, column=1, sticky='w')
                self.cent_radiobutton.grid(row=2, column=0, sticky='w')
                self.width_radiobutton.grid(row=2, column=1, sticky='w')
                self.all_width_radiobutton.grid(row=3, column=0, sticky='w')

                self.frame_font.grid(row=0, column=0)
                self.frame_size.grid(row=0, column=1)
                self.frame_checkbutton.grid(row=1, column=0, columnspan=2, sticky='we')
                self.paragraph_frame.grid(row=2, column=0, columnspan=2, sticky='we')
                self.frame_alignment.grid(row=3, column=0, columnspan=2, sticky='we')

                self.frame_text.grid(row=0, column=0, rowspan=2)
                self.frame_customization.grid(row=0, column=1)

            def grid(self, row=None, column=None):
                if row is not None:
                    self.frame.grid(row=row, column=column, sticky='wens')
                else:
                    self.frame.grid()

            def remove_point(self):
                self.frame.grid_remove()

            def set_text(self, text):
                self.text_content.insert('end', text)

            def checkbutton_paragraph_state_disabled(self):
                self.checkbutton_paragraph.config(state='disabled')

            def disabled(self):
                self.text_content.config(state='disabled')
                self.combobox_font.config(state='disabled')
                self.spinbox_size.config(state='disabled')
                self.checkbutton_bold.config(state='disabled')
                self.checkbutton_italic.config(state='disabled')
                self.checkbutton_underline.config(state='disabled')
                self.left_radiobutton.config(state='disabled')
                self.right_radiobutton.config(state='disabled')
                self.cent_radiobutton.config(state='disabled')
                self.width_radiobutton.config(state='disabled')
                self.all_width_radiobutton.config(state='disabled')

            def get_config(self):
                font = self.combobox_font.get()
                size = self.spinbox_size.get()
                bold = self.bold_var.get()
                italic = self.italic_var.get()
                underline = self.underline_var.get()
                paragraph = self.paragraph_var.get()
                alignment = self.alignment.get()
                text = self.text_content.get('0.0', 'end')
                return font, size, bold, italic, underline, paragraph, alignment, text

            def set_config(self, font, size, bold, italic, underline, paragraph, alignment, text):
                self.combobox_font.set(font)
                self.spinbox_size.set(size)
                self.bold_var.set(bold)
                self.italic_var.set(italic)
                self.underline_var.set(underline)
                self.paragraph_var.set(paragraph)
                self.alignment.set(alignment)
                self.text_content.delete('0.0', 'end')
                self.text_content.insert('0.0', self.insert_content(text))

            def insert_content(self, text):
                content = ''
                for element in text:
                    if element == '':
                        pass
                    content += element
                return content

        class Point_format_content(Point_format):
            def __init__(self, root, labelframe_text, heading, fonts, paragraph_var, alignment, bold_var,
                         bold_italic, bold_underline, list_text, num_var):
                Point_format.__init__(self, root, labelframe_text, heading, fonts, paragraph_var, alignment, bold_var,
                                      bold_italic, bold_underline)

                self.frame_list = tkinter.Frame(self.frame)
                self.sep = ttk.Separator(self.frame_list, orient='horizontal')
                self.list_text = tkinter.StringVar(value=list_text)
                self.radiobutton_row = tkinter.Radiobutton(self.frame_list, text='список в колонку',
                                                           value='ROW',
                                                           variable=self.list_text)
                self.radiobutton_column = tkinter.Radiobutton(self.frame_list, text='список в строку',
                                                              value='COLUMN',
                                                              variable=self.list_text)
                self.frame_symbol_list = tkinter.Frame(self.frame_list)
                self.label_before_list = tkinter.Label(self.frame_symbol_list, text='Начальные символы пункта')
                self.entry_before_list = tkinter.Entry(self.frame_symbol_list, width=3)
                self.label_split_item = tkinter.Label(self.frame_symbol_list, text='Символы разделения пунктов')
                self.entry_split_item = tkinter.Entry(self.frame_symbol_list, width=3)
                self.label_after_list = tkinter.Label(self.frame_symbol_list, text='Завершающие символы списка')
                self.entry_after_list = tkinter.Entry(self.frame_symbol_list, width=3)
                self.num_var = tkinter.BooleanVar(value=num_var)
                self.checkbutton_num = tkinter.Checkbutton(self.frame_list, text='Номеровать список',
                                                           offvalue=False, onvalue=True, variable=self.num_var,
                                                           command=self.num_checking)
                self.label_before_num = tkinter.Label(self.frame_list, text='Символы\nдо номера')
                self.entry_before_num = tkinter.Entry(self.frame_list, width=3)
                self.label_after_num = tkinter.Label(self.frame_list, text='    Символы\nпосле номера')
                self.entry_after_num = tkinter.Entry(self.frame_list, width=3)
                self.sep.grid(row=0, column=0, columnspan=4, sticky='we')
                self.radiobutton_row.grid(row=1, column=0, columnspan=2)
                self.radiobutton_column.grid(row=1, column=2, columnspan=2)
                self.frame_symbol_list.grid(row=2, column=0, columnspan=4, sticky='we')

                self.label_before_list.grid(row=0, column=0, sticky='w')
                self.entry_before_list.grid(row=0, column=1, sticky='w')
                self.label_split_item.grid(row=1, column=0, sticky='w')
                self.entry_split_item.grid(row=1, column=1, sticky='w')
                self.label_after_list.grid(row=2, column=0, sticky='w')
                self.entry_after_list.grid(row=2, column=1, sticky='w')

                self.checkbutton_num.grid(row=3, column=0)
                self.label_before_num.grid(row=4, column=0, sticky='e')
                self.entry_before_num.grid(row=4, column=1)
                self.label_after_num.grid(row=4, column=2, sticky='e')
                self.entry_after_num.grid(row=4, column=3)
                self.frame_list.grid(row=1, column=1)
                self.num_checking()
                self.text_content.config(height=18)

            def get_config(self):
                font = self.combobox_font.get()
                size = self.spinbox_size.get()
                bold = self.bold_var.get()
                italic = self.italic_var.get()
                underline = self.underline_var.get()
                paragraph = self.paragraph_var.get()
                alignment = self.alignment.get()
                list_text = self.list_text.get()
                entry_before_list = self.entry_before_list.get()
                entry_split_item = self.entry_split_item.get()
                entry_after_list = self.entry_after_list.get()
                num_var = self.num_var.get()
                entry_before_num = self.entry_before_num.get()
                entry_after_num = self.entry_after_num.get()
                return (font, size, bold, italic, underline, paragraph, alignment, list_text, entry_before_list,
                        entry_split_item, entry_after_list, num_var, entry_before_num, entry_after_num)

            def set_config(self, font, size, bold, italic, underline, paragraph, alignment, list_text,
                           entry_before_list, entry_split_item, entry_after_list, num_var, entry_before_num,
                           entry_after_num):
                self.combobox_font.set(font)
                self.spinbox_size.set(size)
                self.bold_var.set(bold)
                self.italic_var.set(italic)
                self.underline_var.set(underline)
                self.paragraph_var.set(paragraph)
                self.alignment.set(alignment)

                self.list_text.set(list_text)
                self.entry_before_list.delete(0, 'end')
                self.entry_before_list.insert(0, entry_before_list)
                self.entry_split_item.delete(0, 'end')
                self.entry_split_item.insert(0, entry_split_item)
                self.entry_after_list.delete(0, 'end')
                self.entry_after_list.insert(0, entry_after_list)
                self.num_var.set(num_var)
                self.entry_before_num.delete(0, 'end')
                self.entry_before_num.insert(0, entry_before_num)
                self.entry_after_num.delete(0, 'end')
                self.entry_after_num.insert(0, entry_after_num)

            def num_checking(self):
                if self.num_var.get():
                    self.entry_before_num.config(state='normal')
                    self.entry_after_num.config(state='normal')
                else:
                    self.entry_before_num.config(state='disabled')
                    self.entry_after_num.config(state='disabled')

            def set_content(self, text):
                self.content = text
                self.text_content.delete('0.0', 'end')
                self.text_content.insert('0.0', self.content)

            def get_content(self):
                return self.content

        class Point_general:
            def __init__(self, root, alternation, table_format, table_line, table_line_heading, table_line_explanation):
                self.frame = tkinter.LabelFrame(root, text='Общие параметры пункта')
                self.frame_format = tkinter.Frame(self.frame)

                self.alternation_content_and_explanations = tkinter.BooleanVar(value=alternation)
                self.checkbutton_alternation = tkinter.Checkbutton(self.frame_format,
                                                                   text='Чередование строк содержания и пояснения',
                                                                   offvalue=False, onvalue=True,
                                                                   variable=self.alternation_content_and_explanations)
                self.table_format_var = tkinter.BooleanVar(value=table_format)
                self.checkbutton_table_format = tkinter.Checkbutton(self.frame_format,
                                                                    text='Табличный формат',
                                                                    offvalue=False, onvalue=True,
                                                                    variable=self.table_format_var)
                self.table_line_var = tkinter.StringVar(value=table_line)
                self.radiobutton_content = tkinter.Radiobutton(self.frame_format,
                                                               text='Табличные строки для содержания',
                                                               value='CONTENT', variable=self.table_line_var)
                self.radiobutton_content_end = tkinter.Radiobutton(self.frame_format,
                                                                   text='Только последняя строка табличная',
                                                                   value='CONTENT_END', variable=self.table_line_var)
                self.table_line_heading_var = tkinter.BooleanVar(value=table_line_heading)
                self.checkbutton_table_heading = tkinter.Checkbutton(self.frame_format,
                                                                     text='Табличная строка для заголовка',
                                                                     offvalue=False, onvalue=True,
                                                                     variable=self.table_line_heading_var)
                self.table_line_explanation_var = tkinter.BooleanVar(value=table_line_explanation)
                self.checkbutton_table_explanation = tkinter.Checkbutton(self.frame_format,
                                                                         text='Табличная строка для пояснения',
                                                                         offvalue=False, onvalue=True,
                                                                         variable=self.table_line_explanation_var)
                self.checkbutton_alternation.grid(row=0, column=0, sticky='w')
                self.checkbutton_table_format.grid(row=1, column=0, sticky='w')
                self.radiobutton_content.grid(row=2, column=0, sticky='w')
                self.radiobutton_content_end.grid(row=3, column=0, sticky='w')
                self.checkbutton_table_heading.grid(row=4, column=0, sticky='w')
                self.checkbutton_table_explanation.grid(row=5, column=0, sticky='w')

                self.frame_format.grid(row=0, column=0)

            def grid(self, row=None, column=None):
                if row is not None:
                    self.frame.grid(row=row, column=column, sticky='wens')
                else:
                    self.frame.grid()

            def remove_point(self):
                self.frame.grid_remove()

            def get_config(self):
                alternation = self.alternation_content_and_explanations.get()
                table_format_var = self.table_format_var.get()
                table_line_var = self.table_line_var.get()
                table_line_heading_var = self.table_line_heading_var.get()
                table_line_explanation_var = self.table_line_explanation_var.get()
                return (alternation, table_format_var, table_line_var, table_line_heading_var,
                        table_line_explanation_var)

            def set_config(self, alternation, table_format, table_line, table_line_heading, table_line_explanation):
                self.alternation_content_and_explanations.set(alternation)
                self.table_format_var.set(table_format)
                self.table_line_var.set(table_line)
                self.table_line_heading_var.set(table_line_heading)
                self.table_line_explanation_var.set(table_line_explanation)

        class Point_number_akt:
            def __init__(self, root, fonts, bold_var, bold_italic, bold_underline):
                self.frame = tkinter.LabelFrame(root, text='Номер акта')
                self.frame_text = tkinter.Frame(self.frame)
                self.label_text = tkinter.Label(self.frame_text, text='Содержание номера акта')
                self.text_content = tkinter.Text(self.frame_text, height=8, width=50, wrap='word')
                self.label_text.pack()
                self.text_content.pack()

                self.frame_customization = tkinter.Frame(self.frame)

                self.frame_font = tkinter.Frame(self.frame_customization)
                self.label_font = tkinter.Label(self.frame_font, text='Шрифт:')
                self.combobox_font = ttk.Combobox(self.frame_font, width=25, values=fonts)
                self.label_size = tkinter.Label(self.frame_font, text='Размер:')
                self.spinbox_size = ttk.Spinbox(self.frame_font, width=3, from_=0.0, to=999.0)
                self.frame_font.grid(row=0, column=0)
                self.label_font.grid(row=0, column=0, sticky='w')
                self.combobox_font.grid(row=0, column=1, sticky='w')
                self.label_size.grid(row=0, column=2, sticky='e')
                self.spinbox_size.grid(row=0, column=3, sticky='e')

                self.frame_checkbutton = tkinter.Frame(self.frame_customization)
                self.bold_var = tkinter.BooleanVar(value=bold_var)
                self.checkbutton_bold = tkinter.Checkbutton(self.frame_checkbutton, text='Полужирный',
                                                            offvalue=False, onvalue=True, variable=self.bold_var)
                self.italic_var = tkinter.BooleanVar(value=bold_italic)
                self.checkbutton_italic = tkinter.Checkbutton(self.frame_checkbutton, text='Курсив',
                                                              offvalue=False, onvalue=True, variable=self.italic_var)
                self.underline_var = tkinter.BooleanVar(value=bold_underline)
                self.checkbutton_underline = tkinter.Checkbutton(self.frame_checkbutton, text='Подчеркнутый',
                                                                 offvalue=False, onvalue=True,
                                                                 variable=self.underline_var)
                self.frame_checkbutton.grid(row=1, column=0)
                self.checkbutton_bold.grid(row=0, column=0)
                self.checkbutton_italic.grid(row=0, column=1)
                self.checkbutton_underline.grid(row=0, column=2)

                self.sep = ttk.Separator(self.frame_customization, orient='horizontal')
                self.sep.grid(row=2, column=0, sticky='we', pady=2)

                self.frame_number = tkinter.Frame(self.frame)
                self.frame_symbol_num = tkinter.Frame(self.frame_number)
                self.label_start_num = tkinter.Label(self.frame_symbol_num, text='Начальные символы')
                self.entry_start_num = tkinter.Entry(self.frame_symbol_num, width=3)
                self.label_before_num = tkinter.Label(self.frame_symbol_num, text='Cимволы перед номером')
                self.entry_before_num = tkinter.Entry(self.frame_symbol_num, width=3)
                self.label_split_num = tkinter.Label(self.frame_symbol_num, text='Символы после номера')
                self.entry_split_num = tkinter.Entry(self.frame_symbol_num, width=3)

                self.label_start_num.grid(row=0, column=0, sticky='w')
                self.entry_start_num.grid(row=0, column=1, sticky='e')
                self.label_before_num.grid(row=1, column=0, sticky='w')
                self.entry_before_num.grid(row=1, column=1, sticky='e')
                self.label_split_num.grid(row=2, column=0, sticky='w')
                self.entry_split_num.grid(row=2, column=1, sticky='e')
                self.frame_symbol_num.grid(row=1, column=0, sticky='we')

                self.frame_text.grid(row=0, column=0, rowspan=2)
                self.frame_customization.grid(row=0, column=1)
                self.frame_number.grid(row=1, column=1)

            def grid(self, row=None, column=None):
                if row is not None:
                    self.frame.grid(row=row, column=column, sticky='wens')
                else:
                    self.frame.grid()

            def remove_point(self):
                self.frame.grid_remove()

        class Point_date:
            def __init__(self, root, labelframe_text, heading, fonts, bold_var, bold_italic, bold_underline,
                         format_day, format_day_bold_var, format_day_bold_italic, format_day_bold_underline,
                         format_month, format_month_bold_var, format_month_bold_italic, format_month_bold_underline,
                         format_year, format_year_bold_var, format_year_bold_italic, format_year_bold_underline):

                self.frame = tkinter.LabelFrame(root, text=f'{labelframe_text}')
                self.frame_text = tkinter.Frame(self.frame)
                self.label_text = tkinter.Label(self.frame_text, text=f'{heading}')
                self.text_content = tkinter.Text(self.frame_text, height=8, width=50, wrap='word')
                self.label_text.grid(row=0, column=0)
                self.text_content.grid(row=1, column=0)

                self.frame_customization = tkinter.Frame(self.frame)
                self.frame_font = tkinter.Frame(self.frame_customization)
                self.label_font = tkinter.Label(self.frame_font, text='Шрифт:')
                self.combobox_font = ttk.Combobox(self.frame_font, width=25, values=fonts)
                self.label_size = tkinter.Label(self.frame_font, text='Размер:')
                self.spinbox_size = ttk.Spinbox(self.frame_font, width=3, from_=0.0, to=999.0)
                self.frame_font.grid(row=0, column=0)
                self.label_font.grid(row=0, column=0, sticky='w')
                self.combobox_font.grid(row=0, column=1, sticky='w')
                self.label_size.grid(row=0, column=2, sticky='e')
                self.spinbox_size.grid(row=0, column=3, sticky='e')

                self.frame_checkbutton = tkinter.Frame(self.frame_customization)
                self.bold_var = tkinter.BooleanVar(value=bold_var)
                self.checkbutton_bold = tkinter.Checkbutton(self.frame_checkbutton, text='Полужирный',
                                                            offvalue=False, onvalue=True, variable=self.bold_var)
                self.italic_var = tkinter.BooleanVar(value=bold_italic)
                self.checkbutton_italic = tkinter.Checkbutton(self.frame_checkbutton, text='Курсив',
                                                              offvalue=False, onvalue=True, variable=self.italic_var)
                self.underline_var = tkinter.BooleanVar(value=bold_underline)
                self.checkbutton_underline = tkinter.Checkbutton(self.frame_checkbutton, text='Подчеркнутый',
                                                                 offvalue=False, onvalue=True,
                                                                 variable=self.underline_var)
                self.frame_checkbutton.grid(row=2, column=0)
                self.checkbutton_bold.grid(row=0, column=0)
                self.checkbutton_italic.grid(row=0, column=1)
                self.checkbutton_underline.grid(row=0, column=2)

                self.frame_symbols = tkinter.Frame(self.frame)
                self.label_symbols_before_date = tkinter.Label(self.frame_symbols, text='Символы перед датой:')
                self.entry_symbols_before_date = tkinter.Entry(self.frame_symbols, width=3)
                self.label_symbols_after_day = tkinter.Label(self.frame_symbols, text='Символы после дня:')
                self.entry_symbols_after_day = tkinter.Entry(self.frame_symbols, width=3)
                self.label_symbols_after_month = tkinter.Label(self.frame_symbols, text='Символы после месяца:')
                self.entry_symbols_after_month = tkinter.Entry(self.frame_symbols, width=3)
                self.label_symbols_after_year = tkinter.Label(self.frame_symbols, text='Символы после года:')
                self.entry_symbols_after_year = tkinter.Entry(self.frame_symbols, width=3)

                self.label_symbols_before_date.grid(row=0, column=0, sticky='e')
                self.entry_symbols_before_date.grid(row=0, column=1, sticky='w')
                self.label_symbols_after_day.grid(row=1, column=0, sticky='e')
                self.entry_symbols_after_day.grid(row=1, column=1, sticky='w')
                self.label_symbols_after_month.grid(row=2, column=0, sticky='e')
                self.entry_symbols_after_month.grid(row=2, column=1, sticky='w')
                self.label_symbols_after_year.grid(row=3, column=0, sticky='e')
                self.entry_symbols_after_year.grid(row=3, column=1, sticky='W')

                self.frame_elements_date = tkinter.Frame(self.frame)
                self.sep = ttk.Separator(self.frame_elements_date)
                self.sep.grid(row=0, column=0, sticky='we', pady=2)
                self.frame_format_day = tkinter.Frame(self.frame_elements_date)
                self.label_format_day = tkinter.Label(self.frame_format_day, text='Формат дня:')
                self.combobox_format_day = ttk.Combobox(self.frame_format_day, width=25, values=format_day)
                self.label_format_day.grid(row=0, column=0, sticky='e')
                self.combobox_format_day.grid(row=0, column=1, sticky='e')
                self.format_day_frame_checkbutton = tkinter.Frame(self.frame_elements_date)
                self.format_day_bold_var = tkinter.BooleanVar(value=format_day_bold_var)
                self.format_day_checkbutton_bold = tkinter.Checkbutton(self.format_day_frame_checkbutton,
                                                                       text='Полужирный',
                                                                       offvalue=False, onvalue=True,
                                                                       variable=self.format_day_bold_var)
                self.format_day_italic_var = tkinter.BooleanVar(value=format_day_bold_italic)
                self.format_day_checkbutton_italic = tkinter.Checkbutton(self.format_day_frame_checkbutton,
                                                                         text='Курсив',
                                                                         offvalue=False, onvalue=True,
                                                                         variable=self.format_day_italic_var)
                self.format_day_underline_var = tkinter.BooleanVar(value=format_day_bold_underline)
                self.format_day_checkbutton_underline = tkinter.Checkbutton(self.format_day_frame_checkbutton,
                                                                            text='Подчеркнутый',
                                                                            offvalue=False, onvalue=True,
                                                                            variable=self.format_day_underline_var)
                self.format_day_checkbutton_bold.grid(row=0, column=0)
                self.format_day_checkbutton_italic.grid(row=0, column=1)
                self.format_day_checkbutton_underline.grid(row=0, column=2)
                self.frame_format_day.grid(row=1, column=0)
                self.format_day_frame_checkbutton.grid(row=2, column=0)

                self.frame_format_month = tkinter.Frame(self.frame_elements_date)
                self.label_format_month = tkinter.Label(self.frame_format_month, text='Формат месяца:')
                self.combobox_format_month = ttk.Combobox(self.frame_format_month, width=25, values=format_month)
                self.label_format_month.grid(row=0, column=0, sticky='e')
                self.combobox_format_month.grid(row=0, column=1, sticky='e')
                self.format_month_frame_checkbutton = tkinter.Frame(self.frame_elements_date)
                self.format_month_bold_var = tkinter.BooleanVar(value=format_month_bold_var)
                self.format_month_checkbutton_bold = tkinter.Checkbutton(self.format_month_frame_checkbutton,
                                                                         text='Полужирный',
                                                                         offvalue=False, onvalue=True,
                                                                         variable=self.format_month_bold_var)
                self.format_month_italic_var = tkinter.BooleanVar(value=format_month_bold_italic)
                self.format_month_checkbutton_italic = tkinter.Checkbutton(self.format_month_frame_checkbutton,
                                                                           text='Курсив',
                                                                           offvalue=False, onvalue=True,
                                                                           variable=self.format_month_italic_var)
                self.format_month_underline_var = tkinter.BooleanVar(value=format_month_bold_underline)
                self.format_month_checkbutton_underline = tkinter.Checkbutton(self.format_month_frame_checkbutton,
                                                                              text='Подчеркнутый',
                                                                              offvalue=False, onvalue=True,
                                                                              variable=self.format_month_underline_var)
                self.format_month_checkbutton_bold.grid(row=0, column=0)
                self.format_month_checkbutton_italic.grid(row=0, column=1)
                self.format_month_checkbutton_underline.grid(row=0, column=2)
                self.frame_format_month.grid(row=3, column=0)
                self.format_month_frame_checkbutton.grid(row=4, column=0)

                self.frame_format_year = tkinter.Frame(self.frame_elements_date)
                self.label_format_year = tkinter.Label(self.frame_format_year, text='Формат года:')
                self.combobox_format_year = ttk.Combobox(self.frame_format_year, width=25, values=format_year)
                self.label_format_year.grid(row=0, column=0, sticky='e')
                self.combobox_format_year.grid(row=0, column=1, sticky='e')
                self.format_year_frame_checkbutton = tkinter.Frame(self.frame_elements_date)
                self.format_year_bold_var = tkinter.BooleanVar(value=format_year_bold_var)
                self.format_year_checkbutton_bold = tkinter.Checkbutton(self.format_year_frame_checkbutton,
                                                                        text='Полужирный',
                                                                        offvalue=False, onvalue=True,
                                                                        variable=self.format_year_bold_var)
                self.format_year_italic_var = tkinter.BooleanVar(value=format_year_bold_italic)
                self.format_year_checkbutton_italic = tkinter.Checkbutton(self.format_year_frame_checkbutton,
                                                                          text='Курсив',
                                                                          offvalue=False, onvalue=True,
                                                                          variable=self.format_year_italic_var)
                self.format_year_underline_var = tkinter.BooleanVar(value=format_year_bold_underline)
                self.format_year_checkbutton_underline = tkinter.Checkbutton(self.format_year_frame_checkbutton,
                                                                             text='Подчеркнутый',
                                                                             offvalue=False, onvalue=True,
                                                                             variable=self.format_year_underline_var)
                self.format_year_checkbutton_bold.grid(row=0, column=0)
                self.format_year_checkbutton_italic.grid(row=0, column=1)
                self.format_year_checkbutton_underline.grid(row=0, column=2)
                self.frame_format_year.grid(row=5, column=0)
                self.format_year_frame_checkbutton.grid(row=6, column=0)

                self.frame_text.grid(row=0, column=0, rowspan=3)
                self.frame_customization.grid(row=0, column=1)
                self.frame_symbols.grid(row=1, column=1)
                self.frame_elements_date.grid(row=2, column=1)

            def grid(self, row=None, column=None):
                if row is not None:
                    self.frame.grid(row=row, column=column, sticky='wens')
                else:
                    self.frame.grid()

            def remove_point(self):
                self.frame.grid_remove()

        class Point_explanation_date_and_number(Point_format):
            def __init__(self, root, labelframe_text, heading, heading2, fonts, paragraph_var, alignment, bold_var,
                         bold_italic, bold_underline):
                Point_format.__init__(self, root, labelframe_text, heading, fonts, paragraph_var, alignment, bold_var,
                                      bold_italic, bold_underline)
                self.label_text2 = tkinter.Label(self.frame_text, text=f'{heading2}')
                self.text_content.config(height=3)
                self.text_content2 = tkinter.Text(self.frame_text, height=3, width=50, wrap='word')
                self.label_text2.grid(row=2, column=0)
                self.text_content2.grid(row=3, column=0)

        class Point_date_act_general:
            def __init__(self, root, tab_underline_num, off_tab_num_first, tab_underline_date):
                self.frame = tkinter.LabelFrame(root, text='Общие параметры пункта')
                self.frame_format = tkinter.Frame(self.frame)

                self.tab_underline_num = tkinter.BooleanVar(value=tab_underline_num)
                self.checkbutton_tab_underline_num = tkinter.Checkbutton(self.frame_format,
                                                                         text='Табличное подчеркивание номера',
                                                                         offvalue=False, onvalue=True,
                                                                         variable=self.tab_underline_num)
                self.off_tab_num_first = tkinter.BooleanVar(value=off_tab_num_first)
                self.checkbutton_off_tab_num_first = tkinter.Checkbutton(self.frame_format,
                                                                         text='- Не подчеркивать начальные символы номера',
                                                                         offvalue=False, onvalue=True,
                                                                         variable=self.off_tab_num_first)

                self.tab_underline_date = tkinter.BooleanVar(value=tab_underline_date)
                self.checkbutton_tab_underline_date = tkinter.Checkbutton(self.frame_format,
                                                                          text='Табличное подчеркивание даты',
                                                                          offvalue=False, onvalue=True,
                                                                          variable=self.tab_underline_date)
                self.checkbutton_tab_underline_num.grid(row=0, column=0, sticky='w')
                self.checkbutton_off_tab_num_first.grid(row=1, column=0, sticky='w')
                self.checkbutton_tab_underline_date.grid(row=2, column=0, sticky='w')
                self.frame_format.grid(row=0, column=0)

            def grid(self, row=None, column=None):
                if row is not None:
                    self.frame.grid(row=row, column=column, sticky='wens')
                else:
                    self.frame.grid()

            def remove_point(self):
                self.frame.grid_remove()

        class Point_project_documentation(Point_format_content):
            def __init__(self, root, labelframe_text, heading, fonts, paragraph_var, alignment, bold_var,
                         bold_italic, bold_underline, list_text, num_var, page_format):
                Point_format_content.__init__(self, root, labelframe_text, heading, fonts, paragraph_var, alignment,
                                              bold_var, bold_italic, bold_underline, list_text, num_var)

                self.text_content.config(height=9)
                self.frame_text.grid_remove()
                self.frame_text.grid(row=0, column=0, rowspan=1)

                self.frame_psd = tkinter.Frame(self.frame)
                self.label_symbols_after_organization = tkinter.Label(self.frame_psd, text='Символы после организации:')
                self.entry_symbols_after_organization = tkinter.Entry(self.frame_psd, width=3)
                self.label_symbols_after_document = tkinter.Label(self.frame_psd, text='Символы после наименования:')
                self.entry_symbols_after_document = tkinter.Entry(self.frame_psd, width=3)
                self.label_symbols_before_pages = tkinter.Label(self.frame_psd, text='Символы после всех номеров:')
                self.entry_symbols_before_pages = tkinter.Entry(self.frame_psd, width=3)

                self.frame_page_format = tkinter.Frame(self.frame_psd)
                self.page_format = tkinter.StringVar(value=page_format)
                self.element_radiobutton = tkinter.Radiobutton(self.frame_psd, text='полный список номеров',
                                                               value='ELEMENT', variable=self.page_format)
                self.general_radiobutton = tkinter.Radiobutton(self.frame_psd, text='сокращеный список номеров',
                                                               value='GENERAL', variable=self.page_format)

                self.label_symbols_before_page = tkinter.Label(self.frame_psd, text='Символы до номера листа:')
                self.entry_symbols_before_page = tkinter.Entry(self.frame_psd, width=3)
                self.label_symbols_after_page = tkinter.Label(self.frame_psd, text='Символы после номера листа:')
                self.entry_symbols_after_page = tkinter.Entry(self.frame_psd, width=3)

                self.label_symbols_after_organization.grid(row=0, column=0, sticky='e')
                self.entry_symbols_after_organization.grid(row=0, column=1, sticky='w')
                self.label_symbols_after_document.grid(row=1, column=0, sticky='e')
                self.entry_symbols_after_document.grid(row=1, column=1, sticky='w')
                self.label_symbols_before_pages.grid(row=2, column=0, sticky='e')
                self.entry_symbols_before_pages.grid(row=2, column=1, sticky='w')
                self.element_radiobutton.grid(row=3, column=0, sticky='w')
                self.general_radiobutton.grid(row=3, column=1, sticky='e')
                self.label_symbols_before_page.grid(row=4, column=0, sticky='e')
                self.entry_symbols_before_page.grid(row=4, column=1, sticky='w')
                self.label_symbols_after_page.grid(row=5, column=0, sticky='e')
                self.entry_symbols_after_page.grid(row=5, column=1, sticky='w')

                self.frame_psd.grid(row=1, column=0)

        class Point_deadline(Point_date):
            def __init__(self, root, labelframe_text, heading, fonts, bold_var, bold_italic, bold_underline,
                         format_day, format_day_bold_var, format_day_bold_italic, format_day_bold_underline,
                         format_month, format_month_bold_var, format_month_bold_italic, format_month_bold_underline,
                         format_year, format_year_bold_var, format_year_bold_italic, format_year_bold_underline,
                         bold_start, italic_start, underline_start, bold_finish, italic_finish, underline_finish):
                Point_date.__init__(self, root, labelframe_text, heading, fonts, bold_var, bold_italic, bold_underline,
                                    format_day, format_day_bold_var, format_day_bold_italic, format_day_bold_underline,
                                    format_month, format_month_bold_var, format_month_bold_italic,
                                    format_month_bold_underline,
                                    format_year, format_year_bold_var, format_year_bold_italic,
                                    format_year_bold_underline)

                self.frame_start = tkinter.Frame(self.frame_text)
                self.frame_font_start = tkinter.Frame(self.frame_start)
                self.label_font_start = tkinter.Label(self.frame_font_start, text='Шрифт:')
                self.combobox_font_start = ttk.Combobox(self.frame_font_start, width=25, values=fonts)
                self.label_size_start = tkinter.Label(self.frame_font_start, text='Размер:')
                self.spinbox_size_start = ttk.Spinbox(self.frame_font_start, width=3, from_=0.0, to=999.0)
                self.frame_font_start.grid(row=0, column=0)
                self.label_font_start.grid(row=0, column=0, sticky='w')
                self.combobox_font_start.grid(row=0, column=1, sticky='w')
                self.label_size_start.grid(row=0, column=2, sticky='e')
                self.spinbox_size_start.grid(row=0, column=3, sticky='e')

                self.frame_checkbutton_start = tkinter.Frame(self.frame_start)
                self.bold_var_start = tkinter.BooleanVar(value=bold_start)
                self.checkbutton_bold_start = tkinter.Checkbutton(self.frame_checkbutton_start, text='Полужирный',
                                                                  offvalue=False, onvalue=True,
                                                                  variable=self.bold_var_start)
                self.italic_var_start = tkinter.BooleanVar(value=italic_start)
                self.checkbutton_italic_start = tkinter.Checkbutton(self.frame_checkbutton_start, text='Курсив',
                                                                    offvalue=False, onvalue=True,
                                                                    variable=self.italic_var_start)
                self.underline_var_start = tkinter.BooleanVar(value=underline_start)
                self.checkbutton_underline_start = tkinter.Checkbutton(self.frame_checkbutton_start,
                                                                       text='Подчеркнутый',
                                                                       offvalue=False, onvalue=True,
                                                                       variable=self.underline_var_start)
                self.frame_checkbutton_start.grid(row=1, column=0)
                self.checkbutton_bold_start.grid(row=0, column=0)
                self.checkbutton_italic_start.grid(row=0, column=1)
                self.checkbutton_underline_start.grid(row=0, column=2)

                self.frame_text_start = tkinter.Frame(self.frame_start)
                self.label_text_start = tkinter.Label(self.frame_text_start, text='Текст перед датой начала:')
                self.entry_start = tkinter.Entry(self.frame_text_start, width=37)
                self.frame_text_start.grid(row=2, column=0)
                self.label_text_start.grid(row=0, column=0, sticky='w')
                self.entry_start.grid(row=0, column=1, sticky='e')

                self.frame_finish = tkinter.Frame(self.frame_text)
                self.frame_font_finish = tkinter.Frame(self.frame_finish)
                self.label_font_finish = tkinter.Label(self.frame_font_finish, text='Шрифт:')
                self.combobox_font_finish = ttk.Combobox(self.frame_font_finish, width=25, values=fonts)
                self.label_size_finish = tkinter.Label(self.frame_font_finish, text='Размер:')
                self.spinbox_size_finish = ttk.Spinbox(self.frame_font_finish, width=3, from_=0.0, to=999.0)
                self.frame_font_finish.grid(row=0, column=0)
                self.label_font_finish.grid(row=0, column=0, sticky='w')
                self.combobox_font_finish.grid(row=0, column=1, sticky='w')
                self.label_size_finish.grid(row=0, column=2, sticky='e')
                self.spinbox_size_finish.grid(row=0, column=3, sticky='e')

                self.frame_checkbutton_finish = tkinter.Frame(self.frame_finish)
                self.bold_var_finish = tkinter.BooleanVar(value=bold_finish)
                self.checkbutton_bold_finish = tkinter.Checkbutton(self.frame_checkbutton_finish, text='Полужирный',
                                                                   offvalue=False, onvalue=True,
                                                                   variable=self.bold_var_finish)
                self.italic_var_finish = tkinter.BooleanVar(value=italic_finish)
                self.checkbutton_italic_finish = tkinter.Checkbutton(self.frame_checkbutton_finish, text='Курсив',
                                                                     offvalue=False, onvalue=True,
                                                                     variable=self.italic_var_finish)
                self.underline_var_finish = tkinter.BooleanVar(value=underline_finish)
                self.checkbutton_underline_finish = tkinter.Checkbutton(self.frame_checkbutton_finish,
                                                                        text='Подчеркнутый',
                                                                        offvalue=False, onvalue=True,
                                                                        variable=self.underline_var_finish)
                self.frame_checkbutton_finish.grid(row=1, column=0)
                self.checkbutton_bold_finish.grid(row=0, column=0)
                self.checkbutton_italic_finish.grid(row=0, column=1)
                self.checkbutton_underline_finish.grid(row=0, column=2)

                self.frame_text_finish = tkinter.Frame(self.frame_finish)
                self.label_text_finish = tkinter.Label(self.frame_text_finish, text='Текст перед датой окончания:')
                self.entry_finish = tkinter.Entry(self.frame_text_finish, width=37)
                self.frame_text_finish.grid(row=2, column=0)
                self.label_text_finish.grid(row=0, column=0, sticky='w')
                self.entry_finish.grid(row=0, column=1, sticky='e')

                self.frame_start.grid(row=2, column=0, pady=5)
                self.frame_finish.grid(row=3, column=0)

        class Point_deadline_general:
            def __init__(self, root, heading_row, content_format, line_date):
                self.frame = ttk.LabelFrame(root,  text='Общие параметры пункта')
                self.heading_row = tkinter.BooleanVar(value=heading_row)
                self.checkbutton_heading_row = tkinter.Checkbutton(self.frame,
                                                                       text='Заголовок и содержание в одну строку',
                                                                       offvalue=False, onvalue=True,
                                                                       variable=self.heading_row)
                self.content_format = tkinter.StringVar(value=content_format)
                self.row_radiobutton = tkinter.Radiobutton(self.frame, text='Даты в строку',
                                                               value='ROW', variable=self.content_format)
                self.column_radiobutton = tkinter.Radiobutton(self.frame, text='Даты в колонку',
                                                               value='COLUMN', variable=self.content_format)
                self.line_date = tkinter.BooleanVar(value=line_date)
                self.checkbutton_table_line_date = tkinter.Checkbutton(self.frame,
                                                                       text='Табличное подчеркивание даты',
                                                                       offvalue=False, onvalue=True,
                                                                       variable=self.line_date)
                self.checkbutton_heading_row.grid(row=0, column=0, sticky='w')
                self.row_radiobutton.grid(row=1, column=0, sticky='w')
                self.column_radiobutton.grid(row=2, column=0, sticky='w')
                self.checkbutton_table_line_date.grid(row=3, column=0, sticky='w')

            def grid(self, row=None, column=None):
                if row is not None:
                    self.frame.grid(row=row, column=column, sticky='wens')
                else:
                    self.frame.grid()

            def remove_point(self):
                self.frame.grid_remove()

        class Point_numbers_of_copies(Point_format):
            def __init__(self, root, labelframe_text, heading, fonts, paragraph_var, alignment, bold_var, bold_italic,
                         bold_underline):
                Point_format.__init__(self, root, labelframe_text, heading, fonts, paragraph_var, alignment, bold_var, bold_italic,
                         bold_underline)
                self.frame_copy = tkinter.Frame(self.frame)
                self.sep = ttk.Separator(self.frame_copy, orient='horizontal')
                self.label_copy = tkinter.Label(self.frame_copy, text='Кол-во экземпляров:')
                self.spinbox_copy = ttk.Spinbox(self.frame_copy, width=3, from_=1, to=999)
                self.label_after_symbol = tkinter.Label(self.frame_copy, text='Символы до кол-во\nэкземпляров:')
                self.entry_after_symbol = tkinter.Entry(self.frame_copy, width=20)
                self.label_before_symbol = tkinter.Label(self.frame_copy, text='Символы после кол-во\nэкземпляров:')
                self.entry_before_symbol = tkinter.Entry(self.frame_copy, width=20)

                self.sep.grid(row=0, column=0, columnspan=2, sticky='we', pady=3)
                self.label_copy.grid(row=1, column=0, sticky='e')
                self.spinbox_copy.grid(row=1, column=1, sticky='w')
                self.label_after_symbol.grid(row=2, column=0, sticky='e')
                self.entry_after_symbol.grid(row=2, column=1, sticky='w')
                self.label_before_symbol.grid(row=3, column=0, sticky='e')
                self.entry_before_symbol.grid(row=3, column=1, sticky='w')
                self.frame_copy.grid(row=3, column=1)

        class Point_appendices(Point_format_content):
            def __init__(self, root, labelframe_text, heading, fonts, paragraph_var, alignment, bold_var,
                         bold_italic, bold_underline, list_text, num_var, materials, documents, first_content, type_text):
                Point_format_content.__init__(self, root, labelframe_text, heading, fonts, paragraph_var, alignment,
                                              bold_var, bold_italic, bold_underline, list_text, num_var)

                self.text_content.config(height=9)
                self.frame_text.grid_remove()
                self.frame_text.grid(row=0, column=0, rowspan=1)

                self.frame_appendices = tkinter.Frame(self.frame)

                self.content_app_frame = tkinter.Frame(self.frame_appendices)
                self.content_app_label = tkinter.Label(self.content_app_frame, text='Добавить в приложение:')
                self.materials = tkinter.BooleanVar(value=materials)
                self.checkbutton_materials = tkinter.Checkbutton(self.content_app_frame,
                                                                  text='- материалы',
                                                                  offvalue=False, onvalue=True,
                                                                  variable=self.materials)
                self.documents = tkinter.BooleanVar(value=documents)
                self.checkbutton_documents = tkinter.Checkbutton(self.content_app_frame,
                                                                 text='- документы соответствия работ',
                                                                 offvalue=False, onvalue=True,
                                                                 variable=self.documents)

                self.first_content_label = tkinter.Label(self.content_app_frame, text='Добавить первым в приложения:')
                self.first_content = tkinter.StringVar(value=first_content)
                self.first_materials_radiobutton = tkinter.Radiobutton(self.content_app_frame, text='- материалы',
                                                               value='MATERIALS', variable=self.first_content)
                self.first_documents_radiobutton = tkinter.Radiobutton(self.content_app_frame, text='- документы соответствия работ',
                                                               value='DOCUMENTS', variable=self.first_content)

                self.type_text_frame = tkinter.Frame(self.frame_appendices)
                self.type_text_label = tkinter.Label(self.type_text_frame, text='Вариант текста:')
                self.type_text = tkinter.StringVar(value=type_text)
                self.full_text_radiobutton = tkinter.Radiobutton(self.type_text_frame, text='- полный',
                                                                       value='FULL', variable=self.type_text)
                self.short_text_radiobutton = tkinter.Radiobutton(self.type_text_frame,
                                                                       text='- сократить',
                                                                       value='SHORT', variable=self.type_text)
                self.order_short_text_radiobutton = tkinter.Radiobutton(self.type_text_frame,
                                                                      text='- упорядочить и сократить',
                                                                      value='ORDER_SHORT', variable=self.type_text)

                self.content_app_label.grid(row=0, column=0, columnspan=2, sticky='w')
                self.checkbutton_materials.grid(row=1, column=0, sticky='w')
                self.checkbutton_documents.grid(row=1, column=1, sticky='w')
                self.first_content_label.grid(row=2, column=0, columnspan=2, sticky='w')
                self.first_materials_radiobutton.grid(row=3, column=0, sticky='w')
                self.first_documents_radiobutton.grid(row=3, column=1, sticky='w')
                self.content_app_frame.grid(row=0, column=0, sticky='wens')

                self.type_text_label.grid(row=0, column=0, columnspan=3, sticky='w')
                self.full_text_radiobutton.grid(row=1, column=0, sticky='w')
                self.short_text_radiobutton.grid(row=1, column=1, sticky='w')
                self.order_short_text_radiobutton.grid(row=1, column=2, sticky='w')
                self.type_text_frame.grid(row=1, column=0, sticky='wens')

                self.frame_appendices.grid(row=1, column=0)

        class Point_signature:
            def __init__(self, root, var_row, double_explanation):
                self.frame = tkinter.LabelFrame(root, text='Общие параментры пункта')
                self.var_row_label = tkinter.Label(self.frame, text='Представитель и подпись:')
                self.var_row = tkinter.StringVar(value=var_row)
                self.radiobutton_one_area = tkinter.Radiobutton(self.frame, text='- Одним полем',
                                                           value='ONE', variable=self.var_row)
                self.radiobutton_two_area = tkinter.Radiobutton(self.frame, text='- Разделить на два поля',
                                                              value='TWO', variable=self.var_row)

                self.double_explanation = tkinter.BooleanVar(value=double_explanation)
                self.checkbutton_table_line = tkinter.Checkbutton(self.frame,
                                                                   text='Разделить пояснение',
                                                                   offvalue=False, onvalue=True,
                                                                   variable=self.double_explanation)
                self.var_row_label.grid(row=0, column=0, sticky='w')
                self.radiobutton_one_area.grid(row=1, column=0, sticky='w')
                self.radiobutton_two_area.grid(row=2, column=0, sticky='w')
                self.checkbutton_table_line.grid(row=3, column=0, sticky='w')

            def grid(self, row=None, column=None):
                if row is not None:
                    self.frame.grid(row=row, column=column, sticky='wens')
                else:
                    self.frame.grid()

            def remove_point(self):
                self.frame.grid_remove()


        self.gui_point_dict = dict({'Наименование объекта': (
            Point_format(self.window, 'Заголовок пункта', 'Содержание заголовка наименования объекта',
                         self.__font, True, 'LEFT', True, False, False),
            Point_format_content(self.window, 'Содержание пункта', 'Содержание наименования объекта',
                                 self.__font, True, 'LEFT', False, False,
                                 False, 'ROW', False),
            Point_format(self.window, 'Пояснение к пункту', 'Содержание пояснения к наименованию объекта',
                         self.__font, True, 'LEFT', False, True, False),
            Point_general(self.window, False, False, 'CONTENT', False, False)),
            'Застройщик': (
                Point_format(self.window, 'Заголовок пункта', 'Заголовок пункта "Застройщик"',
                             self.__font, True, 'LEFT', True, False, False),
                Point_format_content(self.window, 'Содержание пункта', 'Содержания пункта "Застройщик"',
                                     self.__font, True, 'LEFT', False, False,
                                     False, 'ROW', False),
                Point_format(self.window, 'Пояснение к пункту', 'Содержание пояснения пункта "Застройщик"',
                             self.__font, True, 'LEFT', False, True, False),
                Point_general(self.window, False, False, 'CONTENT', False, False)),
            'Строитель': (
                Point_format(self.window, 'Заголовок пункта', 'Заголовок пункта "Строитель"',
                             self.__font, True, 'LEFT', True, False, False),
                Point_format_content(self.window, 'Содержание пункта', 'Содержания пункта "Строитель"',
                                     self.__font, True, 'LEFT', False, False,
                                     False, 'ROW', False),
                Point_format(self.window, 'Пояснение к пункту', 'Содержание пояснения пункта "Строитель"',
                             self.__font, True, 'LEFT', False, True, False),
                Point_general(self.window, False, False, 'CONTENT', False, False)),
            'Проектная организация': (
                Point_format(self.window, 'Заголовок пункта', 'Заголовок пункта "Проектная организация"',
                             self.__font, True, 'LEFT', True, False, False),
                Point_format_content(self.window, 'Содержание пункта', 'Содержания пункта "Проектная организация"',
                                     self.__font, True, 'LEFT', False, False,
                                     False, 'ROW', False),
                Point_format(self.window, 'Пояснение к пункту', 'Содержание пояснения пункта "Проектная организация"',
                             self.__font, True, 'LEFT', False, True, False),
                Point_general(self.window, False, False, 'CONTENT', False, False)),
            'Наименование документа': (
                Point_format(self.window, 'Наименование документа, певая строка', 'Содержание первой строки',
                             self.__font, True, 'LEFT', False, False, False),
                Point_format(self.window, 'Наименование документа, вторая строка', 'Содержание второй строки',
                             self.__font, True, 'LEFT', False, False, False)),
            'Номер акта и дата': (
                Point_number_akt(self.window, self.__font, False, False, False),
                Point_date(self.window, 'Содержание пункта', 'Содержание даты акта', self.__font, False, False, False, self.__format_day,
                           False, False, False, self.__format_month,
                           False, False, False, self.__format_year,
                           False, False, False),
                Point_explanation_date_and_number(self.window, 'Пояснение к пункту',
                                                  'Содержание пояснения пункта "Номер акта"',
                                                  'Содержание пояснения пункта "Дата составления акта"', self.__font,
                                                  True, 'LEFT', False, True, False),
                Point_date_act_general(self.window, False, False, False)),
            'Представитель застройщика': (
                Point_format(self.window, 'Заголовок пункта', 'Заголовок пункта "Представитель застройщика"',
                             self.__font, True, 'LEFT', True, False, False),
                Point_format_content(self.window, 'Содержание пункта', 'Содержания пункта "Представитель застройщика"',
                                     self.__font, True, 'LEFT', False, False,
                                     False, 'ROW', False),
                Point_format(self.window, 'Пояснение к пункту',
                             'Содержание пояснения пункта "Представитель застройщика"',
                             self.__font, True, 'LEFT', False, True, False),
                Point_general(self.window, False, False, 'CONTENT', False, False)),
            'Представитель строителя': (
                Point_format(self.window, 'Заголовок пункта', 'Заголовок пункта "Представитель строителя"',
                             self.__font, True, 'LEFT', True, False, False),
                Point_format_content(self.window, 'Содержание пункта', 'Содержания пункта "Представитель строителя"',
                                     self.__font, True, 'LEFT', False, False,
                                     False, 'ROW', False),
                Point_format(self.window, 'Пояснение к пункту', 'Содержание пояснения пункта "Представитель строителя"',
                             self.__font, True, 'LEFT', False, True, False),
                Point_general(self.window, False, False, 'CONTENT', False, False)),
            'Представитель строителя (контроль)': (
                Point_format(self.window, 'Заголовок пункта', 'Заголовок пункта "Представитель строителя (контроль)"',
                             self.__font, True, 'LEFT', True, False, False),
                Point_format_content(self.window, 'Содержание пункта',
                                     'Содержания пункта "Представитель строителя (контроль)"',
                                     self.__font, True, 'LEFT', False, False,
                                     False, 'ROW', False),
                Point_format(self.window, 'Пояснение к пункту',
                             'Содержание пояснения пункта "Представитель строителя (контроль)"',
                             self.__font, True, 'LEFT', False, True, False),
                Point_general(self.window, False, False, 'CONTENT', False, False)),
            'Представитель проектной организации': (
                Point_format(self.window, 'Заголовок пункта', 'Заголовок пункта "Представитель проектной организации"',
                             self.__font, True, 'LEFT', True, False, False),
                Point_format_content(self.window, 'Содержание пункта',
                                     'Содержания пункта "Представитель проектной организации"',
                                     self.__font, True, 'LEFT', False, False,
                                     False, 'ROW', False),
                Point_format(self.window, 'Пояснение к пункту',
                             'Содержание пояснения пункта "Представитель проектной организации"',
                             self.__font, True, 'LEFT', False, True, False),
                Point_general(self.window, False, False, 'CONTENT', False, False)),
            'Представитель исполнителя': (
                Point_format(self.window, 'Заголовок пункта', 'Заголовок пункта "Представитель исполнителя"',
                             self.__font, True, 'LEFT', True, False, False),
                Point_format_content(self.window, 'Содержание пункта', 'Содержания пункта "Представитель исполнителя"',
                                     self.__font, True, 'LEFT', False, False,
                                     False, 'ROW', False),
                Point_format(self.window, 'Пояснение к пункту',
                             'Содержание пояснения пункта "Представитель исполнителя"',
                             self.__font, True, 'LEFT', False, True, False),
                Point_general(self.window, False, False, 'CONTENT', False, False)),
            'Иные представители': (
                Point_format(self.window, 'Заголовок пункта', 'Заголовок пункта "Иные представители"',
                             self.__font, True, 'LEFT', True, False, False),
                Point_format_content(self.window, 'Содержание пункта', 'Содержания пункта "Иные представители"',
                                     self.__font, True, 'LEFT', False, False,
                                     False, 'ROW', False),
                Point_format(self.window, 'Пояснение к пункту', 'Содержание пояснения пункта "Иные представители"',
                             self.__font, True, 'LEFT', False, True, False),
                Point_general(self.window, False, False, 'CONTENT', False, False)),
            'Исполнитель': (
                Point_format(self.window, 'Заголовок пункта', 'Заголовок пункта "Исполнитель"',
                             self.__font, True, 'LEFT', True, False, False),
                Point_format_content(self.window, 'Содержание пункта', 'Содержания пункта "Исполнитель"',
                                     self.__font, True, 'LEFT', False, False,
                                     False, 'ROW', False),
                Point_format(self.window, 'Пояснение к пункту', 'Содержание пояснения пункта "Исполнитель"',
                             self.__font, True, 'LEFT', False, True, False),
                Point_general(self.window, False, False, 'CONTENT', False, False)),
            '"и составили настоящий акт о нижеследующем:"': (
                Point_format(self.window, 'Текст, певая строка', 'Содержание первой строки',
                             self.__font, True, 'LEFT', False, False, False),),
            '1. Наименования работ': (
                Point_format(self.window, 'Заголовок пункта', 'Заголовок пункта "Наименования работ"',
                             self.__font, True, 'LEFT', True, False, False),
                Point_format_content(self.window, 'Содержание пункта', 'Содержания пункта "Наименования работ"',
                                     self.__font, True, 'LEFT', False, False,
                                     False, 'ROW', False),
                Point_format(self.window, 'Пояснение к пункту', 'Содержание пояснения пункта "Наименования работ"',
                             self.__font, True, 'LEFT', False, True, False),
                Point_general(self.window, False, False, 'CONTENT', False, False)),
            '2. Проектно-сметная документация': (
                Point_format(self.window, 'Заголовок пункта', 'Заголовок пункта "Проектно-сметная документация"',
                             self.__font, True, 'LEFT', True, False, False),
                Point_project_documentation(self.window, 'Содержание пункта',
                                            'Содержание пункта "Проектно-сметная документация"',
                                            self.__font, True, 'LEFT', False,
                                            False, False, 'ROW', False, 'GENERAL'),
                Point_format(self.window, 'Пояснение к пункту',
                             'Содержание пояснения пункта "Проектно-сметная документация"',
                             self.__font, True, 'LEFT', False, True, False),
                Point_general(self.window, False, False, 'CONTENT', False, False)),
            '3. Материалы/оснастка': (
                Point_format(self.window, 'Заголовок пункта', 'Заголовок пункта "Материалы/оснастка"',
                             self.__font, True, 'LEFT', True, False, False),
                Point_format_content(self.window, 'Содержание пункта', 'Содержания пункта "Материалы/оснастка"',
                                     self.__font, True, 'LEFT', False, False,
                                     False, 'ROW', False),
                Point_format(self.window, 'Пояснение к пункту', 'Содержание пояснения пункта "Материалы/оснастка"',
                             self.__font, True, 'LEFT', False, True, False),
                Point_general(self.window, False, False, 'CONTENT', False, False)),
            '4. Документы потверждающие соответсвия работ': (
                Point_format(self.window, 'Заголовок пункта',
                             'Заголовок пункта "Документы потверждающие соответсвие работ"',
                             self.__font, True, 'LEFT', True, False, False),
                Point_format_content(self.window, 'Содержание пункта',
                                     'Содержания пункта "Документы потверждающие соответсвие работ"',
                                     self.__font, True, 'LEFT', False, False,
                                     False, 'ROW', False),
                Point_format(self.window, 'Пояснение к пункту',
                             'Содержание пояснения пункта "Документы потверждающие соответсвие работ"',
                             self.__font, True, 'LEFT', False, True, False),
                Point_general(self.window, False, False, 'CONTENT', False, False)),
            '5. Дата': (
                Point_format(self.window, 'Заголовок пункта',
                             'Заголовок пункта "Сроки выполнения работ"',
                             self.__font, True, 'LEFT', True, False, False),
                Point_deadline(self.window, 'Сроки выполнения работ', 'Содержания дат выполнения работ', self.__font,
                               False, False, False, self.__format_day, False,
                               False, False, self.__format_month, False,
                               False, False, self.__format_year, False,
                               False, False, False, False,
                               False, False, False, False),
                Point_explanation_date_and_number(self.window, 'Пояснение к пункту',
                                                  'Содержание пояснения к "начала работ"',
                                                  'Содержание пояснения к "окончания работ"', self.__font,
                                                  True, 'LEFT', False, True, False),
                Point_deadline_general(self.window, False, 'COLUMN', True)),
            '6. Работы выполнены в соответсвии с': (
                Point_format(self.window, 'Заголовок пункта', 'Заголовок пункта "Документы соответсвия работ"',
                             self.__font, True, 'LEFT', True, False, False),
                Point_format_content(self.window, 'Содержание пункта',
                                     'Содержания пункта "Документы соответсвия работ"',
                                     self.__font, True, 'LEFT', False, False,
                                     False, 'ROW', False),
                Point_format(self.window, 'Пояснение к пункту',
                             'Содержание пояснения пункта "Документы соответсвия работ"',
                             self.__font, True, 'LEFT', False, True, False),
                Point_general(self.window, False, False, 'CONTENT', False, False)),
            '7. Последующие работы': (
                Point_format(self.window, 'Заголовок пункта', 'Заголовок пункта "Последующие работы"',
                             self.__font, True, 'LEFT', True, False, False),
                Point_format_content(self.window, 'Содержание пункта',
                                     'Содержания пункта "Последующие работы"',
                                     self.__font, True, 'LEFT', False, False,
                                     False, 'ROW', False),
                Point_format(self.window, 'Пояснение к пункту', 'Содержание пояснения пункта "Последующие работы"',
                             self.__font, True, 'LEFT', False, True, False),
                Point_general(self.window, False, False, 'CONTENT', False, False)),
            'Дополнительные сведения': (
                Point_format(self.window, 'Заголовок пункта', 'Заголовок пункта "Дополнительные сведения"',
                             self.__font, True, 'LEFT', True, False, False),
                Point_format_content(self.window, 'Содержание пункта',
                                     'Содержания пункта "Дополнительные сведения"',
                                     self.__font, True, 'LEFT', False, False,
                                     False, 'ROW', False),
                Point_format(self.window, 'Пояснение к пункту', 'Содержание пояснения пункта "Дополнительные сведения"',
                             self.__font, True, 'LEFT', False, True, False),
                Point_general(self.window, False, False, 'CONTENT', False, False)),
            'Кол-во экземпляров': (
                Point_format(self.window, 'Заголовок пункта', 'Заголовок пункта "кол-во экземпляров"',
                             self.__font, True, 'LEFT', True, False, False),
                Point_numbers_of_copies(self.window, 'Содержание пункта', 'Содержания пункта "Кол-во экземпляров"',
                                        self.__font, True, 'LEFT', True, False, False),
                Point_format(self.window, 'Пояснение к пункту', 'Содержание пояснения пункта "Кол-во экземпляров"',
                             self.__font, True, 'LEFT', False, True, False),
                Point_general(self.window, False, False, 'CONTENT', False, False)
            ),
            'Приложения': (
                Point_format(self.window, 'Заголовок пункта', 'Заголовок пункта "Приложения"',
                             self.__font, True, 'LEFT', True, False, False),
                Point_appendices(self.window, 'Содержание пункта', 'Содержания пункта "Приложения"',
                                 self.__font, True, 'LEFT', False, False, False,
                                 'ROW', False, False, True, 'DOCUMENTS','SHORT'),
                Point_format(self.window, 'Пояснение к пункту', 'Содержание пояснения пункта "Приложения"',
                             self.__font, True, 'LEFT', False, True, False),
                Point_general(self.window, False, False, 'CONTENT', False, False)
            ),
            'Подпись представителя застройщика': (
                Point_format(self.window, 'Заголовок пункта', 'Подпись представителя застройщика',
                             self.__font, True, 'LEFT', True, False, False),
                Point_format(self.window, 'Содеражание данных о представителе', 'Представитель',
                             self.__font, True, 'LEFT', True, False, False),
                Point_explanation_date_and_number(self.window, 'Пояснение к пункту',
                                                  'Содержание первого пояснения',
                                                  'Содержание второго пояснения', self.__font,
                                                  True, 'LEFT', False, True, False),
                Point_signature(self.window, 'ONE', True)
            ),
            'Подпись представителя строителя': (
                Point_format(self.window, 'Заголовок пункта', 'Подпись представителя строителя',
                             self.__font, True, 'LEFT', True, False, False),
                Point_format(self.window, 'Содеражание данных о представителе', 'Представитель',
                             self.__font, True, 'LEFT', True, False, False),
                Point_explanation_date_and_number(self.window, 'Пояснение к пункту',
                                                  'Содержание первого пояснения',
                                                  'Содержание второго пояснения', self.__font,
                                                  True, 'LEFT', False, True, False),
                Point_signature(self.window, 'ONE', True)
            ),
            'Подпись представителя строителя (контроль)': (
                Point_format(self.window, 'Заголовок пункта', 'Подпись представителя строителя (контроль)',
                             self.__font, True, 'LEFT', True, False, False),
                Point_format(self.window, 'Содеражание данных о представителе', 'Представитель',
                             self.__font, True, 'LEFT', True, False, False),
                Point_explanation_date_and_number(self.window, 'Пояснение к пункту',
                                                  'Содержание первого пояснения',
                                                  'Содержание второго пояснения', self.__font,
                                                  True, 'LEFT', False, True, False),
                Point_signature(self.window, 'ONE', True)
            ),
            'Подпись представителя проектной организации': (
                Point_format(self.window, 'Заголовок пункта', 'Подпись представителя проектной организации',
                             self.__font, True, 'LEFT', True, False, False),
                Point_format(self.window, 'Содеражание данных о представителе', 'Представитель',
                             self.__font, True, 'LEFT', True, False, False),
                Point_explanation_date_and_number(self.window, 'Пояснение к пункту',
                                                  'Содержание первого пояснения',
                                                  'Содержание второго пояснения', self.__font,
                                                  True, 'LEFT', False, True, False),
                Point_signature(self.window, 'ONE', True)
            ),
            'Подпись представителя исполнителя': (
                Point_format(self.window, 'Заголовок пункта', 'Подпись представителя исполнителя',
                             self.__font, True, 'LEFT', True, False, False),
                Point_format(self.window, 'Содеражание данных о представителе', 'Представитель',
                             self.__font, True, 'LEFT', True, False, False),
                Point_explanation_date_and_number(self.window, 'Пояснение к пункту',
                                                  'Содержание первого пояснения',
                                                  'Содержание второго пояснения', self.__font,
                                                  True, 'LEFT', False, True, False),
                Point_signature(self.window, 'ONE', True)
            ),
            'Подпись представителя иных лиц': (
                Point_format(self.window, 'Заголовок пункта', 'Подпись представителя иных лиц',
                             self.__font, True, 'LEFT', True, False, False),
                Point_format(self.window, 'Содеражание данных о представителе', 'Представитель',
                             self.__font, True, 'LEFT', True, False, False),
                Point_explanation_date_and_number(self.window, 'Пояснение к пункту',
                                                  'Содержание первого пояснения',
                                                  'Содержание второго пояснения', self.__font,
                                                  True, 'LEFT', False, True, False),
                Point_signature(self.window, 'ONE', True)
            )})

        self.list_point = []
        for key in self.gui_point_dict.keys():
            self.list_point.append(key)
            print(key, self.gui_point_dict[key])
            for num_el in range(len(self.gui_point_dict[key])):
                if self.gui_point_dict[key][num_el] is not None:
                    if num_el == 3:
                        self.gui_point_dict[key][num_el].grid(row=4, column=1)
                        self.gui_point_dict[key][num_el].remove_point()
                    else:
                        self.gui_point_dict[key][num_el].grid(row=num_el + 2, column=0)
                        self.gui_point_dict[key][num_el].remove_point()

        self.list_point = ['<Все заголовки>', '<Все содержания>', '<Все пояснения>'] + self.list_point

        self.list_point = tkinter.Variable(value=(self.list_point))

        self.data_export = x_data_akt.get_akt(self.__index_akt).export()

        self.frame_list_point = tkinter.Frame(self.window)
        self.combobox_list_point = ttk.Combobox(self.frame_list_point, state='readonly', width=47,
                                                values=self.list_point.get())
        self.label_listbox = tkinter.Label(self.frame_list_point, text='Список пунктов')
        self.listbox_point = tkinter.Listbox(self.frame_list_point, listvariable=self.list_point, width=50, height=30)

        self.label_listbox.grid(row=1, column=0, sticky='ns')
        self.combobox_list_point.grid(row=2, column=0, sticky='ns')
        self.listbox_point.grid(row=3, column=0, sticky='ns')

        self.frame_pattern_akt.grid(row=0, column=0)
        self.frame_pattern_name.grid(row=1, column=0)
        self.frame_list_point.grid(row=2, column=1, rowspan=2, sticky='ns')

        self.listbox_point.bind("<<ListboxSelect>>", self.set_item_to_combobox)
        self.combobox_list_point.bind("<<ComboboxSelected>>", self.set_item_to_listbox)

    def load_pattern(self):
        pass

    def add_pattern(self):
        self.Export.add_pattern('Шаблон', self.dict_point)
        self.patterns_names = tkinter.Variable(value=self.Export.list_patterns())
        self.listbox_pattern.config(listvariable=self.patterns_names)

    def change_pattern(self):
        pass

    def delete_pattern(self):
        index_pattern = self.listbox_pattern.curselection()[0]
        self.Export.delete_pattern(self.listbox_pattern.get(index_pattern))
        self.patterns_names = tkinter.Variable(value=self.Export.list_patterns())
        self.listbox_pattern.config(listvariable=self.patterns_names)

    def create_content(self, frame, heading):
        self.frame = tkinter.Frame(frame)
        self.label = tkinter.Label(self.frame, text=heading)
        self.text = tkinter.Text(self.frame, height=8, width=50, wrap='word')
        self.label.grid(row=0, column=0)
        self.text.grid(row=1, column=0)

    def content_grid(self):
        pass

    def set_item_to_combobox(self, event):
        name_point = self.list_point.get()[self.listbox_point.curselection()[0]]
        self.combobox_list_point.set(name_point)
        if self.__point is not None:
            for el in self.__point:
                el.remove_point()
        self.__point = self.gui_point_dict[name_point]
        for el in self.__point:
            el.grid()

    def set_item_to_listbox(self, event):
        name_point = self.combobox_list_point.get()
        self.listbox_point.select_set(self.list_point.get().index(name_point))


def key_rus(event):
    keys = ('z', 'x', 'c', 'v', 'a')
    if event.keysym.lower() not in keys:
        if event.keycode == 86:
            event.widget.event_generate('<<Paste>>')
        elif event.keycode == 67:
            event.widget.event_generate('<<Copy>>')
        elif event.keycode == 88:
            event.widget.event_generate('<<Cut>>')
        elif event.keycode == 65:
            event.widget.event_generate('<<SelectAll>>')


if __name__ == '__main__':
    window = RootGUI()
