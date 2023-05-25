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
    invoiceperson=[]
    for l in posting_date:
        invoiceperson+=frappe.get_list('Sales Team', filters = {'parent': l.name}, fields=['sales_person'])
    list2=[]    
    list2+= frappe.db.get_all("Sales Order",filters=[['delivery_date', 'between', [startday, lasday]]],fields=['delivery_date'] )
    due_date=[]
    for l1 in list2:
        due_date.append(l1.delivery_date)
    if invoiceperson or posting_date or due_date:
        # print(li,list1[0]['posting_date'],li2[0]['due_date'])
        #print(invoiceperson,posting_date,sloderperson,due_date)
        invperson=[]
        pos_date=[]
        check=[]
        for invper in invoiceperson:
            invperson.append(invper.sales_person)

        for pos in posting_date:
            pos_date.append(pos.posting_date)
        
    
           
        x=0
        d1=0
        d2=0
        d3=0
        check=[]
        row=[]
        temp=0
        for fetch in invperson:
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
                
               
            else:
             
                check.append(fetch)

                print(check)
                print(temp)
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
                    str(m1)+str(data_cloumn_add.year)+'total':d1+d2+d3
                    }
                data.append(row)
                temp+=1
            x+=1
            print(data)

    return columns, data
   

        # print(invperson)
        # print(pos_date)
        # print(du_date)   


  


                    
                    








    #         x.append(date(years,scount+1,days))	
    #         y.append(df1)
    # id=[]
    # id1=[]
    # for i,j in zip(x,y):

    #     id+= frappe.db.get_all("Sales Invoice",filters=[['posting_date', 'between', [i,j]]],fields=['name','posting_date'])
    #     id1+= frappe.db.get_all("Sales Order",filters=[['between', [i,j]]],fields=['name'])
    
    #     for l1 in id1:
    #         li2=frappe.get_list('Payment Schedule', filters = {'parent': l1.name}, fields=['due_date'])
    #         print(l1.name,li2)

    #     for l in id:
    #         li=frappe.get_list('Sales Team', filters = {'parent': l.name}, fields=['sales_person'])
    #         s=l.posting_date

      

   


    
    # id= frappe.db.get_all("Sales Invoice",filters={"posting_date":["<=",d2] },fields=['name','posting_date'])
    # print(id)
    # li=[]
    # for x in id:
    # 	li+=frappe.get_list('Sales Team', filters = {'parent': x.name}, fields=['sales_person'])
    # 	li1= frappe.db.get_value("Sales Invoice", x.name, ['posting_date'])
    # 	print(li1)
    # 	print(li)
    
    # id1= frappe.db.get_all("Sales Order")
    # for x in id:
    # 	li2=frappe.get_list('Payment Schedule', filters = {'parent': x.name}, fields=['due_date'])
    # 	print(li2)	
    # for chname in li:
    # 	row = {	'sales_person':chname.sales_person,
    # 			'on_time':None, 
    # 			'delay_upto_4_d': None,
    # 			'delay_above_4_d':None,
    # 			'total':None
    # 	}
    # 	data.append(row)
    

    # 	child1 = frappe.get_doc('Sales Team', person.sales_team[0].name)
    # 	d=getdate() 
    # 	d1 = add_to_date(datetime.now(), days=4, as_string=True)
    # 	d2 =getdate(d1)
    # 	c1=0
    # 	c2=0
    # 	c3=0
    # 	if person.posting_date == d:    
    # 		c1+=1
    # 	if person.posting_date <= d2:    
    # 		c2+=1
    
    # 	if person.posting_date >= d2:    
    # 		c3+=1	
        
    # 	row = {	'sales_person':child1.sales_person,
    # 			'on_time':c1, 
    # 			'delay_upto_4_d': c2,
    # 			'delay_above_4_d':c3,
    # 			'total':c1+c2+c3
    # 	}
    # 	data.append(row)
    



    

