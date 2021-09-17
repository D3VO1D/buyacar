<template>
    <footer class="footer">
        <ul class="footer__section">
            <li>
                We gathered all cars for sale in the US market to allow you easily find the best car to buy.
            </li>
        </ul>
        <hr class="footer__section-divider"/>
        <ul class="footer__section">
            <li>
                @ 2021 buyacar.com
            </li>
            <li>
                info@name.com
            </li>
            <li>
                <font-awesome-icon class="footer__icon" :icon="['fas', 'phone-alt']" />
                <span>+7 495 755-55-77</span>
            </li>
        </ul>
    </footer>
</template>

<script>
export default {
    name: 'TheFooter',
};
</script>

<style lang="scss" scoped>
@import '@/_vars';

.footer {
    display: flex;
    flex-direction: column;
    gap: 12px;
    background-color: $footer-color;
    color: $footer-text-color;
    padding: 24px 10%;
    font-family: $logo-font;

    flex-shrink: 0;

    &__section {
        list-style-type: none;
        display: flex;
        gap: 16px;
        justify-content: space-around;
        margin: 20px 0;
        font-size: 18px;
    }

    &__section-divider {
        margin: 12px 5%;
        background-color: $divider-color;
        color: $divider-color;
        height: 1px;
        border: none;
    }

    &__icon {
        margin-right: 12px;
    }
}

</style>
