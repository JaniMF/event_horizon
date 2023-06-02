import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    
pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',7)
table_NM=pd.read_html('https://www.valioliiga.com/tulokset/')
frames=[]
for i in range(0,len(table_NM)):   
    var=table_NM[i]
    frames.append(var)
rslt=pd.concat(frames).reset_index(drop=True)
rslt['Ottelu']=rslt['Ottelu'].str.replace(" ","")
for x in teams:
    rslt['Ottelu']=rslt['Ottelu'].str.replace(x,teams[x])
rslt[['Koti','Vieras']]=rslt['Ottelu'].str.split(chr(8211),expand=True)
rslt[['K','V']]=rslt['Tulos'].str.split("-",expand=True)
rslt['K']=rslt['K'].astype(int)
rslt['V']=rslt['V'].astype(int)
rslt.drop('Ottelu',inplace=True,axis=1)
rslt.drop('Tulos',inplace=True,axis=1)
rslt['GD']=rslt['K']-rslt['V']
print(rslt)

# KOTIOTTELUT/TIIMI

print("")
tiimi=str(input("Joukkue?"))
print("")
koti=rslt.loc[rslt['Koti']==tiimi]
print("Kotiottelut:")
print(koti)

#MAALIT/KOTI

mk=koti['K'].sum()
vk=koti['V'].sum()
print("Tehdyt maalit:",mk)
print("Keskiarvo:",koti['K'].mean(),"per ottelu")
print("Päästetyt maalit:",vk)
print("Keskiarvo:",koti['V'].mean(),"per ottelu")

# VIERASOTTELUT

print("")
vieras=rslt.loc[rslt['Vieras']==tiimi]
print("Vierasottelut:")
print(vieras)

# MAALIT/VIERAS

mv=vieras['V'].sum()
vv=vieras['K'].sum()
print("Tehdyt maalit:",mv)
print("Keskiarvo:",vieras['V'].mean(),"per ottelu")
print("Päästetyt maalit:",vv)
print("Keskivarvo:",vieras['K'].mean(),"per ottelu")
print("")

# PLOT GD

Y = koti['GD'].to_numpy()

for kk in range(len(Y)):
    y=Y[kk]
    x=kk
    plt.subplot(2,1,1)
    plt.scatter(x,y,color='blue')
    plt.axhline(0,linestyle="dotted",linewidth=0.75)

Y2 = vieras['GD'].to_numpy()

for kx in range(len(Y2)):
    y2=Y2[kx]*(-1)
    x2=kx
    plt.subplot(2,1,2)
    plt.scatter(x2,y2,color='red')
    plt.axhline(0,linestyle="dotted",linewidth=0.75)

plt.suptitle("Maalierot",fontsize=14)
plt.show()












    
    


    
    



        
        

                              
        
        




    


    








    




               

















    
