<template>
    <div
        class="select-container"
        @click="showOptions = !showOptions"
    >
        <div class="select-container__select" :class="{'select-container__has-chosen-value': !!value}">
            <span class="select-container__value">
                {{ value ? value : placeholder }}
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
                @click="value = ''"
            >
                <font-awesome-icon :icon="['fas', 'times']"/>
                Any
            </li>
            <li
                class="select-container__option"
                v-for="option in options"
                :key="option"
                @click="selectOption(option)"
            >
                <label>
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
    props: ['options', 'value', 'placeholder'],
    data() {
        return {
            showOptions: false,
            id: Math.random(),
        };
    },
    methods: {
        selectOption(option) {
            this.$emit('input', option);
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
        height: 36px;
        line-height: 36px;
        list-style-type: none;
        color: $text-color;
        padding-left: 8px;

        &:hover {
            color: $white;
            background-color: #157ee1;
        }
    }

    &__option input {
        display: none;
    }
}
</style>
