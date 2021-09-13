<template>
    <div class="select-container">
        <div
            class="select-container__select"
            :class="{'select-container__has-chosen-value': !!selectedOptions.length}"
            @click="showOptions = !showOptions"
        >
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
        </div>
        <ul class="select-container__options" v-if="showOptions">
            <li
                class="select-container__option"
                @click="$emit('resetSelectedOptions')"
            >
                <font-awesome-icon class="select-container__icon" :icon="['fas', 'times']"/>
                <span>Any</span>
            </li>
            <li
                class="select-container__option"
                v-for="(option, index) in options"
                :key="option"
                @click.prevent="$emit('selectOption', selectedOptions, option)"
            >
                <font-awesome-icon
                    class="select-container__icon"
                    :icon="['fas', 'check']"
                    v-visible="selectedOptions.indexOf(options[index]) !== -1"
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
    props: ['options', 'selectedOptions', 'placeholder'],
    data() {
        return {
            showOptions: false,
            id: Math.random(),
        };
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
</style>
