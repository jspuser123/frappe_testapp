from . import __version__ as app_version

app_name = "testapp"
app_title = "test"
app_publisher = "jagan"
app_description = "no"
app_icon = "yes"
app_color = "yes"
app_email = "asp@gmail.com"
app_license = "no"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/testapp/css/testapp.css"
# app_include_js = "/assets/testapp/js/testapp.js"

# include js, css files in header of web template
# web_include_css = "/assets/testapp/css/testapp.css"
# web_include_js = "/assets/testapp/js/testapp.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "testapp/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Sales Order" : "public/js/sales_order.js"}
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

# before_install = "testapp.install.before_install"
# after_install = "testapp.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "testapp.uninstall.before_uninstall"
# after_uninstall = "testapp.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "testapp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	# "*": {
        
	# 	"on_update": "method",
	# 	"on_cancel": "method",
	# 	"on_trash": "method"
        
	# }

	'Sales Order':{
        "before_save": "testapp.test.test_sales.s1"
	} 

}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"testapp.tasks.all"
#	],
#	"daily": [
#		"testapp.tasks.daily"
#	],
#	"hourly": [
#		"testapp.tasks.hourly"
#	],
#	"weekly": [
#		"testapp.tasks.weekly"
#	]
#	"monthly": [
#		"testapp.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "testapp.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "testapp.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "testapp.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Request Events
# ----------------
# before_request = ["testapp.utils.before_request"]
# after_request = ["testapp.utils.after_request"]

# Job Events
# ----------
# before_job = ["testapp.utils.before_job"]
# after_job = ["testapp.utils.after_job"]

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

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"testapp.auth.validate"
# ]

