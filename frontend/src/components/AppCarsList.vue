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
                :showMobile="showMobile"
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
    data() {
        return {
            windowWidth: window.innerWidth,
        };
    },
    mounted() {
        this.$nextTick(() => window.addEventListener('resize', this.onResize));
    },
    beforeDestroy() {
        window.removeEventListener('resize', this.onResize);
    },
    computed: {
        showMobile() {
            return this.windowWidth < 1000;
        },
    },
    methods: {
        onResize() {
            this.windowWidth = window.innerWidth;
        },
    },
};
</script>
