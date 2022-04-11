# Copyright (c) 2022, Jide Olayinka and contributors
# For license information, please see license.txt

import frappe
import xlsxwriter as xw

def execute(filters=None):
	"""button to export"""
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
	{'fieldname':'date_of_joining','label':'Date of Joining','width':'120'},
	{'fieldname':'name_of_pension_manager','label':'Pension Manager','width':'200'},
	{'fieldname':'pension_id','label':'Pension ID','width':'160'},
	{'fieldname':'pension_eyrr','label':'Pension EYRR','width':'100'},
	{'fieldname':'pension_eyee','label':'Pension EYEE','width':'100'},
	]
	nw_data = "SELECT * FROM (select s.name, s.employee_name, s.employee, s.start_date, s.end_date,e.pension_id,v.pension_eyrr, v.pension_eyee,e.date_of_joining,e.name_of_pension_manager,e.pension_manager,e.employee_name as femployee,s.docstatus from `tabSalary Slip` s left join `tabEmployee` e on s.employee = e.name\
			LEFT JOIN\
				(SELECT Distinct k.parent,\
					IFNULL((select d.amount from `tabSalary Detail` d where d.parentfield='deductions'and d.salary_component ='Pension contribution Employee' and d.parent=k.parent),0) as pension_eyrr,\
					IFNULL((select d.amount from `tabSalary Detail` d where d.parentfield='earnings'and d.salary_component = 'Pension Employer Contr.'and d.parent=k.parent),0) as pension_eyee\
				FROM (select\
				d.amount,\
				d.parent,\
				d.salary_component\
				from `tabSalary Detail` d\
				where d.salary_component\
				in ('Pension contribution Employee','Pension Employer Contr.')\
				) k\
			) v ON s.name = v.parent ) a {} ".format(condition_date)

	data = frappe.db.sql(nw_data, as_dict=1,)

	return columns, data
