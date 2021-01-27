odoo.define('sta_cert_statistics.tree_view_button', function (require){
"use strict";

var core = require('web.core');
var ListView = require('web.ListView');
var QWeb = core.qweb;

ListView.include({

        render_buttons: function($node) {
                var self = this;
                this._super($node);
                    this.$buttons.find('.certificate_info_export_excel_button').click(this.proxy('tree_view_action'));
        },

        tree_view_action: function () {

        this.do_action({
                type: "ir.actions.act_window",
                name: "Export Excel Option",
                res_model: "certificate.info.excel.export.wizard",
                views: [[false,'form']],
                target: 'new',
                // view_type : 'form',
                // view_mode : 'form',
                // flags: {'form': {'action_buttons': true, 'options': {'mode': 'edit', 'no_open': true}}}
        });
        return { 'type': 'ir.actions.client','tag': 'reload', } }

});

});