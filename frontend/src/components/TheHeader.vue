<template>
    <header class="header">
        <h1 class="header__logo" @click="clickLogo">
            <router-link :to="{ name: 'Main Page', query: { page: 1 } }" class="header__logo-link">
                <img class="header__logo-img" src="@/assets/logo.svg" alt="logo"/>
                <span class="header__logo-name">WHOLE CARS</span>
            </router-link>
        </h1>
        <h2 class="header__motto">
            All cars are here
        </h2>
    </header>
</template>

<script>
import eventBus from '@/eventBus';

export default {
    name: 'TheHeader',
    methods: {
        clickLogo() {
            eventBus.$emit('reset-filters');
        },
    },
};
</script>

<style lang="scss" scoped>
@import '@/_vars';

.header {
    background-color: $accent-color;
    color: $white;
    display: flex;
    align-items: center;
    padding: 24px 5%;
    font-family: $logo-font;
    height: 98px;
    flex: 1 0 auto;

    &__logo {
        font-size: 32px;
        width: 920px;
        margin-right: 12px;
    }

    &__logo-img {
        width: 45px;
        height: 45px;
        vertical-align: text-bottom;
        margin-right: 8px;
    }

    &__logo-link {
        color: $white;
        text-decoration: none;
    }

    &__motto {
        font-size: 22px;
        flex-shrink: 0;
    }
}

@media screen and (max-width: 1000px) {
    .header {
        width: 100%;
        justify-content: space-between;

        &__logo {
            width: auto;
            font-size: 28px;
        }

        &__logo-img {
            width: 40px;
            height: 40px;
        }

        &__motto {
            font-size: 20px;
        }
    }
}

@media screen and (max-width: 480px) {
    .header {
        align-items: baseline;

        &__logo {
            font-size: 22px;
        }

        &__logo-img {
            width: 35px;
            height: 35px;
        }

        &__motto {
            font-size: 14px;
        }
    }
}

@media screen and (max-width: 350px) {
    .header {
        flex-direction: column;
    }
}
</style>
