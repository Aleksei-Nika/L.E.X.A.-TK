import pickle
from datetime import date
import sqlite3
import fitz
import os


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


def connection_base_data(path_file):
    conn = sqlite3.connect(path_file)
    return Data_base_materials(conn)


def connection_new_base_data(path_file, db):
    try:
        os.remove(path_file)
    except PermissionError:
        db.close_date_base()
        os.remove(path_file)
    conn = sqlite3.connect(path_file)
    return Data_base_materials(conn)


class Data_Akt:
    def __init__(self):
        self.__akts = ()
        self.__names_object = ()
        self.__organization = ()
        self.__representative = ()
        self.__project_documentation = ()
        self.__materials = ()
        self.__documents = ()
        self.__regulations = ()
        self.__names_classifications = ()

    # функции для АКТОВ
    def set_akt(self, akt):
        self.__akts = list(self.__akts)
        self.__akts.append(akt)
        self.__akts = tuple(self.__akts)

    def change_akt(self, akt, akt_index):
        self.__akts = list(self.__akts)
        self.__akts[akt_index] = akt
        self.__akts = tuple(self.__akts)

    def delete_akt(self, akt_index):
        self.__akts = list(self.__akts)
        del self.__akts[akt_index]
        self.__akts = tuple(self.__akts)

    def get_akt(self, akt_index):
        return self.__akts[akt_index]

    def get_all_akts(self):
        return self.__akts

    def get_all_akts_names_object(self):
        return tuple(akts.get_name_work() for akts in self.get_all_akts())

    def get_all_akts_names_text(self):
        return tuple(akts.get_name_work().get_text() for akts in self.get_all_akts())

    def get_names_previous_works(self, akt_index):
        previous_works = []
        for akt in self.__akts:
            if self.get_akt(akt_index).get_name_work() in akt.get_next_work():
                previous_works.append(akt.get_name_work())
        return tuple(previous_works)


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

    # Функции для ТЕХНИЧЕСКИХ РЕГЛАМЕНТОВ
        # Добавление ТЕХНИЧЕСКОГО РЕГЛАМЕНТА
    def set_regulation(self, text, name):
        self.__regulations = list(self.__regulations)
        self.__regulations.insert(0, Object_element(text, name))
        self.__regulations = tuple(self.__regulations)

        # Изменение ТЕХНИЧЕСКОГО РЕГЛАМЕНТА
    def change_regulation(self, text, name, index):
        self.__regulations = list(self.__regulations)
        self.__regulations[index].set_text(text)
        self.__regulations[index].set_name(name)
        self.__regulations = tuple(self.__regulations)

        # Удаление ТЕХНИЧЕСКОГО РЕГЛАМЕНТА
    def delete_regulation(self, index):
        self.__regulations = list(self.__regulations)
        del self.__regulations[index]
        self.__regulations = tuple(self.__regulations)

        # Возвращение ТЕХНИЧЕСКОГО РЕГЛАМЕНТА
    def get_regulation(self, index):
        return self.__regulations[index]

        # Возвращение всех ТЕХНИЧЕСКИХ РЕГЛАМЕНТОВ
    def get_all_regulations(self):
        return self.__regulations

        # Возвращение ТЕКСТА ТЕХНИЧЕСКОГО РЕГЛАМЕНТА
    def get_regulation_text(self, index):
        return self.__regulations[index].get_text()

        # Возвращение всех ТЕКСТОВ ТЕХНИЧЕСКИХ РЕГЛАМЕНТОВ
    def get_all_regulations_texts(self):
        return tuple(element.get_text() for element in self.__regulations)

        # Возвращение ИМЕНИ ТЕХНИЧЕСКОГО РЕГЛАМЕНТА
    def get_regulation_name(self, index):
        return self.__regulations[index].get_name()

        # Возвращение всех ИМЕН ТЕХНИЧЕСКИХ РЕГЛАМЕНТОВ
    def get_all_regulations_names(self):
        return tuple(element.get_name() for element in self.__regulations)

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

    # функции для ПРОЕКТНО-СМЕТНОЙ ДОКУМЕНТАЦИИ
        # добовление ПРОЕКТНО-СМЕТНОЙ ДОКУМЕНТАЦИИ в конец кортежа
    def set_project_documentation(self, text, name):
        self.__project_documentation = list(self.__project_documentation)
        self.__project_documentation.insert(0, Object_element(text, name))
        self.__project_documentation = tuple(self.__project_documentation)

        # Изменение ПРОЕКТНО-СМЕТНОЙ ДОКУМЕНТАЦИИ в кортеже
    def change_project_documentation(self, text, name, index):
        self.__project_documentation = list(self.__project_documentation)
        self.__project_documentation[index].set_text(text)
        self.__project_documentation[index].set_name(name)
        self.__project_documentation = tuple(self.__project_documentation)

        # Удаление ПРОЕКТНО-СМЕТНОЙ ДОКУМЕНТАЦИИ из кортежа
    def delete_project_documentation(self, index):
        self.__project_documentation = list(self.__project_documentation)
        del self.__project_documentation[index]
        self.__project_documentation = tuple(self.__project_documentation)

        # Возвращение информации о ПРОЕКТНО-СМЕТНОЙ ДОКУМЕНТАЦИИ
    def get_project_documentation_text(self, index):
        return self.__project_documentation[index].get_text()

        # Возвращение имени ПРОЕКТНО-СМЕТНОЙ ДОКУМЕНТАЦИИ
    def get_project_documentation_name(self, index):
        return self.__project_documentation[index].get_name()

        # Возвращение кортежа с информацией о всех ПРОЕКТНО-СМЕТНОЙ ДОКУМЕНТАЦИИ
    def get_all_project_documentations_texts(self):
        return tuple(element.get_text() for element in self.__project_documentation)

        # Возвращение кортежа с именами всех ПРОЕКТНО-СМЕТНОЙ ДОКУМЕНТАЦИИ
    def get_all_project_documentations_names(self):
        return tuple(element.get_name() for element in self.__project_documentation)

        # Возвращение ПРОЕКТНО-СМЕТНОЙ ДОКУМЕНТАЦИИ
    def get_project_documentation(self, index):
        return self.__project_documentation[index]

        # Возвращение кортежа с ПРОЕКТНО-СМЕТНОЙ ДОКУМЕНТАЦИИ
    def get_all_project_documentation(self):
        return self.__project_documentation

    # функции для МАТЕРИАЛОВ
        # Добавление МАТЕРИАЛА в кортеж
    def set_material(self, new_material, index_order=None):
        id = 0
        while id in self.get_all_id_materials():
            id += 1
        new_material.set_id(id)
        self.__materials = list(self.__materials)
        self.setting_order_of_material(new_material, index_order)
        self.__materials = tuple(self.__materials)

        # Изменение порядкового номера МАТЕРИАЛА
    def change_order_of_material(self, material, index_order=None):
        self.__materials = list(self.__materials)
        self.__materials.remove(material)
        self.setting_order_of_material(material, index_order)
        self.__materials = tuple(self.__materials)

        # Установка порядкового номера МАТЕРИАЛА
    def setting_order_of_material(self, material, index_order=None):
        if index_order is not None:
            self.__materials.insert(index_order, material)
        else:
            type_material = material.get_type()
            list_materials = []
            for old_material in self.__materials:
                if old_material.get_type() == type_material:
                    list_materials.append(old_material)
            if not list_materials:
                self.__materials.append(material)
            else:
                index = self.__materials.index(list_materials[-1])
                self.__materials.insert(index+1, material)

        # Установка нового порядка всех материалов
    def setting_complete_material_order(self, order_materials):
        self.__materials = list(self.__materials)
        self.__materials.sort(key=lambda x: order_materials.index(x.get_in_list()))
        self.__materials = tuple(self.__materials)

        # Удаление МАТЕРИАЛА в кортеже
    def delete_material(self, index):
        self.__materials = list(self.__materials)
        del self.__materials[index]
        self.__materials = tuple(self.__materials)

        # Возвращение МАТЕРИАЛА из кортежа
    def get_material(self, index):
        return self.__materials[index]

        # Возвращение кортежа всех МАТЕРИАЛОВ
    def get_all_materials(self):
        return self.__materials

        # Возвращение всех ID МАТЕРИАЛОВ
    def get_all_id_materials(self):
        return tuple(material.get_id() for material in self.__materials)

        # Возвращение уникальных ТИПОВ МАТЕРИАЛОВ
    def get_all_unique_type_materials(self):
        all_unique_type_materials = set()
        for material in self.__materials:
            if material.get_type() is not None:
                all_unique_type_materials.add(material.get_type())
        return tuple(all_unique_type_materials)

        # Возвращение уникальных НАИМЕНОВАНИЙ МАТЕРИАЛОВ
    def get_all_unique_material_materials(self):
        all_unique_material_materials = set()
        for material in self.__materials:
            if material.get_material() is not None:
                all_unique_material_materials.add(material.get_material())
        return tuple(all_unique_material_materials)

        # Возвращение уникальных ИМЁН ДОКУМЕНТА МАТЕРИАЛОВ
    def get_all_unique_document_names_materials(self):
        all_unique_document_name_materials = set()
        for material in self.__materials:
            if material.get_document_name() is not None:
                all_unique_document_name_materials.add(material.get_document_name())
        return tuple(all_unique_document_name_materials)

        # Возвращение уникальных ИМЁН ДОКУМЕНТОВ (множественное число имени) МАТЕРИАЛОВ
    def get_all_unique_documents_names_materials(self):
        all_unique_documents_names_materials = set()
        for material in self.__materials:
            if material.get_documents_name() is not None:
                all_unique_documents_names_materials.add(material.get_documents_name())
        return tuple(all_unique_documents_names_materials)

        # Возвращение соответсвующего ИМЕНИ ДОКУМЕНТОВ (множественное число имени) МАТЕРИАЛОВ
    def get_corresponding_documents_name_materials(self, document_name):
        for material in self.__materials:
            if material.get_document_name() == document_name:
                return material.get_documents_name()

        # Возвращение всех материалов для таблицы
    def get_all_text_materials_table(self):
        return tuple(element.get_in_tabel() for element in self.__materials)

        # Возвращение всех материалов для списка
    def get_all_text_materials_list(self):
        return tuple(element.get_in_list() for element in self.__materials)

    # Функции для ДОКУМЕНТОВ СООТВЕТСТВИЯ
        # Добавление ДОКУМЕНТА СООТВЕТСТВИЯ в кортеж
    def set_document(self, new_document, index_order=None):
        id = 0
        while id in self.get_all_id_documents():
            id += 1
        new_document.set_id(id)
        self.__documents = list(self.__documents)
        self.setting_order_of_document(new_document, index_order)
        self.__documents = tuple(self.__documents)

        # Изменение порядкового номера ДОКУМЕНТА СООТВЕТСТВИЯ
    def change_order_of_document(self, document, index_order=None):
        self.__documents = list(self.__documents)
        self.__documents.remove(document)
        self.setting_order_of_document(document, index_order)
        self.__documents = tuple(self.__documents)

        # Установка порядкового номера ДОКУМЕНТА СООТВЕТСТВИЯ
    def setting_order_of_document(self, document, index_order=None):
        if index_order is not None:
            self.__documents.insert(index_order, document)
        else:
            document_name = document.get_document_name()
            list_documents = []
            list_documents_date = []
            for old_document in self.__documents:
                if old_document.get_document_name() == document_name:
                    list_documents.append(old_document)
            if not list_documents:
                self.__documents.append(document)
            elif document.get_start_date() is None:
                index = self.__documents.index(list_documents[-1])
                self.__documents.insert(index + 1, document)
            elif document.get_start_date() is not None:
                for el in list_documents:
                    if el.get_start_date() is not None:
                        list_documents_date.append(el)
                list_documents_date.append(document)
                list_documents_date.sort(key=lambda x: x.get_start_date().get_date())
                index_by_date = list_documents_date.index(document)
                if index_by_date == 0:
                    index = self.__documents.index(list_documents_date[index_by_date + 1])
                    self.__documents.insert(index, document)
                else:
                    index = self.__documents.index(list_documents_date[index_by_date - 1])
                    self.__documents.insert(index+1, document)


        # Установка нового порядка всех ДОКУМЕНТОВ СООТВЕТСТВИЯ
    def setting_complete_document_order(self, order_documents):
        self.__documents = list(self.__documents)
        self.__documents.sort(key=lambda x: order_documents.index(x.get_in_list()))
        self.__documents = tuple(self.__documents)

        # Удаление ДОКУМЕНТА СООТВЕТСТВИЯ в кортеже
    def delete_document(self, index):
        self.__documents = list(self.__documents)
        del self.__documents[index]
        self.__documents = tuple(self.__documents)

        # Возвращение ДОКУМЕНТА СООТВЕТСТВИЯ из кортежа
    def get_document(self, index):
        return self.__documents[index]

        # Возвращение кортежа всех ДОКУМЕНТОВ СООТВЕТСТВИЯ
    def get_all_documents(self):
        return self.__materials

        # Возвращение всех ID ДОКУМЕНТОВ СООТВЕТСТВИЯ
    def get_all_id_documents(self):
        return tuple(document.get_id() for document in self.__documents)

        # Возвращение уникальных ИМЁН ДОКУМЕНТОВ СООТВЕТСТВИЯ
    def get_all_unique_document_names_documents(self):
        all_unique_document_name_documents = set()
        for document in self.__documents:
            if document.get_document_name() is not None:
                all_unique_document_name_documents.add(document.get_document_name())
        return tuple(all_unique_document_name_documents)

        # Возвращение уникальных ИМЁН ДОКУМЕНТОВ (множественное число имени) ДОКУМЕНТОВ СООТВЕТСТВИЯ
    def get_all_unique_documents_names_documents(self):
        all_unique_documents_names_documents = set()
        for document in self.__documents:
            if document.get_documents_name() is not None:
                all_unique_documents_names_documents.add(document.get_documents_name())
        return tuple(all_unique_documents_names_documents)

        # Возвращение соответсвующего ИМЕНИ ДОКУМЕНТОВ (множественное число имени) ДОКУМЕНТА СООТВЕТСТВИЯ
    def get_corresponding_documents_name_documents(self, document_name):
        for document in self.__documents:
            if document.get_document_name() == document_name:
                return document.get_documents_name()

        # Возвращение всех ДОКУМЕНТОВ СООТВЕТСТВИЯ для таблицы
    def get_all_text_documents_table(self):
        return tuple(element.get_in_tabel() for element in self.__documents)

        # Возвращение всех ДОКУМЕНТОВ СООТВЕТСТВИЯ для списка
    def get_all_text_documents_list(self):
        return tuple(element.get_in_list() for element in self.__documents)

    # Функции для классификаций
        # Назначение классификации
    def set_name_classification(self, name_classification):
        self.__names_classifications = list(self.__names_classifications)
        self.__names_classifications.append(name_classification)
        self.__names_classifications = tuple(self.__names_classifications)

        # Вернуть НАИМЕНОВАНИЯ ВСЕХ КЛАССИФИКАЦИЙ
    def get_all_names_classifications(self):
        return self.__names_classifications

        # Вернуть все НАИМЕНОВАНИЯ КЛАССИФИКАЦИЙ в АКТЕ
    def get_keys_classifications_akt(self, index_akt):
        keys_classifications = list(self.__akts[index_akt].get_keys_classifications())
        keys_classifications.sort(key=lambda x: self.__names_classifications.index(x))
        return tuple(keys_classifications)

        # Вернуть все КЛАССИФИКАЦИИ (КЛАССЫ) по НАИМЕНОВАНИЮ КЛАССИФИКАЦИИ
    def get_all_classifications_by_key(self, name_classification):
        list_classifications = []
        for akt in self.__akts:
            list_classifications.append(akt.get_values_classifications(name_classification))
        list_classifications = set(list_classifications)
        list_classifications = list(list_classifications)
        list_classifications.sort()
        return tuple(list_classifications)

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
        self.__documentation = None
        self.__materials = ()
        self.__documents = ()
        self.__start_date = None
        self.__finish_date = None
        self.__regulations = ()
        self.__next_work = ()
        self.__additional_information = None
        self.__number_of_copies = None
        self.__classifications = dict()

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
    def set_name_work(self, obj):
        self.__work = obj

    def get_name_work(self):
        return self.__work

    # функции для МАТЕРИАЛОВ
    def set_materials_of_akt(self, materials):
        self.__materials = materials

    def set_material_of_akt(self, material):
        self.__materials = list(self.__materials)
        self.__materials.append(material)
        self.__materials = tuple(self.__materials)

    def get_all_materials_of_akt(self):
        return self.__materials

    def get_material_of_akt(self, index_material):
        return self.__materials[index_material]

    def get_text_all_materials_of_akt(self):
        return tuple(element.get_in_list() for element in self.__materials)

    # функции для ДОКУМЕНТОВ СООСТВЕТСВИЯ
    def set_documents_of_akt(self, documents):
        self.__documents = documents

    def set_document_of_akt(self, document):
        self.__documents = list(self.__documents)
        self.__documents.append(document)
        self.__documents = tuple(self.__documents)

    def get_all_documents_of_akt(self):
        return self.__documents

    def get_document_of_akt(self, index_document):
        return self.__documents[index_document]

    def get_text_all_documents_of_akt(self):
        return tuple(element.get_in_list() for element in self.__documents)

    # функции для ДАТ
    def set_object_start_date(self, start_date):
        self.__start_date = start_date

    def set_object_finish_date(self, finish_date):
        self.__finish_date = finish_date

    def set_start_date(self, str_start_date):
        self.__start_date = Date(str_start_date)

    def set_finish_date(self, str_finish_date):
        self.__finish_date = Date(str_finish_date)

        # добавление даты начала и окончания работ в акт
    def add_deadline(self, str_start_date, str_finish_date):
        try:
            if str_start_date is None and str_finish_date is None:
                self.__start_date = None
                self.__finish_date = None
            elif str_start_date is None:
                self.__finish_date = Date(str_finish_date)
                self.__start_date = None
                return
            elif str_finish_date is None:
                self.__start_date = Date(str_start_date)
                self.__finish_date = None
                return
            else:
                self.__start_date = Date(str_start_date)
                self.__finish_date = Date(str_finish_date)
        except (KeyError, IndexError):
            return

    def get_start_date(self):
        return self.__start_date

    def get_finish_date(self):
        return self.__finish_date

        # возвращение строки даты начала для акта
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
            str_date = str(self.__start_date.get_date().strftime('%d.%B.%Y'))
            date1 = str_date.split('.')
            return f'«{date1[0]}» {dictionary[date1[1]]} {date1[2]} г.'

        # возвращение строки даты начала для акта
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
            str_date = str(self.__finish_date.get_date().strftime('%d.%B.%Y'))
            date1 = str_date.split('.')
            return f'«{date1[0]}» {dictionary[date1[1]]} {date1[2]} г.'

    # функции для ПРОЕКТНО-СМЕТНОЙ ДОКУМЕНТАЦИИ
    def set_documentation(self, documentation):
        self.__documentation = documentation

    def get_documentation(self):
        return self.__documentation

    # функция для ВОЗВРАЩЕНИЯ ТЕКСТА С ДОКУМЕНТАЦИЕЙ
    def get_text_of_documentation(self):
        # первая проверка организации
        def first_check_org(text_of_doc, org, name_doc):
            if org == '':
                text_of_doc += name_doc
            else:
                text_of_doc += org + ' ' + name_doc
            return text_of_doc, False

        # проверка организации
        def check_org(analyzed_doc_list, text_of_doc, org, name_doc):
            if org == analyzed_doc_list[-3] and org != '':
                text_of_doc += ', ' + name_doc
                return text_of_doc
            elif org == '':
                text_of_doc += '; ' + name_doc
                return text_of_doc
            else:
                text_of_doc += '; ' + org + ' ' + name_doc
                return text_of_doc

        # проверка содержания страниц
        def check_page(text_of_doc, page):
            if page == '':
                return text_of_doc
            elif page[0] == '"':
                text_of_doc += ' л. ' + page[1:]
            else:
                text_of_doc += ' л. ' + page
            return text_of_doc

        analyzed_doc_list = []
        text_of_doc = ''
        first_doc = True
        for doc in self.__documentation:

            org = doc.get_organization().get_name()
            if org is None:
                org = doc.get_organization().get_text()

            name_doc = doc.get_name_doc().get_text()

            page = doc.get_page()

            if first_doc:
                text_of_doc, first_doc = first_check_org(text_of_doc, org, name_doc)
            else:
                text_of_doc = check_org(analyzed_doc_list, text_of_doc, org, name_doc)

            text_of_doc = check_page(text_of_doc, page)

            analyzed_doc_list.append(org)
            analyzed_doc_list.append(name_doc)
            analyzed_doc_list.append(page)

        return text_of_doc + '.'

    # Функции для ТЕХНИЧЕСКИХ РЕГЛАМЕНТОВ
    def set_regulations(self, regulations):
        self.__regulations = tuple(regulations)

    def get_regulations(self):
        return self.__regulations

    # Функции для ПОСЛЕДУЮЩИХ РАБОТ
    def set_next_work(self, list_next_work):
        self.__next_work = tuple(list_next_work)

    def add_next_work(self, next_work):
        self.__next_work = list(self.__next_work)
        self.__next_work.append(next_work)
        self.__next_work = tuple(self.__next_work)

    def get_next_work(self):
        return self.__next_work

    # Функции для ДОПОЛНИТЕЛЬНЫХ СВЕДЕНИЙ
    def set_additional_information(self, additional_information):
        self.__additional_information = additional_information

    def get_additional_information(self):
        return self.__additional_information

    # Функции для КОЛИЧЕСТВО ЭКЗЕМПЛЯРОВ
    def set_number_of_copies(self, number_of_copies):
        self.__number_of_copies = number_of_copies

    def get_number_of_copies(self):
        return self.__number_of_copies

    # Функции для КЛАССИФИКАЦИИ
    def set_classification(self, classifications):
        self.__classifications = classifications

    def add_classification(self, name_classification, classification):
        self.__classifications[name_classification] = classification

    def get_dict_classifications(self):
        return self.__classifications

    def get_values_classifications(self, key):
        return self.__classifications[key]

    def get_keys_classifications(self):
        return tuple(self.__classifications.keys())


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

