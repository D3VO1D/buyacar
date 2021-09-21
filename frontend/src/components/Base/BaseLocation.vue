<template>
    <div class="location" v-click-outside="hideSearchBox">
        <div class="location__select" @click="showSearchBox = !showSearchBox">
            <div class="location__select-icon">
                <svg viewBox="0 0 24 24" id="geo">
                    <g fill-rule="evenodd" fill="currentColor">
                        <path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2m0 2c4.411 0 8
                    3.589 8 8s-3.589 8-8 8-8-3.589-8-8 3.589-8 8-8"></path>
                        <path d="M7 12l9-4-4 9-1-4z"></path>
                    </g>
                </svg>
            </div>
            <div class="location__text">{{ text }}</div>
        </div>
        <div class="location__search" v-if="showSearchBox">
            <div class="location__search-box">
                <div class="location__dropdown-input-container">
                    <input
                        class="location__dropdown-input"
                        placeholder="City or state"
                        @input="loadOptions"
                        v-model="userLocationInput"
                    />
                </div>
                <div class="location__reset-location" v-if="location || userCity" @click="resetLocation">
                    Reset location
                    <font-awesome-icon class="location__reset-location-icon" :icon="['fas', 'times']"/>
                </div>
            </div>
            <ul class="location__options" v-if="options">
                <li
                    class="location__option"
                    v-for="option in options"
                    :key="`${option.name}${option.longitude}${option.latitude}`"
                    @click="selectLocation(option)"
                >
                    <div class="location__option-region">
                        {{ option.name }}
                    </div>
                    <div class="location__option-parent-region">
                        {{ option.stateCode }}
                    </div>
                </li>
            </ul>
            <BaseLoader v-if="isLoading"/>
        </div>
    </div>
</template>

<script>
import { getStatesCities } from '@/utils/cities';
import { isValidUSZipCode } from '@/utils/zip';
import { getPlacesForZIP } from '@/services/api';
import BaseLoader from '@/components/Base/BaseLoader';

export default {
    name: 'BaseLocation',
    components: { BaseLoader },
    props: {
        userCity: {
            type: String,
            default: '',
        },
    },
    data() {
        return {
            location: '',
            locationOffset: 0,
            showSearchBox: false,
            options: [],
            allOptions: [],
            userLocationInput: '',
            startSearchingOffset: 3,
            isLoading: false,
        };
    },
    created() {
        this.allOptions = getStatesCities();
    },
    computed: {
        text() {
            return this.location || this.userCity || 'Choose location';
        },
    },
    methods: {
        loadOptions() {
            // user can write either a state or city name, or a valid zip code
            if (isValidUSZipCode(this.userLocationInput)) {
                this.isLoading = true;
                getPlacesForZIP(this.userLocationInput)
                    .then((res) => {
                        const { places } = res.data;
                        this.options = places.map((place) => (
                            {
                                name: place['place name'],
                                stateCode: place['state abbreviation'],
                                longitude: place.longitude,
                                latitude: place.latitude,
                            }
                        ));
                    })
                    .catch((err) => console.log(err))
                    .finally(() => {
                        this.isLoading = false;
                    });
                return;
            }

            if (this.userLocationInput.length < this.startSearchingOffset) {
                this.options = [];
                return;
            }

            this.options = this.allOptions.filter((option) => option.name.toLowerCase()
                .startsWith(this.userLocationInput.toLowerCase()));
        },
        selectLocation(option) {
            let chosenLocation = option.name;
            if (option.stateCode) {
                chosenLocation += `, ${option.stateCode}`;
            }
            this.location = chosenLocation;
            this.userLocationInput = chosenLocation;
            this.showSearchBox = false;
            this.$emit('changeLocation', option);
        },
        hideSearchBox() {
            this.showSearchBox = false;
        },
        resetLocation() {
            this.location = '';
            this.userLocationInput = '';
            this.options = [];
            this.showSearchBox = false;
            this.$emit('resetLocation');
        },
    },
};
</script>

<style lang="scss" scoped>
@import '@/_vars.scss';

.location {
    position: relative;

    &__select {
        display: flex;
        align-items: center;
        font-size: 15px;
        height: 44px;
        color: #157ee1;

        &:hover {
            cursor: pointer;
        }
    }

    &__select-icon {
        width: 24px;
        height: 24px;
        margin-right: 12px;
    }

    &__search {
        position: absolute;
        right: 0;
        width: 380px;
        background-color: #fff;
        box-shadow: 0 10px 30px 0 rgb(0 0 0 / 10%);
        border-radius: 8px;
        overflow: hidden;
        z-index: 100;
    }

    &__search-box {
        padding: 20px 15px;
    }

    &__reset-location {
        color: grey;
        font-size: 15px;
        line-height: 24px;
        display: flex;
        justify-content: center;
        align-items: center;
        transition: color .3s ease;
        margin-top: 4px;

        &:hover {
            color: $accent-color;
            cursor: pointer;
        }
    }

    &__reset-location-icon {
        margin-left: 8px;
    }

    &__dropdown-input-container {
        position: relative;
        display: flex;
        align-items: center;
        width: 100%;
        padding: 0 12px;
        border: 1px solid rgba(0, 0, 0, .12);
        background: #f0f0f0;
        border-radius: 8px;

        &:focus-within, &:hover {
            border-color: #157ee1;
        }

        &::before {
            display: inline-block;
            width: 24px;
            height: 24px;
            margin-right: 8px;
            content: "";
            opacity: .5;
            color: #000;
            background: url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill='currentColor' d='M15.437 14.063h-.726l-.253-.25a5.918 5.918 0 001.435-3.867 5.946 5.946 0 10-5.947 5.947 5.919 5.919 0 003.865-1.433l.253.25v.725l4.572 4.566L20 18.637l-4.563-4.574zm-5.49 0a4.116 4.116 0 110-8.233 4.117 4.117 0 010 8.233z' fill-rule='evenodd'/%3E%3C/svg%3E");
        }
    }

    &__dropdown-input {
        width: 100%;
        height: 42px;
        outline: none;
        background: #f0f0f0;
        border: none;
        font: inherit;
        font-size: 15px;
        color: rgba(0, 0, 0, .87);

        &::placeholder {
            font-size: 15px;
            line-height: normal;
            position: absolute;
            top: 50%;
            display: block;
            overflow: hidden;
            max-width: calc(100% - 32px);
            white-space: nowrap;
            text-overflow: ellipsis;
            pointer-events: none;
            color: rgba(0, 0, 0, .54);
            transition: font-size .05s ease-out 0s, margin-top .05s ease-out 0s, opacity .1s ease-out 0s;
            transform: translateY(-50%);
        }
    }

    &__options {
        max-height: 280px;
        overflow-y: auto;
    }

    &__option {
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 42px;
        padding: 5px 15px;
        box-sizing: content-box;
        cursor: pointer;
        border-bottom: 1px solid rgba(0, 0, 0, .1);

        &:hover {
            background-color: #eaf4ff;
        }
    }

    &__option-region {
        font-size: 15px;
        overflow-x: hidden;
        text-overflow: ellipsis;
        color: #000;
    }

    &__option-parent-region {
        font-size: 12px;
        overflow-x: hidden;
        text-overflow: ellipsis;
        color: rgba(0, 0, 0, .6);
    }
}
</style>
