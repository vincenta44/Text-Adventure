##### Record Definitions #####

'''
Records:

World:
    status (str): Whether or not the game is "playing", "quit", "won", or "lost". Initially "playing".

    map (dict[str: Location]): The lookup dictionary matching location names to their information.

    player (Player): The player character's information.

Player:

    location (str): The name of the player's current location.

    inventory (list[str]): The player's collection of items. Initially empty.

    health (int): The players health. Initially 5.

    follower (bool): if the player has a follower or not

Location:

    about (str): A sentence that describes what this location look like and the narrative that goes along with it.

    enemy (str): An enemy at this location that deals damage. Could be None.

    neighbors (list[str]): A list of the names of other places that you can reach from this location.

    items (list[str]): A collection of things available at this location.

'''

##### Core Game Functions #####

def render_introduction():
    '''
    Create the message to be displayed at the start of your game.

    Returns:
        str: The introductory text of your game to be displayed.
    '''
    return ('''
                                      ==== The Impossible Journey ====
                                         ==== By: Vincent Ains ====
********************************************************************************************************************
Hello adventurer...you have quite a journey ahead of you.
There is a dangerous Dragon in his Den up the path and through the magic gate.
You have the job to kill it.
Be careful and move slowly throughout the path, once you go down it you can't go back.
You have nothing, so anything you find on your way will be helpful.
    I hear along the path there are secret compartments that some people hide pretty valuable items.
    Not all places them, but those that do can prove very useful.
    I have this amulet that can glows when there are secret places, however you can only use it 3 times and if you use
    it all in random places and find nothing...well that's on you.
Have a safe journey and do not come back without the Dragon's treasure.
********************************************************************************************************************
'''
          )

def create_world():
    '''
    Creates a new version of the world in its initial state.

    Returns:
        World: The initial state of the world
    '''
    return {
        'map': create_map(),
        'player': create_player(),
        'status': 'playing'
    }

def create_player():
    '''
    Creates the player in its initial state.

    Returns:
        Player: The initial state of the world
    '''
    player = {
        'location': 'Path A',
        'inventory': ["Amulet"],
        'health': 5,
        'follower': False,
        'amulet uses': 0,
        'follower num': 0
    }
    return player

def create_followers():
    '''
    Creates the followers in their initial state.

    Returns:
        Followers: The initial state of the followers
    '''
    followers = {
        'Follower 1': {
            'Name': "Adjorn",
            'Inventory': "key",
            'Alive': True,
            'Health': 2
        },
        'Follower 2': {
            'Name': "Benedek",
            'Inventory': "key",
            'Alive': True,
            'Health': 1
        },
        'Follower 3': {
            'Name': "Frons",
            'Inventory': "",
            'Alive': True,
            'Health': 1
        }
            }
    return followers

def create_map():
    '''
    Creates the map in its initial state.

    Returns: The initial state of the map
    '''
    map = {
        'Path A': {
            'about': '''
There is a fork in the road
To the right is the path,
to the left are the woods,
and next to you is a path to a broken down house.
''',
            'neighbors': ['Broken House', 'Woods', 'Path B'],
            'stuff': [],
            'enemy': False
            },
        'Path B': {
            'about': '''
Up ahead is a tunnel.
It is very dark.
''',
            'neighbors': ['Tunnel'],
            'stuff': [],
            'enemy': False
            },
        'Tunnel': {
            'about': '''
A dark tunnel, you can't see anything.
Out of no where the sconces in the tunnel light with fire.
In the light you can see a Troll.
The Troll jumps around and becomes hostile.
''',
            'neighbors': ['Path C'],
            'stuff': ["Revive Potion"],
            'enemy': True
            },
        'Path C': {
            'about':'''
You are back on the path.
To your left is a town and
forward is a gate that seems to be magical.
''',
            'neighbors': ['Town', 'Magic Gate'],
            'stuff': [],
            'enemy': False
            },
        'Magic Gate': {
            'about':'''
You approach the gate and it slowly opens on its own.
The pathway only moves forward but the nature seems
to be dying and dark past the gate.
''',
            'neighbors': ['Path D'],
            'stuff': [],
            'enemy': False
            },
        'Path D': {
            'about':'''
Ahead seems to get darker, but you can only go forward.
''',
            'neighbors': ['Path E'],
            'stuff': [],
            'enemy': False
            },
        'Path E': {
            'about':'''
It's getting darker and darker....
''',
            'neighbors': ['Path F'],
            'stuff': [],
            'enemy': True
            },
        'Path F': {
            'about':'''
In front of you is more of the winding path.
You also notice a gate to your left with a pathway to a glowing house behind it.
''',
            'neighbors': ['Glowing House', 'Path G'],
            'stuff': [],
            'enemy': False
            },
        'Path G': {
            'about':'''
Getting darker then before, you have no choice but to move forward.
''',
            'neighbors': ['Path H'],
            'stuff': [],
            'enemy': False
            },
        'Path H': {
            'about':'''
You approach a turn in the road.
You are now standing in front of the Dragon's den.
In the woods, to your right, you hear a sound.
''',
            'neighbors': ['Sound C', 'Dragon Den'],
            'stuff': [],
            'enemy': False
            },
        'Dragon Den': {
            'about': '''
You are inside the den...and there are two tunnels splitting your path.
To the right is a glowing gold light and
to the left is a loud grumbling sound.
''',
            'neighbors': ['Treasury', 'Sound D'],
            'stuff': [],
            'enemy': False
            },
        'Sound D': {
            'about':'''
You walk through the left side and in a massive
cavern there is the Dragon there...and she has seen you
''',
            'neighbors': ['Dragon Fight'],
            'stuff': [],
            'enemy': False
            },
        'Dragon Fight': {
            'about':'''
The Dragon stands tall, roars fire from her mouth.
She faces you ready for battle.
''',
            'neighbors': [],
            'stuff': [],
            'enemy': True
            },
        'Broken House': {
            'about': '''
You're in this broken down house.
But seems like someone still lives here.
There is a nice meal on the table you can take for later.
You also hear a sound from behind the house.
''',
            'neighbors': ['Path A', 'Sound A'],
            'stuff': ["Rations"],
            'enemy': False
            },
        'Sound A': {
            'about': '''
The sound is getting louder.
Looks like something left tracks leading further from the house.
''',
            'neighbors': ['Bear', 'Broken House'],
            'stuff': [],
            'enemy': False
            },
        'Bear': {
            'about': '''
You follow the tracks and you catch yourself staring down a humungous bear.
It stands and roars...becoming hostile"
''',
            'neighbors': ['Path A'],
            'stuff': ["Bear Pelt"],
            'enemy': True
            },
        'Woods': {
            'about':'''
The woods have a small path that slowly degrades as you keep walking.
Ahead of you are denser trees with no more path.
To your left you hear a sound, a scream maybe?
''',
            'neighbors': ['Deep Woods', 'Path A', 'Sound B'],
            'stuff': [],
            'enemy': False
            },
        'Sound B': {
            'about':'''
There is a man here with a sword through his back.
You don't currently have a weapon and this may be your only chance to get one.
You can grab the sword, but do it quick before whoever did this comes back.
''',
            'neighbors': ['Woods'],
            'stuff': ["Sword"],
            'enemy': False
            },
        'Deep Woods': {
            'about':'''
Deeper in the woods there is no path.
The trees start to get so dense you can't walk through them.
Behind you is the path in the woods you just came from.
To your left is a cave entrance that is covered in spider webs.
''',
            'neighbors':['Woods', 'Cave'],
            'stuff': [],
            'enemy': False
            },
        'Cave': {
            'about':'''
There is nothing but more cobwebs as you move into the cave.
Everything is getting darker.
There is more darkness ahead of you.
''',
            'neighbors': ['Deep Cave', 'Deep Woods'],
            'stuff': [],
            'enemy': False
            },
        'Deep Cave': {
            'about': '''
You follow the path until you encounter a small room with a plate of armor on it.
You creep toward it.
''',
            'neighbors': ['Woods'],
            'stuff': ["Armor"],
            'enemy': True
            },
        'Town': {
            'about': '''
You are in a small town with people bustling on the sidewalks.
There is nothing here for you.
''',
            'neighbors': ['Path C'],
            'stuff': [],
            'enemy': False
            },
        'Glowing House': {
            'about': '''
You are walking through the path and a spell casts your follower into the air and when he lands he dies
You mourn for a minute but move forward to the house.
''',
            'neighbors': ['Path F'],
            'stuff': ["Upgraded Armor"],
            'enemy': False
            },
        'Sound C': {
            'about': '''
You walk to the sound and before you know it
you are surrounded by a group of small goblins!
''',
            'neighbors': ['Path H'],
            'stuff': ["Shield"],
            'enemy': True
            },
        'Treasury': {
            'about': '''
The room is glowing with gold and gems.
You walk in further...only one piece of this would be a fortune for the town.
''',
            'neighbors': ['Dragon Den', 'Door'],
            'stuff': ["Treasure"],
            'enemy': False
                     },
        'Door': {
            'about': '''
The door opens when you push on it and right infront of you is the dragon.
She heard you in her treasury, now she is awake and ready to fight!
''',
            'neighbors': ['Dragon Fight'],
            'stuff': [],
            'enemy': False
                 }
        }
    return map

