<template>
  <div class="hello">
    <h1 class="special">{{ version }}</h1>

    <h1>{{ msg }}</h1>

    <h2>{{ msg2 }}</h2>

    <p>Here's some API-driven functionality:</p>

    <button @click="SelectKnight()">Select a Knight</button>
    <p>
      {{knight}}
    </p>

    <p class="special">This is a base template for api-consuming Vue-SPAs using Axios. Comes with Fontawesome.</p>

    <a href="https://github.com/heseltime/heroku-django-vue-integration/blob/master/README.md" alt="Read Me Link" class="special">@Heselti.me</a>
    
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
          msg: 'Standard Template',
          msg2: 'Django and Vue Integration on Heroku Deployment',
          version: 'Knights',
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
h1 {
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
.special {
  font-size: 3em;
  font-style: italic;
  font-weight: 800;
}
</style>
