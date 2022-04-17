from . import __version__ as app_version

app_name = "tax_excel"
app_title = "Tax Excel"
app_publisher = "Jide Olayinka"
app_description = "Custom integration to enhenance multi location multi manager reporfor different categories"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "spryng.managed@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/tax_excel/css/tax_excel.css"
# app_include_js = "/assets/tax_excel/js/tax_excel.js"

# include js, css files in header of web template
# web_include_css = "/assets/tax_excel/css/tax_excel.css"
# web_include_js = "/assets/tax_excel/js/tax_excel.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "tax_excel/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {"Salary Structure Assignment" : "tax_excel/helper/assignment.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "tax_excel.install.before_install"
# after_install = "tax_excel.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "tax_excel.uninstall.before_uninstall"
# after_uninstall = "tax_excel.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tax_excel.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"tax_excel.tasks.all"
# 	],
# 	"daily": [
# 		"tax_excel.tasks.daily"
# 	],
# 	"hourly": [
# 		"tax_excel.tasks.hourly"
# 	],
# 	"weekly": [
# 		"tax_excel.tasks.weekly"
# 	]
# 	"monthly": [
# 		"tax_excel.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "tax_excel.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "tax_excel.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "tax_excel.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]
fixtures = ["Custom Field",{
	"doctype":"Print Format",
	"filters": {
		"name": ["in", "Express PSlip"]
	}
},
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"tax_excel.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
