import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        windowWidth: 0,
    },
    mutations: {
        setWindowWidth(state, newWidth) {
            state.windowWidth = newWidth;
        },
    },
    getters: {
        showMobile(state) {
            return state.windowWidth < 1000;
        },
    },
    actions: {
    },
    modules: {
    },
});
