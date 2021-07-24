

# When run from the command line, this file should prompt the user for their year of birth, and print out (approximately):

# Ask when they were born
year = input("What year were you born? ")
year = int(year)

if int(year) >= 2022:
    year = input("Are you from the future or what? Please enter you REAL year of birth! ")
year = int(year)

age = 2021 - year

# or make a variable for minutes in a year, because you use it for every animal
min_per_year = 60 * 24 * 365


beats = 80 * min_per_year * age

print("You heart has beaten", beats, "times in your lifetime.")

print(f"Your heart has beaten {beats:,} times since birth.")

# How many times a blue whale's heart has beaten
# How many times a rabbit's heart has beaten
# If the answer to rabbit heartbeats is more than a million, say "XXX million" instead of the very long raw number

rabbeats = 220 * min_per_year * age

if rabbeats > 1000000: 
    rabbeats_m = round(rabbeats / 1000000)
    print(f"A rabbit's heart has beaten {rabbeats_m:,} million times.")
else:
    print(f"A rabbit's heart has beaten {rabbeats:,} times.")


# How old they are in Venus years
# How old they are in Neptune years
# Whether they are the same age as you, older or younger
#  If older or younger, how many years difference
#  If they were born in an even or odd year
# How many times there has been a president from the Democratic Party in office since they were born (1960 onward, and each president only counts once)
# Which US President was in office when they were born (1960 onward)
# If someone says they were born in the future, try asking them again (assume they'll do it right the second time).


# range(1960, 1963) => list([1960, 1961, 1962]) => [1960, 1961, 1962]
# "if you were born in any of the years between 1960 and 1963"
# elif 1963 <= year <= 1969:
# "I want year to be between 1963 and 1969"
# "If the year is greater than 193 and less than 1969"

if year < 1960:
    print("You're too old for this game!")
elif year in range(1960,1963):
    print("JFK")
elif 1963 <= year < 1969:
    print("LBJ")
elif year >= 1969 and year < 1975:
    print("Nixon")
elif year in list(range(1975,1977)):
    print("Ford")
elif year in list(range(1977,1981)):
    print("Carter")
elif year in list(range(1981,1989)):
    print("Reagan")
elif year in list(range(1989,1993)):
    print("Bush")
elif year in list(range(1993,2001)):
    print("Clinton")
elif year in list(range(2001,2009)):
    print("Bush")
elif year in list(range(2009,2017)):
    print("Obama")
elif year in list(range(2017,2021)):
    print("Trump")
else:
    print("Biden")



if year >= 2021:
    print("Biden")
elif year >= 2016:
    print("Trump")
elif year >= 2008:
    print("Obama")
elif year >= 2001:
    print("George W. Bush")
elif year >= 1993:
    print("Bill Clinton")
elif year >= 1989:
    print("George H.W. Bush")
elif year >= 1981:
    print("Reagen")
elif year >= 1977:
    print("Carter")
elif year >= 1975:
    print("Ford")
elif year >= 1969:
    print("Nixon")
elif year >= 1963:
    print("LBJ")
elif year >= 1960:
    print("JFK")
else: 
    print("Sorry, this game is not intended for you.")


if year >= 1960:
    print("JFK")
elif year >= 1963:
    print("LBJ")
elif year >= 1969:
    print("Nixon")




presidents = {
    'Dwight D. Eisenhower': [1960],
    'John F. Kennedy': range(1961, 1964),
    'Lyndon B. Johnson': list(range(1964, 1969)),
    'Richard Nixon': list(range(1969, 1975)),
    'Gerald Ford': [1975, 1976]
}

years_in_office = {
    1960 : "Eisenhower",
    1961 : "Kennedy",
    1962 : "Kennedy",
    1963 : "Kennedy",
    1964 : "Johnson",
    1965 : "Johnson"
}


presidents = ['JFK', 'LBJ', 'Nixon', 'Gerald Ford', 'Reagan', 'HW Bush', 'Bill Clinton', 'George Bush', 'Obama', 'Trump', 'Biden']
terms = [1961, 1963, 1996, 1974, 1977, 1981, 1989, 1993, 2001, 2009, 2017, 2021]
parties = ['D', 'D', 'R', 'R', 'R', 'R', 'D', 'R', 'D', 'R', 'D']



{
    'key': 'value',
    'key2': 'value2',
    'key3': 'value3'
}


# one thing that has different attributes
cat = {
    'name': 'Jack',
    'age': 1,
    'color': 'white'
}

# different things that all have the same attribute
ages = {
    'Jack': 1,
    'Mulberry': 1,
    'Sid': 9
}

# President has multiple attributes start year, end year, party
# Every single president should be a _________
trump = { 'name': 'Trump', 'start_year': 1930, 'end_year': 1940, 'party': 'R'}
jfk = { 'name': 'JFK', 'start_year': 1920, 'end_year': 1930, 'party': 'R'}
lbj = { 'name': 'LBJ', 'start_year': 1910, 'end_year': 1920, 'party': 'D'}


# I have a bunch of names
[ 'Trump', 'JFK', 'LBJ']
[1930, 1920, 1910]

presidents = [
    {"name" : "Eisenhower", "party" : "Republican", "start" : 1953, "end" : 1960},
    {"name" : "Kennedy", "party" : "Democratic", "start" : 1961, "end" : 1962},
    {"name" : "Johnson", "party" : "Democratic", "start" : 1963, "end" : 1968}
]

presidents = {
    'LBJ': range(1900, 1910),
    'JFK': range(1910, 1920),
    'Trump': range(1920, 1930)
}