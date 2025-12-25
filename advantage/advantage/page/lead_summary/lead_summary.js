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
}