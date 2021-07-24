# Mónica Cordero 
# 05/14/2021
#Homework 2, Part 2




#PART TWO: Dictionaries

#Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 'location_name', 'latitude' and 'longitude'. Pick a tree from: https://en.wikipedia.org/wiki/List_of_trees

tree = {"name": "Acer nigrum", "species": "maple", 'age': 10 , "location_name": "southern Ontario", "latitude": 51.2538, "longitude": -85.3232}

# 2) Print the sentence "{name} is a {years} year old tree that is in {location_name}"

tree = {"name": "Acer nigrum", "species": "maple", "age": 10 , "location_name": "Southern Ontario", "latitude": 51.2538, "longitude": -85.3232}
print (tree["name"], "is a", tree["age"], "year old tree that is in", tree["location_name"])

# The coordinates of New York City are 40.7128° N, 74.0059° W. Check to see if the tree is south of NYC, and print "The tree {name} in {location} is south of NYC" if it is. If it isn't, print "The tree {name} in {location} is north of NYC"

tree = {"name": "Acer nigrum", "species": "maple", "age": 10 , "location_name": "Southern Ontario", "latitude": 51.2538, "longitude": -85.3232}
nyclat= 40.7128
if nyclat < tree["latitude"]:
    print ("The tree", tree["name"], "in", tree["location_name"], "is north of NYC")
else:
    print("The tree", tree["name"], "in", tree["location_name"], "is south of NYC")

# Ask the user how old they are. If they are older than the tree, display "you are {XXX} years older than {name}." If they are younger than the tree, display "{name} was {XXX} years old when you were born."
tree = {"name": "Acer nigrum", "species": "maple", "age": 10 , "location_name": "Southern Ontario", "latitude": 51.2538, "longitude": -85.3232}
user_age = input("How old are you.?")
user_age = int(user_age)
if user_age > tree["age"]:
    print("You are", (user_age -tree["age"]), "years older than", tree["name"])
elif user_age == tree["age"]:
    print("You are the same age than",tree["name"], ".")
else: 
    print(tree["name"], "was",(tree["age"]-user_age), "years old when you were born.")	

## PART TWO: Lists of dictionaries

## Make a list of dictionaries of five places across the world - (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago. Each dictionary should include each city's name and latitude/longitude (see note above).

### Moscou 37.0753° N, 37.3863° E | Tehran 35.6892° N, 51.3890° E | Falkland Islands 51.7963° S, 59.5236° W | Seoul  57.3600'' N, 127° 1' 28.6032'' E | Santiago  33.4489° S, 70.6693° W


## Loop through the list, printing each city's name and whether it is above or below the equator (How do you know? Think hard about the latitude.). When you get to the Falkland Islands, also display the message "The Falkland Islands are a biogeographical part of the mild Antarctic zone," which is a sentence I stole from Wikipedia.

world_places = [
	{"place":"Moscow","latitude":37.0753,"longitude":37.3863},
	{"place":"Tehran", "latitude":35.6892,"longitude":51.3890},
	{"place":"Falkland Islands","latitude":-51.7963,"longitude":-59.5236},
	{"place":"Seoul","latitude":57.3600,"longitude":28.6032},
	{"place":"Samtiago","latitude":-33.448,"longitude":-70.6693}
]
for item in world_places:
	if item["latitude"] < 0: 
		print(item["place"], "is above the Ecuador.")
	elif item["latitude"] < 0:
		print(item["place"], "is below the Ecuador.")
	if item ["latitude"] == -51.7963:
		print(item["place"], "The Falkland Islands are a biogeographical part of the mild Antarctic zone.")

## 3) Loop through the list, printing whether each city is north of south of your tree from the previous section.

for item in world_places: 
	if item ["latitude"] < tree{"latitude"}:
		print (item["place"], "is south of tree called", tree["name"], "in", tree["location_name"], "Canada.")
	elif item ["latitude"] > tree{"latitude"}:
		print (item["place"], "is north of tree called", tree["name"], "in", tree["location_name"], "Canada.")


		




 