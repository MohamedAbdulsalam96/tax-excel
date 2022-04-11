// Copyright (c) 2022, Jide Olayinka and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Payroll Tax Export"] = {
	"filters": [
		{
			fieldname: "date_from_filter",
			label: "Time From Filter",
			fieldtype: "Date",

		},
		{
			fieldname: "date_to_filter",
			label: "Time To Filter",
			fieldtype: "Date",

		}

	],
	onload: function(report){
		report.page.add_inner_button(__("Export To Excel"), function(){
			var fm_d = frappe.query_report.get_filter_value('date_from_filter');
			var to_d = frappe.query_report.get_filter_value('date_to_filter');
			//console.log
			if (fm_d != undefined && fm_d != "" && to_d != undefined && to_d != "") {
				//
				frappe.call({				
					method: "tax_excel.tax_excel.utils.pay_roll_tax_report",
					args: {
					  company: report.company,
					  from_date: fm_d,
					  to_date: to_d
					},
					callback: function (r) {
						if (r.message.length > 0) {
							//
							let msg = r.message;
							let a = "<a href='"+msg+"' target='_blank' >here</a>";
							frappe.msgprint({
								title: __('Notification'),
								indicator: 'green',
								message: __('Document exported successfully get file '+a)
							});
						}
						else{
							frappe.msgprint({
								title: __('Notification'),
								indicator: 'red',
								message: __('No record to export')
							});
						}
					  
					}
				});
			}
			else{
				//
				frappe.msgprint("Please select a valid 'from date' and or 'to date'");
			}
			
		});
		report.page.change_inner_button_type('Export To Excel',null, 'success');
	}
};
