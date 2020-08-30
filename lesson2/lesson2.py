import datetime

import inflect

# 1
print('Task 1')
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
set1 = set(my_list_1)
set2 = set(my_list_2)
resultList = set1 - set2
print(resultList)

# 2
print('Task 2')
# dateUnformatted = '02.11.2013'
# day = dateUnformatted[:dateUnformatted.find('.')]
# month = dateUnformatted[dateUnformatted.find('.')+1:dateUnformatted.find('.', 3)]
# year = dateUnformatted[dateUnformatted.find('.', 3)+1:]
# Here is supposed to be some logic that maps days and months thought dictionaries: 01 into 'first' or '11' into 'november'.
# The task implies <direct> mapping, but it is waste of time.
# Тут должна быть логика маппинга дней и месяцев из числового представления в строковое через справочники.
# Мапить напрямую лень, импортнул функцию

dateStrUnformatted = '02.11.2013'
dateObj = datetime.datetime.strptime(dateStrUnformatted, '%d.%m.%Y')

dayName = dateObj.strftime("%A")
dayNumber = dateObj.strftime("%d")
dayStrNumber = inflect.engine().ordinal(dayNumber)
month = dateObj.strftime("%B")
year = dateObj.strftime("%Y")
print('{} of {} {} - {}'.format(dayStrNumber, month, year, dayName))

# 3
print('Task 2')
my_list_3 = [2, 2, 5, 12, 8, 2, 12]
resulted_list = []
for item in my_list_3:
    if my_list_3.count(item) == 1:
        resulted_list.append(item)
print(resulted_list)
