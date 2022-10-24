odoo.define('ufra_number_of_people_in_pos.models', function (require) {
'use strict';


    const models = require('point_of_sale.models');

    const _super_pos = models.PosModel.prototype;
    models.PosModel = models.PosModel.extend({

        initialize: function(attributes)
        {
            _super_pos.initialize.apply(this, arguments);

            const resPartnerModel = _.find(this.models, function (el)
            {
                return el.model === 'res.partner';
            });
            resPartnerModel.fields.push('number_of_adults');
            resPartnerModel.fields.push('number_of_children');

        },

    });

    const _super_order = models.Order.prototype;
    models.Order = models.Order.extend({
        init_from_JSON: function(json)
        {
            _super_order.init_from_JSON.apply(this, arguments);

            const client = this.get_client();
            this.number_of_adults = json['number_of_adults'] || client.number_of_adults;
            this.number_of_children = json['number_of_children'] || client.number_of_children;

        },

        export_as_JSON: function()
        {
            const json = _super_order.export_as_JSON.apply(this, arguments);

            json['number_of_adults'] = this.number_of_adults;
            json['number_of_children'] = this.number_of_children;

            return json;
        },
    });

});
