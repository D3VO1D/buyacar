<template>
    <div>
        <div class="filters" ref="filtersBlock">
            <div class="filters__row filters__row_header">
                <div class="filters__column">
                    <BaseRadioButtonGroup
                        :options="['All', 'New', 'Used']"
                        :selectedOption="isNewSelectedOption"
                        @selectOption="selectIsNew"
                    />
                </div>
                <div class="filters__column">
                    <BaseRadioButtonGroup
                        :options="['All', 'Working', 'Broken']"
                        :selectedOption="(filters.is_new) ? null : isBrokenSelectedOption"
                        :disabled="!!filters.is_new"
                        @selectOption="selectIsBroken"
                    />
                </div>
                <div class="filters__column filters__column_align-right">
                    <BaseLocation
                        :userCity="filters.location"
                        :distance="filters.distance"
                        @changeLocation="changeUserLocation"
                        @changeLocationOffset="changeDistance"
                        @resetLocation="resetLocation"
                    />
                </div>
            </div>
            <div class="filters__row">
                <div class="filters__column">
                    <BaseSelect
                        class="filters__item_large"
                        placeholder="Make"
                        :options="availableMakes"
                        :selectedOption="filters.make"
                        @selectOption="(option) => {filters.model = ''; filters.make = option;}"
                        @resetSelectedOptions="filters.make = ''"
                        withInput
                    />
                </div>

                <div class="filters__column">
                    <BaseSelect
                        class="filters__item_large"
                        placeholder="Model"
                        :options="modelsList"
                        :selectedOption="filters.model"
                        @selectOption="(option) => filters.model = option"
                        @resetSelectedOptions="filters.model = ''"
                        :disabled="!modelsList.length"
                        withInput
                    />
                </div>
            </div>
            <div class="filters__row">
                <div class="filters__column">
                    <BaseSelect
                        class="filters__item_small"
                        placeholder="Body"
                        :options="bodyOptions"
                        :selectedOption="filters.body"
                        @selectOption="(option) => filters.body = option"
                        @resetSelectedOptions="filters.body = ''"
                    />

                    <BaseSelect
                        class="filters__item_small"
                        placeholder="Transmission"
                        :options="transmissionOptions"
                        :selectedOption="filters.transmission"
                        @selectOption="(option) => filters.transmission = option"
                        @resetSelectedOptions="filters.transmission = ''"
                    />
                </div>

                <div class="filters__column">
                    <BaseSelect
                        class="filters__item_small"
                        placeholder="Drive"
                        :options="driveOptions"
                        :selectedOption="filters.drive"
                        @selectOption="(option) => filters.drive = option"
                        @resetSelectedOptions="filters.drive = ''"
                    />

                    <BaseCheckbox
                        class="filters__item_small filters__item_align-right filters__checkbox"
                        label="With photos"
                        v-model="filters.only_with_photo"
                    />
                </div>
            </div>

            <div class="filters__row">
                <div class="filters__column">
                    <BaseSelect
                        class="filters__item_grouped"
                        placeholder="Year from"
                        :options="yearFromOptions"
                        :selectedOption="filters.year_from"
                        @selectOption="(option) => filters.year_from = option"
                        @resetSelectedOptions="filters.year_from = ''"
                        resetText="Reset"
                        bordersType="left"
                        withInput
                        onlyNumbers
                    />

                    <BaseSelect
                        class="filters__item_grouped"
                        placeholder="to"
                        :options="yearToOptions"
                        :selectedOption="filters.year_to"
                        @selectOption="(option) => filters.year_to = option"
                        @resetSelectedOptions="filters.year_to = ''"
                        resetText="Reset"
                        bordersType="right"
                        withInput
                        onlyNumbers
                    />
                </div>

                <div class="filters__column">
                    <BaseInput
                        class="filters__item_grouped"
                        placeholder="Mileage from, mi"
                        v-model="filters.mileage_from"
                        bordersType="left"
                    />

                    <BaseInput
                        class="filters__item_grouped"
                        placeholder="to"
                        v-model="filters.mileage_to"
                        bordersType="right"
                    />
                </div>

                <div class="filters__column">
                    <BaseInput
                        class="filters__item_grouped"
                        placeholder="Price from, $"
                        v-model="filters.price_from"
                        bordersType="left"
                    />

                    <BaseInput
                        class="filters__item_grouped"
                        placeholder="to"
                        v-model="filters.price_to"
                        bordersType="right"
                    />
                </div>
            </div>

            <div class="filters__row filters__row_last">
                <div class="filters__column">
                    <div class="filters__reset-filters" v-if="appliedFiltersCount" @click="resetFilters">
                        Reset filters
                        <font-awesome-icon class="filters__reset-filters-icon" :icon="['fas', 'times']"/>
                    </div>
                </div>
                <div class="filters__column">
                </div>
                <div class="filters__column">
                    <div class="filters__results-count" v-if="resultsCount > 0">
                        {{ resultsCountFormatted }} results
                    </div>
                    <div class="filters__results-count" v-else-if="resultsCount === 0">
                        No results
                    </div>
                </div>
            </div>
        </div>

        <div class="filters__available-models" v-if="modelsList.length && filters.make && !filters.model">
            <div class="filters__models-items">
                <div
                    class="filters__models-item"
                    v-for="model in availableModels.slice(0, 12)"
                    :key="model.model"
                >
                    <div class="filters__models-item-name" @click="filters.model = model.model">
                        {{ model.model }}
                    </div>
                    <div class="filters__models-item-count">
                        {{ model.count }}
                    </div>
                </div>
            </div>
        </div>

        <div class="filters__below-selects">
            <BaseSelect
                v-visible="!$store.getters.showMobile"
                class="filters__item_small"
                placeholder="25 per page"
                :options="itemsPerPageOptions"
                :selectedOption="filters.items_per_page"
                @selectOption="(option) => filters.items_per_page = option"
                hideResetOption
            />

            <BaseSelect
                :class="($store.getters.showMobile) ? 'filters__item_small' : 'filters__item_large'"
                placeholder="Sort by Distance"
                :options="sortByOptions"
                :selectedOption="filters.ordering"
                @selectOption="(option) => filters.ordering = option"
                hideResetOption
                valuePrependText="Sort by "
            />
        </div>

        <div class="filters__hint-top" v-if="showHintTop">
            <div class="filters__hint-title" @click="scrollToTop">
                <svg class="filters__hint-arrow-icon" viewBox="0 0 24 24" id="arrow-rounded">
                    <path fill-rule="evenodd" fill="currentColor"
                          d="M15.483 9.297l-3.9 3.9-3.9-3.9a.99.99 0 00-1.4
                    1.4l4.593 4.593a1 1 0 001.414 0l4.593-4.593a.99.99 0 10-1.4-1.4z"></path>
                </svg>
                {{ appliedFiltersMessage }}
            </div>
            <div class="filters__hint-results-count" v-if="resultsCount">
                {{ resultsCountFormatted }} results
            </div>
        </div>
    </div>
