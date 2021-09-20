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
        <div v-if="resultsCount !== 0">
            <AppCarsList :cars="cars" />
            <div class="pagination-container">
                <vue-paginate-al
                    :currentPage="page"
                    :totalPage="maxPage"
                    customActiveBGColor="#DB3727"
                    :withNextPrev="false"
                    @btnClick="pageClicked"
                />
            </div>
        </div>
        <p v-else class="no-results">
            Unfortunately, we could not find any cars for you. Consider trying later or changing the filters.
        </p>
    </main>
</template>

<script>
import qs from 'qs';
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
            isLoading: false,
            maxPage: 1,
            resultsCount: null,
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
                        models,
                    } = res.data;
                    this.resultsCount = count;
                    this.cars = results;
                    this.maxPage = totalPages;
                    this.availableModels = models;
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
            this.getCars(newPage, this.filtersQueryString);
        },
        changeFilters(filters) {
            this.filtersQueryString = qs.stringify(filters, { indices: false });
            console.log(this.filtersQueryString);
            this.getCars(this.page, this.filtersQueryString);
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
    display: flex;
    justify-content: center;
}

.no-results {
    padding: 0 16px;
    font-size: 24px;
    max-width: 920px;
    margin: 32px auto;
    text-align: center;
}
</style>
