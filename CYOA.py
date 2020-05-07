from random import random


# class that represents inventory
class Inventory:
    def __init__(self):
        self.items = []


# class that keeps track of possibilities
class DecisionTree:
    def __init__(self):
        root_decision_tree_node = None


    def create_decision_tree(self):
        return None


# class that represents a single possible decision
class DecisionTreeNode:
    def __init__(self, what_happened):
        self.what_happened = what_happened
        connections = {}


# class to keep track of rng
class RNG:
    def __init__(self, rng_type, rng_odds):
        self.rng_type = rng_type
        self.rng_odds = rng_odds

    # This is a function that creates an outcomes based on odds
    def get_negative_event_outcome(self):
        random_event_number = random()
        if random_event_number > self.rng_odds:
            return False
        else:
            return True


# class that keeps track of player data
class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()


# this function returns a dictionary that maps a string to a decimal value
# the strings represent different types of rng and the decimal value represents the probability
def create_rng_odds():
    rng_dict = {"corona": .5, "police": .66, "mugged": .25}
    return rng_dict


# this map represents which nodes have certain types of RNG
def create_rng_node_map():
    rng_node_map = {
        "corona": (14, 21, 31),
        "police": (17, 28),
        "mugged": (25, 27),
    }
    return rng_node_map


# this map represents what happens in each of the nodes
def create_what_happened_strings_map():
    what_happened_strings_map = {
        1: "You Wake up but your stomach is ready to explode from the copious amount of taco-bell you had last night.\n"
           " You head to the washroom but sadly find that you only have a couple sheets of toilet paper left!\n"
           " You are scared of the current COVID-19 virus that is going around, but know it is best to go to the store"
           " and pick up some more toilet paper. How would you like to travel to the store?\n",
        2: "You decide to take the car, but unfortunately there is construction blocking your normal route!\n"
           "Do you choose to take the highway or the side streets\n",
        3: "You decide to walk and arrive at a local family business, but you are interrupted "
           "by your middle school friend! Do you wish to enter the store or go meet your friend?",
        4: "You decide to bike to the store with no helmet, as you are riding you can see that your friend"
           " is throwing a party! Do you wish to join or choose to keep biking to the supermarket.",
        5: "You speed down the highway hurrying as you have urgent business to attend to,"
           " however you foolishly pick up your phone trying to swap playlists"
           " and run through a stop sign to get T-boned by a food delivery truck!"
           " Unfortuneately the crash was deadly. You Die!",
        6: "You're driving down past your elementary and stop to allow the group of kids to cross"
           " the street. However, as you are waiting for the kids to stop a"
           " garbage truck does not see you behind and reverses into your car, crushing you upon impact. You Die!",
        7: "You walk into your local families business but find out all the toilet "
           "paper is out of stock! Dissapointed as you are you grab a chocolate bar"
           " and head to the counter to checkout. Upon paying for the chocolate bar"
           " you notice they have face masks in stock! Do you wish to purchase one?",
        8: "You decide to chat it up with your friend, and he offers you a ride to"
           " either downtown or a party he is having at home! Do you wish to join "
           "the party or take the ride to City Hall?",
        9: "You arrive to the front door and knock, and are warmly greeted by your friend from middle school!",
        10: "As you were biking on the street you were rudely smashed by a drunk"
            " driver! Maybe if you wore a helmet you could have survived... You Die!",
        11: "You decide to purchase the mask and wear it immediately."
            " Your stomach starts to hurt more, and the urgency to unload rises. "
            "Would you like to take the bus to head to the supermarket or continue to walk?",
        12: "You decide not to purchase the mask. Your stomach starts to hurt more, "
            "and the urgency to unload rises. Would you like to take the bus to head to the supermarket"
            " or continue to walk?",
        13: "You opt not to join the party as you are cautious about social distancing,"
            " but still take up the offer of the ride as you need to deal with your business ASAP.",
        # this has two strings because of the path you can choose"
        14: ("You head inside to join the birthday party,"
             " and make contact with the 14 other people who are celebrating the party."
             " However upon leaving you notice a convieniently placed 24 pack of toilet paper by the back entrance."
             " Do you choose to steal the toilet paper?",
             "You head inside to join the birthday party, and make contact with the 14"
             " other people who are celebrating the party. However"
             " upon leaving you notice a convieniently placed helmet by the back entrance."
             " Do you choose to steal the helmet?"),
        15: "You wait for the bus, hoping that the bus will be empty.",
        16: "You choose to keep walking to the supermarket."
            " You can choose to walk through the streets of downtown or travel through the forest!"
            " Where would you like to go?",
        17: "You decide to steal the helmet so you become a safe rider. "
            "You throw that bad boy on and set out to the supermarket.",
        18: "You decide to be a good samaritan and choose not to steal the helmet. "
            "And head back towards the supermarket.",
        19: "Yes! You exclaim as you come across an empty bus. "
            "You decide to pick your faviroute seat at the back corner of the bus. "
            "You put your headphones in and begin to watch some dumb video online and did not pay attention"
            " to the bus driver who decided to drive off a bridge! You Die!",
        20: "You hop on the bus, unfortuneately it is packed and you steal the last available seat!"
            " During the ride you start to hear many coughs and worry for your health.",
        21: "You choose to tread throughout the forest but as you were walking you were cornered by a big grizzly bear!"
            " RAWR XD the bear yells as he swiftly claws you. You Die!",
        22: "needs to be completed",
        23: "needs to be completed",
        24: "needs to be completed",
        25: "needs to be completed",
        26: "needs to be completed",
        27: "needs to be completed",
        28: "needs to be completed",
        29: "needs to be completed",
        30: "needs to be completed",
        31: "needs to be completed",
        32: "needs to be completed",
        33: "needs to be completed",
        34: "gg lol",
    }
# this map represents how decision nodes are connected in the game
# returns the map
def create_game_map():
    game_map = {
        1: (2, 3, 4),
        2: (5, 6),
        3: (7, 8),
        4: (9, 10),
        5: (),
        6: (),
        7: (11, 12),
        8: (13, 14),
        9: (14),
        10: (),
        11: (15, 16),
        12: (15, 16),
        13: (22),
        14: (17, 18, 23),
        15: (19, 20),
        16: (21, 22),
        17: (33, 34),
        18: (10),
        19: (),
        20: (24),
        21: (),
        22: (26, 27),
        23: (22),
        24: (25, 30),
        25: (32, 34),
        26: (31),
        27: (32, 34),
        28: (33, 34),
        30: (34),
        31: (34),
        32: (),
        33: (),
        34: (),
    }
    return game_map


# this function runs the game loop
def game_run():
    is_user_playing = True
    print("Welcome to the game!")
    while is_user_playing == True:
        player = create_player()
        is_user_playing = False


# this function prompts the user for their name
# and then creates and returns the player
def create_player():
    player_name = input("What is your name?")
    player = Player(player_name)
    return player


game_run()

