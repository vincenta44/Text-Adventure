from cisc108 import assert_equal
from game import (
render_introduction,
create_player,
create_world,
create_followers,
create_map,
render,
render_location,
render_enemy,
tunnel,
bear,
path_e,
dragon_fight,
dragon_fight_sword,
dragon_fight_spells,
deep_cave,
glowing_house,
sound_c,
path_f,
town,
follow_path,
follow_sound)
###### Unit Tests #####

#render_introduction()
assert_equal('Hello adventurer...you have quite a journey ahead of you.' in render_introduction(), True)
assert_equal(render_introduction(), '''
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
''')

#create_player()
player = create_player()
assert_equal(isinstance(player, dict), True)
assert_equal(len(player.keys()), 6)
assert_equal("location" in player, True)
assert_equal(player['location'], 'Path A')
assert_equal("inventory" in player, True)
assert_equal(player['inventory'], ['Amulet'])

#create_world()
world = create_world()
assert_equal(isinstance(world, dict), True)
assert_equal('status' in world, True)
assert_equal('map' in world, True)
assert_equal('player' in world, True)
assert_equal(world['status'], 'playing')
assert_equal(world['map'], create_map())
assert_equal(isinstance(world['map'], dict), True)

#create_followers()
followers = create_followers()
assert_equal(len(followers.keys()), 3)
assert_equal(isinstance(followers, dict), True)
assert_equal('Follower 1' in followers, True)
assert_equal('Follower 2' in followers, True)
assert_equal('Follower 3' in followers, True)
assert_equal(followers['Follower 1']['Name'], "Adjorn")
assert_equal(followers['Follower 2']['Name'], "Benedek")
assert_equal(followers['Follower 3']['Name'], "Frons")

#create_map()
map = create_map()
assert_equal(len(map.keys()), 26)
assert_equal(isinstance(map, dict), True)
assert_equal(len(map['Path A'].keys()), 4)
assert_equal('about' in map['Path A'], True)
assert_equal('stuff' in map['Path A'], True)
assert_equal('enemy' in map['Path A'], True)
assert_equal('neighbors' in map['Path A'], True)
assert_equal(isinstance(map['Path A'], dict), True)
assert_equal(isinstance(map['Path A']['about'], str), True)
assert_equal(isinstance(map['Path A']['stuff'], list), True)
assert_equal(isinstance(map['Path A']['enemy'], bool), True)
assert_equal(isinstance(map['Path A']['neighbors'], list), True)

#render(x)
assert_equal(render(world), '\nThere is a fork in the road\nTo the right is the path,\nto the left are the woods,\nand next to you is a path to a broken down house.\nYour health is 5/5\n')

#render_location(x)
assert_equal(render_location(world), world['map']['Path A']['about'])

#render_enemy(x)
test_world = create_world()
test_world['player']['location'] = 'Bear'
assert_equal(render_enemy(test_world), bear(test_world))
test_world['player']['location'] = 'Tunnel'
assert_equal(render_enemy(test_world), tunnel(test_world))
test_world['player']['location'] = 'Path E'
assert_equal(render_enemy(test_world), path_e(test_world))
test_world['player']['location'] = 'Dragon Fight'
assert_equal(render_enemy(test_world), dragon_fight(test_world))
test_world['player']['location'] = 'Deep Cave'
assert_equal(render_enemy(test_world), deep_cave(test_world))
test_world['player']['location'] = 'Sound C'
assert_equal(render_enemy(test_world), sound_c(test_world))

#tunnel(x)
test_world = create_world()
assert_equal(tunnel(world), '''
You have nothing...you look around and find a rock.
You hurl the rock at the Troll, it only get's more upset.
You try to run, but the Troll catches up, grabs you and slams you around
until you die.
''')
test_world['player']['inventory'] = ["Sword"]
assert_equal(tunnel(test_world), '''
You wield your sword and face the troll. With little courage you scoot forward.
The Troll comes stomping at you and you dodge enough to slash it's back.
You thrust forward, but the Troll turns around and knocks you back.
You are cornered on the rocks. In a swift act of terror you scream and stab the troll.
The troll is now laying at your feet...It is slain.
''')

#bear(x)
assert_equal(bear(world), '''
You stare at the bear in terror.
It rushes you and attacks.
You have no way of defending yourself and you get mauled and die.
''')

#path_e(x)
assert_equal(path_e(world), '''
The witch disinigrates you immediatley.
How did you even make it this far with no armor or weapon?
''')

#dragon_fight(x)
assert_equal(dragon_fight(world), '''
You walk up to the dragon...nothing in hand...and you bow.
She creeps up on you and sniffs around.
She drags you to the middle of the room.
She lays back down on you and sleeps.
You slowly get crushed and suffocate.
You are dead.
''')

#dragon_fight_sword(x)
assert_equal(dragon_fight_sword(world), '''
You walk in and pull out you sword.
You charge...but before you get there she
blows fire at you and disengrates you completley.
You are dead.
''')

#dragon_fight_spells(x)
assert_equal(dragon_fight_spells(world), '''
You walk in and wield your spells.
You charge...but before you get there she
blows fire at you and disengrates you completley.
You are dead.
''')

#deep_cave(x)
assert_equal(deep_cave(world), '''
A Giant Spider drops down right on your head.
You have nothing to defend yourself ad you swing around in terror.
The spider ties you up...
waits 2 weeks...
Then eats you...
''')

#glowing_house(x)
assert_equal(glowing_house(world), None)

#sound_c(x)
assert_equal(sound_c(world), '''
Goblins jump all over you and stab you until you die.
''')

#path_f(x)
assert_equal(path_f(world), world['map']['Path A']['about'])

#town(x, y)
assert_equal(town(world, "Benedek"),
            '''
You chose Benedek. Good choice.
''')
assert_equal(town(world, "Frons"),
             '''
You chose Frons. Poor choice.
'''
)
assert_equal(town(world, "Adjorn"),
             '''
You chose Adjorn. Great choice!
'''
)

#follow_sound(x, y)
test_world = create_world()
test_world['player']['location'] = 'Path H'
assert_equal(follow_sound(test_world, 'Follow the Sound'),  '''
You followed the sound
You walk to the sound and before you know it
you are surrounded by a group of small goblins!
Goblins jump all over you and stab you until you die.
''')

#follow_path(x, y)
test_world = create_world()
test_world['player']['location'] = 'Sound C'
test_world['player']['inventory'] = ["Sword", "Armor", "Upgraded Armor"]
sound_c(test_world)
assert_equal(test_world['map']['Path H']['about'], '''
You are at a turn in the road.
You are now standing infront of the Dragon's den.
''')