
import frappe

from frappe.contacts.doctype.contact.contact import Contact
from advantage.utils import get_detailed_connections

class AdvantageContact(Contact):
    def on_update(self):
        if frappe.db.count("Dynamic Link", filters={"parent" :self.name,"link_doctype":"Lead","parenttype" :"Contact"}) > 1 :
            frappe.throw("Can't Link to Multiple Leads")
        if frappe.db.count("Dynamic Link", filters={"parent" :self.name,"link_doctype":"Prospect","parenttype" :"Contact"}) > 0 :
            frappe.throw("Can't Link to Prospect")
        else:
            leads=[]
            for m in  frappe.get_all('Dynamic Link', filters=[["link_doctype",'in',['Opportunity','Customer','Lead']],["parent" ,"=",self.name],["parenttype","=","Contact"]],fields=['*']):
                if frappe.get_doc(m.link_doctype,m.link_name).doctype=='Customer':
                    leads.append(frappe.get_doc(m.link_doctype,m.link_name).lead_name)
                elif frappe.get_doc(m.link_doctype,m.link_name).doctype=='Opportunity':
                    leads.append(frappe.get_doc(m.link_doctype,m.link_name).party_name)
                else:
                    leads.append(frappe.get_doc(m.link_doctype,m.link_name).name)
            if len(set(leads)) != 1 :
                frappe.throw("Can't Link to different Leads")
