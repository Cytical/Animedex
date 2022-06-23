<template>
    <HeaderComp page='home' />
    <div class="container">
        <div class="title-container">
            <div class="title"> {{ anime.title }} </div>
            <div class="type"> &nbsp; &nbsp; {{anime.type}} </div>
            <div class="date"> &nbsp; &nbsp; {{anime.season}} {{anime.year}}</div>
        </div>
        <div class="image-container">
            <a :href="anime.url">
                <img class="image" :src="anime.images" :alt="anime.title" width="350" height="500" />
            </a>
        </div>
        <div class="info-container">
            <h3> Synopsis: </h3>
            <div class="synopsis"> {{ anime.synopsis }}</div>
            <div class="genre"> Genres: </div>
            <div class="genre-list" v-for='genre in anime.genres' :key='genre.mal_id'>
                <a :href="genre.url">
                    {{genre.name}},
                </a>
            </div>
            <div class="theme"> Themes: </div>
            <div class="theme-list" v-for='theme in anime.themes' :key='theme.mal_id'>
                <a :href="theme.url">
                    {{theme.name}},
                </a>
            </div>
        </div>
        <div class="stats-container">
            <div class="rating-container">
                <div class="score">{{anime.score + ' ⭐'}}</div>
                <div class="rank">Ranked #{{anime.rank}}</div>
            </div>
            <div class="popularity-container">
                <div class="members">{{anime.members + ' 👥'}}</div>
                <div class="rank2">Popularity #{{anime.popularity}}</div>
            </div>
            <div class="button">
                <a :href="anime.trailer.url">
                    <button class="trailer"> Watch Trailer </button>
                </a>
            </div>
        </div>
    </div>
</template>


<script>
import HeaderComp from '../components/HeaderComp.vue';
import axios from "axios";
export default {
    components: {
        HeaderComp,
    },
    props: [
        'id'
    ],
    data() {
        return {
            anime : [],
        }
    },

    async created() {

    try {
        var anime_id = this.id;
        const response = await axios.get('https://api.jikan.moe/v4/anime/' + anime_id);
        this.anime = response.data.data;
        var temp = JSON.stringify(this.anime.images).split("large_image_url")[2];
        var image_url = temp.slice(3, temp.length - 3)
        this.anime.images = image_url
    } catch (err) {
        console.error(err);
    }
}
};

</script>

<style scoped>

a:link,
a:visited,
a:hover,
a:active {
    font-weight: bold;
    color: gray;
    text-decoration: none;
}
@media (min-width: 1200px) {
    .title {
        font-family: 'Roboto', sans-serif;
        font-size: 36px;
        font-weight: bold;
        text-align: left;
        margin-top: -6%;
        margin-bottom: 5%;
    }

    .type{
        font-family: 'Roboto', sans-serif;
        font-size: 28px;
        font-weight: bold;
        text-align: right;
        margin-top: -6%;
        margin-bottom: 5%;
        color: gray;
    }
    .date {
        font-family: 'Roboto', sans-serif;
        font-size: 28px;
        font-weight: bold;
        text-align: right;
        margin-top: -6%;
        margin-bottom: 5%;
        color: gray;
    }

    .genre {
        font-size: 18px;
        font-weight: bold;
        padding-right: 8px;
        padding-top: 3%;
        float: left;
    }
    .theme {
        font-size: 18px;
        font-weight: bold;
        padding-right: 8px;
        padding-left: 10px;
        padding-top: 3%;
        float: left;
    }
    .genre-list {
        color: gray;
        font-size: 18px;
        padding-right: 8px;
        padding-top: 3%;
        float: left;
    }
    .theme-list {
        color: gray;
        font-size: 18px;
        padding-right: 8px;
        padding-top: 3%;
        float: left;
    }


    .title-container {
        padding-left: 0%;
        margin-bottom: -2%;
        display: flex;
    }

    .container {
        margin-top: 5%;
        margin-left: 15%;
        margin-right: 15%;

    }

    .image-container {
        width: 50%;
        float: left;
        margin-right: -15%;
    }

    .info-container {
        margin-top: -4%;
        margin-left: 40%;
        width: 50%;
        text-align: justify;
        font-family: Arial, Helvetica, sans-serif;
    }

    .stats-container {
        width: 100%;
        float: left;
    }


    .rating-container {
        margin-top: 5%;
        margin-right: -15%;
        width: 18%;
        float: left;
    }

    .score {
        font-family: 'Roboto', sans-serif;
        font-size: 24px;
        font-weight: bold;
        text-align: left;
        color: white;
        padding-left: 5px;
    }

    .rank {
        padding-top: 5px;
        text-align: left;
    }
    .rank2 {
        padding-left: 5px;
        padding-top: 5px;
        text-align: left;
    }

    .popularity-container {
        margin-top: 5%;
        margin-left: 18%;
        float: left;
    }

    .members {
        font-family: 'Roboto', sans-serif;
        font-size: 24px;
        font-weight: bold;
        text-align: left;
        color: white;
        padding-left: 5px;
    }

    div {
        color: white;
    }

    .button {
        margin-top: 5%;
        margin-left: 18%;
        float: left;
    }
    .trailer {
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        margin: 4px 2px;
        cursor: pointer;
        background-color: #E50914;
        border: none;
        color: white;
        font-size: 20px;
        font-weight: bold;
    }
}



@media (max-width: 1200px) {
    .container {
        flex-direction: column;
    }
    .title {
        font-family: 'Roboto', sans-serif;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-top: -6%;
        margin-bottom: 5%;
    }

    .type, .date {
        color: black;
    }

    .title-container {
        margin-top: 40px;
        margin-bottom: -15px;
        flex: 100%;
    }

    .container {
        margin-top: 20px;
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        
    }

    .image-container {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

    .info-container {
        margin-top: 20px;
        text-align: center;
        font-family: Arial, Helvetica, sans-serif;
        flex: 100%;
    }

    .genre {
        margin-top: 10px;
        font-weight: bold;
    }

    .genre-list {
        color: gray;
        font-size: 18px;
        padding-top: 3%;
    }

    .theme {
        margin-top: 10px;
        font-weight: bold;
    }

    .theme-list {
        color: gray;
        font-size: 18px;
        padding-top: 3%;
    }

    .stats-container {
        margin-top: 10px;
        flex: 100%;
        text-align: center;
    }

    .score {
        font-family: 'Roboto', sans-serif;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        color: white;
        padding-left: 5px;
    }

    .rank {
        padding-top: 5px;
        text-align: center;
    }

    .rank2 {
        padding-top: 5px;
        text-align: center;
    }
    .members {
        padding-top: 16px;
        font-family: 'Roboto', sans-serif;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        color: white;
    }

    .button{
        padding-top: 20px;
        text-align: center;
        flex: 100%;
    }
    .trailer {
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        margin: 4px 2px;
        cursor: pointer;
        background-color: #E50914;
        border: none;
        color: white;
        font-size: 20px;
        font-weight: bold;
    }
    div {
        color: white;
    }
}
</style>
