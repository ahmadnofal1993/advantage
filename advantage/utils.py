import frappe
from frappe.permissions import AUTOMATIC_ROLES
import datetime


def get_permission_query_conditions(user):
    if not user:
        user = frappe.session.user

    task_roles = frappe.permissions.get_doctype_roles("Task")
    task_roles = set(task_roles) - set(AUTOMATIC_ROLES)

    #if any(check in task_roles for check in frappe.get_roles(user)):
    #    return None
    #else:
    if 'Task Admin' in  frappe.get_roles(user) :
        return None
    else:
        return """ ( `tabTask`.name in (select reference_name from `tabToDo` where `tabToDo`.reference_type='Task' and `tabToDo`.status !='Cancelled' and   (`tabToDo`.allocated_to = {user} or `tabToDo`.assigned_by = {user}))) """.format(
            user=frappe.db.escape(user)
        )


def has_permission(doc, ptype="read", user=None):

    user = user or frappe.session.user   
    if 'Task Admin' in  frappe.get_roles(user) :
        return True
    if len(frappe.get_all('ToDo', filters=[["reference_type",'=','Task'],['reference_name','=',doc.name],['status','!=','Cancelled']],or_filters=[["ToDo", "allocated_to", "=", user],["ToDo", "assigned_by", "=", user],],fields=['*'])) ==1:
        return True
    else:
        return False



def get_lead_phone_numbers(lead_name):
    connections=get_detailed_connections(lead_name)
    combined = sum(connections.values(), [])
    combined.append(lead_name)
    data_set=set(combined)
    final_list=list(data_set)    
    dynamic_link=frappe.get_all('Dynamic Link', filters=[["parenttype",'=','Contact'],['parentfield','=','links'],['link_name','in',final_list]],fields=['parent'])
    if len(dynamic_link) > 0 :
        contacts =list(set( [d['parent'] for d in dynamic_link]))
        phones=frappe.get_all('Contact Phone', filters=[["parenttype",'=','Contact'],['parent','in',contacts]],fields=['phone'])
        if len(phones) > 0 :
            return   list(set( [ str(d['phone']).strip() for d in phones]))

def get_detailed_connections(lead_name):
    connections = {}

    # 1. Get Opportunities
    connections['opportunities'] = frappe.db.get_list("Opportunity", 
        filters={"party_name": lead_name, "opportunity_from": "Lead"},
        pluck='name'
    )

    # 2. Get Quotations
    connections['quotations'] = frappe.db.get_list("Quotation", 
        filters={"party_name": lead_name, "quotation_to": "Lead"},
       pluck='name'
    )

    # 3. Get Prospects (If linked)
    # Note: Prospects usually link TO leads, or Leads link TO prospects depending on flow
    connections['prospects'] = frappe.db.get_list("Prospect",
        filters={"lead": lead_name},
        pluck='name'
    )

    # 4. Get Customer (If converted)
    connections['customer'] = frappe.db.get_list("Customer",
        filters={"lead_name": lead_name},
       pluck='name'
    )

    return connections



 

def format_datetime(dt: datetime.datetime) -> str:
    # Helper: add suffix to day
    def day_with_suffix(day: int) -> str:
        if 11 <= day <= 13:
            return f"{day}th"
        else:
            return f"{day}{['th','st','nd','rd','th'][min(day % 10, 4)]}"
    
    # Build formatted string
    return f"{day_with_suffix(dt.day)} {dt.strftime('%B %Y %I:%M%p')}"
 
def show_how_old(dt: datetime.datetime) -> str:
    now = datetime.datetime.now()

    # Calculate difference
     
    delta = now - dt

    # Format as "X days ago"
    days_ago = f"{delta.days} days ago"
    return days_ago
