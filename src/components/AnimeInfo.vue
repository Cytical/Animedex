<template>
    <div class="container">
        <a :href="anime.url">
            <img class="image" :src="anime.images" :alt="anime.title" width="280" height="400" />

            <div class="overlay">
                <div class="title">
                    {{anime.title}}
                </div>
                <div class="ratings">
                    {{ anime.score + '⭐' }}
                </div>
                <div class="type">
                    {{anime.year}}
                </div>
            </div>
        </a>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: 'AnimeInfo',
    props: {
        number: Number,
        category: String,
    },
    data() {
        return {
        anime : [],
        };
    },

    async created() {
        function sleep(milliseconds) {
            var start = new Date().getTime();
            for (var i = 0; i < 1e7; i++) {
                if ((new Date().getTime() - start) > milliseconds) {
                    break;
                }
            }
        }

        try {
            console.log(typeof this.number)
            sleep(100);
            var valid_ids;
            if (this.category == "seasonal") {
                valid_ids = ["filler", 50265, 40356, 43608, 45613, 50631, 49520, 47194, 41461, 50380, 48760, 50175, ]
            }
            else if (this.category == "most-popular") {
                valid_ids = ["filler", 1535, 16498, 11757, 5114, 6547, 1575, 20, 9253, 10620, 4224, 269, 226, 22319, 19815, 121, ]
            }
            else if (this.category == "top-rated") {
                valid_ids = ["filler", 5114, 28977, 9253, 38524, 11061, 820, 39486, 42938, 35180, 28851, 37987, 4181, 2904, ]
            }
            var anime_id = valid_ids[this.number];
            console.log(this.category, anime_id);
            const response = await axios.get('https://api.jikan.moe/v4/anime/' + anime_id);
            this.anime = response.data.data;
            var temp = JSON.stringify(this.anime.images).split("large_image_url")[2];
            var image_url = temp.slice(3, temp.length - 3)
            this.anime.images = image_url 
            sleep(100);
        } catch(err) {
            //alert("Too many requests please wait...");
            console.error(err);
        }
}
};

</script>

<style scoped>

h2 {
    text-align: center;
}
.container {
    position: relative;
    width: 100%;
}

.image {
    opacity: 1;
    display: block;
    padding-left: 3px;
    padding-right: 3px;
    transition: .5s ease;
    backface-visibility: hidden;
}

.overlay {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    opacity: 0;
    transition: .5s ease;
}

.container:hover .overlay {
    opacity: 1;
}

.container:hover .image {
    opacity: 0.3;
}

.title {
    font-family: 'Montserrat', sans-serif;
    color: white;
    font-weight: bold;
    font-size: 20px;
    position: absolute;
    top: 30%;
    left: 50%;
    padding-bottom: 160px;
    -webkit-transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    text-align: center;
}

.ratings {
    font-family: 'Montserrat', sans-serif;
    color: white;
    font-size: 18px;
    position: absolute;
    top: 50%;
    left: 50%;
    padding-top: 100px;
    -webkit-transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    text-align: center;
}

.type {
    font-family: 'Montserrat', sans-serif;
    color: white;
    font-size: 18px;
    position: absolute;
    top: 50%;
    left: 50%;
    padding-bottom: 300px;
    -webkit-transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    text-align: center;
}
</style>