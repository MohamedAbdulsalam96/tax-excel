// Copyright (c) 2022, Jide Olayinka and contributors
// For license information, please see license.txt

frappe.ui.form.on('Payslip Viewer', {
	onload_post_render: function (frm){
		frm.disable_save();
		/*frm.call('get_info').then( r => {
			frm.refresh();
		})*/
	},
	refresh: function (frm) {
		// Default values in From and To Dates
		var today = frappe.datetime.nowdate();
		frm.set_value('from_date', frappe.datetime.month_start(today));
		frm.set_value('to_date', today);
	  },

	  export_pension: function (frm) {
		  if (frm.doc.from_date != undefined && frm.doc.from_date != "" && frm.doc.to_date != undefined && frm.doc.to_date != "") {
			const args = {
				cmd: 'tax_excel.tax_excel.utils.pension_remittance',
				report_name: `${Date.now()}.xlsx`,
				from_date:frm.doc.from_date,
				to_date:frm.doc.to_date,
			};
			open_url_post(frappe.request.url, args);
		  }
		  else{
			frappe.msgprint("Please select a 'from date' or 'to date'");
		  }

	  },

	  payroll_tax: function (frm) {
		  if (frm.doc.from_date != undefined && frm.doc.from_date != "" && frm.doc.to_date != undefined && frm.doc.to_date != "") {
			  //"tax_excel.tax_excel.utils.pay_roll_tax_report",
				const args = {
					cmd: 'tax_excel.tax_excel.utils.pay_roll_tax_report',
					report_name: `${Date.now()}.xlsx`,
					from_date:frm.doc.from_date,
					to_date:frm.doc.to_date,
				};
				open_url_post(frappe.request.url, args);
		  }
		  else{
			frappe.msgprint("Please select a 'from date' or 'to date'");
		  }
		

	  },

	  payroll_detail: function (frm) {
		  //pending reports
		  if (frm.doc.company) {
			frappe.call({
				method: "tax_excel.tax_excel.utils.pay_printslip_formatter",
				args: {
				  company: frm.doc.company,
				  from_date: frm.doc.from_date,
				  to_date: frm.doc.to_date
				},
				callback: function (r) {
					let msg = r.message;
					//let a = "<a href='"+msg+"' target='_blank' >here</a>";
					frappe.msgprint({
						title: __('Notification'),
						  indicator: 'green',
						  message: msg
					  });
				}
			  });
		  }
		  else{
			frappe.msgprint("Please select a 'from date' or 'to date'");
		  } 
	  }
});
