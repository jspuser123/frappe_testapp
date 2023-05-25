
frappe.ui.form.on('Sales Order', {

	refresh:function (frm)

	{
		
		if (frm.doc.spiit == true)
		{
		
			// df = frappe.meta.get_docfield("Sales Order Item", "splite_rate", frm.doc.items[0].name);
			// df.hidden = 1;
			let value = {};
			value['Sales Order Item'] = [{ fieldname: "item_code", columns: 2 },{ fieldname: "delivery_date", columns: 2 },{ fieldname: "qty", columns: 1 },{ fieldname: "rate", columns: 2 },{ fieldname: "amount", columns: 2 },{ fieldname: "splite_rate", columns: 1 }];
			console.log(value)
			frappe.model.user_settings.save('Sales Order', 'GridView', value)
				.then((r) => {
					frappe.model.user_settings['Sales Order'] = r.message || r;
					frm.fields_dict["items"].grid.reset_grid()
				});
	
		
	
	
		}
		else
		{
			let value = {};
			value['Sales Order Item'] = [{ fieldname: "item_code", columns: 3 },{ fieldname: "delivery_date", columns: 2 },{ fieldname: "qty", columns: 1 },{ fieldname: "rate", columns: 2 },{ fieldname: "amount", columns: 2 }];
			console.log(value)
			frappe.model.user_settings.save('Sales Order', 'GridView', value)
				.then((r) => {
					frappe.model.user_settings['Sales Order'] = r.message || r;
					frm.fields_dict["items"].grid.reset_grid()
				});
				
		}
	
	},
	


spiit:function (frm)

{
	
	if (frm.doc.spiit == true)
	{
	
		// df = frappe.meta.get_docfield("Sales Order Item", "splite_rate", frm.doc.items[0].name);
		// df.hidden = 1;
		let value = {};
		value['Sales Order Item'] = [{ fieldname: "item_code", columns: 2 },{ fieldname: "delivery_date", columns: 2 },{ fieldname: "qty", columns: 1 },{ fieldname: "rate", columns: 2 },{ fieldname: "amount", columns: 2 },{ fieldname: "splite_rate", columns: 1 }];
		frappe.model.user_settings.save('Sales Order', 'GridView', value)
			.then((r) => {
				frappe.model.user_settings['Sales Order'] = r.message || r;
				frm.fields_dict["items"].grid.reset_grid()
			});

	


	}
	else
	{
		let value = {};
		value['Sales Order Item'] = [{ fieldname: "item_code", columns: 3 },{ fieldname: "delivery_date", columns: 2 },{ fieldname: "qty", columns: 1 },{ fieldname: "rate", columns: 2 },{ fieldname: "amount", columns: 2 }];
		console.log(value)
		frappe.model.user_settings.save('Sales Order', 'GridView', value)
			.then((r) => {
				frappe.model.user_settings['Sales Order'] = r.message || r;
				frm.fields_dict["items"].grid.reset_grid()
			});
			
	}

}

});


frappe.ui.form.on('Sales Order Item',{
	
	splite_rate: function(frm, cdt, cdn) {

		if (frm.doc.spiit == true)
		{

		var d = locals[cdt][cdn];

		// console.log(cdn,cdt,d.item_code,d.delivery_date,d.qty,d.rate,d.amount)
		// frappe.model.set_value(cdt, cdn, 'amount', d.amount / 2);
		// frappe.model.set_value(cdt, cdn, 'rate', d.rate / 2);
		// let row = frm.add_child('items', {
		// 	item_code:d.item_code,
		// 	delivery_date:d.delivery_date,
		// 	qty:d.qty,
		// 	amount: d.amount,
		// 	rate: d.rate			
		// });
		// frm.refresh_field('items');

		let dia = new frappe.ui.Dialog({
			title: 'Enter details',
			fields: [
				{
					label: 'Delivery Date',
					fieldname: 'date',
					fieldtype: 'Date',
					default: d.delivery_date,
					read_only: 1,
					
				},
		
				{
					label: 'Qty',
					fieldname: 'qty',
					fieldtype: 'Int',
					default: d.qty,
					read_only: 1,
				},
				{
					label: 'Table',
					fieldname: 'table',
					fieldtype: 'Table',
					cannot_add_rows: false,
					in_place_edit: false,
					data: [{qty1:null,date1:null}],
					
					fields: [
							{ fieldname: 'qty1', fieldtype: 'Data', in_list_view: 1, label: 'qty' ,read_only: 0,reqd: 1},
							{ fieldname: 'date1', fieldtype: 'Date', in_list_view: 1, label: 'date' ,read_only: 0,reqd: 1},								
					],
			
					}

			],
		
			primary_action_label: 'Submit',
			primary_action(values) {
				console.log(values)
				const arr = [];
				for (var i of values.table) {    
					arr.push(Number(i.qty1))					
     
				}
				const total = arr.reduce((acc, curr) => acc + curr, 0);

				if (values.qty === total )
				{
				
					frappe.model.set_value(cdt, cdn, 'qty', arr[0]);
					frappe.model.set_value(cdt, cdn, 'delivery_date', values.table[0].date1);
					const data1 = [];
					values.table.shift();
					for (var a of values.table) { 							   
						let row = frm.add_child('items', {
							item_code:d.item_code,
							delivery_date:a.date1,
							qty:a.qty1,
							amount: d.amount,
							rate: d.rate			
						});
		 
					}
					
					frm.refresh_field('items');
					dia.hide();

				}
				else
				{
					frappe.msgprint(('This value not split'));
				}
				
			}
		});
		
		dia.show();
		
	}
	else{
		frappe.msgprint(("this is value",frm.doc.spiit));
	}
	}

});

