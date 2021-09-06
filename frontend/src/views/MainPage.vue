<template>
    <main>
        <AppCarsList :cars="cars"/>
        <div class="pagination-container">
            <vue-paginate-al
                :currentPage="currentPage"
                :totalPage="maxPage"
                customActiveBGColor="#DB3727"
                @btnClick="getPageContent"
            />
        </div>
    </main>
</template>

<script>
import AppCarsList from '@/components/AppCarsList';
import { API } from '@/services/api';

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
            maxPage: 1,
            resultsCount: 0,
        };
    },
    created() {
        this.getPageContent();
    },
    methods: {
        getPageContent(page = 1) {
            API.getCars(page)
                .then((res) => {
                    console.log(res);
                    const { count, totalPages, results } = res.data;
                    this.resultsCount = count;
                    this.cars = results;
                    this.maxPage = totalPages;
                })
                .catch((err) => console.log(err));
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
