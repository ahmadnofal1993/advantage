import frappe
from frappe.cache_manager import clear_controller_cache, clear_user_cache
from advantage.utils import get_detailed_connections
no_cache = 1


def get_context(context):
     try:          		
        clear_user_cache(frappe.session.user)
        #for dev in frappe.get_all('Weighbridge Devices',filters=[ ["parent", "=", weighbridge_name]],order_by='idx',fields = ['*']):
            #    dev_tp.append({'name':dev.device,'type':dev.type,'gross_tare':dev.taregross})

         #       context.update({"dailytotal":get_total(weighbridge_name)[0][0]})
           #     context.update({"weighbridge":weighbridge_name,"doc_type":weighbridge_doctype,"manual_entry":has_manual_entry})
                
          #      context.update({"dev_list":dev_tp})
          #      context.update({"server_connected":is_url_accessible()})
        context.update({"events_num":0})
       
        return context
     except Exception as e :
         
            frappe.log_error(message=f"  file => scale.py page method =>  get_context  for context {context} {frappe.get_traceback()} ", title="Advantage Page") 


def get_events(lead):
   connections=get_detailed_connections(lead)
   event_participants=[]
   event_participants.append(frappe.get_all('Event Participants', filters=[["reference_doctype",'=','Lead'],['reference_docname','=',lead]],fields=['parent']))
   if len(connections.get('prospects')) > 0 :
      event_participants.append(frappe.get_all('Event Participants', filters=[["reference_doctype",'=','Prospect'],['reference_docname','in',connections.get('prospects')]],fields=['parent']))
   if len(connections.get('opportunities')) > 0 :
      event_participants.append(frappe.get_all('Event Participants', filters=[["reference_doctype",'=','Opportunity'],['reference_docname','in',connections.get('opportunities')]],fields=['parent']))
   event_names = [d['parent'] for d in event_participants]
   return frappe.db.get_list('Event',filters=[['name','in',event_names]])


def get_products(lead):
   connections=get_detailed_connections(lead)
   products=[]
   products.append(frappe.get_all('Advantage Products', filters=[['parent','=',lead]],fields=['product_name']))
   if len(connections.get('opportunities')) > 0 :
      products.append(frappe.get_all('Opportunity Item', filters=[["parenttype",'=','Opportunity'],['parent','in',connections.get('opportunities')]],fields=['item_name']))
   if len(connections.get('customer')) > 0 :
      products.append(frappe.get_all('Customer Items', filters= [['parent','in',connections.get('customer')]],fields=['item']))
   return products
