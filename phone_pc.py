# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 21:46:03 2018

@author: The
"""

import pandas as pd
import numpy as np
import pylab as plt

PATH = "C:/Users/The/Desktop/Python_Projekte/"


#Daten als Dataframes einlesen
df_pc = pd.read_excel(PATH+"pc.xlsx", index_col=0)
df_phone = pd.read_excel(PATH+"phone.xlsx", index_col=0)

#Indexnamen kürzen
df_phone.index.name = "Mobile phones per 100"

#df2 hat Strings als Index! - Umwandlung zu Integer
ncol = [int(x) for x in df_phone.columns]
df_phone.set_axis(axis=1, labels=ncol, inplace=True)

#Zeilen und Spalten aus dem Index auswählen
#df1 = df_pc.loc[['Germany','Russia', 'China', 'India', 'United States'],[1994, 1998, 2002, 2006]]
#df2 = df_phone.loc[['Germany','Russia', 'China', 'India', 'United States'],[1994, 1998, 2002, 2006]] 

df_pc_years = df_pc[[1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006]]
df_phone_years = df_phone[[1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006]]

#df1.plot.bar(figsize=(8,10))
#plt.savefig('PC_Balken.png')
#df2.plot.bar(figsize=(8,10))
#plt.savefig('Phones_Balken.png')


#hierarchischen Index erstellen
#sdf1 = df1.stack()
#sdf2 = df2.stack()
sdf_pc_years = df_pc_years .stack()
sdf_phone_years = df_phone_years .stack()

#d = {'PC': sdf1, 'Phones': sdf2} #Series zu Dataframe verbinden, mithilfe eines dictionaries
#df = pd.DataFrame(data=d)
d = {'PC': sdf_pc_years, 'Phones': sdf_phone_years}
df_years = pd.DataFrame(data=d)
df_years = df_years.stack()
df_years = df_years.unstack((1,2))



'''Scatterplot für Germany, Russia, USA - PC gegen Phones'''
df_ger = df_years.loc['Germany']
df_rus = df_years.loc['Russia']
df_usa = df_years.loc['United States']
df_ger = df_ger.unstack(1)
df_rus = df_rus.unstack(1)
df_usa = df_usa.unstack(1)

plt.scatter(df_ger['PC'], df_ger['Phones'], label='Germany')
plt.scatter(df_rus['PC'], df_rus['Phones'], label='Russia')
plt.scatter(df_usa['PC'], df_usa['Phones'], label='USA')
#plt.plot(df_ger['PC'], df_ger['Phones'])
#plt.plot(df_rus['PC'], df_rus['Phones'])
#plt.plot(df_usa['PC'], df_usa['Phones'])
plt.legend()
plt.ylabel('Phones')
plt.xlabel('PC')
plt.axis([0,100,0,100])
plt.grid(True)
plt.title('Entwicklung der Gerätezahlen von 1994 bis 2006 pro 100 Einwohner')
plt.savefig('scatter_94bis06_ger_rus_usa_PCvsPhones.png')
plt.show()

'''Linienplot für Germany, Russia, USA - PC gegen Zeit'''


plt.plot(df_ger.index, df_ger['PC'], label='Germany')
plt.plot(df_rus.index, df_rus['PC'], label='Russia')
plt.plot(df_usa.index, df_usa['PC'], label='USA')
plt.legend()
plt.ylabel('PC')
plt.xlabel('Jahre')
plt.axis([1994, 2006, 0,100])
plt.title('Entwicklung der Gerätezahlen von 1994 bis 2006 pro 100 Einwohner')
plt.savefig('linien94bis06_ger_rus_usa_PCvsZeit.png')
plt.show()


'''Linienplot für Germany, Russia, USA - Phones gegen Zeit'''


plt.plot(df_ger.index, df_ger['Phones'], label='Germany')
plt.plot(df_rus.index, df_rus['Phones'], label='Russia')
plt.plot(df_usa.index, df_usa['Phones'], label='USA')
plt.legend()
plt.ylabel('Phones')
plt.xlabel('Jahre')
plt.axis([1994, 2006, 0,100])
plt.title('Entwicklung der Gerätezahlen von 1994 bis 2006 pro 100 Einwohner')
plt.savefig('linien94bis06_ger_rus_usa_PhonesvsZeit.png')
plt.show()

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