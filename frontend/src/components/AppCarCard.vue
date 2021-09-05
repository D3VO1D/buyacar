<template>
    <div class="card">
        <div class="card__main">
            <div class="card__thumb">
                <img class="card__image" src="https://avatars.mds.yandex.net/get-autoru-vos/4395583/e3e19b3f147e183ebbdcc0fc45078bbd/320x240"/>
            </div>
            <div class="card__description">
                <div class="card__column">
                    <div class="card__column-row">
                        <div class="card__summary">
                            <h3 class="card__title">
                                <a href="/" class="card__title-link">
                                    Hyundai Creta II
                                    <div class="card__clicker"></div>
                                </a>
                            </h3>
                            <div class="card__tech-summary">
                                <div>
                                    <div class="card__cell">1.6 л./ 123 л.с. / Бензин</div>
                                    <div class="card__cell">Автомат</div>
                                    <div class="card__cell">Внедорожник 5 дв.</div>
                                </div>
                                <div>
                                    <div class="card__cell">Передний</div>
                                    <div class="card__cell">Серебристый</div>
                                </div>
                            </div>
                        </div>

                        <div class="card__price">1,656,000 $</div>
                    </div>

                    <div class="card__column-row">
                        <div class="card__additional-info">
                            Москва
                        </div>
                    </div>
                </div>

                <div class="card__column">
                    <div class="card__year">
                        2021
                    </div>
                </div>

                <div class="card__column">
                    <div class="card__column-row">
                        <div class="card__mileage">
                            264,935 mi
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'CarCard',
    props: {
        car: {
            required: true,
            type: Object,
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

    &__description {
        display: flex;
        padding: 0 16px;
        justify-content: space-between;
        width: 100%;
    }

    &__title, &__price {
        font-size: 17px;
        font-weight: 700;
        margin: 0 16px 8px 0;
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
