<template>
    <div>
        <CarCard
            v-for="car in 5"
            :key="car"
            :car="{car}"
        />
    </div>
</template>

<script>
import CarCard from '@/components/AppCarCard';

export default {
    name: 'CarsList',
    components: { CarCard },
    data() {
        return {
            cars: [],
        };
    },
    created() {
        // TODO: API call
    },
};
</script>

<style scoped>

</style>
