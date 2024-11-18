<template>
    <div class="container">
      <h1>Welcome to My Nuxt 3 App!</h1>
      <p>This is the homepage.</p>
      
      <!-- Example of data binding -->
      <p>{{ message }}</p>
      
      <!-- Example of method usage -->
      <button @click="changeMessage">Change Message</button>
    </div>
  </template>
  
  <script setup>
  // Composition API (Vue 3)
  
  // Reactive state
  import { ref } from 'vue';
  
  const message = ref('Hello, Nuxt 3!');
  
  // Method to update message
  const changeMessage = () => {
    message.value = 'You clicked the button!';
  };
  </script>
  
  <style scoped>
  .container {
    text-align: center;
    margin-top: 50px;
  }
  
  h1 {
    font-size: 2em;
    color: #2c3e50;
  }
  
  button {
    margin-top: 20px;
    padding: 10px 20px;
    font-size: 1em;
    background-color: #3498db;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #2980b9;
  }
  </style>
  