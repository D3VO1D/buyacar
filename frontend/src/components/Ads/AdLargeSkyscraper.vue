// Large Skyscraper ad template for AdSense (300x600)
<template>
    <div class="ad">
        <p class="ad__text">Your ad here</p>
    </div>
</template>

<script>
export default {
    name: 'AdLargeSkyscraper',
};
</script>

<style lang="scss" scoped>
.ad {
    width: 300px;
    height: 600px;
    position: relative;
    background-color: lightgrey;

    &:hover {
        cursor: pointer;
    }

    &__text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 24px;
    }
}
</style>
