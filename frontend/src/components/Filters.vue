<template>
    <div>
        <div class="filters" ref="filtersBlock">
            <div class="filters__row filters__row_header">
                <div class="filters__column">
                    <div class="radio-toolbar">
                        <input class="radio-toolbar__radio" type="radio" id="select-all"
                               name="toolbar-1" value="all" checked>
                        <label class="radio-toolbar__label" for="select-all">All</label>

                        <input class="radio-toolbar__radio" type="radio" id="select-new"
                               name="toolbar-1" value="new">
                        <label class="radio-toolbar__label" for="select-new">New</label>

                        <input class="radio-toolbar__radio" type="radio" id="select-used"
                               name="toolbar-1" value="used">
                        <label class="radio-toolbar__label" for="select-used">Used</label>
                    </div>
                </div>
                <div class="filters__column">
                    <div class="radio-toolbar">
                        <input class="radio-toolbar__radio" type="radio" id="select-all-2"
                               name="toolbar-2" value="all">
                        <label class="radio-toolbar__label" for="select-all-2">All</label>

                        <input class="radio-toolbar__radio" type="radio" id="select-working"
                               name="toolbar-2" value="new" checked>
                        <label class="radio-toolbar__label" for="select-working">Working</label>

                        <input class="radio-toolbar__radio" type="radio" id="select-broken"
                               name="toolbar-2" value="used">
                        <label class="radio-toolbar__label" for="select-broken">Broken</label>
                    </div>
                </div>
                <div class="filters__column filters__column_align_right">
                    <BaseLocation
                        :userCity="userCity"
                        @changeLocation="changeUserLocation"
                    />
                </div>
            </div>
            <div class="filters__row">
                <div class="filters__column">
                    <BaseSelect
                        class="filters__item_large"
                        placeholder="Make"
                        :options="availableMakes"
                        :selectedOptions="filters.make"
                        @selectOption="selectOption"
                        @resetSelectedOptions="filters.make = []"
                        selectionMode="single"
                        with-input
                    />
                </div>

                <div class="filters__column">
                    <BaseSelect
                        class="filters__item_large"
                        placeholder="Model"
                        :options="availableModels"
                        :selectedOptions="filters.model"
                        @selectOption="selectOption"
                        @resetSelectedOptions="filters.model = []"
                        selectionMode="single"
                        with-input
                    />
                </div>
            </div>
            <div class="filters__row">
                <div class="filters__column">
                    <BaseSelect
                        class="filters__item_small"
                        placeholder="Body"
                        :options="bodyOptions"
                        :selectedOptions="filters.body"
                        @selectOption="selectOption"
                        @resetSelectedOptions="filters.body = []"
                    />

                    <BaseSelect
                        class="filters__item_small"
                        placeholder="Transmission"
                        :options="transmissionOptions"
                        :selectedOptions="filters.transmission"
                        @selectOption="selectOption"
                        @resetSelectedOptions="filters.transmission = []"
                    />
                </div>

                <div class="filters__column">
                    <BaseSelect
                        class="filters__item_small"
                        placeholder="Drive"
                        :options="driveOptions"
                        :selectedOptions="filters.drive"
                        @selectOption="selectOption"
                        @resetSelectedOptions="filters.drive = []"
                    />

                    <BaseCheckbox
                        class="filters__item_small"
                        label="With photos"
                        v-model="filters.withPhotos"
                    />
                </div>
            </div>

            <div class="filters__row">
                <div class="filters__column">
                    <BaseSelect
                        class="filters__item_grouped"
                        placeholder="Year from"
                        :options="yearOptions"
                        :selectedOptions="filters.yearFrom"
                        @selectOption="selectOption"
                        @resetSelectedOptions="filters.yearFrom = []"
                        selectionMode="single"
                        resetText="Reset"
                        bordersType="left"
                    />

                    <BaseSelect
                        class="filters__item_grouped"
                        placeholder="to"
                        :options="yearOptions"
                        :selectedOptions="filters.yearTo"
                        @selectOption="selectOption"
                        @resetSelectedOptions="filters.yearTo = []"
                        selectionMode="single"
                        resetText="Reset"
                        bordersType="right"
                    />
                </div>

                <div class="filters__column">
                    <BaseInput
                        class="filters__item_grouped"
                        placeholder="Mileage from, mi"
                        v-model="filters.mileageFrom"
                        bordersType="left"
                    />

                    <BaseInput
                        class="filters__item_grouped"
                        placeholder="to"
                        v-model="filters.mileageTo"
                        bordersType="right"
                    />
                </div>

                <div class="filters__column">
                    <BaseInput
                        class="filters__item_grouped"
                        placeholder="Price from, $"
                        v-model="filters.priceFrom"
                        bordersType="left"
                    />

                    <BaseInput
                        class="filters__item_grouped"
                        placeholder="to"
                        v-model="filters.priceTo"
                        bordersType="right"
                    />
                </div>
            </div>
        </div>
        <div class="filters__below-selects">
