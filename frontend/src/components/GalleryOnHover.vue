<template>
    <div class="gallery-hover">
        <div class="gallery-hover__cover-container">
            <img class="gallery-hover__cover" :src="coverSrc">
            <div class="gallery-hover__cover-more-photos" v-if="showMorePhotos">
                <div class="gallery-hover__cover-wrapper">
                    <div class="gallery-hover__wrapper-icon"></div>
                    <div class="gallery-hover__wrapper-text">{{ totalPhotos - photos.length }} more photos</div>
                </div>
            </div>
        </div>
        <div
            class="gallery-hover__button-container"
            v-if="photos.length > 1"
            @mouseleave="mouseLeave"
        >
            <div
                class="gallery-hover__button"
                v-for="(photo, index) in photos"
                :key="index"
                @mouseover="mouseOver(photo, index)"
            >
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'GalleryOnHover',
    props: {
        photos: {
            type: Array,
        },
        totalPhotos: {
            type: Number,
        },
        placeholderUrl: {
            type: String,
        },
    },
    data() {
        return {
            currentHoverPhoto: null,
            showMorePhotos: false,
        };
    },
    computed: {
        coverSrc() {
            if (this.currentHoverPhoto) {
                return this.currentHoverPhoto;
            }
            return this.photos.length > 0 && this.photos[0] !== ''
                ? this.photos[0]
                : this.placeholderUrl;
        },
    },
    methods: {
        mouseOver(photo, index) {
            this.currentHoverPhoto = photo;
            this.showMorePhotos = (index === this.photos.length - 1 && this.totalPhotos > this.photos.length);
        },
        mouseLeave() {
            this.currentHoverPhoto = null;
            this.showMorePhotos = false;
        },
    },
};
</script>

<style lang="scss" scoped>
@import '@/_vars';

.gallery-hover {
    position: relative;

    &__cover-container {
        position: relative;
        height: 150px;
        overflow: hidden;
        border-radius: 8px;
    }

    &__cover {
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        width: 100%;
        max-height: 100%;
        object-fit: contain;
    }

    &__cover-more-photos {
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        text-align: center;
        color: #fff;
        background-color: rgba(0, 0, 0, .5);
    }

    &__cover-wrapper {
        position: absolute;
        top: 50%;
        left: 50%;
        text-align: center;
        transform: translate(-50%,-50%);
    }

    &__wrapper-icon {
        width: 54px;
        height: 46px;
        margin: 0 auto;
        background: url("data:image/svg+xml;charset=utf-8,%3Csvg width='54' height='46' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='%23FFF' fill-rule='evenodd'%3E%3Cpath d='M51.195 42.884C50.535 43.624 49.46 44 48 44H6c-1.46 0-2.535-.376-3.196-1.116C1.817 41.778 2 40.011 2 40v-2l-.003-23.078c-.002-.017-.113-1.719.934-2.844C3.596 11.363 4.63 11 6.001 11h7l.1-.006c.105-.01 2.585-.288 3.781-2.523.927-1.733 2.932-4.888 2.93-4.888C19.86 3.518 20.99 2 23 2h8c2.01 0 3.14 1.518 3.188 1.583-.002 0 2.003 3.155 2.93 4.888 1.196 2.235 3.675 2.513 3.78 2.523L41 11h7c1.371 0 2.403.363 3.07 1.078 1.045 1.125.934 2.827.933 2.844L52 38v2c.001.011.183 1.778-.805 2.884m1.355-32.149C51.491 9.585 49.96 9 48 9h-6.936c-.242-.037-1.549-.288-2.182-1.472-.966-1.804-2.955-4.933-3.039-5.065C35.746 2.323 34.065 0 31 0h-8c-3.066 0-4.746 2.323-4.844 2.463-.084.132-2.073 3.261-3.038 5.065-.633 1.184-1.94 1.435-2.183 1.472H6c-1.96 0-3.492.584-4.55 1.735C-.19 12.516.026 14.702 0 15v24.95c.041.62-.154 2.605 1.295 4.246C2.351 45.393 3.935 46 6 46h42c2.065 0 3.648-.607 4.704-1.804 1.45-1.64 1.254-3.626 1.296-4.247V15c-.028-.298.19-2.484-1.45-4.265'/%3E%3Cpath d='M27 16c-5.514 0-10 4.486-10 10s4.486 10 10 10 10-4.486 10-10-4.486-10-10-10m0 22c-6.617 0-12-5.383-12-12s5.383-12 12-12 12 5.383 12 12-5.383 12-12 12'/%3E%3C/g%3E%3C/svg%3E");
    }

    &__wrapper-text {
        font-size: 13px;
        line-height: 17px;
        margin-top: 13px;
        color: #fff;
    }

    &__button-container {
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        display: flex;
        z-index: 1000;
    }

    &:not(:hover) &__button {
        opacity: 0;
    }

    &__button {
        position: relative;
        flex: 1;
        min-height: 8px;
        opacity: 1;

        &:after {
            position: absolute;
            bottom: 8px;
            right: 1px;
            left: 1px;
            height: 3px;
            content: "";
            background: $whitish;
        }

        &:hover:after {
            background-color: $accent-color;
        }
    }
}
</style>
