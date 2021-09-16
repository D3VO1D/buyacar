<template>
    <div class="loader-container">
        <div class="lds-ring">
            <div></div>
            <div></div>
            <div></div>
            <div></div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'BaseLoader',
};
</script>

<style lang="scss" scoped>
.loader-container {
    width: 100%;
}

.lds-ring {
    position: relative;
    width: 80px;
    height: 80px;
    margin: 0 auto;

    div {
        box-sizing: border-box;
        display: block;
        position: absolute;
        width: 60px;
        height: 60px;
        margin: 8px;
        border: 8px solid #f0f0f0;
        border-radius: 50%;
        animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
        border-color: #f0f0f0 transparent transparent transparent;

        &:nth-child(1) {
            animation-delay: -0.45s;
        }

        &:nth-child(2) {
            animation-delay: -0.3s;
        }

        &:nth-child(3) {
            animation-delay: -0.15s;
        }
    }
}

@keyframes lds-ring {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
}
</style>