class Date:
    def __init__(self, str_date):
        self.__Object_date = self.set_date(str_date)

    # создание объекта дата из строки в объект модуля Date
    def set_date(self, str_date):

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
                          'мая': int(5),
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

    # возвращение объекта дата
    def get_date(self):
        return self.__Object_date

class Material:
    def __init__(self, type=None, material=None, document_name=None, documents_name=None,
                 document_number=None, start_date=None, finish_date=None):
        self.__id = None
        self.__type = type
        self.__material = material
        self.__document_name = document_name
        self.__documents_name = documents_name
        self.__document_number = document_number
        self.__start_date = start_date
        self.__finish_date = finish_date
        self.__bin_images = None

    def set_id(self, id):
        self.__id = id

    def set_type(self, type):
        self.__type = type

    def set_material(self, material):
        self.__material = material

    def set_document_name(self, document_name):
        self.__document_name = document_name

    def set_documents_name(self, documents_name):
        self.__documents_name = documents_name

    def set_document_number(self, document_number):
        self.__document_number = document_number

    def set_str_start_date(self, str_start_date):
        self.__start_date = Date(str_start_date)

    def set_str_finish_date(self, str_finish_date):
        self.__finish_date = Date(str_finish_date)

    def set_object_start_date(self, object_start_date):
        self.__start_date = object_start_date

    def set_object_finish_date(self, object_finish_date):
        self.__finish_date = object_finish_date

    def load_bin_images(self, path_file):
        if path_file is None:
            return
        file = fitz.open(path_file)
        list_image = []
        for page in file:
            list_image.append(page.get_pixmap().tobytes("ppm"))
        self.__bin_images = pickle.dumps(tuple(list_image))

    def set_bin_images(self, bin_file):
        self.__bin_images = bin_file

    def add_deadline(self, str_start_date, str_finish_date):
        try:
            if str_start_date is None and str_finish_date is None:
                self.__start_date = None
                self.__finish_date = None
            elif str_start_date is None:
                self.__finish_date = Date(str_finish_date)
                self.__start_date = None
            elif str_finish_date is None:
                self.__start_date = Date(str_start_date)
                self.__finish_date = None
            else:
                self.__start_date = Date(str_start_date)
                self.__finish_date = Date(str_finish_date)
        except (KeyError, IndexError):
            return

    def get_id(self):
        return self.__id

    def get_type(self):
        return self.__type

    def get_material(self):
        return self.__material

    def get_document_name(self):
        return self.__document_name

    def get_documents_name(self):
        return self.__documents_name

    def get_document_number(self):
        return self.__document_number

    def get_start_date(self):
        return self.__start_date

    def get_finish_date(self):
        return self.__finish_date

    def get_in_tabel(self):

        # Проверка ВИДА материала
        def check_type(type):
            if type is None:
                return ''
            else:
                return type

        # Проверка ДОКУМЕНТА материала
        def check_data_document(document_name, document_number):
            if document_name is None and document_number is None:
                return ''
            elif document_number is None:
                return document_name
            else:
                return document_name + ' ' + document_number

        # Проверка ДАТ ДОКУМЕНТА материала
        def check_dates(start_date, finish_date):
            if start_date is None:
                return ''
            elif finish_date is None:
                return 'от ' + self.get_str_start_date()
            else:
                return 'с ' + self.get_str_start_date() + ' до ' + self.get_str_finish_date()

        # Проверка изображения
        def check_images(images):
            if images is not None:
                return '<Есть загруженный файл>'
            else:
                return '<Файл не загружен>'

        elements_material = []
        elements_material.append(self.__id)
        elements_material.append(check_type(self.__type))
        elements_material.append(self.__material)
        elements_material.append(check_data_document(self.__document_name, self.__document_number))
        elements_material.append(check_dates(self.__start_date, self.__finish_date))
        elements_material.append(check_images(self.__bin_images))
        return tuple(elements_material)

        # возвращение строки даты начала для акта
    def get_str_start_date(self):
        if self.__start_date == '' or self.__start_date is None:
            return None
        else:
            str_date = str(self.__start_date.get_date().strftime('%d.%m.%Y'))
            date1 = str_date.split('.')
            return f'{date1[0]}.{date1[1]}.{date1[2]}'

        # возвращение строки даты начала
    def get_str_finish_date(self):
        if self.__finish_date == '' or self.__finish_date is None:
            return None
        else:
            str_date = str(self.__finish_date.get_date().strftime('%d.%m.%Y'))
            date1 = str_date.split('.')
            return f'{date1[0]}.{date1[1]}.{date1[2]}'

        # возвращение изобажений
    def get_bin_images(self):
        if self.__bin_images is not None:
            return pickle.loads(self.__bin_images)
        else:
            return None

        # удаление изобажений
    def del_bin_images(self):
        self.__bin_images = None

    def get_in_list(self):
        # Проверка ВИДА материала
        def check_type_and_material(type, material):
            if type is None or type == material:
                return material
            else:
                return f'{type} {material}'

        # Проверка ДОКУМЕНТА материала
        def check_data_document(document_name, document_number):
            if document_name is None and document_number is None:
                return ''
            elif document_number is None:
                return document_name
            else:
                return document_name + ' ' + document_number

        # Проверка ДАТ ДОКУМЕНТА материала
        def check_dates(start_date, finish_date):
            if start_date is None:
                return ''
            elif finish_date is None:
                return 'от ' + self.get_str_start_date()
            else:
                return 'с ' + self.get_str_start_date() + ' до ' + self.get_str_finish_date()

        material = (f'{check_type_and_material(self.__type, self.__material)}' +
                    f' {check_data_document(self.__document_name, self.__document_number)}' +
                    f' {check_dates(self.__start_date, self.__finish_date)}')

        return material


