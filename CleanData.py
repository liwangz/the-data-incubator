#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 20:05:08 2018

@author: liwang
"""
import pandas as pd

Whole=pd.read_csv('Faculty Compensation.csv')
Whole[['university','State']]=Whole['university'].str.rsplit(expand=True,n=1)
Whole=Whole.drop(['Unnamed: 0'],axis=1)
Whole['position']=Whole['position'].replace([1591,1596,1601,1606,1611],['P','AP','aP','I','U'])

Doctoral=Whole['university'].str.extract(r'(.*)(Doctor)')
Master=Whole['university'].str.extract(r'(.*)(Master)')
Bac=Whole['university'].str.extract(r'(.*)(Baccalaureate)')
Rank=Whole['university'].str.extract(r'(.*)(Associate\'?s? with Ranks)')
NoRank=Whole['university'].str.extract(r'(.*)(Associate\'?s? without Ranks)')

University=Doctoral[0].str.cat([Master[0],Bac[0],Rank[0],NoRank[0]],na_rep='')
Category=Doctoral[1].str.cat([Master[1],Bac[1],Rank[1],NoRank[1]],na_rep='')
Category=Category.replace(['Associate with Ranks', 'Associate\'s with Ranks',
                  'Associate without Ranks', 'Associate\'s without Ranks'],
                 ['Rank', 'Rank', 'NoRank','NoRank'])

Whole['university']=University
Whole['Category']= Category


Whole['Ave. Salary']=Whole['Ave. Salary'].str.replace('$','')
Whole['Ave. Salary']=Whole['Ave. Salary'].str.replace(',','')
Whole['Avg. Compensation']=Whole['Avg. Compensation'].str.replace('$','')
Whole['Avg. Compensation']=Whole['Avg. Compensation'].str.replace(',','')



Whole['Ave. Salary']=pd.to_numeric(Whole['Ave. Salary'], errors='coerce',downcast='integer')
Whole['Avg. Compensation']=pd.to_numeric(Whole['Avg. Compensation'], errors='coerce',downcast='integer')
Whole['Count']=pd.to_numeric(Whole['Count'], errors='coerce', downcast='integer')

Whole['Avg. Change']=Whole['Avg. Change'].str.replace('%','')
Whole['Avg. Change']=pd.to_numeric(Whole['Avg. Change'], errors='coerce',downcast='float')

Whole.to_csv('Faculty Compensation_clean.csv')