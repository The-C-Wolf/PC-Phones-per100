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

countries = länderliste2

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

#df_years[2006]['PC'] #Jahr und Gerät auswählen
#df = df.stack() #Indizes aufstapeln
#df3 = df.unstack(1) #breite Tabelle erstellen

#df3.index.names = ['Countries', 'Devices'] #multiIndex schöner machen

#df3.plot.bar(figsize=(10,18))
#plt.savefig('Countries_Devices_over_years_barplot.png')

#df_1994 = df3[1994].unstack(1) #Jahr 1994 auswählen
#df_1998 = df3[1998].unstack(1) #Jahr 2000 auswählen
#df_2002 = df3[2002].unstack(1) #Jahr 2002 auswählen
#df_2006 = df3[2006].unstack(1) #Jahr 2006 auswählen


#df_1994.plot.bar(figsize=(6,5))
#plt.savefig('1994_Balken.png')
#df_1998.plot.bar(figsize=(6,5))
#plt.savefig('1998_Balken.png')
#df_2002.plot.bar(figsize=(6,5))
#plt.savefig('2002_Balken.png')
#df_2006.plot.bar(figsize=(6,5))
#plt.savefig('2006_Balken.png')

#df4 = df.unstack((0,2))

#df3[[1995,2000,2005]].plot.bar()