<!--            TODO: fix resetting -->
            <BaseSelect
                class="filters__item_small"
                placeholder="Per page"
                :options="itemsPerPageOptions"
                v-model="filters.itemsPerPage"
                :resetText="'50'"
                @selectOption="selectOption"
                @resetSelectedOptions="filters.itemsPerPage = 50"
                selectionMode="single"
            />

            <BaseSelect
                class="filters__item_small"
                placeholder="Сортировка"
                :options="sortByOptions"
                v-model="filters.sortBy"
                resetText="Default"
                @selectOption="selectOption"
                @resetSelectedOptions="filters.sortBy = []"
                selectionMode="single"
            />
        </div>
        <div class="filters__available-models" v-if="showAvailableModels">
            <div class="filters__models-items">
                <div class="filters__models-column">
                    <div class="filters__models-item">
                        <div class="filters__models-item-name">
                            X5
                        </div>
                        <div class="filters__models-item-count">
                            11
                        </div>
                    </div>

                    <div class="filters__models-item">
                        <div class="filters__models-item-name">
                            X7
                        </div>
                        <div class="filters__models-item-count">
                            1311
                        </div>
                    </div>

                    <div class="filters__models-item">
                        <div class="filters__models-item-name">
                            12314
                        </div>
                        <div class="filters__models-item-count">
                            51
                        </div>
                    </div>
                </div>
                <div class="filters__models-column">
                    <div class="filters__models-item">
                        <div class="filters__models-item-name">
                            X5
                        </div>
                        <div class="filters__models-item-count">
                            11
                        </div>
                    </div>

                    <div class="filters__models-item">
                        <div class="filters__models-item-name">
                            X7
                        </div>
                        <div class="filters__models-item-count">
                            1311
                        </div>
                    </div>

                    <div class="filters__models-item">
                        <div class="filters__models-item-name">
                            12314
                        </div>
                        <div class="filters__models-item-count">
                            51
                        </div>
                    </div>
                </div>
            </div>
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
            <div class="filters__hint-results-count">
                {{ resultsCount }} results
            </div>
        </div>
    </div>
</template>

<script>
import BaseSelect from '@/components/Base/BaseSelect';
import BaseCheckbox from '@/components/Base/BaseCheckbox';
import BaseInput from '@/components/Base/BaseInput';
import BaseLocation from '@/components/Base/BaseLocation';

