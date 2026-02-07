(() => {
  // ../advantage/advantage/public/js/utils.bundle.js
  frappe.provide("advantage.utils");
  advantage.utils.set_leaf_filter = function(frm, fieldname) {
    frm.set_query(fieldname, function() {
      return {
        filters: {
          is_group: false
        }
      };
    });
  };
})();
//# sourceMappingURL=utils.bundle.ZOM5CJPQ.js.map
