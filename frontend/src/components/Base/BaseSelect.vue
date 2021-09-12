<template>
    <div class="form-control">
        <label :for=id v-if="label">{{ label }}</label>
        <select
            class="select"
            :value="modelValue"
            :id="id"
            v-bind=$attrs
            @change="$emit('update:modelValue', $event.target.value)"
        >
            <option value="" selected disabled hidden>{{ placeholder }}</option>
            <option
                v-for="option in options"
                :key="option"
                :value="option"
                :selected="option === modelValue"
            >{{ option }}
            </option>
        </select>
    </div>
</template>

<script>
export default {
    name: 'BaseSelect',
    props: {
        label: {
            type: String,
        },
        placeholder: {
            type: String,
        },
        modelValue: {
            type: [String, Number],
            default: '',
        },
        options: {
            type: Array,
            required: true,
        },
    },
    data() {
        return {
            id: Math.random(),
        };
    },
};
</script>

<style lang="scss" scoped>
</style>
