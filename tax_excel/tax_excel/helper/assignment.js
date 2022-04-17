frappe.ui.form.on("Salary Structure Assignment", {
	
	employee(frm){
		if(frm.is_new()){
			frappe.db.get_doc("Employee", frm.doc.employee)
			.then(ec =>{
				if(ec.annual_salary > 0){
					cur_frm.set_value("base", (ec.annual_salary/12));
				}
				
			});
		}
	},
	
});