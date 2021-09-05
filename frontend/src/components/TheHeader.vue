<template>
    <header class="header">
        <h1 class="header__logo">
            <router-link :to="{ name: 'Main Page'}" class="header__logo-link">buyacar.com</router-link>
        </h1>
        <h2 class="header__motto">
            All cars for sale in the US
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
    background-color: $header-color;
    color: $white;
    display: flex;
    justify-content: space-around;
    align-items: center;
    padding: 24px 0;
    font-family: $logo-font;

    &__logo {
        font-size: 32px;
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
