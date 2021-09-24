<template>
    <div>
        <template
            v-for="(car, index) in cars"
        >
            <AdLeaderboard v-if="index > 0 && index % 10 === 0" :key="car.id" />

            <AppCarCard
                v-else
                :car="car"
                :key="car.id"
            />
        </template>
    </div>
</template>

<script>
import AppCarCard from '@/components/AppCarCard';
import AdLeaderboard from '@/components/Ads/AdLeaderboard';

export default {
    name: 'AppCarsList',
    components: {
        AppCarCard,
        AdLeaderboard,
    },
    props: {
        cars: {
            type: Array,
            required: true,
        },
    },
};
</script>
