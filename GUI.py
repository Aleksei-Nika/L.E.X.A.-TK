import data_akt
import tkinter
from tkinter import ttk
from tkinter import Toplevel

x_data_akt = akt.Date_Akt()
all_akts = ()


class RootGUI:
    def __init__(self):
        # Создание и настройка основного окна
        self.root = tkinter.Tk()
        self.root.title('L.E.X.A.')
        self.root.geometry('700x700')

        # Создание вкладок
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        # Создание вкладки ОБЪЕКТ
        self.frame_object = tkinter.Frame(self.root)
        self.frame_object.pack(expand=True, fill='both')
        self.notebook.add(self.frame_object, text='Объект')

        # Создание группы виджетов ПОЛНОЕ НАИМЕНОВАНИЕ ОБЪЕКТА для вкладке ОБЪЕКТ
        self.frame_name_object = tkinter.LabelFrame(self.frame_object,
                                                    borderwidth=1,
                                                    relief='solid',
                                                    text='Полное наименование объекта')
        #
        # Создание подгруппы виджетов ПОЛНОЕ НАИМЕНОВАНИЕ ОБЪЕКТОВ для группы НАИМЕНОВАНИЕ ОБЪЕКТОВ
        self.frame_text = tkinter.Frame(self.frame_name_object)
        self.frame_text.pack()
        self.text_name = tkinter.Text(self.frame_text,
                                      height=5, width=80,
                                      wrap='word', )
        self.text_name.insert('end', 'Введите наименование объекта')
        self.text_name.pack(side='left')
        self.text_name_scrollbar = tkinter.Scrollbar(self.frame_text,
                                                     command=self.text_name.yview)
        self.text_name_scrollbar.pack(side='right',
                                      fill='y')
        self.text_name.config(yscrollcommand=self.text_name_scrollbar.set)
        # Создание подргуппы виджетов КОРОТКОЕ НИМЕНОВАНИЕ/КНОПКА для группы НАИМЕНОВАНИЕ ОБЪЕКТОВ
        self.frame_button = tkinter.Frame(self.frame_name_object)
        self.entry_short_name = tkinter.Entry(self.frame_button,
                                              width=66)
        self.entry_short_name.pack(side='left', fill='both')
        self.entry_short_name.insert('end', 'Введите короткое название объекта')
        self.button_add_name_object = tkinter.Button(self.frame_button,
                                                     text='Добавить наименование объекта',
                                                     command=self.add_name_object)
        self.button_add_name_object.pack(side='right', fill='both')
        self.frame_button.pack()
        # Создание подгруппы виджетов СПИСОК НАИМЕНОВАНИЙ ОБЪЕКТОВ для группы НАИМЕНОВАНИЕ ОБЪЕКТОВ
        self.frame_names = tkinter.Frame(self.frame_name_object)
        self.label_names = tkinter.Label(self.frame_name_object,
                                         text='Список наименований')
        self.label_names.pack(anchor='w')
        self.frame_llistbox_names = tkinter.Frame(self.frame_name_object)
        self.listbox_names = tkinter.Listbox(self.frame_llistbox_names,
                                             height=3,
                                             width=93)
        self.listbox_names.pack(side='left')
        self.listbox_names_scrollbar = tkinter.Scrollbar(self.frame_llistbox_names,
                                                         command=self.listbox_names.yview)
        self.listbox_names_scrollbar.pack(side='right', fill='y')
        self.listbox_names.config(yscrollcommand=self.listbox_names_scrollbar.set)
        self.listbox_names.bind('<<ListboxSelect>>', self.viewing_name_object)
        self.listbox_names.bind('<Button-3>', self.menu_names_object)
        self.listbox_index_change = ()
        self.__indekator_click = True
        self.__indekator_cursor = True
        self.frame_llistbox_names.pack()
        self.frame_names.pack()
        self.frame_name_object.pack()
        # self.

        # Создание вкладки АКТЫ
        self.frame_akt = tkinter.Frame(self.root)
        self.frame_akt.pack(expand=True, fill='both')
        self.notebook.add(self.frame_akt, text='Акты')

        # Создание виджетов СПИСОК АКТОВ во вкладке АКТЫ
        self.frame1 = tkinter.Frame(self.frame_akt)
        self.button1 = tkinter.Button(self.frame1,
                                      text='Добавить новый акт',
                                      command=self.new_akt)
        self.button1.pack()
        self.label1 = tkinter.Label(self.frame1, text='Список актов:')
        self.label1.pack()
        self.listbox1 = tkinter.Listbox(self.frame1)
        self.listbox1.pack()
        self.frame1.pack()

        self.root.mainloop()

    def add_name_object(self):
        # global x_data_akt
        name_object = self.text_name.get('0.1', 'end')
        name_object = name_object[0: -1]
        x_data_akt.set_name_object(name_object)
        x_data_akt.set_name_short_object(self.entry_short_name.get())
        num = self.listbox_names.size()
        self.listbox_names.insert(0, f'Наименование объекта {num + 1}')
        self.text_name.replace('0.1', 'end', 'Введите наименование объекта')
        self.entry_short_name.delete('0', 'end')
        self.entry_short_name.insert('end', 'Введите короткое название объекта')

    def viewing_name_object(self, event):
        index_list_names_object = self.listbox_names.curselection()
        name_object = x_data_akt.get_name_object(index_list_names_object[0])
        self.text_name.replace('0.1', 'end', name_object)
        short_name_object = x_data_akt.get_name_short_object(index_list_names_object[0])
        self.entry_short_name.delete('0', 'end')
        self.entry_short_name.insert('end', short_name_object)

    def menu_names_object(self, event):
        menu_names = tkinter.Menu(tearoff=0)
        menu_names.add_command(label='Изменить', command=self.change_name_object_button)
        menu_names.add_command(label='Удалить', command=self.delete_name_object)
        menu_names.post(event.x_root, event.y_root)

    def change_name_object_button(self):
        print(1)
        self.listbox_index_change = self.listbox_names.curselection()
        print(2)
        self.button_add_name_object.config(text='Изменить наименование объекта',
                                           command=self.change_name_object)
        print(3)

        def fun_click_on(event):
            self.__indekator_click = True
            print('Отпушен', self.__indekator_click)

        def fun_click_off(event):
            self.__indekator_click = False
            print('Нажат', self.__indekator_click)

        def fun_cursor_on(event):
            self.__indekator_cursor = True
            print('В зоне', self.__indekator_click)

        def fun_cursor_off(event):
            self.__indekator_cursor = False
            print('За зоной', self.__indekator_click)

        print(4)
        self.frame_name_object.bind("<Enter>", fun_cursor_on)
        self.frame_name_object.bind("<Leave>", fun_cursor_off)
        self.root.bind("<ButtonRelease-1>", fun_click_on)
        self.root.bind("<Button-1>", fun_click_off)
        print(5)
        while self.__indekator_cursor:
            print(6)
        print(7)
        self.button_add_name_object.config(text='Добавить наименование объекта',
                                           command=self.add_name_object)
        print(8)
        self.root.unbind("<Button-1>")
        self.root.unbind("<ButtonRelease-1>")
        self.frame_name_object.unbind("<Enter>")
        self.frame_name_object.unbind("<Leave>")
        print(9)

    def change_name_object(self):
        name_object = self.text_name.get('0.1', 'end')
        name_object = name_object[0: -1]
        x_data_akt.change_name_object(name_object, self.listbox_index_change[0])
        x_data_akt.change_name_short_object(self.entry_short_name.get(), self.listbox_index_change[0])
        self.button_add_name_object.config(text='Добавить наименование объекта',
                                           command=self.add_name_object)
        self.text_name.replace('0.1', 'end', 'Введите наименование объекта')
        self.entry_short_name.delete('0', 'end')
        self.entry_short_name.insert('end', 'Введите короткое название объекта')

    def delete_name_object(self):
        index_list_names_object = self.listbox_names.curselection()
        x_data_akt.delete_name_object(index_list_names_object[0])
        x_data_akt.delete_name_short_object(index_list_names_object[0])
        self.listbox_names.delete(index_list_names_object[0])
        self.text_name.replace('0.1', 'end', 'Введите наименование объекта')
        self.entry_short_name.delete('0', 'end')
        self.entry_short_name.insert('end', 'Введите короткое название объекта')

    def new_akt(self):
        self.window_new_akt = Toplevel(self.root)
        self.window_new_akt.title('Создание нового акта')
        self.window_new_akt.geometry('500x500')
        self.window_new_akt.grab_set()

        self.frame1_new_akt = tkinter.Frame(self.window_new_akt)
        self.label_name_work = tkinter.Label(self.frame1_new_akt,
                                             text='Введите название работы:')
        self.label_name_work.pack(side='left')
        self.entry_name_work = tkinter.Entry(self.frame1_new_akt,
                                             width=30)
        self.entry_name_work.pack(side='left')
        self.frame1_new_akt.pack(side='left')

        self.frame2_new_akt = tkinter.Frame(self.window_new_akt)
        self.button_create = tkinter.Button(self.frame2_new_akt,
                                            text='Создать акт',
                                            command=self.create_akt)
        self.button_create.pack(anchor='se')
        self.frame2_new_akt.pack(side='bottom')

    def create_akt(self):
        global all_akts
        x_akt = akt.Akt()
        self.name_work = str(self.entry_name_work.get())
        x_akt.set_name_work(self.name_work)
        self.listbox1.insert(1, self.name_work)
        all_akts = list(all_akts)
        all_akts.append(x_akt)
        all_akts = tuple(all_akts)
        self.window_new_akt.destroy()


if __name__ == '__main__':
    window = RootGUI()


