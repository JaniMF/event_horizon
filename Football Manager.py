import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.linear_model import LinearRegression

teams={
    "ManchesterCityManCity":"ManCity",
    "Arsenal":"Arsenal",
    "ManchesterUnitedManUtd":"ManU",
    "Newcastle":"Newcastle",
    "Liverpool":"Liverpool",
    "Brighton":"Brighton",
    "AstonVilla":"AstonVilla",
    "Tottenham":"Tottenham",
    "Brentford":"Brentford",
    "Fulham":"Fulham",
    "CrystalPalace":"CrystalPalace",
    "Chelsea":"Chelsea",
    "WolverhamptonWolves":"Wolverhampton",
    "WestHam":"WestHam",
    "Bournemouth":"Bournemouth",
    "Nottingham":"Nottingham",
    "Everton":"Everton",
    "Leicester":"Leicester",
    "Leeds":"Leeds",
    "Southampton":"Southampton"}

# Sarjataulukko
taulukko=pd.read_html('https://www.valioliiga.com/sarjataulukko')
df=taulukko[0]
df['F=P/O']=df['P']/df['O']
# Maalierosarake
seri=pd.Series(df['M'])
s1=seri.str.slice(stop=2).astype(str).astype(int)
s2=seri.str.slice(start=-2).astype(str).astype(int)
df['GD']=s1-s2
df['Joukkue']=df['Joukkue'].str.replace(" ","")
for cb in teams:
    df['Joukkue']=df['Joukkue'].str.replace(cb,teams[cb])
df.head()
print(df)

# Ottelut
pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',7)
tulox=pd.read_html('https://www.valioliiga.com/tulokset/')
frames=[]
for i in range(0,len(tulox)):
    var=tulox[i]
    frames.append(var)
result=pd.concat(frames).reset_index(drop=True)
result['Ottelu']=result['Ottelu'].str.replace(" ","")
for x in teams:
    result['Ottelu']=result['Ottelu'].str.replace(x,teams[x])
result[['Koti','Vieras']]=result['Ottelu'].str.split(chr(8211),expand=True)
result[['K','V']]=result['Tulos'].str.split("-",expand=True)
result['K']=result['K'].astype(int)
result['V']=result['V'].astype(int)
result.drop('Ottelu',inplace=True,axis=1)
result.drop('Tulos',inplace=True,axis=1)
result['GD']=result['K']-result['V']
result['Pvm']=pd.to_datetime(result['Pvm'],infer_datetime_format=True)
print("")
print(result)

# Kotiottelut
print("");tiimi=str(input("Joukkue?"))
print("")
koti=result.loc[result['Koti']==tiimi]
print("Kotiottelut:")
print(koti)
print("\nTehdyt maalit:",koti['K'].sum())
print("Keskiarvo:",koti['K'].mean(),"per ottelu")
print("Keskihajonta:",koti['K'].std())
print("Päästetyt maalit:",koti['V'].sum())
print("Keskiarvo:",koti['V'].mean(),"per ottelu")
print("Keskihajonta:",koti['V'].std())
print("")

# Vierasottelut
vieras=result.loc[result['Vieras']==tiimi]
print("Vierasottelut:")
print(vieras)
print("\nTehdyt maalit:",vieras['V'].sum())
print("Keskiarvo:",vieras['V'].mean(),"per ottelu")
print("Keskihajonta:",vieras['V'].std())
print("Päästetyt maalit:",vieras['K'].sum())
print("Keskiarvo:",vieras['K'].mean(),"per ottelu")
print("Keskihajonta:",vieras['K'].std())
print("")

# Otteluohjelma/Joukkue
kaikki=pd.concat([(result.loc[result['Koti']==tiimi]),
                  (result.loc[result['Vieras']==tiimi])
                  ])
kaikki.sort_values(by='Pvm',inplace=True)
vps=[]
lst=len(kaikki['Pvm'])-1
for d in range(0,lst):
    vp=(kaikki.iloc[d+1][0]-kaikki.iloc[d][0]).days
    vps.append(vp)
viim=(kaikki.iloc[-1][0]-kaikki.iloc[-2][0]).days
vps.append(viim)
kaikki['RST']=pd.Series(vps).values

# Replace Strings with 0s and 1s (For Model Features)
#newkaikki=kaikki.copy()
#for FC in newkaikki['Koti']:
    #if FC==tiimi:
        #newkaikki['Koti']=newkaikki['Koti'].replace(tiimi,1)
    #else:
        #newkaikki['Koti']=newkaikki['Koti'].replace(FC,0)
#for FCT in newkaikki['Vieras']:
    #if FCT==tiimi:
        #newkaikki['Vieras']=newkaikki['Vieras'].replace(tiimi,1)
    #else:
        #newkaikki['Vieras']=newkaikki['Vieras'].replace(FCT,0)

# Replace Names with Values from Points Column
nuest=kaikki.copy()
df['P']=df['P'].astype(str)
Names=dict(zip(df['Joukkue'],df['P']))
for nm in Names:
    nuest['Koti']=nuest['Koti'].str.replace(nm,Names[nm])
    nuest['Vieras']=nuest['Vieras'].str.replace(nm,Names[nm])
nuest['Koti']=nuest['Koti'].astype(int)
nuest['Vieras']=nuest['Vieras'].astype(int)

# Features/Labels
features=nuest[['Koti','Vieras','RST']].to_numpy()
lab1=koti['GD'].to_numpy()
lab2=vieras['GD'].to_numpy()
labels=[]
for val1 in lab1:
    labels.append(val1)
for val2 in lab2:
    val2=val2*(-1)
    labels.append(val2)
    
# Lineaarinen Regressio
reg=LinearRegression().fit(features,labels)
score=reg.score(features,labels)
print("Joukkuevalintaan perustuva R2 Score:",score)

# Vastustaja/Keskinäiset Ottelut
vast=str(input("\nVastustaja?"))
keskin=pd.concat([(koti.loc[koti['Vieras']==vast]),
                 (vieras.loc[vieras['Koti']==vast])
                 ])
print("")
print(keskin)
F1=df.loc[df['Joukkue']==tiimi,'F=P/O'].values
F2=df.loc[df['Joukkue']==vast,'F=P/O'].values
erotus=(F1-F2)[0]
print("\nF-kertoimien erotus (kotijoukkueelle)")
print(erotus)

# Ennuste
x1=df.loc[df['Joukkue']==tiimi,'P'].values
x2=df.loc[df['Joukkue']==vast,'P'].values
x3=np.array([int(input("\nVälipäivien lkm?"))])
pred=np.array([x1,x2,x3],dtype=np.int64).reshape(1,-1)
ennuste=reg.predict(pred)
print("Ennuste: maaliero kotijoukkueelle =")
print(ennuste[0])
tod=score*100
print("Todennäköisyydellä:",round(tod,2),"%")



