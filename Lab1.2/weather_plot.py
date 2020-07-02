def getvalue(x): return x.value

from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']

years = list(map(getvalue, sheet['A'][1:]))
rel_temp = list(map(getvalue, sheet['C'][1:]))
sun_act = list(map(getvalue, sheet['D'][1:]))

pyplot.plot(years, sun_act, label="Солнечная активность") 
pyplot.plot(years, rel_temp, label="Относительная температура") 
pyplot.show() 