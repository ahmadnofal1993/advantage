frappe.provide("advantage.utils");
frappe.ui.form.on("Lead", {
    onload: function(frm) {
 
        advantage.utils.set_leaf_filter(frm, "territory");
        
    }
});
