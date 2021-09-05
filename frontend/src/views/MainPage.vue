<template>
  <div>
    <div>Main Page</div>
    <CarsList/>
    <CarCard/>
  </div>
</template>

<script>
import CarsList from '@/components/AppCarsList';
import CarCard from '@/components/AppCarCard';

export default {
    name: 'MainPage',
    components: { CarCard, CarsList },
};
</script>

<style scoped>

</style>
