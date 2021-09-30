<template>
    <div id="app">
        <TheHeader/>
        <router-view/>
        <TheFooter/>
    </div>
</template>

<script>
import TheHeader from '@/components/TheHeader';
import TheFooter from '@/components/TheFooter';

export default {
    components: { TheFooter, TheHeader },
    data() {
        return {
            windowWidth: window.innerWidth,
        };
    },
    mounted() {
        this.$store.commit('setWindowWidth', this.windowWidth);
        this.$nextTick(() => window.addEventListener('resize', this.onResize));
    },
    beforeDestroy() {
        window.removeEventListener('resize', this.onResize);
    },
    methods: {
        onResize() {
            this.windowWidth = window.innerWidth;
            this.$store.commit('setWindowWidth', this.windowWidth);
        },
    },
};
</script>

<style lang="scss">
@import 'index';

#app {
    display: flex;
    flex: 1 0 auto;
    flex-direction: column;
    height: 100%;
}
</style>
