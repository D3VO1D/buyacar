<template>
    <div class="input-container">
        <input
            class="input-container__input"
            type="text"
            :placeholder="placeholder"
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
    border-radius: 8px;
    padding: 0 8px;

    &:hover {
        cursor: text;
        border: 1px solid #157ee1;
    }

    &__input {
        outline: none;
        display: block;
        width: 100%;
        height: 100%;
        font-size: 15px;
        border: transparent;
        background-color: inherit;
    }
}
</style>
