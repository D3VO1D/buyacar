import Vue from 'vue';
import VueRouter from 'vue-router';

import MainPage from '@/views/MainPage';

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'Main Page',
        component: MainPage,
        props: (route) => ({ page: parseInt(route.query.page, 10) || 1 }),
    },
];

const scrollBehavior = (to, from, savedPosition) => {
    if (savedPosition) {
        return savedPosition;
    }
    return {
        x: 0,
        y: 0,
        behavior: 'smooth',
    };
};

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
    scrollBehavior,
});

export default router;
