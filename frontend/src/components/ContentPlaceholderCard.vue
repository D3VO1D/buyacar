<template>
    <content-placeholders
        class="card"
        :rounded="true"
    >
        <div class="card__main">
            <div class="card__thumb">
                    <content-placeholders-img class="card__img" />
            </div>
            <div class="card__description">
                <div class="card__column">
                    <div class="card__column-row">
                        <div class="card__title">
                            <content-placeholders-text :lines="1" />
                        </div>
                    </div>

                    <div class="card__column-row">
                        <div class="card__tech-summary">
                            <div class="card__tech-summary-column">
                                <content-placeholders-text :lines="1" class="card_cell" />
                                <content-placeholders-text :lines="1" class="card_cell" />
                            </div>
                            <div class="card__tech-summary-column">
                                <content-placeholders-text :lines="1" class="card_cell" />
                                <content-placeholders-text :lines="1" class="card_cell" />
                            </div>
                        </div>
                    </div>

                    <div class="card__column-row">
                        <content-placeholders-text
                            :lines="1"
                            class="card__additional-info"
                        />
                    </div>
                </div>

                <div class="card__column">
                    <div class="card__column-row">
                        <content-placeholders-text :lines="1" class="card__price" />
                    </div>
                </div>

                <div class="card__column">
                    <div class="card__column-row">
                        <content-placeholders-text :lines="1" class="card__year" />
                    </div>
                </div>

                <div class="card__column">
                    <div class="card__column-row">
                        <content-placeholders-text :lines="1" class="card__mileage" />
                    </div>

                    <div class="card__column-row">
                        <content-placeholders-text
                            :lines="1"
                            class="card__additional-info card__additional-info_align_right"
                        />
                    </div>
                </div>
            </div>
        </div>
    </content-placeholders>
</template>

<script>
export default {
    name: 'ContentPlaceholderCard',
};
</script>

<style lang="scss" scoped>
@import '@/_vars.scss';

.card {
    width: 100%;
    position: relative;
    padding: 16px;
    background-color: $white;

    &:hover {
        z-index: 1;
        border-radius: 8px;
        background-color: #fff;
        box-shadow: 0 5px 20px 0 $card-shadow-color;
    }

    &::before {
        position: absolute;
        top: 0;
        right: 16px;
        left: 16px;
        display: block;
        height: 1px;
        content: " ";
        border-top: 1px solid $divider-color;
    }

    &:hover:before {
        display: none;
    }

    &:hover + .card::before {
        display: none;
    }

    &:hover .card__title {
        color: $accent-color;
    }

    &__main {
        display: flex;
    }

    &__thumb {
        flex-shrink: 0;
        width: 205px;
        height: 150px;
    }

    &__img {
        width: 205px;
        height: 150px;
    }

    &__description {
        display: flex;
        padding: 0 16px;
        justify-content: space-between;
        width: 100%;
    }

    &__title {
        width: 260px;
        transition: color 0.3s ease;
    }

    &__price {
        width: 120px;
        text-align: right;
        margin-left: 20px;
        margin-right: 20px;
    }

    &__column {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    &__column-row {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        align-items: flex-start;
    }

    &__tech-summary {
        display: flex;
    }

    &__tech-summary-column {
        width: 180px;
    }

    &__tech-summary-column:last-child {
        width: 120px;
    }

    &__cell {
        max-width: 180px;
        font-size: 15px;
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
        color: $secondary-text-color;
    }

    &__additional-info {
        width: 120px;
        margin: 8px 0 0;

        &_align_right {
            flex-grow: 1;
            text-align: right;
        }
    }

    &__year, &__mileage {
        margin-bottom: 8px;
    }

    &__year {
        width: 100px;
        text-align: left;
    }

    &__mileage {
        width: 100px;
        flex-grow: 1;
        text-align: right;
    }
}
</style>
