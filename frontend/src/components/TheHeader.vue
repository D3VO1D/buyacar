<template>
    <header class="header">
        <h1 class="header__logo">
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
export default {
    name: 'TheHeader',
};
</script>

<style lang="scss" scoped>
@import '@/_vars';

.header {
    background-color: $accent-color;
    color: $white;
    display: flex;
    align-items: center;
    padding: 24px 10%;
    font-family: $logo-font;

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
    }
}
</style>
