<template>
    <div>
        <div class="filters">
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
                    <BaseLocation/>
                </div>
            </div>
            <div class="filters__row">
                <div class="filters__column">
                    <BaseSelect
                        class="filters__item_large"
                        placeholder="Make"
                        :options="makeOptions"
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
                        :options="modelOptions"
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
        <div class="filters__hint-top">
            <div class="filters__hint-title">
                <svg class="filters__hint-arrow-icon" viewBox="0 0 24 24" id="arrow-rounded">
                    <path fill-rule="evenodd" fill="currentColor"
                          d="M15.483 9.297l-3.9 3.9-3.9-3.9a.99.99 0 00-1.4
                    1.4l4.593 4.593a1 1 0 001.414 0l4.593-4.593a.99.99 0 10-1.4-1.4z"></path>
                </svg>
                {{ appliedFilters }}
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
        resultsCount: {
            type: Number,
            default: 0,
        },
    },
    data() {
        // TODO: API calls for Make and Model options
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
            },
            makeOptions: [
                'Audi',
                'BMW',
                'Ford',
            ],
            modelOptions: [
                'X3',
                'X5',
                'X7',
            ],
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
            ],
            yearOptions: Array.from(new Array(40), (x, i) => i + 1980),
        };
    },
    computed: {
        appliedFilters() {
            return Object.keys(this.filters)
                .reduce((acc, key) => {
                    const value = this.filters[key];
                    if (value !== undefined && value.length !== 0) {
                        acc[key] = this.filters[key];
                    }
                    return acc;
                }, {});
        },
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
        //top: -60px;
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
        margin-left: 16px;
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
