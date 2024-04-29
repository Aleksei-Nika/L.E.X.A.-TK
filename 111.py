#import locale
#locale.setlocale(locale.LC_ALL, 'ru_RU')
from datetime import datetime
from datetime import date
from datetime import time
'''
def f_str_date(y):
    dictionary = {'January':'январь',
                  'February':'февраль',
                  'March':'март',
                  'April':'апрель',
                  'May':'май',
                  'June':'июнь',
                  'July':'июль',
                  'August':'август',
                  'September':'сентябрь',
                  'October':'октябрь',
                  'November':'ноябрь',
                  'December':'декабрь'}

    str_date = str(y.strftime('%d.%B.%Y'))
    date1 = str_date.split('.')
    return f'«{date1[0]}» {dictionary[date1[1]]} {date1[2]} г.'
'''

class Date_akt:
    def __init__(self, date):
        self.__date = date
        self.__str_date = self.f_str_date(date)

    def f_str_date(self, y):
        dictionary = {'January':'январь',
                  'February':'февраль',
                  'March':'март',
                  'April':'апрель',
                  'May':'май',
                  'June':'июнь',
                  'July':'июль',
                  'August':'август',
                  'September':'сентябрь',
                  'October':'октябрь',
                  'November':'ноябрь',
                  'December':'декабрь'}
        str_date = str(y.strftime('%d.%B.%Y'))
        date1 = str_date.split('.')
        return f'«{date1[0]}» {dictionary[date1[1]]} {date1[2]} г.'

    def get_date(self):
        return self.__date
    def get_str_date(self):
        return self.__str_date
    def __str__(self):
        return self.__str_date

x = []
'''
date_input = input('Введите дату: ')
date_str = date_input.split('.')
x.append(Date_akt(date(date_str[2], date_str[1], date_str[0]))
day = input('Введите число: ')
'''
day = input('Введите число: ')
while day != '':
    day = int(day)
    month  = int(input('Введите месяц: '))
    year = int(input('Введите год: '))
    x.append(Date_akt(date(year, month, day)))
    day = input('Введите число: ')

x.sort(key = lambda date_akt: date_akt.get_date(), reverse = False)

print(x)
for data in x:
    print(data)
