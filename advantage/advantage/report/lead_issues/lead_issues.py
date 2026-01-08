import frappe
 

def execute(filters=None):
    filters = frappe._dict(filters or {})
    #filters.meeting= frappe.get_doc('Meeting',{'closed':False}).meet_name
    columns = get_columns(filters)
    data = get_data(filters)
    #data=[]
    #columns =[]
    #data.append({"Shareholdernn":"ahmad","b_party":"ll"})
   #tr_date <= %(trx_date)s
    return columns, data

def get_conditions(filters):
    conditions = {}
    #current_day=frappe.utils.nowdate()
    #conditions="where cast(ts.creation as date) >= cast('"+current_day+"' as Date) and cast(ts.creation as date) <= cast('"+current_day+"' as Date)"
    #conditions="where 1=1 "
    conditions.update({'lead':filters.get("lead")})
    # if filters.get("status") is not None:
    #     if filters.get("status") != "All":
    #     #conditions["status"] = filters.status
    #     #return conditions
    #         conditions += "and  srv_status  =  %(status)s "
    # if filters.get("from_service_creation"):
    #     conditions += "and  cast(ts.creation as date)  >=  cast(%(from_service_creation)s as date) "
    
    # if filters.get("to_service_creation"):
    #     conditions += "and  cast(ts.creation as date)  <=  cast(%(to_service_creation)s as date) "
    return conditions
	

def get_columns(filters):
    columns = [
        {
            "label": "Issue",
            "fieldtype": "Link",
            "fieldname": "issue",
          "options":"Issue",
            "width": 100
        },
        {
            "label": "Subject",
            "fieldtype": "Data",
            "fieldname": "subject",
            "width": 100
        },
        {
            "label": "Type",
            "fieldtype": "Select",
            "options":"Open\nReplied\nOn Hold\nResolved\nClosed",
            "fieldname": "status",
            "width":200
        }, 
         
        {
            "label": "Priority",
            "fieldtype": "Link",
            "options":"Issue Priority",
            "fieldname": "priority",
         
            "width":200
        }, 
        {
            "label": "Issue Type",
            "fieldtype": "Link",
            "options":"Issue Type",
            "fieldname": "issue_type",
         
            "width":200
        },  {
            "label": "Opening Date",
            "fieldtype": "Date",        
            "fieldname": "opening_date",
         
            "width":200
        }
        
    
    
        
         
    ]

    return columns

 

def get_data(filters):

        data = []
        conditions = get_conditions(filters)
        from advantage.advantage.page.lead_overview.lead_overview import get_issues
        result=get_issues(conditions.get('lead'),['name','creation','description','status','priority','issue_type','opening_date','subject'],200)
        for d in result:
            
            #row = {"shareholder": d['name'] ,"shareholdername":d['full_name'],"nationality":d["nationality"] ,"type":d["type"] ,
            #"tranasction": d["transaction_type"],"volume":d["volume"],"price":d["price"],"date":d["tr_date"]
            
            
            #}
            
            row = { "issue":d.name,"status":d.status,"priority":d.priority ,"issue_type":d.issue_type,"opening_date":d.opening_date ,"subject":d.subject
            
            }
            data.append(row)

        return data
