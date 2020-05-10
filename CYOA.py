from random import random


# class that represents inventory
class Inventory:
    def __init__(self):
        self.items = []


# class that keeps track of possibilities
class DecisionTree:
    def __init__(self):
        self.node_map = self.create_decision_tree()
        self.root_decision_tree_node = self.node_map[1]

    def create_decision_tree(self):
        game_map = create_game_map()
        what_happened_strings_map = create_what_happened_strings_map()
        rng_node_map = create_rng_node_map()
        decision_strings_map = create_decision_strings_map()
        node_map = {}
        for node_id in game_map.keys():
            what_happened = what_happened_strings_map[node_id]
            connections = game_map[node_id]
            decision_strings = decision_strings_map[node_id]
            if node_id in rng_node_map:
                rng_type = rng_node_map[node_id]
            else:
                rng_type = None
            rng = RNG(rng_type)
            decision_tree_node = DecisionTreeNode(what_happened, node_id, connections, rng, decision_strings)
            node_map[node_id] = decision_tree_node
        return node_map


# class that represents a single possible decision
class DecisionTreeNode:
    def __init__(self, what_happened, node_id, connections, rng, decision_strings):
        self.what_happened = what_happened
        self.node_id = node_id
        self.connections = connections
        self.rng = rng
        self.decision_strings = decision_strings


# class to keep track of rng
class RNG:
    def __init__(self, rng_type,):
        self.rng_type = rng_type
        self.rng_odds_map = create_rng_odds_map()
        if rng_type in self.rng_odds_map:
            self.rng_odds = self.rng_odds_map[rng_type]
        else:
            self.rng_odds = 0

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
def create_rng_odds_map():
    rng_dict = {"corona": .5, "police": .66, "mugged": .25}
    return rng_dict


# this map represents which nodes have certain types of RNG
def create_rng_node_map():
    rng_node_map = {
        14: "corona",
        21: "corona",
        30: "corona",
        17: "police",
        28: "police",
        25: "mugged",
        27: "mugged",
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
        33: "gg lol",
    }
    return what_happened_strings_map


# this function returns a dictionary that represents the choices
def create_decision_strings_map():
    decision_strings_map = {
        1: ("1) Take the car", "2) Walk", "3) Bike"),
        2: ("1) Take the highway", "2) Take the side streets"),
        3: ("1) Enter the store", "2) See your friend"),
        4: ("1) Join the party", "2) Continue Biking"),
        5: (),
        6: (),
        7: ("1) Buy the mask", "2) Don't buy the mask"),
        8: ("1) Don't go to the party", "2) Go to the party"),
        9: ("1) Go to the party"),
        10: (),
        11: ("1) Take the bus", "2) Keep Walking"),
        12: ("1) Take the bus", "2) Keep Walking"),
        13: ("1) Go through city hall"),
        14: ("1) Steal the helmet", "2)Don't steal the helmet"),
        # rng determines number 15, but there are two outcomes
        15: ("1) hop on the bus"),
        16: ("1) Go through the forest", "2) Go through city hall"),
        # rng determines number 17, but there are two outcomes
        17: ("1) head to the store"),
        18: (),
        19: (),
        20: ("1) Help the grandma", "2) Continue heading to the store"),
        21:  (),
        22:  ("needs to be completed", "2)tbd"),
        23:  ("1)needs to be completed"),
        24:  ("1)needs to be completed", "2)tbd"),
        25:  ("1)needs to be completed", "2)tbd"),
        26:  ("1) Walk through the protesters"),
        # 27 and 28 are RNG choices, two outcomes
        27:  ("1) head to the store"),
        28:  ("1) head to the store"),
        29:  ("1) head to the store"),
        30:  ("1) head to the store"),
        31:  (),
        32:  (),
        33:  (),
    }
    return decision_strings_map


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
        9: tuple([14]),
        10: (),
        11: (15, 16),
        12: (15, 16),
        13: tuple([22]),
        14: (17, 18, 23),
        15: (19, 20),
        16: (21, 22),
        17: (32, 33),
        18: tuple([10]),
        19: (),
        20: tuple([24]),
        21: (),
        22: (26, 27),
        23: tuple([22]),
        24: (25, 29),
        25: (31, 33),
        26: tuple([30]),
        27: (31, 33),
        28: (32, 33),
        29: tuple([33]),
        30: tuple([33]),
        31: (),
        32: (),
        33: (),
    }
    return game_map


# this function runs the game loop
def game_run():
    is_user_playing = True
    game_decision_tree = DecisionTree()
    game_decision_tree.create_decision_tree()
    player = create_player()
    print(player.name)
    print("Welcome to the game!")
    current_decision_tree_node = game_decision_tree.root_decision_tree_node

    while is_user_playing is True:
        is_user_playing, decision = prompt_decision(current_decision_tree_node)
        if is_user_playing is False and decision is None:
            break
        next_decision_tree_node = find_next_decision_tree_node(current_decision_tree_node, decision, game_decision_tree)
        current_decision_tree_node = next_decision_tree_node

# this function prompts the user for their name
# and then creates and returns the player
def create_player():
    player_name = input("What is your name?")
    player = Player(player_name)
    return player


def prompt_decision(current_decision_tree_node):
    print(current_decision_tree_node.what_happened)
    if len(current_decision_tree_node.connections) == 0:
        return False, None
    for decision_string in current_decision_tree_node.decision_strings:
        print(decision_string)
    decision = input("what do you do? (response should be a number)")
    # TODO: error checking
    return True, decision


def find_next_decision_tree_node(current_decision_tree_node, decision, game_decision_tree):
    next_node_id = current_decision_tree_node.connections[int(decision) - 1]
    next_decision_tree_node = game_decision_tree.node_map[next_node_id]
    return next_decision_tree_node


game_run()

