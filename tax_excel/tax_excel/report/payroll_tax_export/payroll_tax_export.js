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
			let fm_d = frappe.query_report.get_filter_value('date_from_filter');
			let to_d = frappe.query_report.get_filter_value('date_to_filter');

			if (fm_d != undefined && fm_d != "" && to_d != undefined && to_d != "") {
				//method: "tax_excel.tax_excel.utils.pay_roll_tax_report",
				const args = {
					cmd: 'tax_excel.tax_excel.utils.pay_roll_tax_report',
					report_name: `${Date.now()}.xlsx`,
					from_date:fm_d,
					to_date:to_d,
				};
				open_url_post(frappe.request.url, args);
			}
			else{
				//
				frappe.msgprint("Please select a valid 'from date' and or 'to date'");
			}
			
		});
		report.page.change_inner_button_type('Export To Excel',null, 'success');
	},
	/*"formatter": function (value, row, column, data, default_formatter) {
		value = default_formatter(value, row, column, data);

		if (column.fieldname == "contrib" && data && data.debit > 0) {
			value = "<span style='color:red'>" + value + "</span>";
		}
		else if (column.fieldname == "liabil" && data && data.credit > 0) {
			value = "<span style='color:green; font-weight:bolder'>" + value + "</span>";
		}

		return value;
	}*/
};
