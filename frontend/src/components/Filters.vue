<template>
    <div class="filters">
        <div class="filters__row filters__row_header">
            <div class="filters__column">
                <div class="radio-toolbar">
                    <input class="radio-toolbar__radio" type="radio" id="select-all"
                           name="toolbar" value="all" checked>
                    <label class="radio-toolbar__label" for="select-all">All</label>

                    <input class="radio-toolbar__radio" type="radio" id="select-new"
                           name="toolbar" value="new">
                    <label class="radio-toolbar__label" for="select-new">New</label>

                    <input class="radio-toolbar__radio" type="radio" id="select-used"
                           name="toolbar" value="used">
                    <label class="radio-toolbar__label" for="select-used">Used</label>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Filters',
};
</script>

<style lang="scss" scoped>
@import '@/_vars.scss';

.filters {
    margin: 0 0 24px 16px;
    padding: 20px;
    border-radius: 8px;
    background: $white;
    box-shadow: 0 3px 14px $filters-shadow-color;

    &__row {
        display: flex;
        margin: 12px 0;

        &_header {
            margin-top: 0;
        }
    }

    &__column {
        display: flex;
        flex: 1;
        flex-shrink: 0;
        align-items: center;
        min-width: 0;
        margin-left: 20px;

        &:first-child {
            margin-left: 0;
        }
    }
}

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
        padding: 10px 20px;
        font-size: 15px;
        border: 1px solid rgba(0, 0, 0, .12);
        background-color: $white;
        color: grey;
        height: 36px;
        text-align: center;

        &:hover {
            color: $white;
            background-color: #157ee1;
            cursor: pointer;
        }

        &:first-of-type {
            border-top-left-radius: 8px;
            border-bottom-left-radius: 8px;
        }

        &:last-of-type {
            border-top-right-radius: 8px;
            border-bottom-right-radius: 8px;
        }
    }
}
</style>
