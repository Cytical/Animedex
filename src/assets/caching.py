import json
import requests


ids = [22319, 19815, 121, 6702,
9919, 3588, 2904, 2167, 2001, 6746, 30276, 21881, 8074, 11111, 1735, 20507, 13601, 18679, 21, 22199, 1, 5081, 199, 9989, 9756, 30, 10793, 4181, 10087, 6880, 50265, 40356, 43608, 45613, 50631, 49520, 47194, 41461, 50380, 48760, 50175, 1535, 16498, 11757, 5114, 6547, 1575, 20, 9253, 10620, 4224, 269, 226, 22319, 19815, 121, 5114, 28977, 9253, 38524, 11061, 820, 39486, 42938, 35180, 28851, 37987, 4181, 2904 ]

count = 0 

#r = requests.get("https://api.jikan.moe/v4/anime/20").json()
#print(f"{{ image: {r['data']['images']['webp']['large_image_url']} , title: {r['data']['title']} , type: {r['data']['type']} , score: {r['data']['score']} }}\n")


f = open("src/assets/cache.txt", "w", encoding="utf-8")
f.write("const anime_ids = {\n")
for id in list(set(ids)):
    r = requests.get(f"https://api.jikan.moe/v4/anime/{id}").json()
    temp_str = (
        f"'{id}' : {{ 'image': '{r['data']['images']['webp']['large_image_url']}' , 'title': '{r['data']['title']}' , 'year': '{r['data']['year']}' , 'type': '{r['data']['type']}', 'score': '{r['data']['score']}' }},\n")
    f.write(temp_str)
    print(id)
f.write("}")
f.close()
print("DONE")




