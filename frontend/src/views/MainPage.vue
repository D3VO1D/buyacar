<template>
  <div>
    <div>Main Page</div>
    <CarsList/>
    <CarCard/>
  </div>
</template>

<script>
import CarsList from '@/components/CarsList';
import CarCard from '@/components/CarCard';

export default {
    name: 'MainPage',
    components: { CarCard, CarsList },
};
</script>

<style scoped>

</style>
