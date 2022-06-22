<template>
  <HeaderComp/>
  <router-view/>
</template>

<script>
import HeaderComp from './components/HeaderComp.vue'
export default {
  name: 'App',
  components: {
    HeaderComp,
  }
}
</script>
 
<style>

/* width */
::-webkit-scrollbar {
  width: 10px;
}

/* Track */
::-webkit-scrollbar-track {
  background: black;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: #E50914;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #555;
}
  
 
</style>
