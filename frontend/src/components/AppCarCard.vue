<template>
    <div class="card">
        <div class="card__main">
            <a :href="car.url" class="card__link" target="_blank" rel="noreferrer">
                <div class="card__thumb">
                    <GalleryOnHover
                        :photos="previewPhotos"
                        :placeholder-url="placeholderPhotoUrl"
                    />
                </div>
                <div class="card__clicker"></div>
            </a>
            <div class="card__description">
                <div class="card__column">
                    <div class="card__column-row">
                        <h3 class="card__title">
                            {{ title }}
                        </h3>
                    </div>

                    <div class="card__column-row">
                        <div class="card__tech-summary">
                            <div class="card__tech-summary-column">
                                <div v-if="present(car.power) && car.power !== 0" class="card__cell">
                                    {{ car.power }}
                                </div>
                                <div v-else class="card__cell">&nbsp;</div>
                                <div v-if="present(car.transmission)" class="card__cell">
                                    {{ car.transmission }}
                                </div>
                            </div>
                            <div class="card__tech-summary-column">
                                <div v-if="present(car.drive)" class="card__cell">{{ car.drive }}</div>
                                <div v-else class="card__cell">&nbsp;</div>
                                <div v-if="present(car.body)" class="card__cell">{{ car.body }}</div>
                            </div>
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
                        <div class="card__price">
                            {{ price }}
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
                            {{ mileage }}
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
import GalleryOnHover from '@/components/GalleryOnHover';

export default {
    name: 'AppCarCard',
    components: { GalleryOnHover },
    props: {
        car: {
            required: true,
            type: Object,
        },
    },
    created() {
        this.preloadPhotos();
    },
    computed: {
        title() {
            if (!this.car.title || this.car.title === 'nan') {
                return `${this.car.make} ${this.car.model}`;
            }
            return this.car.title;
        },
        price() {
            if (!this.car.price) {
                return 'Priceless';
            }
            const USFormat = Intl.NumberFormat('en-US');
            return `$${USFormat.format(this.car.price)}`;
        },
        mileage() {
            if (!this.car.mileage) {
                return 'New';
            }
            const USFormat = Intl.NumberFormat('en-US');
            return `${USFormat.format(this.car.mileage)} mi`;
        },
        previewPhotos() {
            return this.car.photos.slice(0, 5);
        },
        placeholderPhotoUrl() {
            return `https://via.placeholder.com/200x150?text=${this.title}`;
        },
    },
    methods: {
        present(property) {
            return property !== 'nan';
        },
        preloadPhotos() {
            this.previewPhotos.map((photo) => {
                const img = new Image();
                img.src = photo;
                return img;
            });
        },
    },
};
</script>

<style lang="scss" scoped>
@import '@/_vars';

.card {
    width: fit-content;
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
    }

    &__description {
        display: flex;
        padding: 0 16px;
        justify-content: space-between;
        width: 100%;
    }

    &__title {
        font-size: 17px;
        font-weight: 700;
        transition: color 0.3s;
    }

    &__price {
        font-size: 17px;
        font-weight: 700;
        min-width: 120px;
        text-align: right;
        margin-right: 20px;
    }

    &__link {
        color: $text-color;
        text-decoration: none;
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

    &__tech-summary-column:first-child {
        width: 180px;
    }

    &__tech-summary-column:last-child {
        min-width: 80px;
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

    &__year {
        min-width: 60px;
        text-align: left;
    }

    &__mileage {
        min-width: 100px;
        text-align: right;
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
