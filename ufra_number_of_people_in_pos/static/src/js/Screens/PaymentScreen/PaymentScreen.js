odoo.define('ufra_number_of_people_in_pos.PaymentScreen', function (require) {
'use strict';

const PaymentScreen = require('cha.PaymentScreen');
const Registries = require('point_of_sale.Registries');

const UFRAPaymentScreen = (PaymentScreen) =>
    class extends PaymentScreen {

        constructor()
        {
            super(...arguments);

            this.changes['number_of_adults'] = this.currentOrder.number_of_adults || 1;
            this.changes['number_of_children'] = this.currentOrder.number_of_children || 0;

            console.log(this.currentOrder);
        }

        async _finalizeValidation()
        {

            this.currentOrder.number_of_adults = this.changes.number_of_adults;
            this.currentOrder.number_of_children = this.changes.number_of_children;

            await super._finalizeValidation(...arguments);
        }

        async selectClient() {
            const oldClient = this.currentOrder.get_client();
            await super.selectClient();

            const client = this.currentOrder.get_client();
            if (oldClient !== client) {
                this.changes.number_of_adults  = client.number_of_adults;
                this.changes.number_of_children  = client.number_of_children;
            }
        }

    };


Registries.Component.extend(PaymentScreen, UFRAPaymentScreen);


return PaymentScreen;


});
