<template>
    <div class="gallery-hover">
        <div class="gallery-hover__cover-container">
            <img class="gallery-hover__cover" :src="coverSrc">
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
                @mouseover="mouseOver(photo)"
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
        placeholderUrl: {
            type: String,
        },
    },
    data() {
        return {
            currentHoverPhoto: null,
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
        mouseOver(photo) {
            this.currentHoverPhoto = photo;
        },
        mouseLeave() {
            this.currentHoverPhoto = null;
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
        width: 100%;
        height: 150px;
    }

    &__cover {
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        width: 100%;
        max-height: 100%;
        object-fit: contain;
        border-radius: 8px;
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
