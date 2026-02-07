
import frappe
from erpnext.selling.doctype.customer.customer import Customer
from advantage.utils import get_detailed_connections
class AdvantageCustomer(Customer):
    def on_update(self):
        if self.lead_name is not None and self.lead_name != "" and self.opportunity_name is not None and self.opportunity_name != "":
            connections=get_detailed_connections(self.lead_name)
            if len(connections.get('opportunities')) > 0 :
                if self.opportunity_name not in  connections.get('opportunities') :
                    frappe.throw(frappe._("Lead and Opportunities not to same Person"))
