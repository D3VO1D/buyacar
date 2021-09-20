<template>
    <main>
        <Filters
            :minAvailableYear="minYear"
            :userCity="userCity"
            :availableMakes="availableMakes"
            :availableModels="availableModels"
            :resultsCount="resultsCount"
            @changeFilters="changeFilters"
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
            userCity: '',
            availableMakes: [],
            availableModels: [],
            filtersQueryString: '',
        };
    },
    created() {
        this.getMinYear();
        this.getAvailableMakes();
        this.getUserCity();

        this.getCars(this.page);
    },
    methods: {
        getCars(page = 1, filters = '') {
            API.getCars(page, filters)
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
                    this.minYear = res.data.min_year;
                })
                .catch((err) => console.log(err));
        },
        getUserCity() {
            API.getUserCity()
                .then((res) => {
                    const { data } = res;
                    this.userCity = `${data.city}, ${data.region}`;
                })
                .catch((err) => console.log(err));
        },
        getAvailableMakes() {
            API.getMakes()
                .then((res) => {
                    this.availableMakes = res.data.map((item) => item.make);
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
        changeFilters(filters) {
            // TODO: create GET request with filters
            console.log(filters);
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
