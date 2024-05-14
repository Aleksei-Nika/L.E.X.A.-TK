import pickle
from datetime import date


def new():
    x_data_akt = Data_Akt()
    return x_data_akt


def load(path_file):
    input_file = open(path_file, 'rb')
    file = pickle.load(input_file)
    data_akts = file
    input_file.close()
    return data_akts


def save(path_file, file):
    output_file = open(path_file, 'wb')
    pickle.dump(file, output_file)
    output_file.close()


class Data_Akt:
    def __init__(self):
        self.__akts = ()
        self.__names_object = ()
        self.__names_shorts = ()
        self.__organization = ()
        self.__representative = ()

    # функции для АКТОВ
    def set_akt(self, akt):
        self.__akts = list(self.__akts)
        self.__akts.append(akt)
        self.__akts = tuple(self.__akts)

    def change_akt(self, akt, index):
        self.__akts = list(self.__akts)
        self.__akts[index] = akt
        self.__akts = tuple(self.__akts)

    def delete_akt(self, akt_index):
        self.__akts = list(self.__akts)
        del self.__akts[akt_index]
        self.__akts = tuple(self.__akts)

    def get_akt(self, akt_index):
        return self.__akts[akt_index]

    def get_all_akts(self):
        return self.__akts

    def get_all_akts_names(self):
        return tuple(akts.get_name_work() for akts in self.get_all_akts())

    # функции для ИМЁН ОБЪЕКТА
    # Добавление ИМЕНИ ОБЪЕКТА в конец кортежа
    def set_name_object(self, text, name):
        self.__names_object = list(self.__names_object)
        self.__names_object.insert(0, Object_element(text, name))
        self.__names_object = tuple(self.__names_object)

        # Изменение ИМЕНИ ОБЪЕКТА в кортеже
    def change_name_object(self, text, name, index):
        self.__names_object = list(self.__names_object)
        self.__names_object[index].set_text(text)
        self.__names_object[index].set_name(name)
        self.__names_object = tuple(self.__names_object)

        # Удаление ИМЕНИ ОБЪЕКТА из кортежа
    def delete_name_object(self, index):
        self.__names_object = list(self.__names_object)
        del self.__names_object[index]
        self.__names_object = tuple(self.__names_object)

        # Возвращение ПОЛНОГО ИМЕНИ из кортежа
    def get_name_object_text(self, index):
        return self.__names_object[index].get_text()

        # Возвращение КОРОТКОГО ИМЕНИ из кортежа
    def get_name_object_name(self, index):
        return self.__names_object[index].get_name()

        # Возвращение кортежа ПОЛНЫХ ИМЁН
    def get_all_name_object_texts(self):
        return tuple(element.get_text() for element in self.__names_object)

        # Возвращение кортежа КОРОТКИХ ИМЁН
    def get_all_name_object_names(self):
        return tuple(element.get_name() for element in self.__names_object)

        # Возвращение ИМЕНИ
    def get_name_object(self, index):
        return self.__names_object[index]

        # Возвращение кортежа ПОЛНЫХ ИМЁН
    def get_all_names_object(self):
        return self.__names_object

    # функции для ОРГАНИЗАЦИЙ
    def set_organization(self, text, name):
        self.__organization = list(self.__organization)
        self.__organization.insert(0, Object_element(text, name))
        self.__organization = tuple(self.__organization)

    def change_organization(self, text, name, index):
        self.__organization = list(self.__organization)
        self.__organization[index].set_text(text)
        self.__organization[index].set_name(name)
        self.__organization = tuple(self.__organization)

    def delete_organization(self, index):
        self.__organization = list(self.__organization)
        del self.__organization[index]
        self.__organization = tuple(self.__organization)

    def get_organization_text(self, index):
        return self.__organization[index].get_text()

    def get_organization_name(self, index):
        return self.__organization[index].get_name()

    def get_all_organizations_texts(self):
        return tuple(element.get_text() for element in self.__organization)

    def get_all_organizations_names(self):
        return tuple(element.get_name() for element in self.__organization)

    def get_organization(self, index):
        return self.__organization[index]

    def get_all_organizations(self):
        return self.__organization

    # функции для ПРЕДСТВАВИТЕЛЕЙ
    # Добавление ПРЕДСТАВИТЕЛЯ в конец кортежа
    def set_representative(self, text, name):
        self.__representative = list(self.__representative)
        self.__representative.insert(0, Object_element(text, name))
        self.__representative = tuple(self.__representative)

        # Изменение ПРЕДСТАВИТЕЛЯ в кортеже
    def change_representative(self, text, name, index):
        self.__representative = list(self.__representative)
        self.__representative[index].set_text(text)
        self.__representative[index].set_name(name)
        self.__representative = tuple(self.__representative)

        # Удаление ПРЕДСТВИТЕЛЯ из кортежа
    def delete_representative(self, index):
        self.__representative = list(self.__representative)
        del self.__representative[index]
        self.__representative = tuple(self.__representative)

        # Возвращение информации о ПРЕДСТАВИТЕЛЕ
    def get_representative_text(self, index):
        return self.__representative[index].get_text()

        # Возвращение имени ПРЕДСТАВИТЕЛЯ
    def get_representative_name(self, index):
        return self.__representative[index].get_name()

        # Возвращение кортежа с информацией о всех ПРЕДСТАВИТЕЛЯХ
    def get_all_representatives_texts(self):
        return tuple(element.get_text() for element in self.__representative)

        # Возвращение кортежа с именами всех ПРЕДСТАВИТЕЛЯХ
    def get_all_representatives_names(self):
        return tuple(element.get_name() for element in self.__representative)

        # Возвращение ПРЕДСТАВИТЕЛЯ
    def get_representative(self, index):
        return self.__representative[index]

        # Возвращение кортежа с ПРЕДСТАВИТЕЛЯМИ
    def get_all_representatives(self):
        return self.__representative


