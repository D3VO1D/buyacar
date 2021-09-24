<template>
    <main>
        <Filters
            :minAvailableYear="minYear"
            :availableMakes="availableMakes"
            :availableModels="availableModels"
            :resultsCount="resultsCount"
            @changeFilters="changeFilters"
        />
        <div v-if="isLoading || requestsPending > 0">
            <content-placeholders
                class="loading-placeholder"
                :rounded="true"
                v-for="_ in perPage"
                :key="_"
            >
                <content-placeholders-img class="loading-placeholder__image" />
                <div>
                    <content-placeholders-text :lines="1" class="loading-placeholder__title" />
                    <content-placeholders-text :lines="2" />
                </div>
            </content-placeholders>
        </div>
        <div v-else-if="resultsCount !== 0">
            <AppCarsList
                class="cars-list"
                :cars="cars"
            />
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
            requestsPending: 0,
            maxPage: 1,
            resultsCount: null,
            minYear: 2000,
            availableMakes: [],
            availableModels: [],
            filtersQueryString: 'only_with_photo=true&is_broken=false',
            perPage: 50,
        };
    },
    created() {
        this.isLoading = true;
        this.getMinYear();
        this.getAvailableMakes();

        this.getCars(this.page, this.filtersQueryString);
    },
    methods: {
        getCars(page = 1, filters = '') {
            this.isLoading = true;
            ++this.requestsPending;
            const oldModels = this.availableModels;
            const shouldUpdateModelsList = !this.filtersQueryString.includes('model');
            this.availableModels = [];
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
                    this.availableModels = (shouldUpdateModelsList) ? models : oldModels;
                })
                .catch((err) => console.log(err))
                .finally(() => {
                    --this.requestsPending;
                    this.isLoading = false;
                });
        },
        getMinYear() {
            API.getMinYear()
                .then((res) => {
                    this.minYear = res.data.min_year;
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
            window.scrollTo({
                top: 0,
                behavior: 'smooth',
            });

            // redirect if we are not on that page already
            if (parseInt(this.$route.query.page, 10) !== newPage) {
                this.$router.push({
                    name: 'Main Page',
                    query: { page: newPage },
                });
            }

            // Firefox bug: without setTimeout scrollTo doesn't happen
            setTimeout(() => this.getCars(this.$route.query.page, this.filtersQueryString), 100);
        },
        changeFilters(filters) {
            this.perPage = parseInt(filters.items_per_page, 10) || 50;
            this.filtersQueryString = qs.stringify(filters, { indices: false });
            console.log(this.filtersQueryString);
            this.pageClicked(1);
        },
    },
};
</script>

<style lang="scss" scoped>
main {
    width: 920px;
    padding: 40px 0 40px 10%;
    box-sizing: content-box;
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

.loading-placeholder {
    width: 100%;
    padding: 16px;
    margin: 0 auto;
    display: flex;

    &__image {
        width: 200px;
        height: 150px;
        margin-right: 24px;
    }

    &__title {
        width: 450px;
        margin-bottom: 40px;;
    }
}

.cars-list {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}
</style>
