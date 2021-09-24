<template>
    <div :class="['input-container', `input-container_borders-${bordersType}`]">
        <input
            class="input-container__input"
            type="text"
            :placeholder="placeholder"
            :value="value"
            @input="$emit('input', $event.target.value)"
        />
    </div>
</template>

<script>
export default {
    name: 'BaseInput',
    props: {
        placeholder: {
            type: String,
            default: '',
        },
        value: {
            type: String,
            required: true,
        },
        bordersType: {
            type: String,
            default: 'all',
            validator: (value) => value === 'all' || value === 'left' || value === 'right',
        },
    },
};
</script>

<style lang="scss" scoped>
@import '@/_vars.scss';

.input-container {
    position: relative;
    font-size: 15px;
    height: 36px;
    background-color: $white;
    border: 1px solid rgba(0, 0, 0, .12);
    padding: 0 8px;

    &:hover {
        cursor: text;
        border: 1px solid #157ee1;
    }

    &_borders-all {
        border-radius: 8px;
    }

    &_borders-left {
        border-top-left-radius: 8px;
        border-bottom-left-radius: 8px;
    }

    &_borders-right {
        border-top-right-radius: 8px;
        border-bottom-right-radius: 8px;
    }

    &__input {
        outline: none;
        display: block;
        width: 100%;
        height: 100%;
        font-family: inherit;
        font-size: 15px;
        border: transparent;
        background-color: inherit;
    }
}
</style>
