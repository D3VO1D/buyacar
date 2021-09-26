<template>
    <div>
        <template
            v-for="(car, index) in cars"
        >
            <component
                v-if="index > 0 && index % 10 === 0"
                :key="car.id"
                :is="($store.getters.showMobile) ? 'AdMobileLeaderboard' : 'AdLeaderboard'"
            />

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
import AdMobileLeaderboard from '@/components/Ads/AdMobileLeaderboard';

export default {
    name: 'AppCarsList',
    components: {
        AppCarCard,
        AdLeaderboard,
        AdMobileLeaderboard,
    },
    props: {
        cars: {
            type: Array,
            required: true,
        },
    },
};
</script>
