<template>
  <div id="app">
    <DersListesi/>
  </div>
</template>

<script>
import DersListesi from './components/DersListesi.vue';

export default{
  components: {
    DersListesi
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
