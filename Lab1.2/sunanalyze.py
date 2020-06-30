# импорт нужных функций
from matplotlib import pyplot
from openpyxl import load_workbook

# выгрузка данных из файла excel в интерпритатор
wd = load_workbook('data_analysis_lab.xlsx')

# перенос листа "Data" в переменную sheet в виде словаря
sheet = wd['Data']


# создание функции вызова конкретного значения
def getval(x):
    return x.value


# Выгрузка в переменные списков из словаря(sheet), sheet['A'][1:] это слайсинг словаря(листа Excel) по ключу A(столбец А) за исключением первого значения списка(первой строки)
ye = list(map(getval, sheet['A'][1:]))
te = list(map(getval, sheet['C'][1:]))
sa = list(map(getval, sheet['D'][1:]))

g1 = pyplot.plot(ye, te)
g2 = pyplot.plot(ye, sa)
pyplot.show()
