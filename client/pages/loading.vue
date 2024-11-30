<template>
    <div class="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <h1 class="text-xl font-semibold mb-4">Processing...</h1>
      <div class="mt-9">
        <LoadingAnimation />
      </div>
      <p class="text-gray-500 mt-4">Please wait while we process your image.</p>
    </div>
</template>

<script>
    import LoadingAnimation from '../components/LoadingAnimation.vue';
    import { useStore } from '../store/store';

    export default {
        async mounted() {
            const store = useStore(); 
            console.log("Upload ID: ", store.uploadId);
            try { 
                const success = await store.pollResult();
                if (success) {
                    await navigateTo({ path: "/results"});
                } else {
                    await navigateTo({ path: "/"});
                }
            } catch(e) {
                throw e;
            }
        }
    }
</script>