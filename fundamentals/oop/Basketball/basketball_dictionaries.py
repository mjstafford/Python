players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]

#more data
kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}

class Player:
    players_list = []

    def __init__(self, dictionary):
        self.name = dictionary["name"]
        self.age = dictionary["age"]
        self.position = dictionary["position"]
        self.team = dictionary["team"]

    @classmethod
    def get_team(cls, team_list):
        for person in team_list:
            cls.players_list.append( Player(person))
        return cls.players_list
        


# Create your Player instances here!
player_jason = Player(jason)
player_kevin = Player(kevin)
player_kyrie = Player(kyrie)

# make a list of playe instances from a list of dictionaries
new_team = []

for person in players:
    new_team.append( Player(person))
print(new_team)


print("bonus below:")
Player.get_team(players)

count = 0
for person in Player.players_list:
    print(person.name)
    count += 1