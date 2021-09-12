<template>
    <main>
        <AppCarsList :cars="cars"/>
        <div class="pagination-container">
            <vue-paginate-al
                :currentPage="page"
                :totalPage="maxPage"
                customActiveBGColor="#DB3727"
                @btnClick="pageClicked"
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
        page: {
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
        this.getCars(this.page);
    },
    methods: {
        getCars(page = 1) {
            API.getCars(page)
                .then((res) => {
                    const {
                        count,
                        totalPages,
                        results,
                    } = res.data;
                    this.resultsCount = count;
                    this.cars = results;
                    this.maxPage = totalPages;
                })
                .catch((err) => console.log(err));
        },
        pageClicked(newPage) {
            this.$router.push({
                name: 'Main Page',
                query: { page: newPage },
            });
            this.getCars(newPage);
        },
    },
};
</script>

<style lang="scss" scoped>
main {
    padding: 40px 0 40px calc(10% - 16px);
}

.pagination-container {
    padding: 16px;
}
</style>