def tunnel(world):
    '''
    Consumes a world and updates the world to its given state. Returns a statement for this given location that is dynamic to the states of the world.
    Can enemy status to False. Can change the status of the game.

    Args:
        world [World]: The current state of the world.
    Returns:
        str: A statement for this given location that is dynamic to the states of the world.
    '''
    inventory = world['player']['inventory']
    world['map']['Tunnel']['enemy'] = False
    world['map']['Tunnel']['about'] = ""
    if 'Sword' in inventory:
        if 'Armor' in inventory:
            world['map']['Tunnel']['about'] = '''
You can move forward from this dimly lit tunnel.
'''
            return '''
You wield your sword and face the Troll. Puffing out your armor, you attack.
You slash at his feet while he smacks your chest. Your armor defends the attack.
You slash again, but in a more lethal spot. You get it through the back.
It kneels and dies. You have slain the troll.
'''
        else:
            world['map']['Tunnel']['about'] = '''
You can move forward from this dimly lit tunnel.
'''
            world['player']['health'] = world['player']['health'] - 2
            if world['player']['health'] <= 0:
                world['status'] = 'lost'
                return '''
You wield your sword and face the troll. With little courage you scoot forward.
The Troll comes stomping at you and you dodge enough to slash it's back.
You thrust forward, but the Troll turns around and knocks you back.
You are cornered on the rocks. He slaps the sword out of your hand and crushes you.
You died.
'''
            if world['status'] == 'playing':
                return '''
You wield your sword and face the troll. With little courage you scoot forward.
The Troll comes stomping at you and you dodge enough to slash it's back.
You thrust forward, but the Troll turns around and knocks you back.
You are cornered on the rocks. In a swift act of terror you scream and stab the troll.
The troll is now laying at your feet...It is slain.
'''
    else:
        world['player']['health'] = world['player']['health'] - 5
        world['status'] = 'lost'
        return '''
You have nothing...you look around and find a rock.
You hurl the rock at the Troll, it only get's more upset.
You try to run, but the Troll catches up, grabs you and slams you around
until you die.
'''

def bear(world):
    '''
    Consumes a world and updates the world to its given state. Returns a statement for this given location that is dynamic to the states of the world.
    Can enemy status to False. Can change the status of the game.

    Args:
        world [World]: The current state of the world.
    Returns:
        str: A statement for this given location that is dynamic to the states of the world.
    '''
    inventory = world['player']['inventory']
    world['map']['Bear']['enemy'] = False
    world['map']['Bear']['about'] = ""
    if 'Sword' in inventory:
        if 'Armor' in inventory:
            world['map']['Bear']['about'] = '''
The bear is slain and you may skin it.
You may move forward.
'''
            return '''
You bring out your sword and wave it at the bear.
It charges you and tackles you, making you drop your sword.
It is biting and clawing at your chest but your armor deflects the blows.
This gives you time, you reach for your sword and stab its side.
The bear leaps off of you and you spring up and stab it one more time.
This finishes the bear.
'''
        else:
            world['player']['health'] = world['player']['health'] - 2
            if world['player']['health'] <= 0:
                world['status'] = 'lost'
                return '''
You unsheathe your sword and stand your ground.
The bear rushes at you and swiftly move to the side.
You thrash at it with your sword. The bear turns toward you and claws your chest.
You take a few too many slashes to the chest.
You died.
'''
            if world['status'] == 'playing':
                world['map']['Bear']['about'] = '''
The bear is slain and you may skin it.
You may move forward.
'''
                return '''
You unsheathe your sword and stand your ground.
The bear rushes at you and swiftly move to the side.
You thrash at it with your sword. The bear turns toward you and claws your chest.
You take a few claws to the chest, but with your sword out you are able to stab
the bear in the head. You killed the bear.
'''
    else:
        world['player']['health'] = world['player']['health'] - 5
        world['status'] = 'lost'
        return '''
You stare at the bear in terror.
It rushes you and attacks.
You have no way of defending yourself and you get mauled and die.
'''

def path_e(world):
    '''
    Consumes a world and updates the world to its given state. Returns a statement for this given location that is dynamic to the states of the world.
    Can enemy status to False. Can change the status of the game.

    Args:
        world [World]: The current state of the world.
    Returns:
        str: A statement for this given location that is dynamic to the states of the world.
    '''
    world['map']['Path E']['enemy'] = False
    world['map']['Path E']['about'] = ""
    if_follower = world['player']['follower']
    inventory = world['player']['inventory']
    foll_num = world['player']['follower num']
    create_follower = create_followers()
    if foll_num > 0:
        follower = create_follower['Follower ' + str(foll_num)]['Name']

    if 'Sword' in inventory:
        if 'Armor' in inventory:
            if if_follower:
                world['player']['health'] = world['player']['health'] - 1
                if world['player']['health'] <= 0:
                    world['status'] = 'lost'
                    return '''
A Witch springs out of the darkness...wielding spells.
%s jumps in front to attack first.
You bring out your sword and rush with him.
She casts a spell at your follower, and he gets struck back.
This distraction give you time to pursue.
You jab your sword through her, she turns and casts a spell at you.
Your armor withstands the blow and you pull your sword out,
before you can slash she casts a fireball that melts through your armor and you.
You died.
'''% (follower)
                if world['status'] == 'playing':
                    return '''
A Witch springs out of the darkness...wielding spells.
%s jumps in front to attack first.
You bring out your sword and rush with him.
She casts a spell at your follower, and he gets struck back.
This distraction give you time to pursue.
You jab your sword through her, she turns and casts a spell at you.
Your armor withstands the blow and you pull your sword out.
You jab again kill her.
    She has a book of spells on her.
    You can read the book and learn the spells,
    however you will lose your sword.
'''% (follower)
            else:
                world['player']['health'] = world['player']['health'] - 2
                if world['player']['health'] <= 0:
                    world['status'] = 'lost'
                    return '''
A Witch springs out of the darkness...wielding spells.
The witch stares you down. She starts glowing then attacks.
Her spells shoot at you, but you manage to dive away.
She shoots again this time burning your arm.
You manage to dodge a few shots and you rush her.
You jab your sword through her, she turns and casts a spell at you.
Your armor withstands the blow and you pull your sword out,
before you can slash she casts a fireball that melts through your armor and you.
You died.
'''
                if world['status'] == 'playing':
                    return '''
A Witch springs out of the darkness...wielding spells.
The witch stares you down. She starts glowing then attacks.
Her spells shoot at you, but you manage to dive away.
She shoots again this time burning your arm.
You manage to dodge a few shots and you rush her.
You slash her side and her face. She hits you with a spell,
but your armor protects it. You jab her through her chest.
The witch is dead.
    She has a book of spells on her.
    You can read the book and learn the spells,
    however you will lose your sword.
'''
        else:
            world['player']['health'] = world['player']['health'] - 5
            world['status'] = 'lost'
            return '''
You run up sword in hand.
The witch jumps and dodges you.
You turn and slash the witches face,
but she manifested a fireball and blew it straight through you.
You died.
'''
    else:
        world['player']['health'] = world['player']['health'] - 5
        world['status'] = 'lost'
        return '''
The witch disintegrates you immediately.
How did you even make it this far with no armor or weapon?
'''

