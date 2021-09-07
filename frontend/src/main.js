import Vue from 'vue';

import { library } from '@fortawesome/fontawesome-svg-core';
import { faPhoneAlt } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import VuePaginateAl from 'vue-paginate-al';

import App from './App';
import router from './router';
import store from './store';

library.add(faPhoneAlt);

Vue.component('font-awesome-icon', FontAwesomeIcon);
Vue.component('vue-paginate-al', VuePaginateAl);

Vue.config.productionTip = false;

new Vue({
    router,
    store,
    render: (h) => h(App),
}).$mount('#app');
