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
            "label": "Note",
            "fieldtype": "Data",
            "fieldname": "note",
         
            "width": 200
        },
        {
            "label": "Added On",
            "fieldtype": "Datetime",
            "fieldname": "added_on",
            "width": 100
        },
        {
            "label": "Owner",
            "fieldtype": "Link",
            "options":"User",
            "fieldname": "user",
         
            "width":200
        },  
    
    
        
         
    ]

    return columns

 

def get_data(filters):

        data = []
        conditions = get_conditions(filters)
        from advantage.advantage.page.lead_overview.lead_overview import get_notes
        result=get_notes(conditions.get('lead'),['owner','note','parent','added_on','parenttype'],200)
        for d in result:
            
            #row = {"shareholder": d['name'] ,"shareholdername":d['full_name'],"nationality":d["nationality"] ,"type":d["type"] ,
            #"tranasction": d["transaction_type"],"volume":d["volume"],"price":d["price"],"date":d["tr_date"]
            
            
            #}
            
            row = { "note":d.note,"user":d.owner,"added_on":d.added_on
            
            }
            data.append(row)

        return data