def dragon_fight(world):
    '''
    Consumes a world and updates the world to its given state. Returns a statement for this given location that is dynamic to the states of the world.
    Can enemy status to False. Can change the status of the game.

    Args:
        world [World]: The current state of the world.
    Returns:
        str: A statement for this given location that is dynamic to the states of the world.
    '''
    world['map']['Path E']['enemy'] = False
    if_follower = world['player']['follower']
    inventory = world['player']['inventory']
    foll_num = world['player']['follower num']
    create_follower = create_followers()
    if foll_num > 0:
        follower = create_follower['Follower ' + str(foll_num)]['Name']

    if 'Sword' in inventory:
        return dragon_fight_sword(world)
    elif 'Spells' in inventory:
        return dragon_fight_spells(world)
    else:
        world['status'] = 'lost'
        return '''
You walk up to the dragon...nothing in hand...and you bow.
She creeps up on you and sniffs around.
She drags you to the middle of the room.
She lays back down on you and sleeps.
You slowly get crushed and suffocate.
You are dead.
'''

def dragon_fight_sword(world):
    '''
    Consumes a world and updates the world to its given state. Returns a statement for this given location that is dynamic to the states of the world.
    Can enemy status to False. Can change the status of the game.

    Args:
        world [World]: The current state of the world.
    Returns:
        str: A statement for this given location that is dynamic to the states of the world.
    '''
    world['map']['Path E']['enemy'] = False
    if_follower = world['player']['follower']
    inventory = world['player']['inventory']
    foll_num = world['player']['follower num']
    create_follower = create_followers()
    if foll_num > 0:
        follower = create_follower['Follower ' + str(foll_num)]['Name']

    if 'Armor' in inventory:
        if ('Upgraded Armor' in inventory) and if_follower:
            if 'Shield' in inventory:
                world['player']['health'] = world['player']['health'] - 1
                if world['player']['health'] <= 0:
                    world['status'] = 'lost'
                    return '''
You pull out your sword, puff out your armor and move forward.
%s moves at your side. You both now charge.
The dragon focuses on %s and moves toward him.
You move around the back while she's is distracted.
She slaps you with her tail, but you block it with your shield.
You shield flies away from you, but you move forward.
you climb her and throws you off her tail onto the cave wall.
Your armor stops glowing. %s take the opportunity and stabs her in the chest.
You pick yourself up and run forward and jump onto her wing then to her back.
You crawl up her neck and get to head, but you stumble and fall.
The dragon kills %s then eats you.
You Died.
''' % (follower, follower, follower, follower)
                if world['status'] == 'playing':
                    world['status'] = 'won'
                    return '''
You pull out your sword, puff out your armor and move forward.
%s moves at your side. You both now charge.
The dragon focuses on %s and moves toward him.
You move around the back while she's is distracted.
She slaps you with her tail, but you block it with your shield.
You shield flies away from you, but you move forward.
you climb her and throws you off her tail onto the cave wall.
Your armor stops glowing. %s take the opportunity and stabs her in the chest.
You pick yourself up and run forward and jump onto her wing then to her back.
You crawl up her neck and get to head, you stab your sword through her.
She falls...You killed the dragon!
''' % (follower, follower, follower)
            else:
                world['player']['health'] = world['player']['health'] - 2
                if world['player']['health'] <= 0:
                    world['status'] = 'lost'
                    return '''
You pull out your sword, puff out your armor and move forward.
%s moves at your side. You both now charge.
The dragon focuses on %s and moves toward him.
You move around the back while she's is distracted.
You jump up on her tail. In one motion she grabs %s with her teeth
and throws you off her tail onto the cave wall.
%s is on the ground not moving. Your armor stops glowing.
You pick yourself up and run forward and jump onto her wing then to her back.
You crawl up her neck and get to head, but you stumble and fall.
The dragon kills %s then eats you.
You Died.
''' % (follower, follower, follower, follower)
                if world['status'] == 'playing':
                    if_follower = False
                    world['status'] = 'won'
                    return '''
You pull out your sword, puff out your armor and move forward.
%s moves at your side. You both now charge.
The dragon focuses on %s and moves toward him.
You move around the back while she's is distracted.
You jump up on her tail. In one motion she grabs %s with her teeth
and throws you off her tail onto the cave wall.
%s is on the ground not moving. Your armor stops glowing.
You pick yourself up and run forward and jump onto her wing then to her back.
You crawl up her neck and get to head, you stab your sword through her.
She falls...You killed the dragon!
''' % (follower, follower, follower, follower)
        elif 'Upgraded Armor' in inventory:
            if 'Shield' in inventory:
                world['player']['health'] = world['player']['health'] - 2
                if world['player']['health'] <= 0:
                    world['status'] = 'lost'
                    return '''
You pull out your sword and run shouting battle cries.
She bites at you, you armor withstands her jaw,
but its glow begins to fade. You wiggle around a bite and stab her neck.
She throws herself up and charges her voice.
You pull up your shield and kneel behind it as she blows fire toward you.
You shield melts under the heat so you charge.
You run around the sides of the cave and throw her off.
You jump high onto her wing and slice her with your sword.
You run up her back but stumble and fall.
She stand over you and breathes fire on you.
You Died.
'''
                if world['status'] == 'playing':
                    world['status'] = 'won'
                    return'''
You pull out your sword and run shouting battle cries.
She bites at you, you armor withstands her jaw,
but its glow begins to fade. You wiggle around a bite and stab her neck.
She throws herself up and charges her voice.
You pull up your shield and kneel behind it as she blows fire toward you.
You shield melts under the heat so you charge.
You run around the sides of the cave and throw her off.
You jump high onto her wing and slice her with your sword.
You run up her back and sink your sword in her head.
The dragon is slain.
'''
            else:
                world['player']['health'] = world['player']['health'] - 3
                if world['player']['health'] <= 0:
                    world['status'] = 'lost'
                    return '''
You pull out your sword and run shouting battle cries.
She bites at you, you armor withstands her jaw,
but its glow begins to fade. You wiggle around a bite and stab her neck.
She throws herself up and charges her voice.
You jump behind a rock as she blows red hot flames toward you.
She burns you and melt part of your armor.
You get up and charge after she is done.
You try to slide under her neck but you trip.
She stand over you and breathes fire on you.
You Died.
'''
                if world['status'] == 'playing':
                    world['status'] = 'won'
                    return '''
You pull out your sword and run shouting battle cries.
She bites at you, you armor withstands her jaw,
but it's glow begins to fade. You wiggle around a bite and stab her neck.
She throws herself up and charges her voice.
You jump behind a rock as she blows red hot flames toward you.
She burns you and melt part of your armor.
You get up and charge after she is done.
You slide under her head and slash her neck.
Then you victoriously stand with you sword pointed up through her stomach.
The dragon is slain.
'''
        elif if_follower:
            if 'Shield' in inventory:
                world['player']['health'] = world['player']['health'] - 2
                if world['player']['health'] <= 0:
                    world['status'] = 'lost'
                    return'''
You pull out your sword, puff out your armor and move forward.
%s moves at your side. You both now charge.
The dragon focuses on you and moves toward you.
%s moves around out of her vision.
She clamps on you with her jaw and flails you around.
%s stabs her from behind and she lets go of you.
Your glowing armor fades away. She focuses on %s
You pick yourself up and run forward and bash her head with your shield.
Now you both stab mount her wings and slash her.
You stumble and try to grab %s, but you knock him off and he lands and dies.
You fall off the other side and the dragon stand over you then eats you.
You died.
''' % (follower, follower, follower, follower, follower)
                if world['status'] == 'playing':
                    if_follower = False
                    world['status'] = 'won'
                    return'''
You pull out your sword, puff out your armor and move forward.
%s moves at your side. You both now charge.
The dragon focuses on you and moves toward you.
%s moves around out of her vision.
She clamps on you with her jaw and flails you around.
%s stabs her from behind and she lets go of you.
Your glowing armor fades away. She focuses on %s
You pick yourself up and run forward and bash her head with your shield.
Now you both stab mount her wings and slash her.
Together you stab her neck...she flies up...
you jump off, but %s gets crushed at the top of the cave.
The dragon falls and lays dead.
The dragon is slain.
''' % (follower, follower, follower, follower, follower)
            else:
                world['player']['health'] = world['player']['health'] - 3
                if world['player']['health'] <= 0:
                    world['status'] = 'lost'
                    return '''
You pull out your sword, puff out your armor and move forward.
%s moves at your side. You both now charge.
The dragon focuses on %s and moves toward him.
You move around out of her vision.
She clamps on %s with her jaw and flails him around.
You stab her from behind and she lets go of %s.
She whips you with her tail, knocking you back and causing your glowing armor to fade.
While you are on the ground she stand tall and takes a snap at you.
%s jumps in the way at the last second and takes the blow.
He dies...you fall back but she stomps toward you.
She stands and blows fire on you.
You died.
''' % (follower, follower, follower, follower, follower)
                if world['status'] == 'playing':
                    if_follower = False
                    world['status'] = 'won'
                    return '''
You pull out your sword, puff out your armor and move forward.
%s moves at your side. You both now charge.
The dragon focuses on %s and moves toward him.
You move around out of her vision.
She clamps on %s with her jaw and flails him around.
You stab her from behind and she lets go of %s.
She whips you with her tail, knocking you back and causing your glowing armor to fade.
While you are on the ground she stand tall and takes a snap at you.
%s jumps in the way at the last second and takes the blow.
He dies...but with haste you get up and slide underneath the dragon.
You rapidly stab her and then roll out from under her.
She falls and dies. The Dragon is slain.
''' % (follower, follower, follower, follower, follower)
        elif "Shield" in inventory:
            world['player']['health'] = world['player']['health'] - 3
            if world['player']['health'] <= 0:
                world['status'] = 'lost'
                return '''
You pull out your sword and shield, puff out your armor and move forward.
The dragon focuses on you as you charge.
She slaps her skull up to your shield and you slide back.
You regain your feet and attack again.
You slide under her neck and gash her throat.
She roars great fire in your direction, you put up your shield.
It blocks the fire but burns and melts.
You realize you shield is gone so you charge again.
You jump on her wing and on to her back, you climb up her neck,
but stumble off and fall to the ground.
She stand over you and eat you.
You Died.
'''
            if world['status'] == 'playing':
                world['status'] = 'won'
                return'''
You pull out your sword and shield, puff out your armor and move forward.
The dragon focuses on you as you charge.
She slaps her skull up to your shield and you slide back.
You regain your feet and attack again.
You slide under her neck and gash her throat.
She roars great fire in your direction, you put up your shield.
It blocks the fire but burns and melts.
You realize you shield is gone so you charge again.
You jump on her wing and on to her back, you climb up her neck
and stab her in the head.
The dragon is slain.
'''
        else:
            world['status'] = 'lost'
            return '''
You walk in and pull out your sword.
You armor doesn't seem so strong next to her scales.
You charge and she swipes you with her tail.
Your armor breaks apart and falls right off of you.
You try to get up and move away, but she catches you and eats you.
You are dead.
'''
    else:
        world['status'] = 'lost'
        return '''
You walk in and pull out you sword.
You charge...but before you get there she
blows fire at you and disintegrates you completely.
You are dead.
'''

