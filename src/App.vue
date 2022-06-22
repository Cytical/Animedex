<template>
  <h2> This Season </h2>
  <hr class="solid">
  <div class="seasonal">
    <li v-for='index in 10' :key='index'>
      <AnimeInfo :number='index' category="seasonal" />
    </li>
  </div>
  <h2> Popular </h2>
  <hr class="solid">
  <div class="seasonal">
    <li v-for='index in 10' :key='index'>
      <AnimeInfo :number='index' category="most-popular" />
    </li>
  </div>
  <h2> Top Rated </h2>
  <hr class="solid">
  <div class="seasonal">
    <li v-for='index in 10' :key='index'>
      <AnimeInfo :number='index' category="top-rated" />
    </li>
  </div>


</template>

<script>
import AnimeInfo from "./components/AnimeInfo.vue";

export default {
  name: 'App',
  components: {
    AnimeInfo,
  }
}
</script>



<style scoped>

h2 {
  font-family: 'Montserrat', sans-serif;
  color: white;
  font-weight: bold;
  font-size: 26px;
  margin-bottom: 0px;
  padding-left: 20px;
}

hr.solid {
  border-top: 1px solid white;
  margin-bottom: -8px;
}
.seasonal {
  display: flex;
  overflow-x: scroll;
}

/* width */
::-webkit-scrollbar {
  width: 10px;
  height: 10px;
}

/* Track */
::-webkit-scrollbar-track {
  background: #f1f1f1;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: #888;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #555;
}

</style>