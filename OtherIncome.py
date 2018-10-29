#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 00:09x:03 2018

@author: liwang
"""
import pandas as pd

f=pd.read_csv('Faculty Compensation_clean.csv')
f=f.drop(['Unnamed: 0'],axis=1)

def complete(row): #return no value is null
    for i in row:
        if pd.isnull(i):
            return False
    return True
f['Complete']=f.apply(complete, axis=1)
f=f.loc[f['Complete']==True, :]

f['Other_Income']=f['Avg. Compensation']-f['Ave. Salary']
f['Ratio']=f['Other_Income']/f['Avg. Compensation']

Cat_ratio=f.groupby(['Category'])['Ratio'].mean()
Cat_comp=f.groupby(['Category'])['Avg. Compensation'].mean()
Cat=pd.concat([Cat_ratio,Cat_comp], axis=1)
Cat.columns=['Other income', 'Compensation']
Cat=(Cat-Cat.mean())/Cat.std()
plot1_1=Cat.plot(kind='bar',fontsize=15)


Pos_ratio=f.groupby(['position'])['Ratio'].mean()
Pos_comp=f.groupby(['position'])['Avg. Compensation'].mean()
Pos=pd.concat([Pos_ratio,Pos_comp], axis=1)
Pos=(Pos-Pos.mean())/Pos.std()
Pos.columns=['Other income', 'Compensation']
plot1_2=Pos.plot(kind='bar',fontsize=15).legend(loc='lower left')


Cat_E=f.groupby(['Category'])['Salary Equity'].mean()
Cat_S=f.groupby(['Category'])['Ave. Salary'].mean()
Cat=pd.concat([Cat_S,Cat_E], axis=1)
Cat.columns=['Salary','Equity']
Cat=(Cat-Cat.mean())/Cat.std()
plot2_1=Cat.plot(kind='bar',fontsize=15)


Pos_E=f.groupby(['position'])['Salary Equity'].mean()
Pos_S=f.groupby(['position'])['Ave. Salary'].mean()
Pos=pd.concat([Pos_S,Pos_E], axis=1)
Pos=(Pos-Pos.mean())/Pos.std()
Pos.columns=['Salary','Equity' ]
plot1_2=Pos.plot(kind='bar',fontsize=15)#.legend(loc='lower left')

f['Salary_(K)']=f['Ave. Salary']/1000
plot_2=f.plot(x='Salary_(K)', y='Salary Equity',kind='scatter')

import statsmodels.formula.api as smf
Fitdata=f.loc[:,['Salary Equity', 'Salary_(K)']]
Fitdata.columns=['A','B']

FD=smf.ols(formula="A~B", data=Fitdata).fit()

Ones=pd.Series(np.ones(260)*100,name='Equal line')
Ones.plot(legend=True,color='b')
Y=pd.DataFrame({'B': range(260)})
X=FD.predict(Y)
X.name='Fit line'
X.plot(legend=True,color='r')