class Akt:
    def __init__(self):
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
        self.__work = None

        self.__start_date = None
        self.__finish_date = None

        self.__documentation = None

    # Функции для ИМЕНИ ОБЪЕКТА
    def set_name_object(self, obj):
        self.__name_object = obj

    def get_name_object(self):
        return self.__name_object

    # Функции для ЗАСТРОЙЩИКА
    def set_developer(self, obj):
        self.__developer = obj

    def get_developer(self):
        return self.__developer

    # функции для ЛИЦА ОСУЩЕСТВЛЯЮЩЕГО СТРОИТЕЛЬСТВА
    def set_builder(self, obj):
        self.__builder = obj

    def get_builder(self):
        return self.__builder

    # функции для ПРОЕКТИРОВЩИКА
    def set_designer(self, obj):
        self.__designer = obj

    def get_designer(self):
        return self.__designer

    # функции для ПРЕДСТАВИТЕЛЯ ЗАСТРОЙЩИКА
    def set_developer_name(self, obj):
        self.__developer_name = obj

    def get_developer_name(self):
        return self.__developer_name

    # функции для ПРЕДСТАВИТЕЛЯ ЛИЦА ОСУЩЕСТВЛЯЮЩЕГО СТРОИТЕЛЬСТВО
    def set_builder_name(self, obj):
        self.__builder_name = obj

    def get_builder_name(self):
        return self.__builder_name

    # функции для ПРЕДСТАВИТЕЛЯ ЛИЦА ОСУЩЕСТВЛЯЮЩЕГО СТРОИТЕЛЬСТВО ПО ВОПРОСАМ СТРОИТЕЛЬНОГО КОНТРОЛЯ
    def set_builder_control_name(self, obj):
        self.__builder_control_name = obj

    def get_builder_control_name(self):
        return self.__builder_control_name

    # функции для ПРЕДСТАВИТЕЛЯ ПРОЕКТИРОВЩИКА
    def set_designer_name(self, obj):
        self.__designer_name = obj

    def get_designer_name(self):
        return self.__designer_name

    # функции для ПРЕДСТАВИТЕЛЯ ВЫПОЛНЯЮЩЕГО РАБОТЫ
    def set_contractor_name(self, obj):
        self.__contractor_name = obj

    def get_contractor_name(self):
        return self.__contractor_name

    # функции для ДРУГИХ ПРЕДСТАВИТЕЛЕЙ
    def set_another_person(self, obj):
        self.__another_person = obj

    def get_another_person(self):
        return self.__another_person

    # функции для ВЫПОЛНЯЮЩЕГО РАБОТЫ
    def set_contractor(self, obj):
        self.__contractor = obj

    def get_contractor(self):
        return self.__contractor

    # функции для НАИМЕНОВАНИЯ РАБОТ
    def set_name_work(self, name):
        self.__work = str(name)

    def get_name_work(self):
        return self.__work

    # функции для ДАТЫ
        # добавление даты начала и окончания работ в акт
    def add_deadlines(self, str_start_date, str_finish_date):
        try:
            if str_start_date == '' and str_finish_date == '':
                self.__start_date = str_start_date
                self.__finish_date = str_finish_date
            elif str_start_date == '':
                self.__finish_date = self.date_modification(str_finish_date)
                self.__start_date = ''
                return
            elif str_finish_date == '':
                self.__start_date = self.date_modification(str_start_date)
                self.__finish_date = ''
                return
            else:
                start_date = self.date_modification(str_start_date)
                finish_date = self.date_modification(str_finish_date)
                if self.date_comparison(start_date, finish_date):
                    self.__start_date = start_date
                    self.__finish_date = finish_date
                else:
                    return 'Дата начала не может быть позднее даты окончание'
        except (KeyError, IndexError):
            return 'Некорректно введены даты'

        # создание даты из строки в объект модуля Date
    def date_modification(self, str_date):

        date_split = []
        date_element = ''

        str_date = str_date.lower()

        str_date = str_date.replace('г', '')

        for el in range(len(str_date)):
            if el == len(str_date) - 1:
                if str_date[el].isalnum():
                    date_element += str_date[el]
                    date_split.append(date_element)
                else:
                    date_split.append(date_element)
            elif str_date[el].isalnum():
                date_element += str_date[el]
            else:
                date_split.append(date_element)
                date_element = ''

        date_obj = []

        for el in date_split:
            if el:
                date_obj.append(el)

        if date_obj[0].isdigit():
            date_obj[0] = int(date_obj[0])

        if date_obj[1].isdigit():
            date_obj[1] = int(date_obj[1])
        elif date_obj[1].isalpha():
            dictionary = {'января': int(1),
                          'янв': int(1),
                          'февраля': int(2),
                          'фев': int(2),
                          'марта': int(3),
                          'мар': int(3),
                          'апреля': int(4),
                          'апр': int(4),
                          'майя': int(5),
                          'май': int(5),
                          'июня': int(6),
                          'июн': int(6),
                          'июля': int(7),
                          'июл': int(7),
                          'августа': int(8),
                          'авг': int(8),
                          'сентября': int(9),
                          'сен': int(9),
                          'октября': int(10),
                          'окт': int(10),
                          'ноября': int(11),
                          'ноя': int(11),
                          'декабря': int(12),
                          'дек': int(12)}
            date_obj[1] = dictionary[date_obj[1]]

        if date_obj[2].isdigit():
            if len(date_obj[2]) == 4:
                date_obj[2] = int(date_obj[2])
            elif len(date_obj[2]) == 2:
                date_obj[2] = int('20' + date_obj[2])
                date_obj[2] = int(date_obj[2])
        return date(date_obj[2], date_obj[1], date_obj[0])

    # Сравнение дат начала и окончания работ
    def date_comparison(self, start_date, finis_date):
        if start_date <= finis_date:
            return True
        elif start_date > finis_date:
            return False

    def set_start_date(self, obj):
        self.__start_date = obj

    def set_finish_date(self, obj):
        self.__finish_date = obj

    def get_start_date(self):
        return self.__start_date

    def get_finish_date(self):
        return self.__finish_date

    def get_str_start_date(self):
        dictionary = {'January': 'января',
                      'February': 'февраля',
                      'March': 'марта',
                      'April': 'апреля',
                      'May': 'мая',
                      'June': 'июня',
                      'July': 'июля',
                      'August': 'августа',
                      'September': 'сентября',
                      'October': 'октября',
                      'November': 'ноября',
                      'December': 'декабря'}
        if self.__start_date == '' or self.__start_date is None:
            return ''
        else:
            str_date = str(self.__start_date.strftime('%d.%B.%Y'))
            date1 = str_date.split('.')
            return f'«{date1[0]}» {dictionary[date1[1]]} {date1[2]} г.'

    def get_str_finish_date(self):
        dictionary = {'January': 'января',
                      'February': 'февраля',
                      'March': 'марта',
                      'April': 'апреля',
                      'May': 'мая',
                      'June': 'июня',
                      'July': 'июля',
                      'August': 'августа',
                      'September': 'сентября',
                      'October': 'октября',
                      'November': 'ноября',
                      'December': 'декабря'}
        if self.__finish_date == '' or self.__finish_date is None:
            return ''
        else:
            str_date = str(self.__finish_date.strftime('%d.%B.%Y'))
            date1 = str_date.split('.')
            return f'«{date1[0]}» {dictionary[date1[1]]} {date1[2]} г.'

    # функции для ПРОЕКТНО-СМЕТНОЙ ДОКУМЕНТАЦИИ
    def set_documentation(self, documentation):
        self.__documentation = documentation

    def get_documentation(self):
        return self.__documentation

    def get_text_of_documentation(self):
        list_text_of_doc = []
        for doc in self.__documentation:
            org = doc.get_organization().get_name()
            if org is None:
                org = doc.get_organization().get_text()
            name_doc = doc.get_name_doc().get_name()
            if name_doc is None:
                name_doc = doc.get_name_doc().get_text()
            page = doc.get_page()
            if page[0:0] == '"':
                page = page[1: -1]

            list_text_of_doc.append(f'{org} {name_doc}, л. {page}; ')

        text_of_doc = ''
        for el in list_text_of_doc:
            text_of_doc += el
        text_of_doc = text_of_doc[0:-2]+'.'

        return text_of_doc

        '''
        list_org = []
        list_name_doc = []
        list_page = []
        for doc in self.__documentation:
            org = doc.get_organization().get_name()
            if org is None:
                org = doc.get_organization().get_text()
            list_org.append(org)
            name_doc = doc.get_name_doc().get_name()
            if name_doc is None:
                name_doc = doc.get_name_doc().get_text()
            list_name_doc.append(name_doc)
            page = doc.get_page()
            list_page.append(page)
        list_text_of_doc = []
        iteration = 0
        while len(list_org) != 0:
            org = list_org[iteration]
            print(org, list_org[iteration])
            name_doc = list_name_doc[iteration]
            print(name_doc, list_name_doc[iteration])
            page = list_page[iteration]
            print(page, list_page[iteration])
            list_text_of_doc.append((org, name_doc, page))
            print(list_text_of_doc)
            del list_org[iteration]
            del list_name_doc[iteration]
            del list_page[iteration]
            if list_text_of_doc[iteration][0] != '':
                while list_text_of_doc[iteration][0] in list_org:
                    next_org = ''
                    index = list_org.index(list_text_of_doc[iteration][0])
                    if list_text_of_doc[iteration][1] != list_name_doc[index] or list_name_doc[index] != '':
                        next_name_doc = list_name_doc[index]
                    else:
                        next_name_doc = ''
                    if list_text_of_doc[iteration][2] != list_page[index] or list_page[index] != '':
                        next_page = list_page[index]
                    else:
                        next_page = ''
                    list_text_of_doc.append((next_org, next_name_doc, next_page))
                    del list_org[index]
                    del list_name_doc[index]
                    del list_page[index]
                iteration += 1
        text_of_doc = ''
        for iteration in range(len(list_text_of_doc)):
            for el in range(len(list_text_of_doc[iteration])):
                if el == 2 and iteration == len(list_text_of_doc):
                    text_of_doc += '.'
                elif el != '':
                    text_of_doc += list_text_of_doc[iteration][el] + ', '
        return text_of_doc
        '''



    def __str__(self):
        return f'{self.__name_hous}'


