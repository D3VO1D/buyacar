<template>
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
        </div>
        <div class="filters__row">
            <div class="filters__column">
                <BaseSelect
                    class="filters__item_large"
                    placeholder="Make"
                    :options="makeOptions"
                    :selectedOptions="make"
                    @selectOption="selectOption"
                    @resetSelectedOptions="make = []"
                    selectionMode="single"
                    with-input
                />
            </div>

            <div class="filters__column">
                <BaseSelect
                    class="filters__item_large"
                    placeholder="Model"
                    :options="modelOptions"
                    :selectedOptions="model"
                    @selectOption="selectOption"
                    @resetSelectedOptions="model = []"
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
                    :selectedOptions="body"
                    @selectOption="selectOption"
                    @resetSelectedOptions="body = []"
                />

                <BaseSelect
                    class="filters__item_small"
                    placeholder="Transmission"
                    :options="transmissionOptions"
                    :selectedOptions="transmission"
                    @selectOption="selectOption"
                    @resetSelectedOptions="transmission = []"
                />
            </div>

            <div class="filters__column">
                <BaseSelect
                    class="filters__item_small"
                    placeholder="Drive"
                    :options="driveOptions"
                    :selectedOptions="drive"
                    @selectOption="selectOption"
                    @resetSelectedOptions="drive = []"
                />

                <BaseCheckbox
                    class="filters__item_small"
                    label="With photos"
                    v-model="withPhotos"
                />
            </div>
        </div>

        <div class="filters__row">
            <div class="filters__column">
                <BaseSelect
                    class="filters__item_grouped"
                    placeholder="Year, from"
                    :options="yearOptions"
                    :selectedOptions="yearFrom"
                    @selectOption="selectOption"
                    @resetSelectedOptions="yearFrom = []"
                    selectionMode="single"
                    resetText="Reset"
                    bordersType="left"
                />

                <BaseSelect
                    class="filters__item_grouped"
                    placeholder="to"
                    :options="yearOptions"
                    :selectedOptions="yearTo"
                    @selectOption="selectOption"
                    @resetSelectedOptions="yearTo = []"
                    selectionMode="single"
                    resetText="Reset"
                    bordersType="right"
                />
            </div>

            <div class="filters__column">
                <BaseInput
                    class="filters__item_grouped"
                    placeholder="Mileage, from"
                    v-model="mileageFrom"
                    bordersType="left"
                />

                <BaseInput
                    class="filters__item_grouped"
                    placeholder="to"
                    v-model="mileageTo"
                    bordersType="right"
                />
            </div>

            <div class="filters__column">
                <BaseInput
                    class="filters__item_grouped"
                    placeholder="Price, from"
                    v-model="priceFrom"
                    bordersType="left"
                />

                <BaseInput
                    class="filters__item_grouped"
                    placeholder="to"
                    v-model="priceTo"
                    bordersType="right"
                />
            </div>
        </div>
    </div>
</template>

<script>
import BaseSelect from '@/components/Base/BaseSelect';
import BaseCheckbox from '@/components/Base/BaseCheckbox';
import BaseInput from '@/components/Base/BaseInput';

export default {
    name: 'Filters',
    components: {
        BaseInput,
        BaseCheckbox,
        BaseSelect,
    },
    data() {
        // TODO: API calls for Make and Model options
        return {
            make: [],
            makeOptions: [
                'Audi',
                'BMW',
                'Ford',
            ],
            model: [],
            modelOptions: [
                'X3',
                'X5',
                'X7',
            ],
            drive: [],
            driveOptions: [
                'AWD',
                'RWD',
                'FWD',
            ],
            transmission: [],
            transmissionOptions: [
                'Automatic',
                'Manual',
            ],
            body: [],
            bodyOptions: [
                'Hatchback',
                'Coupe',
                'Convertible',
            ],
            withPhotos: true,
            yearFrom: [],
            yearTo: [],
            yearOptions: Array.from(new Array(40), (x, i) => i + 1980),
            mileageFrom: '',
            mileageTo: '',
            priceFrom: '',
            priceTo: '',
        };
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
