# Copyright (c) 2023, jagan and contributors
# For license information, please see license.txt

#import frappe
from __future__ import unicode_literals


def execute(filters=None):
	columns, data = [], []
	columns = [
        {
            'fieldname': 'sales_person_name',
            'label': ('Sales Person'),
            'fieldtype': 'Data',
            # 'options': 'Sales Person'
        },
        {
            'fieldname': 'currency',
            'label': ('Currency'),
            'fieldtype': 'Link',
            'options': 'Currency'
        },
        {  
            'fieldname': 'balance',
            'label': ('Balance'),
            'fieldtype': 'Currency',
            'options': 'currency'
        }
    ]

	data = [
        {
            'sales_person_name': 'Application of Funds (Assets)',
            'currency': 'INR',
            'balance': '15182212.738'
        },
        {
            'sales_person_name': 'Current Assets - GTPL',
            'currency': 'INR',
            'balance': '17117932.738'
        },
        
    ]


	return columns, data

