from __future__ import unicode_literals
from http.client import HTTPResponse
import frappe
from xlsxwriter.workbook import Workbook
import io
from frappe.utils import (
    today,
    format_time,
    global_date_format,
    now,
    get_first_day,
)
from frappe import _




@frappe.whitelist()
def pension_remittance(company=None, from_date=None, to_date=None):
    """
    from io import BytesIO
    import xlsxwriter as xw
    """
    condition_date = ""
    if not from_date:
        from_date = get_first_day(today()).strftime("%Y-%m-%d")
    if not to_date:
        to_date = today()
    
    #date_time = global_date_format(now()) + " " + format_time(now())
    #currency = frappe.db.get_value("Company", company, "default_currency")

    condition_date = "where start_date BETWEEN '"+ from_date + \
        "' AND '" + to_date + "'"
    output = io.BytesIO()
    wbook = Workbook(output, {'in_memory':True})
    nw_data = "SELECT * FROM (select s.name, s.employee_name, s.employee, s.start_date, s.end_date,e.pension_id,v.pension_eyee, v.pension_eyrr,e.name_of_pension_manager,e.pension_manager,e.employee_name as femployee,s.docstatus from `tabSalary Slip` s left join `tabEmployee` e on s.employee = e.name\
			LEFT JOIN\
				(SELECT Distinct k.parent,\
					IFNULL((select d.amount from `tabSalary Detail` d where d.parentfield='deductions'and d.salary_component ='Pension EYEE' and d.parent=k.parent),0) as pension_eyee,\
					IFNULL((select d.amount from `tabSalary Detail` d where d.parentfield='earnings'and d.salary_component = 'Pension EYRR'and d.parent=k.parent),0) as pension_eyrr\
				FROM (select\
				d.amount,\
				d.parent,\
				d.salary_component\
				from `tabSalary Detail` d\
				where d.salary_component\
				in ('Pension EYEE','Pension EYRR')\
				) k\
			) v ON s.name = v.parent ) a {} ".format(condition_date)
    data = frappe.db.sql(nw_data, as_dict=1,)

    pm_lst =[]
    headers_list =[
		'Salary Slip ID','Employee','Employee Name','Start Date','End Date','Pension ID',
		'Pension EYEE','Pension EYRR','Total'
	]
    
    #header format
    heading_format= wbook.add_format({
        "bottom":1,
        "bold": True,
    })
    #data formater
    date_format=wbook.add_format({'num_format': 'mm/dd/yyyy'})
    #money formater
    money_format= wbook.add_format({'num_format':'#,##0'})
    total_format = wbook.add_format({
        "bottom":1,
        "top":1,
        "bold": True,
        'num_format':'#,##0',
    })
    for e in data:
        if e['name_of_pension_manager'] not in pm_lst:
            pm_lst.append(e['name_of_pension_manager'])
    for pm in pm_lst:
        ws = wbook.add_worksheet(pm[:30])
        ws.write_row(3,0, headers_list,heading_format)

        rwnum = 4
        colnum = 0 
        dr_size = 2
        t_contr = 0
        t_liabil = 0
        populate = [x for x in data if x['name_of_pension_manager']==pm]
        for i in range(len(populate)):
            t_con = populate[i]['pension_eyee'] or 0
            t_bill = populate[i]['pension_eyrr'] or 0
            ws.write(rwnum,colnum,populate[i]['name'])
            ws.write(rwnum,colnum+1,populate[i]['employee'])
            ws.write(rwnum,colnum+2,populate[i]['employee_name'])
            ws.write(rwnum,colnum+3,populate[i]['start_date'],date_format)
            ws.write(rwnum,colnum+4,populate[i]['end_date'],date_format)
            ws.write(rwnum,colnum+5,populate[i]['pension_id'])
            ws.write(rwnum,colnum+6,t_con,money_format)
            ws.write(rwnum,colnum+7,t_bill,money_format)
            ws.write(rwnum,colnum+8,t_con+t_bill,money_format)

            rwnum += 1
            t_contr +=t_con
            t_liabil +=t_bill

        ws.write_number(rwnum+dr_size, 6, t_contr,total_format)
        ws.write_number(rwnum+dr_size, 7, t_liabil,total_format)
        ws.write_number(rwnum+dr_size, 8, t_contr+t_liabil,total_format)
        
        ws.write("A1",from_date)
        ws.write("B1",to_date)
        ws.write("A2","Pension Manager")
        ws.write("B2", pm)

    wbook.close()

    output.seek(0)

    frappe.response["filename"] = "penremit.xlsx"
    frappe.response["filecontent"] = output.read()
    frappe.response["type"] = "binary"
    output.close()
    
