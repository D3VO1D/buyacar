<template>
    <div class="radio-toolbar">
        <template v-for="(option, index) in options">
            <input
                class="radio-toolbar__radio"
                type="radio"
                :id="`${id}-${index}`"
                :name="`toolbar-${id}`"
                :checked="option === selectedOption"
                :key="`${id}-${index}-input`"
                :disabled="disabled"
            />
            <label
                class="radio-toolbar__label"
                :class="(disabled) ? 'radio-toolbar__label_disabled' : 'radio-toolbar__label_enabled'"
                :for="id"
                @click="$emit('selectOption', option)"
                :key="`${id}-${index}-label`"
            >
                {{ option }}
            </label>
        </template>
    </div>
</template>

<script>
export default {
    name: 'BaseRadioButtonGroup',
    props: {
        options: {
            type: Array,
            required: true,
        },
        selectedOption: {
            type: [String, Number],
        },
        disabled: {
            type: Boolean,
            default: false,
        },
    },
    data() {
        return {
            id: `radio-button-group-${Math.random() * 100}`,
        };
    },
};
</script>

<style lang="scss" scoped>
@import '@/_vars.scss';

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
        width: calc(280px / 3);
        padding: 10px 20px;
        font-size: 15px;
        border: 1px solid rgba(0, 0, 0, .12);
        background-color: $white;
        color: grey;
        text-align: center;

        &_disabled {
            border-color: rgba(0, 0, 0, .08);
            color: rgba(0, 0, 0, .24);

            &:hover {
                cursor: default;
            }
        }

        &_enabled:hover {
            color: $white;
            background-color: #157ee1;
            cursor: pointer;
        }

        &:first-of-type {
            border-top-left-radius: 8px;
            border-bottom-left-radius: 8px;
            border-right: none;
        }

        &:last-of-type {
            border-top-right-radius: 8px;
            border-bottom-right-radius: 8px;
            border-left: none;
        }
    }
}

@media screen and (max-width: 1000px) {
    .radio-toolbar {
        width: 100%;

        &__label {
            width: calc(100% / 3);
        }
    }
}

@media screen and (max-width: 360px) {
    .radio-toolbar {
        text-align: center;

        &__label {
            width: auto;
        }
    }
}
</style>
