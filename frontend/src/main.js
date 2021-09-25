import Vue from 'vue';

import { library } from '@fortawesome/fontawesome-svg-core';
import {
    faPhoneAlt,
    faChevronUp,
    faChevronDown,
    faTimes,
    faCheck,
    faSearch,
} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import VueContentPlaceholders from 'vue-content-placeholders';
import VueSlider from 'vue-slider-component';
import Paginate from 'vuejs-paginate';

import App from './App';
import router from './router';
import store from './store';

library.add(faPhoneAlt, faChevronUp, faChevronDown, faTimes, faCheck, faSearch);

Vue.use(VueContentPlaceholders);
Vue.component('font-awesome-icon', FontAwesomeIcon);
Vue.component('paginate', Paginate);
Vue.component('vue-slider', VueSlider);

Vue.config.productionTip = false;

Vue.directive('visible', (el, binding) => {
    // eslint-disable-next-line no-param-reassign
    el.style.visibility = binding.value ? 'visible' : 'hidden';
});

Vue.directive('click-outside', {
    bind(el, binding, vnode) {
        // eslint-disable-next-line no-param-reassign
        el.clickOutsideEvent = (event) => {
            // here I check that click was outside the el and his children
            if (!(el === event.target || el.contains(event.target))) {
                // and if it did, call method provided in attribute value
                vnode.context[binding.expression](event);
            }
        };
        document.body.addEventListener('click', el.clickOutsideEvent);
    },
    unbind(el) {
        document.body.removeEventListener('click', el.clickOutsideEvent);
    },
});

new Vue({
    router,
    store,
    render: (h) => h(App),
}).$mount('#app');
