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
df = pd.read_csv("/Users/luisquinonespr/code/hw4/data/covid.csv")

for i in ['Deaths', 'Confirmed']:
    for n in [500,1000,5000]:
        rows = df[i] > n
        avg = df[rows][i].mean()
        print('Average number of deaths greater than ' + str(n) + ": " + str(avg))
        print(df[rows][['Country', i]])
