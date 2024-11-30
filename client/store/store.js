import { defineStore } from 'pinia';
import upload from '../aws/upload';
import results from '../aws/results';

export const useStore = defineStore('store', {
  state: () => ({
    uploadId: "demo",
    result: null,
    image: ""
  }),
  actions: {
    setImage(image) {
        this.image = image
    },
    async fetchUpload(filename, image) {
        this.uploadId = await upload(filename, image);
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