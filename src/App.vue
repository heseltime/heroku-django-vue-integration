<template>
  <div id="app">
    <font-awesome-icon id="header_icon" icon="chess-knight" />
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'Knights Standard App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#header_icon {
  font-size: 4em;
}
</style>
