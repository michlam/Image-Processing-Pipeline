<template>
    <div class="grid grid-cols-4 gap-16 -ml-10 -mt-10">
        <div class="relative">
            <div class="base-circle border border-gray-200"></div>
            <div
                class="coloured-spin border border-cyan-500">
            </div>
        </div>

        <div class="relative">
            <div class="base-circle border-2 border-gray-200"></div>
            <div
                class="coloured-spin border-2 border-indigo-500">
            </div>
        </div>

        <div class="relative">
            <div class="base-circle border-4 border-gray-200"></div>
            <div
                class="coloured-spin border-4 border-pink-500">
            </div>
        </div>
        <div class="relative">
            <div class="base-circle border-8 border-gray-200"></div>
            <div
                class="coloured-spin border-8 border-green-500">
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'LoadingAnimation',
    };
</script>

<style scoped>
    .coloured-spin {
        @apply w-12 h-12 rounded-full animate-spin absolute border-t-transparent border-solid;
    }
    .base-circle {
        @apply w-12 h-12 rounded-full absolute border-solid;
    }
</style>