def dragon_fight_spells(world):
    '''
    Consumes a world and updates the world to its given state. Returns a statement for this given location that is dynamic to the states of the world.
    Can enemy status to False. Can change the status of the game.

    Args:
        world [World]: The current state of the world.
    Returns:
        str: A statement for this given location that is dynamic to the states of the world.
    '''
    world['map']['Path E']['enemy'] = False
    if_follower = world['player']['follower']
    inventory = world['player']['inventory']
    foll_num = world['player']['follower num']
    create_follower = create_followers()
    if foll_num > 0:
        follower = create_follower['Follower ' + str(foll_num)]['Name']

    if 'Armor' in inventory:
            if ('Upgraded Armor' in inventory) and if_follower:
                world['player']['health'] = world['player']['health'] - 2
                if world['player']['health'] <= 0:
                    world['status'] = 'lost'
                    return '''
You wield your spells, puff out your armor and move forward.
%s moves at your side. You both now charge.
The dragon focuses on %s and moves toward him.
You move around the back while she's is distracted.
She slaps you with her tail and you get knocked back.
you climb her and throws you off her tail onto the cave wall.
Your armor stops glowing. %s take the opportunity and stabs her in the chest.
You pick yourself up and run forward and aim your spells at her.
With great power you cast your spells and engulf her in pain.
The spells get too powerful and you get knocked back.
You and %s get eaten.
You died.
''' % (follower, follower, follower, follower)
                if world['status'] == 'playing':
                    world['status'] = 'won'
                    return '''
You wield your spells, puff out your armor and move forward.
%s moves at your side. You both now charge.
The dragon focuses on %s and moves toward him.
You move around the back while she's is distracted.
She slaps you with her tail and you get knocked back.
you climb her and throws you off her tail onto the cave wall.
Your armor stops glowing. %s take the opportunity and stabs her in the chest.
You pick yourself up and run forward and aim your spells at her.
With great power you cast your spells and engulf her in pain.
You stand your ground while she slowly gets weaker.
%s climbs on her and finished her off.
The Dragon is slain.
''' % (follower, follower, follower, follower)
            elif 'Upgraded Armor' in inventory:
                world['player']['health'] = world['player']['health'] - 3
                if world['player']['health'] <= 0:
                    world['status'] = 'lost'
                    return '''
                    You wield your spells, puff out your armor and move forward.
You stand tall and cast your spells.
The dragon roars fire in your direction and counters your spells.
She slaps you with her tail and you get knocked back.
Your armor stops glowing.
You pick yourself up and run forward and aim your spells at her.
With great power you cast your spells and engulf her in pain.
You stand your ground while she slowly gets weaker.
While she is down you approach and she bites at you and get your arm.
With great power you cast your spells and engulf her in pain.
The spells get too powerful and you get knocked back.
She stands over you and eats you.
You died.
'''
                if world['status'] == 'playing':
                    world['status'] = 'won'
                    return'''
You wield your spells, puff out your armor and move forward.
You stand tall and cast your spells.
The dragon roars fire in your direction and counters your spells.
She slaps you with her tail and you get knocked back.
Your armor stops glowing.
You pick yourself up and run forward and aim your spells at her.
With great power you cast your spells and engulf her in pain.
You stand your ground while she slowly gets weaker.
While she is down you approach and she bites at you and get your arm.
You move back and cast more spells until she falls.
The Dragon is slain.
'''
            elif if_follower:
                world['player']['health'] = world['player']['health'] - 3
                if world['player']['health'] <= 0:
                    world['status'] = 'lost'
                    return '''
You wield your spells, puff out your armor and move forward.
%s moves at your side. You both now charge.
The dragon focuses on %s and moves toward him.
You move around the back while she's is distracted.
She slaps you with her tail and you get knocked back.
you climb her and throws you off her tail onto the cave wall.
Your armor breaks off of your body. %s take the opportunity and stabs her in the chest.
You pick yourself up and run forward and aim your spells at her.
With great power you cast your spells and engulf her in pain.
You stand your ground while she slowly gets weaker.
%s climbs on her and she slips him off and he lands on a rock that impales him.
With great power you cast your spells and engulf her in pain.
The spells get too powerful and you get knocked back.
She stands over you and eats you.
You died.
''' % (follower, follower, follower, follower)
                if world['status'] == 'playing':
                    world['status'] = 'won'
                    if_follower = False
                    return '''
You wield your spells, puff out your armor and move forward.
%s moves at your side. You both now charge.
The dragon focuses on %s and moves toward him.
You move around the back while she's is distracted.
She slaps you with her tail and you get knocked back.
you climb her and throws you off her tail onto the cave wall.
Your armor breaks off of your body. %s take the opportunity and stabs her in the chest.
You pick yourself up and run forward and aim your spells at her.
With great power you cast your spells and engulf her in pain.
You stand your ground while she slowly gets weaker.
%s climbs on her and she slips him off and he lands on a rock that impales him.
You scream and enhance your spells which drain your power, but she slowly falls.
The Dragon is slain.
''' % (follower, follower, follower, follower)
            else:
                world['status'] = 'lost'
                return '''
You walk in and wield your spells.
You charge...but before you get there she
blows fire at you and melts your armor.
You try to run back, but she flies toward you and eats you.
You are dead.
'''
    else:
        world['status'] = 'lost'
        return '''
You walk in and wield your spells.
You charge...but before you get there she
blows fire at you and disintegrates you completely.
You are dead.
'''

