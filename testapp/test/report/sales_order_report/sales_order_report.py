# Copyright (c) 2023, jagan and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from datetime import datetime,date
from frappe.utils import now,today,getdate,add_to_date,get_last_day
#import pdb; pdb.set_trace()

def execute(filters=None):
    fl=filters
    data=[]
    columns=[]
    m=["January","February","March","April","May","June","July","August","September","October","November","December"]
    col1= [{
        
            'fieldname': 'sales_person',
            'label': ('Sales Person'),
            'fieldtype': 'Link',
            'options': 'Sales Team',
          },]
    
    columns +=col1
    
    ycount=(int(fl['yearly1']) - int(fl['yearly'])) 
    if not 1 > ycount and 5 >= ycount:
        years=0
        
        for j in range(ycount+1):
            years=int(fl['yearly'])+j
            scount= m.index(fl['Monthly'])
            ecount= m.index(fl['Monthly1'])+1
            for i in range(scount,ecount):				
                col2 = [

                {
                    'fieldname':str(i)+str(years)+'on_time',
                    'label': (m[i]+str(years)+' OnTime'),
                    'fieldtype': 'Data',
                    
                },
                {  
                    'fieldname':str(i)+str(years)+'delay_upto_4_d',
                    'label': (m[i]+str(years)+'Delay Up 4 D'),
                    'fieldtype': 'int',
                    
                },
                    {
                    'fieldname':str(i)+str(years)+'delay_above_4_d',
                    'label': (m[i]+str(years)+'Delay Upto 4 D'),
                    'fieldtype': 'int',
                },
                {  
                    'fieldname':str(i)+str(years)+'total',
                    'label': (m[i]+str(years)+'Total'),
                    'fieldtype': 'int',
                },]
                
                columns +=col2
                days=1
                df1=date(years, i+1, days)
                lasday=get_last_day(df1)

    
    col3=[	{  
        'fieldname': 'total',
        'label': ('Total'),
        'fieldtype': 'int',
    }]
    columns +=col3
    stm=m.index(fl['Monthly'])+1
    sty=int(fl['yearly'])
    startday= date(sty,stm,1)
    posting_date=[]
    posting_date+= frappe.db.get_all("Sales Invoice",filters=[['posting_date', 'between', [startday, lasday]]],fields=['name','posting_date'])
  
        
    if posting_date:
        invoiceperson=[]
        for invper in posting_date:
            l=frappe.get_value('Sales Team',{'parent': invper.name}, 'sales_person')
            invoiceperson.append(l)
        sloder=[]
        for invper1 in posting_date:
            l0=frappe.get_value('Sales Invoice Item',{'parent': invper1.name},'sales_order')
            sloder.append(l0)
        due_date=[]
        for slodname in sloder:
            l1=frappe.get_value('Sales Order',slodname,'delivery_date')    
            due_date.append(l1)
        pos_date=[]
        check=[]

        for pos in posting_date:
            pos_date.append(pos.posting_date)
        
        x=0
        d1=0
        d2=0
        d3=0
        check=[]
        row=[]
        temp=0
        for fetch in invoiceperson:
            result=str(due_date[x]-pos_date[x]) 
            data_cloumn_add=pos_date[x]
            
            m1=(data_cloumn_add.month-1)

            on='0:00:00'

            if fetch in check:
                count1= check.index(fetch)
                if result ==on: 
                    d1+=1
                elif 4 >= int(result[0]):
                    d2+=1
                elif 4 <= int(result[0]):
                    d3+=1
                data[count1][str(m1)+str(data_cloumn_add.year)+'on_time']+=d1 
                data[count1][str(m1)+str(data_cloumn_add.year)+'delay_upto_4_d']+=d2
                data[count1][str(m1)+str(data_cloumn_add.year)+'delay_above_4_d']+=d3
                data[count1][str(m1)+str(data_cloumn_add.year)+'total']+=d1+d2+d3
                data[count1]['total']+=d1+d2+d3
            else:
                check.append(fetch)
                if result ==on: 
                    d1+=1
                elif 4 >= int(result[0]):
                    d2+=1
                elif 4 <= int(result[0]):
                    d3+=1
                
                row ={
                    'sales_person':fetch,
                    str(m1)+str(data_cloumn_add.year)+'on_time':d1, 
                    str(m1)+str(data_cloumn_add.year)+'delay_upto_4_d': d2,
                    str(m1)+str(data_cloumn_add.year)+'delay_above_4_d':d3,
                    str(m1)+str(data_cloumn_add.year)+'total':d1+d2+d3,
                    'total':+d1+d2+d3
                    }
                data.append(row)
                
                temp+=1
            x+=1

    return columns, data

    # id1=[]
    # for i,j in zip(x,y):

    #     id+= frappe.db.get_all("Sales Invoice",filters=[['posting_date', 'between', [i,j]]],fields=['name','posting_date'])
    # ########
    #   for nameid in list2: 
    #     getlist=frappe.get_doc("Sales Order",nameid)
    #     print("s")