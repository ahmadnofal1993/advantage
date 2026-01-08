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
            "label": "Event",
            "fieldtype": "Link",
            "fieldname": "event_name",
            "options":"Event",
            "width": 100,
        },
        {
            "label": "Subject",
            "fieldtype": "Data",
            "fieldname": "subject",
         
            "width": 100,
        },
         {
            "label": "Event Category",
            "fieldtype": "Select",
             "options": "Event\nMeeting\nCall\nSent/Received Email\nOther",
            "fieldname": "event_category",
         
            "width":200,
        }, 
        {
            "label": "Event Type",
            "fieldtype": "Select",
             "options": "Private\nPublic",
            "fieldname": "event_type",
         
            "width":200,
        }, 
        {
            "label": "Status",
            "fieldtype": "Select",
             "options": "Open\nCompleted\nClosed\nCancelled",
            "fieldname": "status",
         
            "width":200,
        }, 
           {
            "label": "Start on",
            "fieldtype": "Datetime",
           
            "fieldname": "starts_on",
         
            "width":200,
        }, 
        
    
    
        
         
    ]

    return columns

 

def get_data(filters):

        data = []
        conditions = get_conditions(filters)
        from advantage.advantage.page.lead_overview.lead_overview import get_events
        result=get_events(conditions.get('lead'),['subject','status','name','event_category','creation','event_type','starts_on'],200)
        for d in result:
            
            #row = {"shareholder": d['name'] ,"shareholdername":d['full_name'],"nationality":d["nationality"] ,"type":d["type"] ,
            #"tranasction": d["transaction_type"],"volume":d["volume"],"price":d["price"],"date":d["tr_date"]
            
            
            #}
            
            row = { "subject":d.subject,"event_category":d.event_category,"event_type":d.event_type ,"status":d.status,"starts_on":d.starts_on ,"event_name":d.name
            
            }
            data.append(row)

        return data
