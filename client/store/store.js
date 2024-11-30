import { defineStore } from 'pinia';
import upload from '../aws/upload';
import results from '../aws/results';

export const useStore = defineStore('store', {
  state: () => ({
    uploadId: null,
    result: null,
    image: "",
    ext: ""
  }),
  actions: {
    setImage(image, ext) {
        this.image = image;
        this.ext = ext;
    },
    async fetchUpload(ext, image) {
        this.uploadId = await upload(ext, image);
    },
    async pollResult() {
        if (!this.uploadId) {
            throw new Error("No upload ID")
        }
        const maxAttempts = 40;
        const delay = 5000;
        let attempts = 0;

        await new Promise((resolve) => setTimeout(resolve, 30000)); 
        while (attempts < maxAttempts) {
            this.result = await results(this.uploadId);
            if (this.result) {
                console.log(this.result);
                return true;
            }
            attempts++;
            await new Promise((resolve) => setTimeout(resolve, delay)); 
        }
        return false; 
    }
  },
});