</template>

<script>
import BaseSelect from '@/components/Base/BaseSelect';
import BaseCheckbox from '@/components/Base/BaseCheckbox';
import BaseInput from '@/components/Base/BaseInput';
import BaseLocation from '@/components/Base/BaseLocation';
import BaseRadioButtonGroup from '@/components/Base/BaseRadioButtonGroup';
import eventBus from '@/eventBus';

const DEFAULT_FILTERS = {
    is_new: null,
    is_broken: false,
    make: '',
    model: '',
    drive: '',
    transmission: '',
    body: '',
    only_with_photo: true,
    year_from: '',
    year_to: '',
    mileage_from: '',
    mileage_to: '',
    price_from: '',
    price_to: '',
    longitude: 0,
    latitude: 0,
    ordering: 'Distance (nearest first)',
    items_per_page: '25 per page',
    location: '',
    distance: '',
};

export default {
    name: 'Filters',
    components: {
        BaseLocation,
        BaseInput,
        BaseCheckbox,
        BaseSelect,
        BaseRadioButtonGroup,
    },
    props: {
        minAvailableYear: {
            type: Number,
            default: 2000,
        },
        availableMakes: {
            type: Array,
            default: () => [],
        },
        availableModels: {
            type: Array,
            default: () => [],
        },
        resultsCount: {
            type: Number,
            default: 0,
        },
    },
    data() {
        // snake case is used to provide valid querystring for backend
        return {
            filters: { ...DEFAULT_FILTERS },
            driveOptions: [
                'AWD',
                'RWD',
                'FWD',
            ],
            transmissionOptions: [
                'Automatic',
                'Manual',
            ],
            bodyOptions: [
                'Hatchback',
                'Coupe',
                'Convertible',
                'Sedan',
                'SUV',
                'Pickup Truck',
                'Commercial',
                'Minivan',
                'Wagon',
            ],
            sortByOptions: [
                'Distance (nearest first)',
                'Price ↑ (min first)',
                'Price ↓ (max first)',
                'Year ↑ (min first)',
                'Year ↓ (max first)',
            ],
            itemsPerPageOptions: [
                '25 per page',
                '50 per page',
                '100 per page',
            ],
            showHintTop: false,
        };
    },
    computed: {
        resultsCountFormatted() {
            return new Intl.NumberFormat('en-US').format(this.resultsCount);
        },
        yearsRange() {
            // an array of [min_available_year; current_year]
            const yearsRange = new Date().getFullYear() - this.minAvailableYear + 1;
            return Array.from(new Array(yearsRange), (x, i) => (i + this.minAvailableYear).toString()).reverse();
        },
        yearFromOptions() {
            if (!this.filters.year_to) {
                return this.yearsRange;
            }
            return this.yearsRange.filter((year) => parseInt(year, 10) <= this.filters.year_to);
        },
        yearToOptions() {
            if (!this.filters.year_from) {
                return this.yearsRange;
            }
            return this.yearsRange.filter((year) => parseInt(year, 10) >= this.filters.year_from);
        },
        modelsList() {
            return this.availableModels.map((item) => item.model);
        },
        isNewSelectedOption() {
            return {
                null: 'All',
                true: 'New',
                false: 'Used',
            }[this.filters.is_new];
        },
        isBrokenSelectedOption() {
            return {
                null: 'All',
                true: 'Broken',
                false: 'Working',
            }[this.filters.is_broken];
        },
        appliedFilters() {
            // select not empty values from filters object
            return Object.keys(this.filters)
                .reduce((acc, key) => {
                    const value = this.filters[key];
                    // Either a boolean or a 'truthy' value
                    // Also we make an exception for distance because we do want to pass '&distance=0'
                    if (typeof value === 'boolean' || value || (key === 'distance' && value !== '')) {
                        acc[key] = value;
                    }
                    return acc;
                }, {});
        },
        appliedFiltersInfo() {
            const appliedFiltersInfo = [];
            let appliedFiltersCount = 0;
            Object.entries(this.appliedFilters)
                .forEach(([key, value]) => {
                    switch (key) {
                    case 'make':
                    case 'model':
                        appliedFiltersInfo.push(value);
                        break;
                    case 'withPhotos':
                    case 'location':
                    case 'distance':
                    case 'longitude':
                    case 'latitude':
                        break;
                    default:
                        appliedFiltersCount += 1;
                        break;
                    }
                });
            return [appliedFiltersInfo, appliedFiltersCount];
        },
        appliedFiltersMessage() {
            const [appliedFiltersInfo, appliedFiltersCount] = this.appliedFiltersInfo;
            let result = (appliedFiltersInfo.length) ? appliedFiltersInfo.join(' ') : 'Any model';
            result += (appliedFiltersCount) ? `, ${appliedFiltersCount} parameters` : '';
            return result;
        },
        appliedFiltersCount() {
            return this.appliedFiltersInfo[1];
        },
    },
    created() {
        window.addEventListener('scroll', this.onScroll);
    },
    mounted() {
        eventBus.$on('reset-filters', this.resetFilters);
    },
    destroyed() {
        window.removeEventListener('scroll', this.onScroll);
        eventBus.$off('reset-filters');
    },
    methods: {
        scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth',
            });
        },
        onScroll() {
            const { filtersBlock } = this.$refs;
            const rect = filtersBlock.getBoundingClientRect();
            const isVisible = rect.bottom > 0;
            this.showHintTop = !isVisible;
        },
        changeUserLocation(location, distance) {
            this.filters.location = location.name;
            if (location.stateCode) {
                this.filters.location += `, ${location.stateCode}`;
            }
            this.filters.distance = distance;
            this.filters.longitude = location.longitude;
            this.filters.latitude = location.latitude;
        },
        changeDistance(distance) {
            this.filters.distance = distance;
        },
        resetLocation() {
            this.filters.location = '';
            this.filters.distance = '';
            this.filters.longitude = 0;
            this.filters.latitude = 0;
        },
        resetFilters() {
            this.filters = { ...DEFAULT_FILTERS };
            eventBus.$emit('clear-form');
        },
        sortByForQuery(param) {
            return {
                'Distance (nearest first)': '',
                'Price ↑ (min first)': 'price',
                'Price ↓ (max first)': '-price',
                'Year ↑ (min first)': 'year',
                'Year ↓ (max first)': '-year',
            }[param];
        },
        selectIsNew(option) {
            switch (option) {
            case 'New':
                this.filters.is_new = true;
                // new car can't be broken, resetting is_broken filter
                this.filters.is_broken = false;
                break;
            case 'Used':
                this.filters.is_new = false;
                break;
            default:
                this.filters.is_new = null;
                break;
            }
        },
        selectIsBroken(option) {
            switch (option) {
            case 'Working':
                this.filters.is_broken = false;
                break;
            case 'Broken':
                this.filters.is_broken = true;
                break;
            default:
                this.filters.is_broken = null;
                break;
            }
        },
    },
    watch: {
        filters: {
            handler() {
                const { ordering } = this.appliedFilters;
                const normalizedOrdering = this.sortByForQuery(ordering);
                if (normalizedOrdering) {
                    this.appliedFilters.ordering = normalizedOrdering;
                } else {
                    delete this.appliedFilters.ordering;
                }
                this.$emit('changeFilters', this.appliedFilters);
            },
            deep: true,
        },
    },
};
</script>

