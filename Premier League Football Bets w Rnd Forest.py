# Premier League Football in Random Forest

import pandas as pd
import numpy as np
from numpy import mean
from numpy import std
from datetime import datetime
import matplotlib.pyplot as plt
import random

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
#from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold


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

# SARJATAULUKKO

taulukko=pd.read_html('https://www.valioliiga.com/sarjataulukko')
df=taulukko[0]
# Pisteet/Ottelut-kerroin
df['F=P/O']=df['P']/df['O']
df['F=P/O']=df['F=P/O'].astype(str)
df['P']=df['P'].astype(int)
# Maaliero
mero=pd.Series(df['M'])
s1=mero.str.slice(stop=2).astype(int)
s2=mero.str.slice(start=-2).astype(int)
df['GD']=s1-s2
# Joukkuesarakkeen siivous
df['Joukkue']=df['Joukkue'].str.replace(" ","")
for cb in teams:
    df['Joukkue']=df['Joukkue'].str.replace(cb,teams[cb])
df.head()
print(df)
        
# OTTELUDATA

pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',7)
tulokset=pd.read_html('https://www.valioliiga.com/tulokset/')
frames=[]
for i in range(0,len(tulokset)):
    var=tulokset[i]
    frames.append(var)
mats=pd.concat(frames).reset_index(drop=True)

# Ottelusarakkeen siivous

mats['Ottelu']=mats['Ottelu'].str.replace(" ","")
for x in teams:
    mats['Ottelu']=mats['Ottelu'].str.replace(x,teams[x])
mats[['Koti','Vieras']]=mats['Ottelu'].str.split(chr(8211),expand=True)
mats[['K','V']]=mats['Tulos'].str.split("-",expand=True)
mats['K']=mats['K'].astype(int)
mats['V']=mats['V'].astype(int)
mats.drop('Ottelu',inplace=True,axis=1)
mats.drop('Tulos',inplace=True,axis=1)
mats['GD']=(mats['K']-mats['V']).astype(int)
mats['Pvm']=pd.to_datetime(mats['Pvm'],infer_datetime_format=True)
print("")

# Feature Adj.
feats=mats.copy()
feats.drop('K',inplace=True,axis=1)
feats.drop('V',inplace=True,axis=1)
df['P']=df['P'].astype(str)
df['F=P/O']=df['F=P/O'].astype(str)

feats['HP']=feats['Koti'].copy()
feats['GP']=feats['Vieras'].copy()

Names=dict(zip(df['Joukkue'],df['P']))
for name in Names:
    feats['Koti']=feats['Koti'].str.replace(name,Names[name])
    feats['Vieras']=feats['Vieras'].str.replace(name,Names[name])
                  
Points=dict(zip(df['Joukkue'],df['F=P/O']))
for pg in Points:
    feats['HP']=feats['HP'].replace(pg,Points[pg])
    feats['GP']=feats['GP'].replace(pg,Points[pg])
   
feats['Koti']=feats['Koti'].astype(int)
feats['Vieras']=feats['Vieras'].astype(int)
feats['HP']=feats['HP'].astype(float)
feats['GP']=feats['GP'].astype(float)

# Feature Space
FeatureSpace=feats.copy()

# Luokat
luokat=[]
for v in FeatureSpace['GD']:
    if v<0:
        lk="H";luokat.append(lk)
    if v==0:
        lk="T";luokat.append(lk)
    if v>0:
        lk="V";luokat.append(lk)
FeatureSpace['GD']=pd.Series(luokat).values

# Features & Labels
y=FeatureSpace['GD']
X=FeatureSpace.drop(['GD'],axis=1).drop(['Pvm'],axis=1)

# Train/Test Split
X_train,X_test,y_train,y_test = train_test_split(X,y,
                                                 test_size=0.3,
                                                 random_state=44)
# Training
RFC=RandomForestClassifier(n_estimators=3,max_depth=2,
                           random_state=44)

# Fit & Predict the Test Labels
RFC.fit(X_train,y_train)
y_pred=RFC.predict(X_test)

# Visualize
features=X.columns.values
classes=['H','T','V']
for estimator in RFC.estimators_:
    print(estimator)
    plt.figure(figsize=(12,6))
    tree.plot_tree(estimator,
                   feature_names=features,
                   class_names=classes,
                   fontsize=8,
                   filled=True,
                   rounded=True)
plt.show()

# Eval
cv=RepeatedStratifiedKFold(n_splits=10,n_repeats=3,random_state=1)
n_scores=cross_val_score(RFC,X,y,scoring='accuracy',cv=cv,
                         n_jobs=-1,error_score='raise')

print("Accuracy: %.3f (%.3f)" % (mean(n_scores),std(n_scores)))

# Make a Single Prediction

kotij=str(input("Kotijoukkue?"))
vierasj=str(input("Vierasjoukkue?"))
x1=Names[kotij]
x2=Names[vierasj]
x3=Points[kotij]
x4=Points[vierasj]
row=np.array([x1,x2,x3,x4]).reshape(1,-1)

single=RFC.predict(row)
print("Ennuste kotijoukkueelle: %s" % single[0])
                    
                    



