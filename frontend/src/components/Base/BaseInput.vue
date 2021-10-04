<template>
    <div :class="[
                    'input-container',
                    { 'input-container_focused': isInputFocused,
                      'input-container_selected': isValueSelected },
                    `input-container_borders-${bordersType}`,
                ]"
    >
        <input
            class="input-container__input"
            type="text"
            :placeholder="placeholder"
            v-model="tempValue"
            @focus="isInputFocused = true"
            @blur="isInputFocused = false"
            @keyup.enter="finishedTyping = true"
            ref="input"
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
    data(props) {
        return {
            finishedTyping: false,
            timeout: null,
            tempValue: props.value,
            isInputFocused: false,
            isValueSelected: false,
        };
    },
    watch: {
        tempValue(val) {
            // we don't update the value immediately to not send http request every time user types a letter
            // instead, we update the value 500ms after the user typed the last symbol
            this.finishedTyping = false;
            clearTimeout(this.timeout);
            const onlyDigits = val.replace(/\D/g, '');
            if (!onlyDigits) {
                this.tempValue = '';
                return;
            }

            this.tempValue = new Intl.NumberFormat('en-US').format(onlyDigits);
            this.timeout = setTimeout(() => {
                if (!this.tempValue) return;
                this.finishedTyping = true;
            }, 500);
        },
        finishedTyping(val) {
            this.isValueSelected = !!val;
            if (val) {
                this.$refs.input.blur();
                this.$emit('input', this.tempValue.replaceAll(',', ''));
            }
        },
        value(val) {
            if (val !== this.tempValue.replaceAll(',', '')) {
                this.tempValue = val;
            }
            if (!val) {
                this.isValueSelected = false;
            }
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

    &:hover, &_focused {
        cursor: text;
        border: 1px solid #157ee1;
        z-index: 100;
    }

    &_selected {
        border: 1px solid rgba(21, 126, 225, .5) !important;
        background-color: #eef4fa;
        z-index: 100;
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
        margin-left: -1px;
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
        color: #000 !important;

        &::placeholder {
            color: grey !important;
        }
    }
}
</style>