def deep_cave(world):
    '''
    Consumes a world and updates the world to its given state. Returns a statement for this given location that is dynamic to the states of the world.
    Can enemy status to False. Can change the status of the game.

    Args:
        world [World]: The current state of the world.
    Returns:
        str: A statement for this given location that is dynamic to the states of the world.
    '''
    inventory = world['player']['inventory']
    world['map']['Deep Cave']['enemy'] = False
    world['map']['Deep Cave']['about'] = ""
    if 'Sword' in inventory:
        world['player']['health'] = world['player']['health'] - 1
        if world['player']['health'] <= 0:
            world['status'] = 'lost'
            return '''
A Giant Spider jumps down from the top of the cave.
You pull out you sword and charge.
You get bitten once and can't react fast enough
and get bitten again and again and again...
until you die.
'''
        if world['status'] == 'playing':
            return '''
A Giant Spider jumps down from the top of the cave.
You pull out you sword and charge.
You get bitten once but with swift justice you
stab it in the head. The spider is killed.
'''
    else:
        world['player']['health'] = world['player']['health'] - 5
        world['status'] = 'lost'
        return '''
A Giant Spider drops down right on your head.
You have nothing to defend yourself ad you swing around in terror.
The spider ties you up...
waits 2 weeks...
Then eats you...
'''

def glowing_house(world):
    '''
    Consumes a world and updates the world to its given state. Returns a statement for this given location that is dynamic to the states of the world.

    Args:
        world [World]: The current state of the world.
    Returns:
        str: A statement for this given location that is dynamic to the states of the world.
    '''
    location = world['player']['location']
    here = world['map'][location]
    about = here['about']
    inventory = world['player']['inventory']
    if_follower = world['player']['follower']
    inventory = world['player']['inventory']
    foll_num = world['player']['follower num']
    followers = create_followers()
    if if_follower:
        follower = followers['Follower ' + str(foll_num)]['Name']
    world['map']['Path F']['neighbors'].remove('Glowing House')
    if if_follower:
        if (follower == "Frons"):
            return '''
The gate requires a key...you ask your Frons.
He doesn't have anything. You can't get through.
'''
        if (follower == "Benedek") or (follower == "Adjorn"):
            location = 'Glowing House'
            world['player']['follower'] = False
            if "Armor" in inventory:
                world['map']['Glowing House']['about'] = '''
You are walking through the path and a spell casts your follower into the air and when he lands he dies
You mourn for a minute but move forward to the house.
When you step in there is a large rumble and your armor begins to glow.
You feel more powerful. The only way now is back to the path.
'''
                inventory.append("Upgraded Armor")
                return '''
The gate requires a key. You ask your follower.
He looks in his bag and he pulls out a key.
You put it in the door and it unlocks.
''' + world['map']['Glowing House']['about']
            else:
                world['map']['Glowing House']['about'] = '''
You are walking through the path and a spell casts your follower into the air and when he lands he dies
You mourn for a minute but move forward to the house.
When you step in there is a large rumble but nothing happens.
'''
                return '''
The gate requires a key. You ask your follower.
He looks in his bag and he pulls out a key.
You put it in the door and it unlocks.
''' + world['map']['Glowing House']['about']
    else:
        return None

