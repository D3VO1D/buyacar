<template>
    <div class="root">
    <content-placeholders
        class="card-m"
        :rounded="true"
    >
        <div class="card-m__header">
            <p class="card-m__title">
                <content-placeholders-text :lines="1" />
            </p>
            <h3 class="card-m__price">
                <content-placeholders-text :lines="1" />
            </h3>
        </div>
        <div class="card-m__gallery">
            <content-placeholders-img class="card-m__photo" />
            <content-placeholders-img class="card-m__photo" />
            <content-placeholders-img class="card-m__photo" />
        </div>
        <div class="card-m__params">
            <div class="card-m__params-column">
                <div class="card-m__params-cell">
                    <content-placeholders-text :lines="1" />
                </div>
                <div class="card-m__params-cell">
                    <content-placeholders-text :lines="1" />
                </div>
                <div class="card-m__params-cell">
                    <content-placeholders-text :lines="1" />
                </div>
            </div>
            <div class="card-m__params-column">
                <div class="card-m__params-cell">
                    <content-placeholders-text :lines="1" />
                </div>
                <div class="card-m__params-cell">
                    <content-placeholders-text :lines="1" />
                </div>
            </div>
        </div>
        <div class="card-m__footer">
            <div class="card-m__location">
                <content-placeholders-text :lines="1" />
            </div>
            <div class="card-m__source">
                <content-placeholders-text :lines="1" />
            </div>
        </div>
    </content-placeholders>
    </div>
</template>

<script>
export default {
    name: 'ContentPlaceholderCardMobile',
};
</script>

<style lang="scss" scoped>
@import '@/_vars.scss';

.root {
    width: 100%;
}

.card-m {
    padding: 20px;
    border-radius: 8px;
    background: $white;
    margin: 8px 5% 8px 0;
    box-shadow: 0 3px 14px $card-shadow-color;

    &__header {
        display: flex;
        flex-direction: column;
        margin-bottom: 12px;
    }

    &__title {
        width: 250px;
        line-height: 20px;
        margin: 0 0 2px;
    }

    &__price {
        width: 150px;
    }

    &__gallery {
        height: 65vw;
        display: flex;
        flex-wrap: wrap;
        flex-direction: column;
        overflow-x: auto;
        overflow-y: hidden;
        overscroll-behavior-x: contain;
        -webkit-overflow-scrolling: touch;
        scroll-snap-type: x mandatory;
        margin-top: 12px;
    }

    &__photo {
        overflow: hidden;
        scroll-snap-align: start;
        flex-shrink: 0;
        border-radius: 8px;
        margin-right: 2px;
        width: 280px;
        height: 65vw;
        object-fit: contain;
    }

    &__params {
        display: flex;
        margin-top: 14px;
        margin-bottom: 12px;
    }

    &__params-column {
        flex: 1;
        min-width: 0;

        &:first-child .card-m__params-cell {
            padding-right: 12px;
        }
    }

    &__params-cell {
        overflow: hidden;
        margin: 4px 0;
        white-space: nowrap;
        text-overflow: ellipsis;
        width: 130px;

        &:first-child {
            margin-top: 0;
        }
    }

    &__footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-top: 1px solid #e0e0e0;
        padding-top: 14px;
    }

    &__location {
        width: 150px;
        min-width: 0;
        color: grey;
    }

    &__source {
        width: 80px;
        color: grey;
    }
}

@media screen and (orientation: landscape) {
    .card-m {
        &__gallery {
            height: 65vh;
        }

        &__photo {
            width: 250px;
            height: 65vh;
        }
    }
}
</style>
