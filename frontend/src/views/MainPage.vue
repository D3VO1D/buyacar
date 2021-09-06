<template>
    <main>
        <AppCarsList :cars="cars"/>
        <div class="pagination-container">
            <vue-paginate-al
                :currentPage="currentPage"
                :totalPage="maxPage"
                customActiveBGColor="#DB3727"
                @btnClick="pageClick"
            />
        </div>
    </main>
</template>

<script>
import AppCarsList from '@/components/AppCarsList';

export default {
    name: 'MainPage',
    components: { AppCarsList },
    props: {
        currentPage: {
            type: Number,
            default: 1,
        },
    },
    data() {
        return {
            cars: [],
            maxPage: 100,
        };
    },
    created() {
        // TODO: API call
        this.cars = [];
        this.maxPage = 10;
    },
    methods: {
        pageClick(n) {
            console.log(n);
        },
    },
};
</script>

<style lang="scss" scoped>
main {
    width: 80%;
    margin: 0 auto;
    padding: 40px 0;
    flex: 1 0 auto;
}

.pagination-container {
    padding: 16px;
}
</style>
