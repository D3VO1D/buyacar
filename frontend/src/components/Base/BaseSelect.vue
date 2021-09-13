<template>
    <div class="select-container" v-click-outside="clickOutside">
        <div
            class="select-container__select"
            :class="{'select-container__has-chosen-value': !!selectedOptions.length}"
            @click="showOptions = !showOptions"
            @keyup.esc="resetSelections"
        >
            <template v-if="withInput">
                <input
                    class="input"
                    type="text"
                    :placeholder="inputPlaceholder"
                    v-model="inputValue"
                    @input="showOptions = true"
                    @focus="focusInput"
                    @blur="blurInput"
                    ref="input"
                />

                <span class="select-container__arrow" v-if="showChevron">
                    <font-awesome-icon :icon="['fas', 'chevron-down']"/>
                </span>
            </template>
            <template v-else>
                <span class="select-container__value">
                    {{ selectedOptions.length ? selectedOptions.join(', ') : placeholder }}
                </span>
                <span class="select-container__value-counter" v-if="selectedOptions.length > 1">
                    ({{ selectedOptions.length }})
                </span>

                <span class="select-container__arrow" v-if="!showOptions">
                    <font-awesome-icon :icon="['fas', 'chevron-down']"/>
                </span>
                <span class="select-container__arrow" v-if="showOptions">
                    <font-awesome-icon :icon="['fas', 'chevron-up']"/>
                </span>
            </template>
        </div>
        <ul class="select-container__options" v-if="showOptions">
            <li
                class="select-container__option"
                @click="resetSelections"
            >
                <font-awesome-icon class="select-container__icon" :icon="['fas', 'times']"/>
                <span>{{ resetText }}</span>
            </li>
            <li
                class="select-container__option"
                v-for="(option, index) in filteredOptions"
                :key="option"
                @mousedown.prevent="selectOption(option)"
            >
                <font-awesome-icon
                    class="select-container__icon"
                    :icon="['fas', 'check']"
                    v-visible="selectedOptions.indexOf(filteredOptions[index]) !== -1"
                />

                <label class="select-container__label">
                    <input type="checkbox" :value="option"/>
                    {{ option }}
                </label>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'BaseSelect',
    props: {
        options: {
            type: Array,
            required: true,
        },
        selectedOptions: {
            type: Array,
            default: () => [],
        },
        placeholder: {
            type: String,
            default: '',
        },
        withInput: {
            type: Boolean,
            default: false,
        },
        selectionMode: {
            type: String,
            default: 'multiple',
            validator: (value) => value === 'single' || value === 'multiple',
        },
        resetText: {
            type: String,
            default: 'Any',
        },
    },
    data() {
        return {
            showOptions: false,
            showChevron: true,
            id: Math.random(),
            inputValue: '',
            tempInputValue: '',
            userChoseOption: false,
        };
    },
    computed: {
        filteredOptions() {
            if (!this.withInput) {
                return this.options;
            }
            // if user entered sth, we should autocomplete and suggest filtered options
            return this.options.filter((option) => option.toLowerCase()
                .indexOf(this.inputValue.toLowerCase()) !== -1);
        },
        inputPlaceholder() {
            return this.tempInputValue || this.placeholder;
        },
    },
    methods: {
        selectOption(option) {
            this.userChoseOption = true;
            this.showOptions = false;
            if (!this.withInput) {
                this.$emit('selectOption', this.selectedOptions, option, this.selectionMode);
                return;
            }
            // if user typed sth and then selected item from dropdown, set his selected to that value
            this.inputValue = option;
            this.tempInputValue = option;
            this.showChevron = true;
            this.$emit('selectOption', this.selectedOptions, option, this.selectionMode);
            this.$refs.input.blur();
        },
        resetSelections() {
            this.userChoseOption = false;
            this.showOptions = false;
            this.inputValue = '';
            this.$emit('resetSelectedOptions');
        },
        focusInput() {
            this.showChevron = false;
            if (this.userChoseOption) {
                this.tempInputValue = this.inputValue;
                this.inputValue = '';
            }
        },
        blurInput() {
            this.showChevron = true;
            if (this.userChoseOption) {
                this.inputValue = this.tempInputValue;
                this.tempInputValue = '';
            }
        },
        clickOutside() {
            this.showOptions = false;
        },
    },
};
</script>

<style lang="scss" scoped>
@import '@/_vars.scss';

.select-container {
    position: relative;
    font-size: 15px;

    &__select {
        height: 36px;
        background-color: $white;
        border: 1px solid rgba(0, 0, 0, .12);
        border-radius: 8px;
        padding-left: 8px;
        display: flex;
        justify-content: space-between;
        align-items: center;

        &:hover {
            cursor: pointer;
            border: 1px solid #157ee1;
        }
    }

    &__value {
        color: grey;
        text-overflow: ellipsis;
        white-space: nowrap;
        overflow: hidden;
    }

    &__value-counter {
        margin-right: 4px;
    }

    &__has-chosen-value {
        border: 1px solid rgba(21, 126, 225, .5);
        background-color: #eef4fa;

        .select-container__value {
            color: $text-color;
        }
    }

    &__arrow {
        height: 100%;
        line-height: 36px;
        padding-right: 8px;
        opacity: .543;
    }

    &__options {
        position: absolute;
        width: 100%;
        z-index: 1500;
        margin-top: 10px;
        border-radius: 8px;
        background-color: $white;
        box-shadow: 0 10px 30px 0 rgb(0 0 0 / 10%);
        max-height: 200px;
        overflow: auto;
    }

    &__option {
        display: flex;
        align-items: center;
        height: 36px;
        line-height: 36px;
        list-style-type: none;
        color: $text-color;
        padding-left: 8px;

        &:hover {
            cursor: pointer;
            color: $white;
            background-color: #157ee1;
        }

        &:hover * {
            opacity: 1;
        }
    }

    &__icon {
        width: 15px;
        height: 15px;
        margin-right: 10px;
        opacity: .543;
    }

    &__label {
        &:hover {
            cursor: pointer;
        }
    }

    &__option input {
        display: none;
    }
}

.input {
    outline: none;
    display: block;
    width: 100%;
    height: 100%;
    font-size: 15px;
    border: transparent;
    margin-right: 8px;
    background-color: inherit;
}
</style>
