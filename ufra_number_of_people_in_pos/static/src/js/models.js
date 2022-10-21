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

});
