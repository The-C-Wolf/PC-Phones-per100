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
df_gni = pd.read_excel(PATH+"GNI.xlsx", index_col=0)

'''Indexnamen kürzen'''
df_phone.index.name = "Mobile phones per 100"

'''df.phone und df_gni haben Strings als Index! - Umwandlung zu Integer'''
ncol1 = [int(x) for x in df_phone.columns]
df_phone.set_axis(axis=1, labels=ncol1, inplace=True)
ncol2 = [int(x) for x in df_gni.columns]
df_gni.set_axis(axis=1, labels=ncol2, inplace=True)

'''Index-Namen anpassen'''
df_gni = df_gni.rename(index={'Russian Federation': 'Russia'})

'''Jahre auswählen'''
years = list(range(1994,2007))
df_pc_years = df_pc[years]
df_phone_years = df_phone[years]
df_gni = df_gni[years]

'''hierarchischen Index erstellen'''
sdf_pc_years = df_pc_years .stack()
sdf_phone_years = df_phone_years .stack()
sdf_gni = df_gni.stack()

#df_gni = sdf_gni.unstack(1)

'''Series zu Dataframe verbinden, mithilfe eines dictionaries'''
d = {'PC': sdf_pc_years, 'Phones': sdf_phone_years, 'GNI' : sdf_gni}
df_years = pd.DataFrame(data=d)
df_years = df_years.stack()
df_years = df_years.unstack((1,2))

#df_years.to_csv('data.csv')
'''Länderauswahl treffen'''
länderliste1 = ['Germany','Russia','United States']
länderliste2 = ['France','Australia','Bolivia','Ghana','China','United Kingdom','Japan']
länderliste3 = ['France','Germany', 'Hungary','Bolivia','Russia']

countries = länderliste3        ##### hier die entsprechende Liste auswählen
countries_name = 'länderliste3' ##### hier die entsprechende Liste auswählen

def scatterplot(list, name):
    for country in list[:]:
        plt.scatter(df_years.loc[country].unstack(1)['PC'], df_years.loc[country].unstack(1)['Phones'], s= df_years.loc[country].unstack(1)['GNI']/200, label=country)
    plt.legend(loc=0)
    plt.ylabel('Mobile Phones')
    plt.xlabel('PCs')
    plt.axis([0,100,0,150])
    plt.grid(True)
    plt.title('PCs und Mobiltelefone 1994-2006 pro 100 Einwohner (Punktgröße:BSP)')
    plt.savefig(name+'scatterplot.png', dpi=900)
    plt.show()

def lineplot_pc(list, name):
    for country in list[:]:
        plt.plot(df_years.loc[country].unstack(1).index, df_years.loc[country].unstack(1)['PC'], label=country)
    plt.legend()
    plt.ylabel('PCs')
    plt.xlabel('Jahre')
    plt.axis([1994, 2006, 0,150])
    plt.grid(True)
    plt.title('PCs 1994 bis 2006 pro 100 Einwohner')
    plt.savefig(name+'lineplot_pc.png', dpi=900)
    plt.show()

def lineplot_phones(list, name):
    for country in list[:]:
        plt.plot(df_years.loc[country].unstack(1).index, df_years.loc[country].unstack(1)['Phones'], label=country)
    plt.legend()
    plt.ylabel('Mobile Phones')
    plt.xlabel('Jahre')
    plt.axis([1994, 2006, 0,150])
    plt.grid(True)
    plt.title('Mobiltelefone von 1994 bis 2006 pro 100 Einwohner')
    plt.savefig(name+'lineplot_phones.png',dpi=900)
    plt.show()
    
def lineplot_GNI(list, name):
    for country in list[:]:
        plt.plot(df_years.loc[country].unstack(1).index, df_years.loc[country].unstack(1)['GNI'], label=country)
    plt.legend()
    plt.ylabel('BSP')
    plt.xlabel('Jahre')
    plt.axis([1994, 2006, 0,50000])
    plt.grid(True)
    plt.title('Entwicklung des BSP von 1994 bis 2006')
    plt.savefig(name+'lineplot_BSP.png',dpi=900)
    plt.show()
 
    
'''Plots erstellen'''   
scatterplot(countries, countries_name)
lineplot_pc(countries, countries_name)
lineplot_phones(countries, countries_name)
lineplot_GNI(countries, countries_name)
