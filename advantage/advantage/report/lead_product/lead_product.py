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
            "label": "Item",
            "fieldtype": "Data",
            "fieldname": "item",
         
            "width": 100,
        },
         {
            "label": "Type",
            "fieldtype": "Data",
            
            "fieldname": "subject",
         
            "width":200,
        }, 
         
           {
            "label": "Creation",
            "fieldtype": "Datetime",
           
            "fieldname": "starts_on",
         
            "width":200,
        }, 
        
    
    
        
         
    ]

    return columns

 

def get_data(filters):

        data = []
        conditions = get_conditions(filters)
        from advantage.advantage.page.lead_overview.lead_overview import get_products
        result=get_products(conditions.get('lead'),[],200)
        for d in result:
            
            #row = {"shareholder": d['name'] ,"shareholdername":d['full_name'],"nationality":d["nationality"] ,"type":d["type"] ,
            #"tranasction": d["transaction_type"],"volume":d["volume"],"price":d["price"],"date":d["tr_date"]
            
            
            #}
            
            row = { "item":d.item,"subject":d.subject,"event_type":d.event_type ,"status":d.status,"starts_on":d.creation 
            
            }
            data.append(row)

        return data
