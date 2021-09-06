<template>
    <div>
        <AppCarCard
            v-for="car in 5"
            :key="car"
            :car="{car}"
        />
    </div>
</template>

<script>
import AppCarCard from '@/components/AppCarCard';

export default {
    name: 'AppCarsList',
    components: { AppCarCard },
    props: {
        cars: {
            type: Array,
            required: true,
        },
    },
};
</script>

<style scoped>

</style>
