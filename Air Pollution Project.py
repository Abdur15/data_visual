#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Study of Air Pollution around the World from 1990-2017

## Importing necessary libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = 'C:/Users/nasse/Downloads/Air Pollution Data.csv'
df_test = pd.read_csv(path)
df = df_test.drop(columns ='Code')

## Manipulating the Data
df = df.rename(columns={'Air pollution (total) (deaths per 100,000)':'Total'})
df = df.rename(columns={'Indoor air pollution (deaths per 100,000)':'Indoor'})
df = df.rename(columns={'Outdoor particulate matter (deaths per 100,000)':'Outdoor'})
df = df.rename(columns={'Outdoor ozone pollution (deaths per 100,000)':'Ozone'})
df = df.rename(columns={'Entity':'Country'})


india = df.iloc[2662:2688,:].reset_index().drop(columns = 'index')
aus = df.iloc[310:336,:].reset_index().drop(columns = 'index')
china = df.iloc[1262:1288,:].reset_index().drop(columns = 'index')
usa = df.iloc[4146:4172,:].reset_index().drop(columns = 'index')
png = df.iloc[4426:4452,:].reset_index().drop(columns = 'index')


## Plotting the Figure

fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,figsize=(20,10))
ax1.plot(india['Year'],india['Total'],color='red',label='India')
ax1.plot(aus['Year'],aus['Total'],color='blue',label='Australia')
ax1.plot(china['Year'],china['Total'],color='green',label='China')
ax1.plot(usa['Year'],usa['Total'],color='yellow',label='USA')
ax1.plot(png['Year'],png['Total'],color='brown',label='PNG')
ax1.set(title = 'Air Pollution',xlabel='Year',ylabel='Total')
ax1.legend()

ax2.plot(india['Year'],india['Indoor'],color='red',label='India')
ax2.plot(aus['Year'],aus['Indoor'],color='blue',label='Australia')
ax2.plot(china['Year'],china['Indoor'],color='green',label='China')
ax2.plot(usa['Year'],usa['Indoor'],color='yellow',label='USA')
ax2.plot(png['Year'],png['Indoor'],color='brown',label='PNG')
ax2.set(title ='Indoor Air Pollution',xlabel='Year',ylabel='Indoor')
ax2.legend()

ax3.plot(india['Year'],india['Outdoor'],color='red',label='India')
ax3.plot(aus['Year'],aus['Outdoor'],color='blue',label='Australia')
ax3.plot(china['Year'],china['Outdoor'],color='green',label='China')
ax3.plot(usa['Year'],usa['Outdoor'],color='yellow',label='USA')
ax3.plot(png['Year'],png['Outdoor'],color='brown',label='PNG')
ax3.set(title = 'Outdoor Air Pollution',xlabel='Year',ylabel='Outdoor')
ax3.legend()

ax4.plot(india['Year'],india['Ozone'],color='red',label='India')
ax4.plot(aus['Year'],aus['Ozone'],color='blue',label='Australia')
ax4.plot(china['Year'],china['Ozone'],color='green',label='China')
ax4.plot(usa['Year'],usa['Ozone'],color='yellow',label='USA')
ax4.plot(png['Year'],png['Ozone'],color='brown',label='PNG')
ax4.set(title = 'Ozone Air Pollution',xlabel='Year',ylabel='Ozone')
ax4.legend()
plt.show()

