<template>
  <HeaderComp page='home' />
  <h2> Recommended </h2>
  <hr class="solid">
  <div class="shows">
    <li v-for='index in 10' :key='index'>
      <AnimeInfo :number='recommended_ids[index]' />
    </li>
  </div>
  <h2> Popular </h2>
  <hr class="solid">
  <div class="shows">
    <li v-for='index in 10' :key='index'>
      <AnimeInfo :number='popular_ids[index + 1]' />
    </li>
  </div>
  <h2> This Season </h2>
  <hr class="solid">
  <div class="shows">
    <li v-for='index in 8' :key='index'>
      <AnimeInfo :number='seasonal_ids[index + 1]' />
    </li>
  </div>
  <h2> Top Rated </h2>
  <hr class="solid">
  <div class="shows">
    <li v-for='index in 10' :key='index'>
      <AnimeInfo :number='toprated_ids[index + 1]' />
    </li>
  </div>
</template>

<script>
import AnimeInfo from "../components/AnimeInfo.vue";
import HeaderComp from '../components/HeaderComp.vue';

//Fisher-Yates Shuffle
function shuffle(array) {
  let currentIndex = array.length, randomIndex;

  // While there remain elements to shuffle.
  while (currentIndex != 0) {

    // Pick a remaining element.
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;

    // And swap it with the current element.
    [array[currentIndex], array[randomIndex]] = [
      array[randomIndex], array[currentIndex]];
  }

  return array;
}

export default {
    name: 'HomePage',
    components: {
        AnimeInfo,
        HeaderComp,
      },
    data() {
      return {
        recommended_ids: shuffle([22319, 19815, 121, 6702, 9919, 3588, 2904, 2167, 2001, 6746,
          30276, 21881, 8074, 11111, 1735, 20507, 13601, 18679, 21, 22199,
          1, 5081, 199, 9989, 9756, 30, 10793, 4181, 10087, 6880,]),
        seasonal_ids: shuffle([50265, 40356, 43608, 45613, 50631, 49520, 47194, 41461, 50380, 48760, 50175,]),
        popular_ids: shuffle([1535, 16498, 11757, 5114, 6547, 1575, 20, 9253, 10620, 4224, 269, 226, 22319, 19815, 121,]),
        toprated_ids: shuffle([5114, 28977, 9253, 38524, 11061, 820, 39486, 42938, 35180, 28851, 37987, 4181, 2904,]),
      }
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
  border-top: 2px solid white;
  margin-bottom: -12px;
}
.shows {
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

@media (max-width: 1200px) {
  h2 {
    padding-top: 20px;
    text-align: center;
  }
}
</style>