// Copyright (c) 2022, Jide Olayinka and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Pension Remittance Export"] = {
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
			let frm_d = frappe.query_report.get_filter_value('date_from_filter');
			let to_d = frappe.query_report.get_filter_value('date_to_filter');

			if (frm_d != undefined && frm_d != "" && to_d != undefined && to_d != ""){
				const args = {
					cmd: 'tax_excel.tax_excel.utils.pension_remittance',
					report_name: `${Date.now()}.xlsx`,
					from_date:frm_d,
					to_date:to_d,
				};
				open_url_post(frappe.request.url, args);
			}
			else{
				//
				frappe.msgprint("Please select a valid 'from date' and or 'to date'");
			}
			
		},);
		report.page.change_inner_button_type('Export To Excel', null, 'success');
	},
	
};