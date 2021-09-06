<template>
    <div class="card">
        <div class="card__main">
            <div class="card__thumb">
                <img class="card__image" :src="car.photos[0]" :alt="title"/>
            </div>
            <div class="card__description">
                <div class="card__column">
                    <div class="card__column-row">
                        <div class="card__summary">
                            <h3 class="card__title">
                                <a :href="car.url" class="card__title-link" target="_blank" rel="noreferrer">
                                    {{ title }}
                                    <div class="card__clicker"></div>
                                </a>
                            </h3>
                            <div class="card__tech-summary">
                                <div class="card__tech-summary-column">
                                    <div v-if="present(car.power)" class="card__cell">{{ car.power }}</div>
                                    <div v-if="present(present(car.transmission))" class="card__cell">
                                        {{ car.transmission }}
                                    </div>
                                </div>
                                <div class="card__tech-summary-column">
                                    <div v-if="present(car.drive)" class="card__cell">{{ car.drive }}</div>
                                    <div v-if="present(car.body)" class="card__cell">{{ car.body }}</div>
                                </div>
                            </div>
                        </div>

                        <div class="card__price">
                            {{ price }}
                        </div>
                    </div>

                    <div class="card__column-row">
                        <div v-if="present(car.location)" class="card__additional-info">
                            {{ car.location }}
                        </div>
                    </div>
                </div>

                <div class="card__column">
                    <div class="card__column-row">
                        <div v-if="present(car.year)" class="card__year">
                            {{ car.year }}
                        </div>
                    </div>
                </div>

                <div class="card__column">
                    <div class="card__column-row">
                        <div v-if="present(car.mileage)" class="card__mileage">
                            {{ car.mileage }} mi
                        </div>
                    </div>

                    <div class="card__column-row">
                        <div v-if="present(car.source)" class="card__additional-info card__additional-info_align_right">
                            {{ car.source }}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'AppCarCard',
    props: {
        car: {
            required: true,
            type: Object,
        },
    },
    computed: {
        title() {
            if (!this.car.title || this.car.title === 'nan') {
                return `${this.car.make} ${this.car.model}`;
            }
            return this.car.title;
        },
        price() {
            if (this.car.price === 0) {
                return 'Priceless';
            }
            return `${this.car.price} $`;
        },
    },
    methods: {
        present(property) {
            return property && property !== 'nan';
        },
    },
};
</script>

<style lang="scss" scoped>
@import '@/_vars';

.card {
    width: 70%;
    position: relative;
    padding: 16px;
    background-color: $white;

    &:hover {
        z-index: 1000;
        border-radius: 8px;
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

    &__main {
        display: flex;
    }

    &__thumb {
        flex-shrink: 0;
        width: 205px;
    }

    &__image {
        display: block;
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 8px;
    }

    &__summary {
        width: 290px;
    }

    &__description {
        display: flex;
        padding: 0 16px;
        justify-content: space-between;
        width: 100%;
    }

    &__title, &__price {
        font-size: 17px;
        font-weight: 700;
        margin: 0 16px 16px 0;
    }

    &__title-link {
        color: $text-color;
        text-decoration: none;

        &:hover {
            color: $accent-color;
        }
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
        margin-bottom: 8px;
    }

    &__tech-summary-column:not(:last-child) {
        width: 180px;
    }

    &__cell {
        max-width: 180px;
        margin-right: 12px;
        font-size: 15px;
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
        color: $secondary-text-color;
    }

    &__additional-info {
        margin: 8px 0 0;
        font-size: 13px;
        color: $secondary-text-color;

        &_align_right {
            flex-grow: 1;
            text-align: right;
        }
    }

    &__year, &__mileage {
        font-size: 17px;
        margin-bottom: 8px;
    }

    &__clicker {
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
    }
}
</style>
