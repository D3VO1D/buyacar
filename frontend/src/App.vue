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
};
</script>

<style lang="scss">
@import 'index';

#app {
    display: flex;
    flex-direction: column;
    height: 100%;
}
</style>
