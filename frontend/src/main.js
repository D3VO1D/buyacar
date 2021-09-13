import Vue from 'vue';

import { library } from '@fortawesome/fontawesome-svg-core';
import {
    faPhoneAlt,
    faChevronUp,
    faChevronDown,
    faTimes,
    faCheck,
} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import VuePaginateAl from 'vue-paginate-al';

import App from './App';
import router from './router';
import store from './store';

library.add(faPhoneAlt, faChevronUp, faChevronDown, faTimes, faCheck);

Vue.component('font-awesome-icon', FontAwesomeIcon);
Vue.component('vue-paginate-al', VuePaginateAl);

Vue.config.productionTip = false;

Vue.directive('visible', (el, binding) => {
    // eslint-disable-next-line no-param-reassign
    el.style.visibility = binding.value ? 'visible' : 'hidden';
});

new Vue({
    router,
    store,
    render: (h) => h(App),
}).$mount('#app');
