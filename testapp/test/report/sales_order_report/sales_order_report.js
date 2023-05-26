// Copyright (c) 2023, jagan and contributors
// For license information, please see license.txt
/* eslint-disable */
frappe.query_reports["sales order report"] = {
	"filters": [
		// {
		// 	    fieldname: 'customer',
		// 	    label: __('person'),
		// 	    fieldtype: 'Link',
		// 	    options: 'Customer',
		// 	    // default: frappe.defaults.get_user_default('date')
		// 	},
		{
            fieldname: 'Monthly',
            label: __('Monthly'),
            fieldtype: 'Select',
            options: [
				"January", 
				"February", 
				"March", 
				"April", 
				"May", 
				"June",
				"July", 
				"August", 
				"September", 
				"October", 
				"November", 
				"December"
            ],
            default: 'January',
            // depends_on: 'eval:doc.company=="Gadget Technologies Pvt. Ltd."'
        },
        {
            fieldname: 'Monthly1',
            label: __('Monthly1'),
            fieldtype: 'Select',
            options: [
				"January", 
				"February", 
				"March", 
				"April", 
				"May", 
				"June",
				"July", 
				"August", 
				"September", 
				"October", 
				"November", 
				"December"
            ],
            default: "February",
            // depends_on: 'eval:doc.company=="Gadget Technologies Pvt. Ltd."'
        },
		{
            fieldname: 'yearly',
            label: __('yearly'),
            fieldtype: 'Select',
            options: [
              '2000',
			  '2001',
			  '2002',
			  '2003',
			  '2004',
			  '2005',
			  '2006',
			  '2007',
			  '2008',
			  '2009',
			  '2010',
			  '2011',
			  '2012',
			  '2013',
			  '2014',
			  '2015',
			  '2016',
			  '2018',
			  '2019',
			  '2020',
			  '2021',
			  '2022',
			  '2023',
			  '2024',
			  '2025',
			  '2026',
			  '2027',
			  '2028',
			  '2029',
			  '2030'

            ],
            default: '2022',
           
        },
		{
            fieldname: 'yearly1',
            label: __('yearly1'),
            fieldtype: 'Select',
            options: [
				'2000',
				'2001',
				'2002',
				'2003',
				'2004',
				'2005',
				'2006',
				'2007',
				'2008',
				'2009',
				'2010',
				'2011',
				'2012',
				'2013',
				'2014',
				'2015',
				'2016',
				'2018',
				'2019',
				'2020',
				'2021',
				'2022',
				'2023',
				'2024',
				'2025',
				'2026',
				'2027',
				'2028',
				'2029',
				'2030'
            ],
            default: '2023',
           
        },


	],		


};





