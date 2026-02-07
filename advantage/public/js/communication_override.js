// apps/your_app/your_app/public/js/custom_communication.js

// Ensure the original class is loaded before we try to extend it
$(document).ready( function() {
    
    if (frappe.views.CommunicationComposer) {
        
        // 1. Save the original class reference (optional, if you need super calls)
        const OriginalComposer = frappe.views.CommunicationComposer;

        // 2. Override the class directly in the global namespace
        frappe.views.CommunicationComposer = class CustomCommunicationComposer extends OriginalComposer {
            
            // Example 1: Overriding the 'make' function (Initial rendering)
             get_fields() {
                let me=this;
                // Call the original logic first
                let fields = super.get_fields();
               
                let senderIndex = fields.findIndex(f => f.fieldname === 'sender');

                if (senderIndex !== -1) {
                  
                       frappe.call({
                        method: "advantage.utils.get_sender_email",   // dotted path to server method
                        async: false, 
                        callback: function(r) {
                            console.log(r.message);
                            if (r.message != undefined && r.message.length > 0 )
                              {
                                
                              
                                let my_custom_sender = {
                                    label: __('From'),
                                    fieldname: 'sender',
                                    fieldtype: 'Select',                                 
                                    // Example: Hardcoding options or logic to get them
                                    options:r.message,
                                    default: r.message[0],  
                                    onchange: () => {
                                        me.setup_recipients_if_reply();
                                    },
                                };
                               
                                // 4. Replace the original field with your new one
                                fields[senderIndex] = my_custom_sender;
                                
                              
                            }
                        },
                        
                    });
                    
                  
                    // 3. Define your NEW Sender Field
                    // You can change the fieldtype, options, label, etc.
       

                    
                }
                
                return fields;
               
                // Add your custom logic here
                // Example: Pre-fill the subject field differently
                // this.dialog.set_value('subject', 'Custom Subject Prefix: ');
            }

           
        };
    }
});