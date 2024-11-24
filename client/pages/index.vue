<template>
  <div class="min-h-screen bg-gray-100 flex flex-col items-center justify-center px-4">
    <!-- Breadcrumb/Title -->
    <nav class="text-sm text-gray-500 mb-4">
      <span class="font-medium">Home</span> › License Plate Recognition
    </nav>
    <h1 class="text-3xl font-bold text-gray-800 mb-6">Upload and Recognize License Plates</h1>

    <!-- Upload Area -->
    <div
      class="relative w-full max-w-xl bg-purple-200 border-dashed border-2 border-purple-400 rounded-lg p-6 flex flex-col items-center justify-center text-center hover:bg-purple-300"
      @click="triggerFileInput"
      @dragover.prevent="handleDragOver"
      @dragleave.prevent="handleDragLeave"
      @drop.prevent="handleDrop"
      :class="{
        'bg-purple-300': isDragOver
      }"
    >
    <input
        ref="fileInput"
        type="file"
        accept="image/*"
        class="hidden"
        @change="onFileChange"
      />
      
      <div class="flex flex-col items-center justify-center text-center" v-if="!imagePreviewUrl">
        <div class="mb-3">
          <img src="public/image-icon.svg"/>
        </div>
        <div>
          <button
            class="bg-white text-purple-500 px-4 py-2 font-semibold rounded-md shadow-md hover:bg-purple-100 mb-2 flex items-center"
          >
            <div style="width:24px;height:24px">
              <img src="public/upload-icon.svg" alt="Upload Icon" class="h-full w-full" />
            </div>
            <span class="ml-1">CHOOSE IMAGES</span>
          </button>
        </div>
        <p class="text-sm text-gray-700">or drag and drop your images here</p>
      </div> 
      
      <!-- Image Preview Section -->
      <div v-if="imagePreviewUrl" class="mt-6 text-center" >
        <!-- <p class="text-gray-600 mb-4">Image Preview:</p> -->
         <!-- Close Button -->
        <button
          @click="removeImage"
          class="absolute top-2 left-2 bg-white text-gray-700 border border-gray-300 rounded-full h-8 w-8 flex items-center justify-center shadow-md hover:bg-gray-100"
          title="Remove Image"
        >
          ✕
        </button>
        <img
          :src="imagePreviewUrl" v-if="imagePreviewUrl"
          alt="Preview"
          class="max-w-full h-64 object-contain rounded-md shadow-md"
        />
      </div>
    </div>


    <!-- Description Section -->
    <div class="mt-6 text-center">
      <p class="text-gray-600">
        Upload images of license plates to extract plate numbers and other information.
        Ensure the license plate is clear for accurate recognition.
      </p>
      <!-- <ul class="mt-4 text-sm text-gray-700 text-left list-disc mx-auto w-full max-w-md">
        <li>Process images quickly and securely.</li>
        <li>Drag and drop functionality for ease of use.</li>
        <li>No image storage—processing is done in real-time.</li>
      </ul> -->
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedFile: null,
      imagePreviewUrl: "",
      isDragOver: false
    };
  },
  methods: {
    triggerFileInput() {
      this.$refs.fileInput.click();
    },
    handleDrop(event) {
      event.preventDefault();
      const file = event.dataTransfer.files[0];
      this.selectedFile = file;
      this.createImagePreview(file);
      this.handleDragLeave();
    },
    handleDragOver() {
      this.isDragOver = true;
    },
    handleDragLeave() {
      this.isDragOver = false;
    },
    onFileChange: function (event) {
      const file = event.target.files[0];
      if (!file) {
        return false;
      }
      if (!file.type.match('image.*')) {
        return false;
      }
      this.selectedFile = file;
      this.createImagePreview(file);
    },
    createImagePreview(file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        this.imagePreviewUrl = e.target.result;
      };
      reader.readAsDataURL(file); // Convert file to data URL for preview
    },
  },
};
</script>

<style scoped>
/* Add any additional styles here */
</style>