def sound_c(world):
    '''
    Consumes a world and updates the world to its given state. Returns a statement for this given location that is dynamic to the states of the world.
    Can enemy status to False. Can change the status of the game.

    Args:
        world [World]: The current state of the world.
    Returns:
        str: A statement for this given location that is dynamic to the states of the world.
    '''
    world['map']['Sound C']['enemy'] = False
    world['map']['Sound C']['about'] = ""
    if_follower = world['player']['follower']
    inventory = world['player']['inventory']
    foll_num = world['player']['follower num']
    create_follower = create_followers()
    if foll_num > 0:
        follower = create_follower['Follower ' + str(foll_num)]['Name']
    if 'Sword' in inventory:
        if ('Upgraded Armor' in inventory) and if_follower:
            world['player']['health'] = world['player']['health'] - 1
            if world['player']['health'] <= 0:
                world['status'] = 'lost'
                return '''
The goblins surround you and %s. You pull out your sword and charge.
The goblins jump on you while you attack others, you slash down a few
and throw others off you back. %s is fighting well behind you.
The goblins manage to slice you and %s. You guys start bleeding out.
The goblins start gathering up and overcoming you.
You both lay there and die.
''' % (follower, follower, follower)
            if world['status'] == 'playing':
                world['map']['Path H']['about'] = '''
You are at a turn in the road.
You are now standing in front of the Dragon's den.
'''
                return '''
The goblins surround you and %s. You pull out your sword and charge.
The goblins jump on you while you attack others, you slash down a few
and throw others off you back.%s is fighting well behind you.
The goblins manage to slice you and %s a little bit, but you manage the kill them.
The goblin group is slain.
''' % (follower, follower, follower)
        elif 'Upgraded Armor' in inventory:
            world['player']['health'] = world['player']['health'] - 2

            if world['player']['health'] <= 0:
                world['status'] = 'lost'
                return '''
The goblins surround you. You pull out your sword and charge.
The goblins jump on you while you attack others, you slash down a few
and throw others off you back. You keep getting overwhelmed.
The goblins manage to slice you as you fight and start bleeding out.
You fall down and get overcome by goblins.
You died.
'''
            if world['status'] == 'playing':
                world['map']['Path H']['about'] = '''
You are at a turn in the road.
You are now standing in front of the Dragon's den.
'''
                return '''
The goblins surround you. You pull out your sword and charge.
The goblins jump on you while you attack others, you slash down a few
and throw others off you back. You keep getting overwhelmed.
The goblins manage to slice you as you fight, but with will and power
you knock them all down..
The goblin group is slain.
'''
        elif if_follower:
            world['player']['health'] = world['player']['health'] - 2
            if world['player']['health'] <= 0:
                world['status'] = 'lost'
                return '''
The goblins surround you and %s. You pull out your sword and charge.
The goblins jump on you while you attack others, you slash down a few
and throw others off you back. %s is fighting well behind you.
The goblins manage to slice through your armor a lot,
You and %s use all of your energy and it's not enough.
You get overcome by the goblins.
You died.
''' % (follower, follower, follower)
            if world['status'] == 'playing':
                world['map']['Path H']['about'] = '''
You are at a turn in the road.
You are now standing in front of the Dragon's den.
'''
                return '''
The goblins surround you and %s. You pull out your sword and charge.
The goblins jump on you while you attack others, you slash down a few
and throw others off you back. %s is fighting well behind you.
The goblins manage to slice through your armor a lot,
You and %s use up most of your energy, but you manage the kill them.
The goblin group is slain.
''' % (follower, follower, follower)
    elif 'Spells' in inventory:
        if ('Upgraded Armor' in inventory) and if_follower:
            world['player']['health'] = world['player']['health'] - 1
            if world['player']['health'] <= 0:
                world['status'] = 'lost'
                return '''
The goblins surround you and %s. You stand your ground and charge your spells.
The goblins jump on you while you attack others, you blast down a few
and throw others off you back. %s is fighting well behind you.
The goblins manage to slice you and %s. You guys start bleeding out.
The goblins start gathering up and overcoming you.
You both lay there and die.
''' % (follower, follower, follower)
            if world['status'] == 'playing':
                world['map']['Path H']['about'] = '''
You are at a turn in the road.
You are now standing in front of the Dragon's den.
'''
                return '''
The goblins surround you and %s. You stand your ground and charge your spells.
The goblins jump on you while you attack others, you blast down a few
and throw others off you back. %s is fighting well behind you.
The goblins manage to slice you and %s a little bit, but you manage the kill them.
The goblin group is slain.
''' % (follower, follower, follower)
            elif 'Upgraded Armor' in inventory:
                world['player']['health'] = world['player']['health'] - 2
                if world['player']['health'] <= 0:
                    world['status'] = 'lost'
                    return '''
The goblins surround you. You stand your ground and charge your spells.
The goblins jump on you while you attack others, you blast down a few
and throw others off you back. You keep getting overwhelmed.
The goblins manage to slice you as you fight and start bleeding out.
You fall down and get overcome by goblins.
You died.
'''
                if world['status'] == 'playing':
                    world['map']['Path H']['about'] = '''
You are at a turn in the road.
You are now standing in front of the Dragon's den.
'''
                    return '''
The goblins surround you. You stand your ground and charge your spells.
The goblins jump on you while you attack others, you blast down a few
and throw others off you back. You keep getting overwhelmed.
The goblins manage to slice you as you fight, but with will and power
you knock them all down..
The goblin group is slain.
'''
            elif if_follower:
                world['player']['health'] = world['player']['health'] - 2
                if world['player']['health'] <= 0:
                    world['status'] = 'lost'
                    return '''
The goblins surround you and %s. You stand your ground and charge your spells.
The goblins jump on you while you attack others, you blast a few down
and throw others off you back. %s is fighting well behind you.
The goblins manage to slice through your armor a lot,
You and %s use all of your energy and it's not enough.
You get overcome by the goblins.
You died.
''' % (follower, follower, follower)
                if world['status'] == 'playing':
                    world['map']['Path H']['about'] = '''
You are at a turn in the road.
You are now standing in front of the Dragon's den.
'''
                    return '''
The goblins surround you and %s. You stand your ground and charge your spells.
The goblins jump on you while you attack others, you blast a few down
and throw others off you back. %s is fighting well behind you.
The goblins manage to slice through your armor a lot,
You and %s use up most of your energy, but you manage the kill them.
The goblin group is slain.
''' % (follower, follower, follower)
    else:
        world['status'] = 'lost'
        return '''
Goblins jump all over you and stab you until you die.
'''

def path_f(world):
    '''
    Consumes a world and updates the world to its given state. Returns a statement for this given location that is dynamic to the states of the world.

    Args:
        world (World): The current state of the world.
    Returns:
        str: A statement for this given location that is dynamic to the states of the world.
    '''
    location = world['player']['location']
    here = world['map'][location]
    about = here['about']
    inventory = world['player']['inventory']
    if_follower = world['player']['follower']
    inventory = world['player']['inventory']
    foll_num = world['player']['follower num']
    create_follower = create_followers()
    if foll_num > 0:
        follower = create_follower['Follower ' + str(foll_num)]['Name']

    if "Upgraded Armor" in inventory:
        if "Revive Potion" in inventory:
           return '''
You have a revive potion. You can use this to revive your follower.
'''
        else:
            return '''
You have made it back to the path.
'''
    elif if_follower:
        if (follower == 'Benedek') or (follower == 'Adjorn'):
            return about + "Your follower has a key to open the gate to the house."
        else:
            world['map']['Path F']['neighbors'].remove("Glowing House")
            return about + "Your follower doesn't have the key to open the gate to the house."

    elif ("Upgraded Armor" in inventory) and ("Revive Potion" not in inventory):
        return about[:len("You also notice a gate to your left with a pathway to a glowing house behind it.")]
    else:
        return about

def town(world, command):
    '''
    Consumes a world and a command updates the world to its given state. Returns a statement for this given location that is dynamic to the command.
    Changes the about statement of the 'Town' location.

    Args:
        world (World): The current state of the world.
        command (str): A command
    Returns:
        str: A statement for this given location that is dynamic to the states of the world.
    '''
    if "Benedek" in command:
        world['player']['follower'] = True
        world['player']['follower num'] = 2
        world['map']['Town']['about']=  '''
You've finished all your business in the town.
You may move forward.
'''
        return '''
You chose Benedek. Good choice.
'''
    elif "Adjorn" in command:
        world['player']['follower'] = True
        world['player']['follower num'] = 1
        world['map']['Town']['about']=  '''
You've finished all your business in the town.
You may move forward.
'''
        return '''
You chose Adjorn. Great choice!
'''
    elif "Frons" in command:
        world['player']['follower'] = True
        world['player']['follower num'] = 3
        world['map']['Town']['about']=  '''
You've finished all your business in the town.
You may move forward.
'''
        return '''
You chose Frons. Poor choice.
'''
    else:
        return ''

def render(world):
    '''
    Consumes a world and produces a string that will describe the current state
    of the world. Does not print.

    Args:
        world (World): The current world to describe.

    Returns:
        str: A textual description of the world.
    '''
    return (render_location(world) + render_player(world)) + "\n"

def render_location(world):
    '''
    Consumes a world and produces a string that will describe the current state
    of the location. Does not print.

    Args:
        world (World): The current world to describe.

    Returns:
        str: A textual description of the current location
    '''
    location = world['player']['location']
    here = world['map'][location]
    about = here['about']
    inventory = world['player']['inventory']
    if location == 'Path F':
        return path_f(world)
    else:
        return about

