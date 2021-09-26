// Mobile Leaderboard ad template for AdSense (320x50)
<template>
    <div class="ad">
        <p class="ad__text">Your ad here</p>
    </div>
</template>

<script>
export default {
    name: 'AdMobileLeaderboard',
};
</script>

<style lang="scss" scoped>
.ad {
    width: 320px;
    height: 50px;
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