export default {
    name: 'Filters',
    components: {
        BaseLocation,
        BaseInput,
        BaseCheckbox,
        BaseSelect,
    },
    props: {
        minAvailableYear: {
            type: Number,
            default: 2000,
        },
        userCity: {
            type: String,
            default: '',
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
        return {
            filters: {
                make: [],
                model: [],
                drive: [],
                transmission: [],
                body: [],
                withPhotos: true,
                yearFrom: [],
                yearTo: [],
                mileageFrom: '',
                mileageTo: '',
                priceFrom: '',
                priceTo: '',
                longitude: 0,
                latitude: 0,
                sortBy: [],
                itemsPerPage: [],
            },
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
                'Distance',
                'Price ↑',
                'Price ↓',
                'Year ↑',
                'Year ↓',
            ],
            itemsPerPageOptions: [
                100,
                150,
                200,
            ],
            showHintTop: false,
            showAvailableModels: false,
        };
    },
    computed: {
        yearOptions() {
            // an array of [min_available_year; current_year]
            const currentYear = new Date().getFullYear() - this.minAvailableYear;
            return Array.from(new Array(currentYear), (x, i) => i + this.minAvailableYear);
        },
        perPageMessage() {
            return `${this.filters.itemsPerPage} per page`;
        },
        appliedFilters() {
            // select not empty values from filters object
            return Object.keys(this.filters)
                .reduce((acc, key) => {
                    const value = this.filters[key];
                    // either a 'truthy' primitive or a non-empty object
                    if ((value && typeof value !== 'object') || (value.length !== undefined && value.length !== 0)) {
                        acc[key] = this.filters[key];
                    }
                    return acc;
                }, {});
        },
        appliedFiltersMessage() {
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
                        break;
                    default:
                        appliedFiltersCount += 1;
                        break;
                    }
                });
            let result = (appliedFiltersInfo.length) ? appliedFiltersInfo.join(' ') : 'Any model';
            result += (appliedFiltersCount) ? `, ${appliedFiltersCount} parameters` : '';
            return result;
        },
    },
    created() {
        window.addEventListener('scroll', this.onScroll);
    },
    destroyed() {
        window.removeEventListener('scroll', this.onScroll);
    },
    methods: {
        selectOption(list, newOption, mode = 'multiple') {
            if (mode === 'single') {
                list.splice(0);
                list.push(newOption);
                return;
            }
            const index = list.indexOf(newOption);
            if (index === -1) {
                list.push(newOption);
                return;
            }
            list.splice(index, 1);
        },
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
        changeUserLocation(location) {
            this.filters.longitude = location.longitude;
            this.filters.latitude = location.latitude;
        },
    },
    watch: {
        filters: {
            handler(val) {
                console.log(this.appliedFilters);
                // TODO: create GET request with filters
                this.showAvailableModels = !!val.make.length && !val.model.length;
            },
            deep: true,
        },
    },
};
</script>

<style lang="scss" scoped>
@import '@/_vars.scss';

.filters {
    margin: 0 0 24px 16px;
    padding: 20px;
    border-radius: 8px;
    background: $white;
    box-shadow: 0 3px 14px $filters-shadow-color;

    &__row {
        display: flex;
        margin: 12px 0;

        &_header {
            margin-top: 0;
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

        &_align_right {
            justify-content: right;
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
        width: 280px;
        display: flex;
        margin-left: auto;
        margin-right: 0;
    }

    &__available-models {
        padding: 24px 16px 9px;
        margin-bottom: 15px;
        margin-left: 16px;
    }

    &__models-items {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
    }

    &__models-column {
        display: flex;
        flex-direction: column;
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

.radio-toolbar {

    &__radio {
        opacity: 0;
        position: fixed;
        width: 0;

        &:checked + label {
            background-color: #eef4fa;
            border: 1px solid rgba(21, 126, 225, .5);
            color: $text-color;

            &:hover {
                cursor: default;
            }
        }
    }

    &__label {
        display: inline-block;
        padding: 10px 20px;
        font-size: 15px;
        border: 1px solid rgba(0, 0, 0, .12);
        background-color: $white;
        color: grey;
        height: 36px;
        text-align: center;

        &:hover {
            color: $white;
            background-color: #157ee1;
            cursor: pointer;
        }

        &:first-of-type {
            border-top-left-radius: 8px;
            border-bottom-left-radius: 8px;
        }

        &:last-of-type {
            border-top-right-radius: 8px;
            border-bottom-right-radius: 8px;
        }
    }
}
</style>
