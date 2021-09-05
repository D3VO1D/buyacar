<template>
  <main>
    <CarsList/>
  </main>
</template>

<script>
import CarsList from '@/components/AppCarsList';

export default {
    name: 'MainPage',
    components: { CarsList },
};
</script>

<style lang="scss" scoped>
main {
    width: 80%;
    margin: 0 auto;
    padding: 40px 0;
    flex: 1 0 auto;
}
</style>
