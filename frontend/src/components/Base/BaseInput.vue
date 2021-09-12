<template>
    <div class="form-control">
        <label :for=id v-if="label">{{ label }}</label>
        <datalist :id="`available-options-${id}`">
            <option v-for="option in autocompleteOptions" :key="option">{{ option }}</option>
        </datalist>
        <input
            class="input"
            :list="`available-options-${id}`"
            v-bind=$attrs
            :id=id
            :placeholder="placeholder"
            :value="modelValue"
            @input="$emit('update:modelValue', $event.target.value)"
        >
    </div>
</template>

<script>
export default {
    name: 'BaseInput',
    props: {
        label: {
            type: String,
            default: '',
        },
        placeholder: {
            type: String,
            default: (props) => props.label,
        },
        modelValue: {
            type: [String, Number],
            default: '',
        },
        autocompleteOptions: {
            type: Array,
            default: () => [],
        },
    },
    data() {
        return {
            id: `input-${Math.random()}`,
        };
    },
};
</script>

<style lang="scss" scoped>
</style>
