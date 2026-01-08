// Copyright (c) 2026, ItsPrivate and contributors
// For license information, please see license.txt

frappe.query_reports["Lead Events"] = {
	"filters": [
        {
            "fieldname": "lead",
            "label": __("Lead"),
            "fieldtype": "Link",
            "options": "Lead",
            
        },
	]
};