def render_enemy(world):
    '''
    Consumes a world and produces a string that will describe the current state
    of the location. Does not print. Calls functions to render enemies in given locations.

    Args:
        world (World): The current world to describe.

    Returns:
        str: A textual description of the current enemy
    '''
    location = world['player']['location']
    here = world['map'][location]
    enemy = here['enemy']
    if enemy:
        if location == 'Tunnel':
            return tunnel(world)
        if location == 'Bear':
            return bear(world)
        if location == 'Path E':
            return path_e(world)
        if location == 'Dragon Fight':
            return dragon_fight(world)
        if location == 'Deep Cave':
            return deep_cave(world)
        if location == 'Sound C':
            return sound_c(world)

def render_player(world):
    '''
    Consumes a world and produces a string that will describe the current health
    of the player. Does not print.

    Args:
        world (World): The current world to describe.

    Returns:
        str: A textual description of the players current health
    '''
    health = str(world['player']['health'])
    if health == 0:
        world['status'] = 'lost'
    return "Your health is " + health + "/5\n"

def get_options(world):
    '''
    Consumes a world and produces a list of strings representing the options
    that are available to be chosen given this state.

    Args:
        world (World): The current world to get options for.

    Returns:
        list[str]: The list of commands that the user can choose from.
    '''
    location = world['player']['location']
    here = world['map'][location]
    inventory = world['player']['inventory']
    commands = ["Quit", "See Inventory"]
    if_follower = world['player']['follower']
    inventory = world['player']['inventory']
    foll_num = world['player']['follower num']
    followers = create_followers()

    if foll_num > 0:
        follower = followers['Follower ' + str(foll_num)]['Name']
    if "Bear Pelt" in inventory:
        if location == "Town":
            commands.append("Get Benedek")
            commands.append("Get Frons")
            commands.append("Get Adjorn")
    if location == 'Path E':
        commands = ["Quit", "Learn Spells", "Keep Sword"]
        return commands
    for neighbor in here['neighbors']:
        if "Sound" in neighbor:
            neighbor = neighbor[:5]
            commands.append("Follow the " + neighbor)
        elif "Path" in neighbor:
            neighbor = neighbor[:4]
            commands.append("Follow " + neighbor)
        elif neighbor == "Bear":
            commands.append("Follow the Tracks")
        else:
            commands.append("Go to " + neighbor)
    if "Amulet" in inventory:
        commands.append("Use Amulet")
    for item in here['stuff']:
        if item == "Revive Potion":
            pass
        elif item == "Shield":
            if "Sword" in inventory:
                commands.append("Get " + item)
            else:
                pass
        elif item == "Upgraded Armor":
            pass
        else:
            commands.append("Get " + item)
    if "Revive Potion" in inventory:
        if "Upgraded Armor" in inventory:
            if location == 'Path F':
                commands.append("Revive Follower")
    if "Rations" in inventory:
        commands.append("Eat Rations")
    if here == 'Sound C':
        if "Spells" in inventory:
            commands.remove("Get Shield")
    return commands

def goto(world, command):
    '''
    Consumes a world and command and returns a statement indicating what the command did.
    Can call render_enemy(). Changes players location.

    Args:
        world (World): The current state of the world
        command (str): A command
    Returns:
        str: A statement indicating what the command did.
    '''
    if "Tracks" in command:
        world['player']['location'] = 'Bear'
        location = world['player']['location']
        about = world['map'][location]['about']
        return '''
You followed the tracks.
''' + about + render_enemy(world)

    new_location = command[len('Go to '):]
    world['player']['location'] = new_location
    about = world['map'][new_location]['about']
    if world['map'][new_location]['enemy']:
        return '''
You went to %s
''' % (new_location) + about + render_enemy(world)
    else:
        return '''
You went to %s
''' % (new_location)

def get(world, command):
    '''
    Consumes a world and command and returns a statement indicating what the command did.
    Removes an item from the given location. Adds the same item to players inventory.

    Args:
        world (World): The current state of the world
        command (str): A command
    Returns:
        str: A statement indicating what the command did.
    '''
    item = command[len('Get '):]
    inventory = world['player']['inventory']
    inventory.append(item)
    location = world['player']['location']
    world['map'][location]['stuff'].remove(item)
    world['map'][location]['about'] = '''
Everything in this area is looted, you may move on.
'''
    if 'Sound B' in world['map']['Woods']['neighbors']:
        if world['map']['Sound B']['stuff'] == []:
            world['map']['Woods']['neighbors'].remove('Sound B')
            world['map']['Woods']['about'] = '''
The woods have a small path that slowly degrades as you keep walking.
Ahead of you are denser trees with no more path.
'''
    if 'Sound A' in world['map']['Broken House']['neighbors']:
        if world['map']['Bear']['stuff'] == []:
            world['map']['Broken House']['neighbors'].remove('Sound A')
    if item == "Rations":
        return '''
You picked up some Rations, these can restore your health when eaten.
'''
    if item == "Bear Pelt":
        if "Rations" not in inventory:
            world['map']['Broken House']['about'] ='''
You're in this broken down house.
But seems like someone still lives here.
There is a nice meal on the table you can take for later.
'''
        world['map']['Town']['about'] = '''
You are in a small town with people bustling on the sidewalks.
You are approached by 3 vendors who wish to have you bear pelt in exchange for their service.
You can give only one of them the pelt, whoever you choose will
follow you throughout your journey. Choose wisely...
'''
    return '''
You picked up %s
''' % (item)

def follow_sound(world, command):
    '''
    Consumes a world and command and returns a statement indicating what the command did.
    Changes players location.

    Args:
        world (World): The current state of the world
        command (str): A command
    Returns:
        str: A statement indicating what the command did.
    '''
    location = world['player']['location']
    here = world['map'][location]
    for neighbor in here['neighbors']:
        if "Sound" in neighbor:
            world['player']['location'] = neighbor
    location = world['player']['location']
    here = world['map'][location]
    about = world['map'][location]['about']
    if world['map'][location]['enemy']:
        world['map']['Path H']['neighbors'].remove('Sound C')
        return '''
You followed the sound
''' + about + render_enemy(world)
    return '''
You followed the sound
'''

def follow_path(world, command):
    '''
    Consumes a world and command and returns a statement indicating what the command did.
    Changes players location.

    Args:
        world (World): The current state of the world
        command (str): A command
    Returns:
        str: A statement indicating what the command did.
    '''
    location = world['player']['location']
    here = world['map'][location]
    for neighbor in here['neighbors']:
        if "Path" in neighbor:
            world['player']['location'] = neighbor
    location = world['player']['location']
    here = world['map'][location]
    about = world['map'][location]['about']
    if world['map'][location]['enemy']:
        return '''
You followed the path.
''' + about + render_enemy(world)
    else:
        return '''
You followed the path.
'''

def revive_follower(world):
    '''
    Consumes a world and returns a statement indicating what the function did.
    Changes player follower state from False to True. Removes Revive Potion from inventory.

    Args:
        world (World): The current state of the world
        command (str): A command
    Returns:
        str: A statement indicating what the command did.
    '''
    world['player']['inventory'].remove("Revive Potion")
    world['player']['follower'] = True
    return '''
You revived your follower
'''

