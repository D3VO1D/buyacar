<template>
  <div id="app">
    <Header/>
    <router-view/>
  </div>
</template>

<script>
import Header from '@/components/TheHeader';

export default {
    components: { Header },
};
</script>

<style lang="scss">
@use 'index';
</style>
