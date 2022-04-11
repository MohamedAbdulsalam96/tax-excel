# Copyright (c) 2022, Jide Olayinka and contributors
# For license information, please see license.txt

import frappe
import xlsxwriter as xw

def execute(filters=None):
	"""Tax report tester"""
	condition_date = ""
	condition_pm = ""
	if filters.date_from_filter and filters.date_to_filter :
		if filters.date_from_filter == None:
			filters.date_from_filter = frappe.datetime.get_today()
		if filters.date_to_filter == None:
			filters.date_to_filter = frappe.datetime.get_today()
		condition_date = "where start_date BETWEEN '"+ filters.date_from_filter + \
        "' AND '" + filters.date_to_filter + "'"

	if filters.get("pm_filter"):
		pm_item = filters.get("pm_filter")
		#print(f"view it {pm_item} ")
		condition_pm += f" AND name_of_pension_manager = '{pm_item}'"

	columns = [
    {'fieldname':'name','label':'Salary Slip ID','width':'200'},
    {'fieldname':'employee','label':'Employee','width':'120'},
	{'fieldname':'employee_name','label':'Employee Name','width':'150'},
	{'fieldname':'date_of_joining','label':'Date Join','width':'100'},
	{'fieldname':'branch','label':'Current State','width':'100'},    
	{'fieldname':'designation','label':'Designation','width':'100'},
	{'fieldname':'department','label':'Department','width':'150'},
	{'fieldname':'contrib','label':'Tax','width':'150'},
	{'fieldname':'liabil','label':'Overtime Tax','width':'150'},
	]
	
	nw_data = "SELECT name, employee,employee_name,date_of_joining,department,designation,grade,start_date,end_date,contrib,liabil,branch FROM (select \
		s.name,s.employee,s.employee_name,s.start_date,s.end_date,s.docstatus, \
		e.tax_id,e.date_of_joining,e.department,e.current_state_of_abode_ as branch,e.designation,e.grade, e.pension_id,e.name_of_pension_manager,e.pension_manager,e.employee_name as femployee, \
		v.contrib, v.liabil,v.parent \
 		from `tabSalary Slip` s left join `tabEmployee` e on s.employee = e.name \
		LEFT JOIN \
				(SELECT Distinct k.parent, \
        					IFNULL((select d.amount from `tabSalary Detail` d where d.parentfield='deductions'and d.salary_component ='Tax' and d.parent=k.parent),0) as contrib, \
        					IFNULL((select d.amount from `tabSalary Detail` d where d.parentfield='deductions'and d.salary_component = 'Overtime Tax'and d.parent=k.parent),0) as liabil \
        FROM (select d.amount,d.parent,d.salary_component from `tabSalary Detail` d where d.salary_component in ('Tax','Overtime Tax') ) k \
			) v ON s.name = v.parent ) a {} ".format(condition_date) 

	data = frappe.db.sql(nw_data, as_dict=1,)

	return columns, data