def amulet(world):
    '''
    Consumes a world and returns a statement indicating what the command did and the current state of the players amulet.
    Changes the state of the players amulet.

    Args:
        world (World): The current state of the world
    Returns:
        str: A statement indicating what the command did and state of amulet.
    '''
    location = world['player']['location']
    here = world['map'][location]
    inventory = world['player']['inventory']
    if world['player']['amulet uses'] < 3:
            world['player']['amulet uses'] = world['player']['amulet uses'] + 1
            if world['player']['amulet uses'] == 3:
                inventory.remove("Amulet")
                if "Revive Potion" in here['stuff']:
                    here['stuff'].remove("Revive Potion")
                    inventory.append("Revive Potion")
                    return '''
You use your amulet.
You see a revive potion mounted on the wall and you take it.
You have used up all the power the amulet has.
'''
                else:
                    return '''
You used your amulet.
You found nothing.
You have used up all the power the amulet has.
'''
            if "Revive Potion" in here['stuff']:
                here['stuff'].remove("Revive Potion")
                inventory.append("Revive Potion")
                return '''
You use your amulet.
You see a revive potion glowing through some dust and you take it.
'''
            else:
                return '''
You used your amulet.
You found nothing.
'''
    else:
        inventory.remove("Amulet")
        return '''
You have used up all the power the amulet has.
'''

def see_inventory(world):
    '''
    Consumes a world and returns a statement showing the players inventory.

    Args:
        world (World): The current state of the world
    Returns:
        str: The players inventory.
    '''
    inventory = world['player']['inventory']
    new_inventory = ", ".join(inventory)
    return "Inventory: " + new_inventory

def learn_spells(world):
    '''
    Consumes a world and returns a statement indicating what the player chose.
    Removes Sword from inventory and adds Spells. Changes players location.

    Args:
        world (World): The current state of the world
    Returns:
        str: A statement indicating that the player learned spells.
    '''
    world['player']['location'] = 'Path F'
    inventory = world['player']['inventory']
    inventory.remove("Sword")
    inventory.append("Spells")
    return '''
You learned Spells
'''

def keep_sword(world):
    '''
    Consumes a world and returns a statement indicating what the player chose.
    Changes players location.

    Args:
        world (World): The current state of the world
    Returns:
        str: A statement indicating that the player kept their sword.
    '''
    world['player']['location'] = 'Path F'
    return '''
You kept your Sword
'''

def eat_rations(world):
    '''
    Consumes a world and returns a statement indicating what the player did.
    Restores players health to 5. Removes Rations from inventory.

    Args:
        world (World): The current state of the world
    Returns:
        str: A statement indicating that the player ate rations.
    '''
    world['player']['health'] = 5
    world['player']['inventory'].remove("Rations")
    return '''
You ate your rations.
'''

def update(world, command):
    '''
    Consumes a world and a command and updates the world according to the
    command, also producing a message about the update that occurred. This
    function should modify the world given, not produce a new one.

    Args:
        world (World): The current world to modify.

    Returns:
        str: A message describing the change that occurred in the world.
    '''
    location = world['player']['location']
    here = world['map'][location]
    inventory = world['player']['inventory']
    if_follower = world['player']['follower']
    inventory = world['player']['inventory']
    foll_num = world['player']['follower num']
    followers = create_followers()
    if if_follower:
        follower = followers['Follower ' + str(foll_num)]['Name']

    if (command == "Get Benedek") or (command == "Get Adjorn") or (command == "Get Frons"):
        inventory.remove("Bear Pelt")
        return town(world, command)
    if foll_num > 3:
        follower = followers['Follower ' + foll_num]['Name']
    if command == "Go to Glowing House":
        return glowing_house(world)
    if command == "Eat Rations":
        return eat_rations(world)
    if command == "See Inventory":
        return see_inventory(world)
    if command == "Use Amulet":
        return amulet(world)
    if "Get" in command:
        return get(world, command)
    if "Go to" in command:
        return goto(world, command)
    if command == "Quit":
        world['status'] = 'quit'
        return ""
    if "Path" in command:
        return follow_path(world, command)
    if "Sound" in command:
        return follow_sound(world, command)
    if "Follow the Tracks" == command:
        return goto(world, command)
    if command == "Revive Follower":
        return revive_follower(world)
    if command == "Learn Spells":
        return learn_spells(world)
    if command == "Keep Sword":
        return keep_sword(world)

def render_ending(world):
    '''
    Create the message to be displayed at the end of your game.

    Args:
        world (World): The final world state to use in describing the ending.

    Returns:
        str: The ending text of your game to be displayed.
    '''
    if world['status'] == 'won':
        return "You Won!" + render_ending_won(world)
    elif world['status'] == 'lost':
        return "You Died!."
    elif world['status'] == 'quit':
        return "You Quit."

def render_ending_won(world):
    '''
    Consumes a world and returns a win statement based on the current state of the world.

    Args:
        world (World): The current state of the world.
    Returns:
        str: A win statement based on the current state of the world.
    '''
    if_follower = world['player']['follower']
    foll_num = world['player']['follower num']
    followers = create_followers()
    if if_follower:
        follower = followers['Follower ' + str(foll_num)]['Name']

    if 'Treasure' in world['player']['inventory']:
        if world['player']['follower']:
            return '''
Congratulations! You have slain the Dragon!
You and %s head home, you drop %s at his town and go home.
You have treasure and made the your whole home town rich!
You are now the most famous adventurer in the land!
''' % (follower, follower)
        else:
            return '''
Congratulations! You have slain the Dragon!
You head back home now.
You have treasure and made the your whole home town rich!
You are now the most famous adventurer in the land!
'''
    else:
        if world['player']['follower']:
            return '''
Congratulations! You have slain the Dragon!
You and %s head home, you drop %s at his town and go home.
Unfortunately you did not grab the treasure, therefore you town resents you.
You are the most hated Dragon slayer in the land.
''' % (follower, follower)
        else:
            return '''
Congratulations! You have slain the Dragon!
You head back home now.
Unfortunately you did not grab the treasure, therefore you town resents you.
You are the most hated Dragon slayer in the land.
'''

def choose(options):
    '''
    Consumes a list of commands, prints them for the user, takes in user input
    for the command that the user wants (prompting repeatedly until a valid
    command is chosen), and then returns the command that was chosen.

    Note:
        Use your answer to Programming Problem #42.3

    Args:
        options (list[str]): The potential commands to select from.

    Returns:
        str: The command that was selected by the user.
    '''
    choice = "choice"
    for command in options:
        print(command)
    while choice not in options:
    	choice = input()
    if choice in options:
        return choice


###### Win/Lose Paths #####

WIN_PATH = [
    "Go to Woods",
    "Follow the Sound",
    "Get Sword",
    "Go to Woods",
    "Go to Deep Woods",
    "Go to Cave",
    "Go to Deep Cave",
    "Get Armor",
    "Go to Woods",
    "Follow Path",
    "Go to Broken House",
    "Get Rations",
    "Follow the Sound",
    "Follow the Tracks",
    "Get Bear Pelt",
    "Follow Path",
    "Follow Path",
    "Go to Tunnel",
    "Use Amulet",
    "Follow Path",
    "Go to Town",
    "Get Adjorn",
    "Follow Path",
    "Go to Magic Gate",
    "Follow Path",
    "Follow Path",
    "Keep Sword",
    "Go to Glowing House",
    "Revive Follower",
    "Follow Path",
    "Follow Path",
    "Follow the Sound",
    "Get Shield",
    "Follow Path",
    "Go to Dragon Den",
    "Go to Treasury",
    "Get Treasure",
    "Go to Door",
    "Eat Rations",
    "Go to Dragon Fight"
]
LOSE_PATH = [
    "Go to Broken House",
    "Get Rations",
    "Follow the Sound",
    "Follow the Tracks"
    ]

###### Main Function #####

def main():
    '''
    Run your game using the Text Adventure console engine.
    Consumes and produces nothing, but prints and indirectly takes user input.
    '''
    print(render_introduction())
    world = create_world()
    while world['status'] == 'playing':
        print(render(world))
        options = get_options(world)
        command = choose(options)
        print(update(world, command))
    print(render_ending(world))

if __name__ == '__main__':
    main()