@frappe.whitelist()
def pay_roll_tax_report(company=None, from_date=None, to_date=None):
    """"""
    condition_date = ""
    if not from_date:
        from_date = get_first_day(today()).strftime("%Y-%m-%d")
    if not to_date:
        to_date = today()
    
    #date_time = global_date_format(now()) + " " + format_time(now())
    #currency = frappe.db.get_value("Company", company, "default_currency")

    condition_date = "where start_date BETWEEN '"+ from_date + \
        "' AND '" + to_date + "'"
    
    output = io.BytesIO()
    #wbook = xw.Workbook(name_path(fp))
    wbook = Workbook(output, {'in_memory':True})
    nw_data = "SELECT * FROM (select \
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

    state_lst =[]
    headers_list =[
		'Salary Slip ID', 'Employee','Employee Name','Tax ID','Date of Joining',
		'Designation','Grade','Start Date','End Date','Tax','Overtime Tax'
	]

    #header format
    heading_format= wbook.add_format({
        "bottom":1,
        "bold": True,
    })
    #data formater
    date_format=wbook.add_format({'num_format': 'mm/dd/yyyy'})
    #money formater
    money_format= wbook.add_format({'num_format':'#,##0'})
    total_format = wbook.add_format({
        "bottom":1,
        "top":1,
        "bold": True,
        'num_format':'#,##0',
    })
    for s in data:
        if s['branch'] not in state_lst:
            state_lst.append(s['branch'])
    for cs in state_lst:
        populate = []
        ws = wbook.add_worksheet(cs[:30])
        ws.write_row(3,0, headers_list,heading_format)

        rwnum = 4
        colnum = 0 
        dr_size = 2
        t_contr = 0
        t_liabil = 0
        populate = [x for x in data if x['branch']==cs]
        for i in range(len(populate)):
            t_con = populate[i]['contrib'] or 0
            t_bill = populate[i]['liabil'] or 0
            ws.write(rwnum,colnum,populate[i]['name'])
            ws.write(rwnum,colnum+1,populate[i]['employee'])
            ws.write(rwnum,colnum+2,populate[i]['employee_name'])
            ws.write(rwnum,colnum+3,populate[i]['tax_id'])
            ws.write(rwnum,colnum+4,populate[i]['date_of_joining'],date_format)
            ws.write(rwnum,colnum+5,populate[i]['designation'])
            ws.write(rwnum,colnum+6,populate[i]['grade'])
            ws.write(rwnum,colnum+7,populate[i]['start_date'],date_format)
            ws.write(rwnum,colnum+8,populate[i]['end_date'],date_format)
            ws.write(rwnum,colnum+9,t_con,money_format)
            ws.write(rwnum,colnum+10,t_bill,money_format)

            rwnum += 1
            t_contr +=t_con
            t_liabil +=t_bill

        ws.write_number(rwnum+dr_size, 9, t_contr,total_format)
        ws.write_number(rwnum+dr_size, 10, t_liabil,total_format)

        ws.write("A1",from_date)
        ws.write("B1",to_date)
        ws.write("A2", "State")
        ws.write("B2", cs)

    wbook.close()
    output.seek(0)

    frappe.response["filename"] = "paytax.xlsx"
    frappe.response["filecontent"] = output.read()
    frappe.response["type"] = "binary"
    output.close()


@frappe.whitelist()
def pay_printslip_formatter (company=None, from_date=None, to_date=None):    
    """ """
    ps = frappe.db.get_list('Salary Slip', filters={'name':'frm.name' },
    fields=['*'])
    #print(f'\n\n\n\n  : {ps} \n\n\n\n')
    


    return True
    #error
    """ response = HTTPResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" )
TypeError: __init__() got an unexpected keyword argument 'content_type'"""

