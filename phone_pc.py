# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 21:46:03 2018

@author: The
"""

import pandas as pd
import pylab as plt

PATH = "C:/Users/HP/Desktop/PC-Phones-per100-master/"


'''Daten als Dataframes einlesen'''
df_pc = pd.read_excel(PATH+"pc.xlsx", index_col=0)
df_phone = pd.read_excel(PATH+"phone.xlsx", index_col=0)

'''Indexnamen kürzen'''
df_phone.index.name = "Mobile phones per 100"

'''df.phone hat Strings als Index! - Umwandlung zu Integer'''
ncol = [int(x) for x in df_phone.columns]
df_phone.set_axis(axis=1, labels=ncol, inplace=True)

'''Jahre auswählen'''
years = list(range(1994,2007))
df_pc_years = df_pc[years]
df_phone_years = df_phone[years]

'''hierarchischen Index erstellen'''
sdf_pc_years = df_pc_years .stack()
sdf_phone_years = df_phone_years .stack()

'''Series zu Dataframe verbinden, mithilfe eines dictionaries'''
d = {'PC': sdf_pc_years, 'Phones': sdf_phone_years}
df_years = pd.DataFrame(data=d)
df_years = df_years.stack()
df_years = df_years.unstack((1,2))

#df_years.to_csv('data.csv')
'''Länderauswahl treffen'''
länderliste1 = ['Germany','Russia','United States','China','United Kingdom','Japan']
länderliste2 = ['France','Australia','Bolivia','Ghana']
länderliste3 = ['Austria','Hungary','Germany']

countries = länderliste3

def scatterplot(list):
    for country in list[:]:
        plt.scatter(df_years.loc[country].unstack(1)['PC'], df_years.loc[country].unstack(1)['Phones'], label=country)
    plt.legend()
    plt.ylabel('Mobile Phones')
    plt.xlabel('PC')
    plt.axis([0,100,0,150])
    plt.grid(True)
    plt.title('Entwicklung der Gerätezahlen von 1994 bis 2006 pro 100 Einwohner')
    plt.savefig('scatter_94bis06PCvsPhones.png')
    plt.show()

def lineplot_pc(list):
    for country in list[:]:
        plt.plot(df_years.loc[country].unstack(1).index, df_years.loc[country].unstack(1)['PC'], label=country)
    plt.legend()
    plt.ylabel('PC')
    plt.xlabel('Jahre')
    plt.axis([1994, 2006, 0,150])
    plt.grid(True)
    plt.title('Entwicklung der Gerätezahlen von 1994 bis 2006 pro 100 Einwohner')
    plt.savefig('lineplot_pc.png')
    plt.show()

def lineplot_phones(list):
    for country in list[:]:
        plt.plot(df_years.loc[country].unstack(1).index, df_years.loc[country].unstack(1)['Phones'], label=country)
    plt.legend()
    plt.ylabel('Mobile Phones')
    plt.xlabel('Jahre')
    plt.axis([1994, 2006, 0,150])
    plt.grid(True)
    plt.title('Entwicklung der Gerätezahlen von 1994 bis 2006 pro 100 Einwohner')
    plt.savefig('lineplot_phones.png')
    plt.show()
 
    
'''Plots erstellen'''   
scatterplot(countries)
lineplot_pc(countries)
lineplot_phones(countries)