<style lang="scss" scoped>
@import '@/_vars.scss';

.filters {
    margin-bottom: 24px;
    padding: 20px;
    border-radius: 8px;
    background: $white;
    box-shadow: 0 3px 14px $card-shadow-color;

    &__row {
        display: flex;
        margin: 12px 0;

        &_header {
            margin-top: 0;
        }

        &_last {
            margin-bottom: 0;
        }
    }

    &__column {
        width: 280px;
        display: flex;
        align-items: center;
        margin-left: 20px;

        &:first-child {
            margin-left: 0;
        }

        &_align-right {
            justify-content: flex-end;
        }
    }

    &__item {
        &_large {
            width: 100%;
        }

        &_small {
            width: calc(50% - 5px);

            &:first-of-type {
                margin-right: 10px;
            }
        }

        &_grouped {
            width: 50%;
        }

        &_align-right {
            justify-content: flex-end;
        }
    }

    &__reset-filters {
        color: grey;
        font-size: 15px;
        line-height: 24px;
        display: flex;
        justify-content: center;
        align-items: center;
        transition: color .3s ease;
        flex-shrink: 0;

        &:hover {
            color: $accent-color;
            cursor: pointer;
        }
    }

    &__reset-filters-icon {
        margin-left: 8px;
    }

    &__results-count {
        font-size: 15px;
        color: grey;
        margin-left: auto;
        margin-right: 0;
    }

    &__hint-top {
        top: 0;
        font-size: 15px;
        position: fixed;
        z-index: 3000;
        display: flex;
        justify-content: space-between;
        align-items: center;
        overflow: hidden;
        width: 920px;
        height: 44px;
        border-radius: 0 0 8px 8px;
        background: #fff;
        box-shadow: 0 3px 14px rgb(0 0 0 / 12%);
        transition: top .2s;
    }

    &__hint-title {
        line-height: 44px;
        transition: color .3s ease;

        &:hover {
            cursor: pointer;
            color: $accent-color;
        }
    }

    &__hint-arrow-icon {
        width: 24px;
        height: 24px;
        margin: 0 8px 0 16px;
        vertical-align: middle;
        transform: rotate(180deg) translateY(2px);
    }

    &__hint-results-count {
        line-height: 44px;
        margin: 0 24px 0 auto;
        color: grey;
    }

    &__below-selects {
        width: 50%;
        display: flex;
        margin: 0 0 16px auto;
    }

    &__available-models {
        padding: 24px 16px 9px;
        margin-bottom: 15px;
    }

    &__models-items {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
    }

    &__models-item {
        font-size: 15px;
        line-height: 18px;
        position: relative;
        display: flex;
        justify-content: space-between;
        width: 210px;
        margin: 0 12px 15px 0;
        white-space: nowrap;
    }

    &__models-item-name {
        position: relative;
        z-index: 2;
        overflow: hidden;
        flex-shrink: 0;
        max-width: 84%;
        padding-right: 8px;
        text-overflow: ellipsis;
        font-size: 15px;
        color: #157ee1;

        &:hover {
            cursor: pointer;
            color: $accent-color;
        }
    }

    &__models-item-count {
        position: relative;
        z-index: 2;
        display: flex;
        width: 100%;
        margin-left: auto;
        color: grey;

        &::before {
            width: 100%;
            margin-right: 8px;
            margin-bottom: 4px;
            content: "";
            border-bottom: 1px solid #e0e0e0
        }
    }
}

@media screen and (max-width: 1000px) {
    .filters {
        width: auto;
        margin-right: 5%;

        &__row {
            width: 100%;
            gap: 10px;

            &_header {
                flex-direction: column;
                gap: 16px;
                flex-direction: column-reverse;
            }

            &:nth-of-type(3), &:nth-of-type(4) {
                flex-direction: column;
                gap: 16px;
            }
        }

        &__column {
            width: 100%;
            margin: 0;
        }

        &__checkbox {
            justify-content: flex-start;
        }

        &__hint-top {
            width: calc(100% - 10%);
        }

        &__below-selects {
            width: auto;
            margin-bottom: 16px;
            margin-right: 5%;
        }

        &__available-models {
            margin: 0;
            margin-right: 5%;
            padding: 0;
        }

        &__models-items {
            grid-template-columns: repeat(2, 1fr);
        }

        &__models-item {
            width: auto;
        }
    }
}

@media screen and (max-width: 360px) {
    .filters {
        &__hint-top {
            flex-direction: column;
            align-items: flex-start;
            height: auto;
        }

        &__hint-results-count {
            margin: 0;
            margin-left: 20px;
        }
    }
}
</style>
