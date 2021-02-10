<template>
  <div class="hello">
    <h1>{{ msg }}</h1>

    <button @click="SelectKnight()">Select a Knight</button>
    <p>
      {{knight}}
    </p>
    
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'HelloWorld',
  data() {
      return {
          names: null,
          knight: null,
          msg: 'Welcome to the Heseltime Knights Standard App',
      }
  },
  mounted: function() {
    this.FetchData();
  },
  methods: {
      FetchData: function() {
          var app = this;
          axios.get(process.env.API_URL + "/standard_api").then(response => {
              app.names = response.data.names;
          });
      },
      SelectKnight: function() {
        var knight = this.names[Math.floor(Math.random()*this.names.length)];
        this.knight = knight;
      },
  }
}
</script>
<style>
</style>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
