###############
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# respectively.
# Follow DRY principles in order to complete this exercise.
#
#
# #

import pandas as pd

covid =pd.read_csv('/Users/luisquinonespr/code/hw4/data/covid.csv', sep=',', low_memory=False)
covid['Death rate']=covid['Deaths']/covid['Confirmed']

for i in ['Death rate']:
    for n in [500, 1000, 5000]:
        rows=covid['Active'] > n
        deathrate = covid['Death rate'][rows].mean()
        print('Mean death rate for countries  ' + str(n) + ' active cases' + ': ' + "{:.2%}".format(deathrate))
        print(covid[rows][['Country']])
