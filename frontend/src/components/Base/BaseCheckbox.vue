<template>
    <div class="checkbox-container">
        <input
            class="custom-checkbox"
            :id="id"
            type="checkbox"
            :checked="value"
            @change="$emit('input', $event.target.checked)"
        >
        <label :for="id" class="checkbox__label">{{ label }}</label>
    </div>
</template>

<script>
export default {
    name: 'BaseCheckbox',
    props: {
        label: {
            type: String,
            required: true,
        },
        value: {
            type: Boolean,
            default: false,
        },
    },
    data() {
        return {
            id: `base-checkbox-${Math.random()}`,
        };
    },
};
</script>

<style lang="scss" scoped>
.checkbox-container {
    display: flex;
    justify-content: right;
    align-items: center;
    font-size: 15px;
}

.custom-checkbox {
    position: absolute;
    z-index: -1;
    opacity: 0;
}

.custom-checkbox + label {
    display: inline-flex;
    align-items: center;
    user-select: none;
}

.custom-checkbox + label::before {
    content: '';
    display: inline-block;
    width: 23px;
    height: 23px;
    border: 1px solid rgba(0, 0, 0, .2);
    border-radius: 4px;
    background-color: #fff;
    transition: background-color .2s, border-color .2s;
    margin-right: 12px;

    background-repeat: no-repeat;
    background-position: center center;
}

.custom-checkbox:not(:disabled):not(:checked) + label:hover::before {
    border-color: #2c8be4;
}

.custom-checkbox:checked + label::before {
    border-color: transparent;
    background-color: #157ee1;
    background-image: url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='10'%3E%3Cpath fill='%23fff' d='M.295 5.477a.951.951 0 010-1.378l-.033.031a1.042 1.042 0 011.437.004l2.88 2.77L11.464.282a1.045 1.045 0 011.431.001l-.033-.031a.949.949 0 01-.004 1.382L5.3 8.902a1.053 1.053 0 01-1.438.005L.295 5.477z'/%3E%3C/svg%3E");
}

</style>
