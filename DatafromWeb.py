#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 14:22:10 2018

@author: liwang
"""

import pandas as pd
import numpy as np
head=['university', 'Ave. Salary', 'Avg. Change','Count', 'Avg. Compensation','Salary Equity']

Whole=pd.DataFrame()
for j in range(1591,1611,5):
    print (j)
    JPage, =pd.read_html("https://www.insidehighered.com/aaup-compensation-survey?institution-name=&professor-category={}".format(j),
                        header=0)   
    JPage.columns=head
    for i in range(1,95):
        Page, =pd.read_html("https://www.insidehighered.com/aaup-compensation-survey?institution-name=&professor-category={}&page={}".format(j,i), 
                            header=0)
        Page.columns=head
        JPage=pd.concat([JPage, Page],axis=0)
        
    L=JPage['university'].count()
    Position=pd.Series([j for x in range(L)])
    JPage['position']=Position
    Whole=pd.concat([Whole,JPage],ignore_index=True)
    
Page, =pd.read_html("https://www.insidehighered.com/aaup-compensation-survey?institution-name=&professor-category=1611",header=0)   
Page.columns=head
L=Page['university'].count()
Page['position']=[1611 for x in range(L)]
Whole=pd.concat([Whole,Page],ignore_index=True)

Page, =pd.read_html("https://www.insidehighered.com/aaup-compensation-survey?institution-name=&professor-category=1611&page=1",header=0)
Page.columns=head
L=Page['university'].count()
Page['position']=[1611 for x in range(L)]
Whole=pd.concat([Whole,Page],ignore_index=True)

Whole=Whole.sort_values(by=['university','position'])

Whole.to_csv('Faculty Compensation.csv')

