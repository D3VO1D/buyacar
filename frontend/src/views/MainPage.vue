<template>
    <main>
        <Filters
            :minAvailableYear="minYear"
            :userCity="userCity"
            :availableMakes="availableMakes"
            :availableModels="availableModels"
            :resultsCount="resultsCount"
        />
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
import Filters from '@/components/Filters';

export default {
    name: 'MainPage',
    components: {
        Filters,
        AppCarsList,
    },
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
            minYear: 2000,
            userCity: 'New York',
            availableMakes: [
                'Audi',
                'BMW',
                'Ford',
            ],
            availableModels: [
                'X3',
                'X5',
                'X7',
            ],
        };
    },
    created() {
        this.getMinYear();
        this.getUserCity();
        this.getAvailableMakes();

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
        getMinYear() {
            API.getMinYear()
                .then((res) => {
                    console.log(res.data);
                    this.minYear = res.data.min_year;
                })
                .catch((err) => console.log(err));
        },
        getUserCity() {
            API.getUserCity()
                .then((res) => {
                    console.log(res.data);
                    const { data } = res;
                    this.userCity = `${data.city}, ${data.region}`;
                })
                .catch((err) => console.log(err));
        },
        getAvailableMakes() {
            API.getMakes()
                .then((res) => {
                    console.log(res.data);
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
    width: fit-content;
    padding: 40px 0 40px calc(10% - 16px);
}

.pagination-container {
    padding: 16px;
}
</style>