# класс ЭЛЕМЕНТЫ для АКТА
class Object_element:
    def __init__(self, text, name):
        self.__text = text
        self.__name = name

    def set_text(self, text):
        self.__text = text

    def set_name(self, name):
        self.__name = name

    def get_text(self):
        return self.__text

    def get_name(self):
        return self.__name


class Doc:
    def __init__(self, organization=None, name_doc=None, page=None):
        self.__organization = organization
        self.__name_doc = name_doc
        self.__page = page

    def set_organization(self, organization):
        self.__organization = organization

    def get_organization(self):
        return self.__organization

    def set_name_doc(self, name_doc):
        self.__name_doc = name_doc

    def get_name_doc(self):
        return self.__name_doc

    def set_page(self, page):
        self.__page = page

    def get_page(self):
        return self.__page

def page_modification(input_page):
    try:
        input_sheet_number = input_page

        # Отчистка введенных данных от лишних пробелов и перевод в список
        split_sheet_number = input_sheet_number.split(' ')
        str_sheet_number = str()
        for el in split_sheet_number:
            str_sheet_number += el
        input_sheet_number = str_sheet_number.split(',')

        # Создание словаря для дробный чисел без точки
        special_page = {}

        # Поиск дробных чисел
        # Удаление дробных чисел со списка полного перечня листов
        # Если номер страницы записан через дробь, то записать через точку
        fractional_numbers = list()
        for el in input_sheet_number:
            if '.' in el:
                fractional_numbers.append(el)
            elif '/' in el:
                element = ''
                for simbol in el:
                    if simbol == '/':
                        element += '.'
                    else:
                        element += simbol
                fractional_numbers.append(float(element))
                special_page[element] = el

        for key in special_page:
            input_sheet_number.remove(special_page[key])

        # Создание списка для полного перечисления всех введеных листов
        full_sheet_number = list()

        # Анализ диапозонов листов (например 1-10) во веденных данных, их разбивка на отдельные элементы
        # Перевод всех элементов в целочисленные данные
        for el in range(len(input_sheet_number)):
            if '-' in input_sheet_number[el]:
                element = input_sheet_number[el]
                index_tire = element.find('-')
                first_num = element[0:index_tire]
                second_num = element[(index_tire + 1):(len(element))]
                first_num = int(first_num)
                second_num = int(second_num)
                if first_num > second_num:
                    first_num, second_num = second_num, first_num
                for num in range(first_num, second_num + 1):
                    full_sheet_number.append(int(num))
            else:
                full_sheet_number.append(int(input_sheet_number[el]))

        # Удаление повторяющихся номеров листов, путём преобразования во множество
        full_sheet_number = set(full_sheet_number)
        # Преобразования в список
        full_sheet_number = list(full_sheet_number)
        # Объединение списков целочисленых и дробных чисел
        full_sheet_number += fractional_numbers
        # Сортировака номеров листов по возрастанию
        full_sheet_number.sort()
        # Преобразование списка в кортедж
        full_sheet_number = tuple(full_sheet_number)

        # Создание списка для конечной работы
        final_sheet_number = []
        index = 0  # Переменная номера индекса анализируемого элемента
        # Анализ номеров листов для поиска диапазона листов (например 1-10)
        while index <= (len(full_sheet_number) - 1):
            minim = full_sheet_number[index]
            try:
                while (full_sheet_number[index] + 1) == (full_sheet_number[index + 1]):
                    index += 1
            except IndexError:
                pass
            maxim = full_sheet_number[index]
            index += 1
            if minim == maxim:
                final_sheet_number.append(str(minim))
            elif minim < maxim:
                str_minim = str(minim)
                str_maxim = str(maxim)
                final_sheet_number.append(str_minim + '-' + str_maxim)

        for index in range(len(final_sheet_number)):
            if final_sheet_number[index] in special_page:
                final_sheet_number[index] = special_page[final_sheet_number[index]]

        # Создание переменной для преобразования кортеджа в литерал
        text_sheet_number = str()
        # Преобразование кортеджа в литерал
        for el in range(len(final_sheet_number)):
            if el != (len(final_sheet_number) - 1):
                text_sheet_number += (final_sheet_number[el] + ', ')
            else:
                text_sheet_number += final_sheet_number[el]
    except:
        return

    return text_sheet_number

if __name__ == '__main__':
    pass
