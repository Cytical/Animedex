<template>
    <div class="header">
        <a href="#/" class="logo">
            <img src="../assets/Logo.png">
        </a>
        <div class="header-right">
            <a class="active" href="#/">Home</a>
            <a href="#about">About</a>
        </div>
    </div>
</template>

<style scoped>
* {
    box-sizing: border-box;
}
.logo {
    color: white;
    margin-top: -10px;
    margin-bottom: 0px;
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
}



.header-right a:hover {
    background-color: #ddd;
    color: black;
}

.header-right a.active {
    background-color: #E50914;
    color: white;
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