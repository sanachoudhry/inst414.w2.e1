import json
target_actor = "Hugh Jackman"
ratings = [] #list of ratings

#open the ratings data
with open("/Users/sanachoudhry/Downloads/imdb_movies_1985to2022.json") as in_file:
    #each line in the file is a JSON item
    for line in in_file:
        #read this movie
        movie = json.loads(line)
        #iterate over each actor to see if it matches the target actor
        for actor in movie["actors"]:
            #if this movie has the target actor as a principal,
            #add its rating to the list
            if actor[1] == target_actor:
                ratings.append(movie["rating"]["avg"])
                break

#calculate average rating
x = sum(ratings) / len(ratings)
print(x)
