import pandas as pd
import numpy as np
# Hae Sarjataulukko Netistä
table_MN = pd.read_html('https://www.valioliiga.com/sarjataulukko/')
df=table_MN[0]
# Laske Kerroin (Pisteet/Matsit)
df['F=P/O']=df['P']/df['O']
# Askartele Maalierosarake
seri=pd.Series(df['M'])
s1=seri.str.slice(stop=2).astype(str).astype(int)
s2=seri.str.slice(start=-2).astype(str).astype(int)
df['GD']=s1-s2
# Näytä Taulukko
df.head()
print(df)
