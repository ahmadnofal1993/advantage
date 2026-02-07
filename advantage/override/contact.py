
import frappe

from frappe.contacts.doctype.contact.contact import Contact
from advantage.utils import get_detailed_connections

class AdvantageContact(Contact):
    def on_update(self):
        # if frappe.db.count("Dynamic Link", filters={"parent" :self.name,"link_doctype":"Lead","parenttype" :"Contact"}) > 1 :
        #     frappe.throw("Can't Link to Multiple Leads")
        # if frappe.db.count("Dynamic Link", filters={"parent" :self.name,"link_doctype":"Prospect","parenttype" :"Contact"}) > 0 :
        #     frappe.throw("Can't Link to Prospect")
        # else:
        #     leads=[]
        #     for m in  frappe.get_all('Dynamic Link', filters=[["link_doctype",'in',['Opportunity','Customer','Lead']],["parent" ,"=",self.name],["parenttype","=","Contact"]],fields=['*']):
        #         if frappe.get_doc(m.link_doctype,m.link_name).doctype=='Customer':
        #             leads.append(frappe.get_doc(m.link_doctype,m.link_name).lead_name)
        #         elif frappe.get_doc(m.link_doctype,m.link_name).doctype=='Opportunity':
        #             leads.append(frappe.get_doc(m.link_doctype,m.link_name).party_name)
        #         else:
        #             leads.append(frappe.get_doc(m.link_doctype,m.link_name).name)
        #     if len(set(leads)) != 1 :
        #         frappe.throw("Can't Link to different Leads")
        self.update_company()
    def after_insert(self):
        self.update_company()

    def deny_multiple(self):
       
        contact= self.name
        phones = [m.phone for m in self.phone_nos ]
        distinct_phone= list(set(phones))
        phones_string = "('" + "','".join(distinct_phone) + "')"
        data = frappe.db.sql(f"""
            SELECT f.* 
            FROM `tabContact Phone` tcp  
            JOIN `tabContact` f ON (tcp.parent = f.name)
            WHERE tcp.parenttype = 'Contact' 
            AND tcp.parent = '{contact}' 
            AND f.phone IN {phones_string}
        """, as_dict=True)
        return data
    def update_company(self):
        # contact= self.name
        # user_role = "System Manager"

        # data = frappe.db.sql("""
        #     SELECT parent 
        #     FROM `tabDynamic Link`
        #     WHERE parent = %s AND role = %s
        # """, (contact, user_role))
        for dynamic_link in frappe.get_all('Dynamic Link', filters=[["link_doctype",'in',['Opportunity','Customer','Lead']],["parent" ,"=",self.name],["parenttype","=","Contact"]],fields=['link_doctype','link_name']):    
            doc=frappe.get_doc(dynamic_link.link_doctype,dynamic_link.link_name)
            self.db_set('company_name',doc.company,False,False,True)   