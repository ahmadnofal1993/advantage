frappe.pages['lead-summary'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
	 
		single_column: true
	});
	$(frappe.render_template("lead_summary")).appendTo(page.main);
	page.wrapper.find('.layout-main-section').css({
        'max-width': '100%',
        'width': '100%',
        'padding': '0'
    });
    
    // Optional: Remove default padding from the page body
    page.wrapper.find('.page-body').css({
        'min-height': 'calc(100vh - 100px)' // Ensure full height usage
    });
	$('header.navbar').hide();
    
    // Hide Page Title
    page.wrapper.find('.page-head').hide();
    
    // Remove spacing
    $('.page-container').css('padding-top', '0');

    let lead_summary = new LeadSummary(wrapper);
    
}
LeadSummary = class {
    constructor(wrapper) {
      this.wrapper = $(wrapper).find(".layout-main-section");
    
      this.init(wrapper);
      this.make_inupt(wrapper);
     
    }
    async get_lead(lead){
        await frappe
        .call({
          method: "advantage.advantage.page.lead_summary.lead_summary.get_events",
          args: {
            lead: lead,
          },
          async: false,
        })
        .then((r) => {
          if (r.message) {
            console.log(r);
           
          }
        });
    }
    test(ff){
        console.log(ff);
    }
    make_inupt(wrapper){
        let me=this;
        let field = frappe.ui.form.make_control(
            { df:
                { fieldname: 'linked_customer',
                 label: 'Linked Customer',
                  fieldtype: 'Link', 
                  options: 'Customer' ,
                  change: function() {    // Event handler
                    // code on change
                    me.test(this);
                }
                }, 
                parent: me.wrapper.find("#customer"), 
                //only_input: true ,
                render_input: true       
        });
      // field.make_input();
    }
    async init(wrapper) {
      var me = this;
      $(me.wrapper.find("#lead"))[0].addEventListener(
        "click",
        function () {
          // In a real implementation, this would connect to the scale hardware
          // For demo purposes, we'll simulate a weight reading
            me.get_lead('CRM-LEAD-2025-00002')
          console.log("Ho");
        }
      );
    }
}