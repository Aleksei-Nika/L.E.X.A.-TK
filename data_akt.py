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

    def set_name_object(self, obj):
        self.__name_object = obj

    def get_name_object(self):
        return self.__name_object

    def set_developer(self, obj):
        self.__developer = obj

    def get_developer(self):
        return self.__developer

    def set_builder(self, obj):
        self.__builder = obj

    def get_builder(self):
        return self.__builder

    def set_designer(self, obj):
        self.__designer = obj

    def get_designer(self):
        return self.__designer

    def set_developer_name(self, obj):
        self.__developer_name = obj

    def get_developer_name(self):
        return self.__developer_name

    def set_builder_name(self, obj):
        self.__builder_name = obj

    def get_builder_name(self):
        return self.__builder_name

    def set_builder_control_name(self, obj):
        self.__builder_control_name = obj

    def get_builder_control_name(self):
        return self.__builder_control_name

    def set_designer_name(self, obj):
        self.__designer_name = obj

    def get_designer_name(self):
        return self.__designer_name

    def set_contractor_name(self, obj):
        self.__contractor_name = obj

    def get_contractor_name(self):
        return self.__contractor_name

    def set_another_person(self, obj):
        self.__another_person = obj

    def get_another_person(self):
        return self.__another_person

    def set_contractor(self, obj):
        self.__contractor = obj

    def get_contractor(self):
        return self.__contractor

    def set_name_work(self, name):
        self.__work = str(name)

    def get_name_work(self):
        return self.__work

    # функции для ДАТЫ
    def entry_date(self, x_date):

        x_date_split = []
        x_date_element = ''

        x_date = x_date.lower()

        x_date = x_date.replace('г', '')

        for el in range(len(x_date)):
            if el == len(x_date) - 1:
                if x_date[el].isalnum():
                    x_date_element += x_date[el]
                    x_date_split.append(x_date_element)
                else:
                    x_date_split.append(x_date_element)
            elif x_date[el].isalnum():
                x_date_element += x_date[el]
            else:
                x_date_split.append(x_date_element)
                x_date_element = ''

        x_date = []

        for el in x_date_split:
            if el:
                x_date.append(el)

        if x_date[0].isdigit():
            x_date[0] = int(x_date[0])

        if x_date[1].isdigit():
            x_date[1] = int(x_date[1])
        elif x_date[1].isalpha():
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
            x_date[1] = dictionary[x[1]]

            if x_date[2].isdigit():
                if len(x_date[2]) == 4:
                    x_date[2] = int(x[2])
                elif len(x_date[2]) == 2:
                    x_date[2] = '20' + x_date[2]
                    x_date[2] = int(x_date[2])

        return x_date

    def set_start_date(self, start_date):
        self.__start_date = date(start_date)

    def get_start_date(self):
        return self.__start_date

    def set_finish_date(self, finis_date):
        self.__finis_date = date(finis_date)

    def get_finish_date(self):
        return self.__finish_date

    def __str__(self):
        return self.__name_hous


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


if __name__ == '__main__':
    pass