class Data_base_materials:
    def __init__(self, connection):
        self.__conn = connection
        self.__cur = self.__conn.cursor()
        self.__cur.execute('''CREATE TABLE IF NOT EXISTS materials (ItemID INTEGER PRIMARY KEY NOT NULL,
                                type TEXT,
                                material TEXT,
                                document_name TEXT,
                                documents_name TEXT,
                                document_number TEXT,
                                start_date TEXT,
                                finish_date TEXT,
                                file BLOB)''')

        # Выдать всю базу данных
    def extract_all_data_from_database(self):
        self.__cur.execute('''SELECT * FROM materials''')
        return self.__cur.fetchall()

        # Добавить новый материал в базу данных
    def insert_data(self, type, material, document_name, documents_name, document_number, start_date, finish_date,
                    path_file):
        if path_file is None:
            self.__cur.execute('''INSERT INTO materials(type, material, document_name, documents_name, document_number,
                                            start_date, finish_date) VALUES (?, ?, ?, ?, ?, ?, ?)''',
                               (type, material, document_name, documents_name, document_number, start_date,
                                finish_date))
        else:
            file = fitz.open(path_file)
            list_image = []
            for page in file:
                list_image.append(page.get_pixmap().tobytes("ppm"))
            file_bin = pickle.dumps(tuple(list_image))
            self.__cur.execute('''INSERT INTO materials(type, material, document_name, documents_name, document_number,
                                start_date, finish_date, file) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                               (type, material, document_name, documents_name, document_number, start_date, finish_date,
                                file_bin))

        # Изменить материал в базе данных
    def change_data(self, material_id, type, material, document_name, documents_name, document_number, start_date,
                    finish_date, path_file):
        if path_file is None:
            self.__cur.execute('''UPDATE materials
                                        SET type = ?,
                                            material = ?,
                                            document_name = ?,
                                            documents_name = ?,
                                            document_number = ?,
                                            start_date = ?,
                                            finish_date = ?
                                        WHERE ItemID == ?''',
                               (type, material, document_name, documents_name, document_number, start_date, finish_date,
                                material_id))
        else:
            file = fitz.open(path_file)
            list_image = []
            for page in file:
                list_image.append(page.get_pixmap().tobytes("ppm"))
            file_bin = pickle.dumps(tuple(list_image))
            self.__cur.execute('''UPDATE materials
                                SET type = ?,
                                    material = ?,
                                    document_name = ?,
                                    documents_name = ?,
                                    document_number = ?,
                                    start_date = ?,
                                    finish_date = ?,
                                    file = ?
                                WHERE ItemID == ?''',
                               (type, material, document_name, documents_name, document_number, start_date, finish_date,
                                file_bin, material_id))

        # Удаление материала по ID
    def delete_data(self, material_id):
        self.__cur.execute('''DELETE FROM materials WHERE ItemID = ?''', (material_id,))

        # Выборка материалов для поиска
    def selection_materials_for_search(self, search):
        self.__cur.execute(f'''SELECT * FROM materials
                            WHERE type LIKE "%{search}%" OR
                            material LIKE "%{search}%" OR
                            document_name LIKE "%{search}%" OR
                            documents_name LIKE "%{search}%" OR
                            document_number LIKE "%{search}%" OR
                            start_date LIKE "%{search}%" OR
                            finish_date LIKE "%{search}%"''')# (search, search, search, search, search, search, search))
        return self.__cur.fetchall()

        # Выборка материалов для сортироваки в таблицы
    def selection_materials_for_table(self, material_names, document_number, column_for_order):
        str_request_material = ''
        str_request_document_number = ''
        str_where = 'WHERE'
        str_and1 = ' AND '

        for el in material_names:
            str_request_material += f'material != "{el}" AND '
        if str_request_material != '':
            str_request_material = '(' + str_request_material[:-5] + ')'

        for el in document_number:
            str_request_document_number += f'document_number != "{el}" AND '
        if str_request_document_number != '':
            str_request_document_number = '(' + str_request_document_number[:-5] + ')'

        if str_request_material == '' and str_request_document_number == '':
            str_where = ''
            str_and1 = ''
        elif str_request_material == '' or str_request_document_number == '':
            str_and1 = ' '

        if column_for_order is not None:
            str_order = f'ORDER BY {column_for_order}'
        else:
            str_order = ''
        self.__cur.execute(f'''SELECT * FROM materials
                            {str_where} {str_request_material}{str_and1}{str_request_document_number}
                            {str_order}''')
        return self.__cur.fetchall()

        # Выборка материалов по столбцу и условию
    def selection_materials(self, column, condition):
        self.__cur.execute(f'''SELECT * FROM materials WHERE {column} == ?''', (condition,))
        return self.__cur.fetchall()

        # Найти материал по ID
    def material_selection_by_id(self, material_id):
        self.__cur.execute('''SELECT * FROM materials WHERE ItemID == ?''', (material_id,))
        return self.__cur.fetchone()

        # Выдать все ID материалов из базы данных
    def all_id_material(self):
        self.__cur.execute('''SELECT ItemID FROM materials''')
        result = self.__cur.fetchall()
        list_id = []
        for el in result:
            list_id.append(el[0])
        return tuple(list_id)

        # Выдать все типы материалов из базы данных
    def all_type_material(self):
        self.__cur.execute('''SELECT type FROM materials''')
        result = self.__cur.fetchall()
        list_type = []
        for el in result:
            list_type.append(el[0])
        list_type = set(list_type)
        list_type = list(list_type)
        list_type.sort()
        return tuple(list_type)

        # Выдать все наименования материалов из базы данных
    def all_name_material(self, type_material=None):
        if type_material is None:
            self.__cur.execute('''SELECT material FROM materials''')
        else:
            self.__cur.execute('''SELECT material FROM materials WHERE type == ?''', (type_material,))
        result = self.__cur.fetchall()
        list_material = []
        for el in result:
            list_material.append(el[0])
        list_material = set(list_material)
        list_material = list(list_material)
        list_material.sort()
        return tuple(list_material)

        # Выдать все наименования документов из базы данных
    def all_document_name(self):
        self.__cur.execute('''SELECT document_name FROM materials''')
        result = self.__cur.fetchall()
        list_document_name = []
        for el in result:
            list_document_name.append(el[0])
        list_document_name = set(list_document_name)
        list_document_name = list(list_document_name)
        list_document_name.sort()
        return tuple(list_document_name)

        # Выдать все номера документов из базы данных
    def all_document_number(self, document_name=None):
        if document_name is None:
            self.__cur.execute('''SELECT document_number FROM materials''')
        else:
            self.__cur.execute('''SELECT document_number FROM materials WHERE document_name == ?''', (document_name,))
        result = self.__cur.fetchall()
        list_document_number = []
        for el in result:
            list_document_number.append(el[0])
        list_document_number = set(list_document_number)
        list_document_number = list(list_document_number)
        list_document_number.sort()
        return tuple(list_document_number)

        # Выдать все даты начала документов
    def all_start_date(self):
        self.__cur.execute('''SELECT start_date FROM materials''')
        result = self.__cur.fetchall()
        list_start_date = []
        for el in result:
            list_start_date.append(el[0])
        list_start_date = set(list_start_date)
        list_start_date = list(list_start_date)
        return tuple(list_start_date)

        # Выдать все даты окончания документов
    def all_finish_date(self):
        self.__cur.execute('''SELECT finish_date FROM materials''')
        result = self.__cur.fetchall()
        list_finish_date = []
        for el in result:
            if el[0] is not None:
                list_finish_date.append(el[0])
        list_finish_date = set(list_finish_date)
        list_finish_date = list(list_finish_date)
        list_finish_date.sort()
        return tuple(list_finish_date)

        # Выдать файл материала
    def get_file_material(self, material_id):
        self.__cur.execute('''SELECT file FROM materials WHERE ItemID == ?''', (material_id,))
        file_bit = self.__cur.fetchone()
        file = pickle.loads(file_bit[0])
        return file

        # Выдать материал для экспорта в исполнительную документацию
    def material_export(self, material_id):
        self.__cur.execute('''SELECT * FROM materials WHERE ItemID == ?''', (material_id,))
        data_material = list(self.__cur.fetchone())
        if data_material[6] is not None:
            data_material[6] = Date(data_material[6])
        if data_material[7] is not None:
            data_material[7] = Date(data_material[6])
        return tuple(data_material)

        # Удалить файл материала с записи
    def del_file_material(self, material_id):
        self.__cur.execute('''UPDATE materials SET file = NULL WHERE ItemID == ?''', (material_id,))

        # Сохранить базу данных
    def commit_data_base(self):
        self.__conn.commit()

        # Отключить базу данных
    def close_date_base(self):
        self.__conn.close()


class Document:
    def __init__(self, document_name=None, documents_name=None, document_number=None, start_date=None,
                 finish_date=None):
        self.__id = None
        self.__document_name = document_name
        self.__documents_name = documents_name
        self.__document_number = document_number
        self.__start_date = start_date
        self.__finish_date = finish_date
        self.__bin_images = None

    def set_id(self, id):
        self.__id = id

    def set_document_name(self, document_name):
        self.__document_name = document_name

    def set_documents_name(self, documents_name):
        self.__documents_name = documents_name

    def set_document_number(self, document_number):
        self.__document_number = document_number

    def set_str_start_date(self, str_start_date):
        self.__start_date = Date(str_start_date)

    def set_str_finish_date(self, str_finish_date):
        self.__finish_date = Date(str_finish_date)

    def set_object_start_date(self, object_start_date):
        self.__start_date = object_start_date

    def set_object_finish_date(self, object_finish_date):
        self.__finish_date = object_finish_date

    def load_bin_images(self, path_file):
        if path_file is None:
            return
        file = fitz.open(path_file)
        list_image = []
        for page in file:
            list_image.append(page.get_pixmap().tobytes("ppm"))
        self.__bin_images = pickle.dumps(tuple(list_image))

    def set_bin_images(self, bin_file):
        self.__bin_images = bin_file

    def add_deadline(self, str_start_date, str_finish_date):
        try:
            if str_start_date is None and str_finish_date is None:
                self.__start_date = None
                self.__finish_date = None
            elif str_start_date is None:
                self.__finish_date = Date(str_finish_date)
                self.__start_date = None
            elif str_finish_date is None:
                self.__start_date = Date(str_start_date)
                self.__finish_date = None
            else:
                self.__start_date = Date(str_start_date)
                self.__finish_date = Date(str_finish_date)
        except (KeyError, IndexError):
            return

    def get_id(self):
        return self.__id

    def get_document_name(self):
        return self.__document_name

    def get_documents_name(self):
        return self.__documents_name

    def get_document_number(self):
        return self.__document_number

    def get_start_date(self):
        return self.__start_date

    def get_finish_date(self):
        return self.__finish_date

    def get_in_tabel(self):

        # Проверка НАИМЕНОВАНИЯ ДОКУМЕНТА
        def check_data_document(document_name, document_number):
            if document_name is None and document_number is None:
                return ''
            elif document_number is None:
                return document_name
            else:
                return document_name + ' ' + document_number

        # Проверка ДАТ ДОКУМЕНТА
        def check_dates(start_date, finish_date):
            if start_date is None:
                return ''
            elif finish_date is None:
                return 'от ' + self.get_str_start_date()
            else:
                return 'с ' + self.get_str_start_date() + ' до ' + self.get_str_finish_date()

        # Проверка изображения
        def check_images(images):
            if images is not None:
                return '<Есть загруженный файл>'
            else:
                return '<Файл не загружен>'

        elements_document = []
        elements_document.append(self.__id)
        elements_document.append(check_data_document(self.__document_name, self.__document_number))
        elements_document.append(check_dates(self.__start_date, self.__finish_date))
        elements_document.append(check_images(self.__bin_images))
        return tuple(elements_document)

    def get_str_start_date(self):
        if self.__start_date == '' or self.__start_date is None:
            return None
        else:
            str_date = str(self.__start_date.get_date().strftime('%d.%m.%Y'))
            date1 = str_date.split('.')
            return f'{date1[0]}.{date1[1]}.{date1[2]}'

        # возвращение строки даты начала
    def get_str_finish_date(self):
        if self.__finish_date == '' or self.__finish_date is None:
            return None
        else:
            str_date = str(self.__finish_date.get_date().strftime('%d.%m.%Y'))
            date1 = str_date.split('.')
            return f'{date1[0]}.{date1[1]}.{date1[2]}'

        # возвращение изобажений
    def get_bin_images(self):
        if self.__bin_images is not None:
            return pickle.loads(self.__bin_images)
        else:
            return None

        # удаление изобажений
    def del_bin_images(self):
        self.__bin_images = None

    def get_in_list(self):
        # Проверка наименования ДОКУМЕНТА
        def check_data_document(document_name, document_number):
            if document_name is None and document_number is None:
                return ''
            elif document_number is None:
                return document_name
            else:
                return document_name + ' ' + document_number

        # Проверка ДАТ ДОКУМЕНТА
        def check_dates(start_date, finish_date):
            if start_date is None:
                return ''
            elif finish_date is None:
                return 'от ' + self.get_str_start_date()
            else:
                return 'с ' + self.get_str_start_date() + ' до ' + self.get_str_finish_date()

        document = (f' {check_data_document(self.__document_name, self.__document_number)}' +
                    f' {check_dates(self.__start_date, self.__finish_date)}')

        return document


# Сравнение дат
def date_comparison(start_date, finish_date):
    if start_date.get_date() <= finish_date.get_date():
        return False
    elif start_date.get_date() > finish_date.get_date():
        return True

if __name__ == '__main__':
    pass
