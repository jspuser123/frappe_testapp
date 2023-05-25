// Copyright (c) 2023, jagan and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Sales Person"] = {
	"filters": [


		// {
        //     fieldname: 'company',
        //     label: __('Company'),
        //     fieldtype: 'Link',
        //     options: 'Company',
        //     default: frappe.defaults.get_user_default('company')
        // },

		{
            fieldname: 'Monthly',
            label: __('Monthly'),
            fieldtype: 'Select',
            options: [
                'Monthly',
                'Quarterly',
                'Half-Yearly',
                'Yearly'
            ],
            default: 'Yearly',
            // depends_on: 'eval:doc.company=="Gadget Technologies Pvt. Ltd."'
        },
        {
            fieldname: 'periodicity',
            label: __('Periodicity'),
            fieldtype: 'Select',
            options: [
                'Monthly',
                'Quarterly',
                'Half-Yearly',
                'Yearly'
            ],
            default: 'Yearly',
            
        },
		{
            fieldname: 'periodicity',
            label: __('Periodicity'),
            fieldtype: 'Select',
            options: [
                'Monthly',
                'Quarterly',
                'Half-Yearly',
                'Yearly'
            ],
            default: 'Yearly',
           
        },
		{
            fieldname: 'periodicity',
            label: __('Periodicity'),
            fieldtype: 'Select',
            options: [
                'Monthly',
                'Quarterly',
                'Half-Yearly',
                'Yearly'
            ],
            default: 'Yearly',
            // depends_on: 'eval:doc.company=="Gadget Technologies Pvt. Ltd."'
        }
	]
};
