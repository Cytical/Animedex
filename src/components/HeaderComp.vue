<template>
    <div class="header">
        <a href="#/" class="logo">
            <img src="../assets/logo.png">
        </a>
        <div class="header-right" v-if="page == 'home'">
            <a class="active" href="#/">Home </a>
            <a class="inactive" href="#about">About</a>
        </div>
        <div class="header-right" v-if="page == 'about'">
            <a class="inactive" href="#/">Home </a>
            <a class="active" href="#about">About</a>
        </div>
    </div>
</template>

<script>
export default {
    name: 'HeaderComp',
    props: {
        page: String,
        },
}
</script>

<style scoped>




* {
    box-sizing: border-box;
}
@media (min-width: 1200px) {
    .logo {
        margin-top: -10px;
        margin-bottom: 0px;
    }
}
@media (max-width: 1200px) {
    .logo {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 50%;
        }
}

body {
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
}

.header {
    overflow: hidden;
    background-color: black;
    margin-bottom: -20px;
}

.header a {
    float: left;
    color: white;
    text-align: center;
    padding: 12px;
    text-decoration: none;
    font-size: 18px;
    line-height: 25px;
    border-radius: 4px;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}



.header-right a:hover {
    background-color: #ddd;
    color: black;
}

.header-right a.active {
    background-color: #E50914;
    color: white;
    text-align: center;
}

.header-right a.inactive {
    text-align: center;
}

.header-right {
    float: right;
}

@media screen and (max-width: 500px) {
    .header a {
        float: none;
        display: block;
        text-align: left;
    }

    .header-right {
        float: none;
    }
}
</style>
