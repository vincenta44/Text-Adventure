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
render_player,
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
follow_sound
)

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
test_world = create_world()
assert_equal(render(test_world), '\nThere is a fork in the road\nTo the right is the path,\nto the left are the woods,\nand next to you is a path to a broken down house.\nYour health is 5/5\n')
assert_equal(render(test_world), render_location(test_world) + render_player(test_world))

#render_location(x)
test_world = create_world()
assert_equal(render_location(test_world), test_world['map']['Path A']['about'])
test_world['player']['location'] = 'Path F'
assert_equal(render_location(test_world), path_f(test_world))

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

#render_player(x)
test_world = create_world()
assert_equal(render_player(test_world), "Your health is 5/5\n")
test_world['player']['health'] = 4
assert_equal(render_player(test_world), "Your health is 4/5\n")
test_world['player']['health'] = 3
assert_equal(render_player(test_world), "Your health is 3/5\n")
test_world['player']['health'] = 2
assert_equal(render_player(test_world), "Your health is 2/5\n")
test_world['player']['health'] = 1
assert_equal(render_player(test_world), "Your health is 1/5\n")

#tunnel(x)
test_world = create_world()
assert_equal(tunnel(test_world), '''
You have nothing...you look around and find a rock.
You hurl the rock at the Troll, it only get's more upset.
You try to run, but the Troll catches up, grabs you and slams you around
until you die.
''')

test_world = create_world()
test_world['player']['inventory'] = ["Sword"]
assert_equal(tunnel(test_world), '''
You wield your sword and face the troll. With little courage you scoot forward.
The Troll comes stomping at you and you dodge enough to slash it's back.
You thrust forward, but the Troll turns around and knocks you back.
You are cornered on the rocks. In a swift act of terror you scream and stab the troll.
The troll is now laying at your feet...It is slain.
''')
assert_equal(test_world['map']['Tunnel']['about'], '''
You can move forward from this dimly lit tunnel.
''')
test_world['player']['health'] = 2
assert_equal(tunnel(test_world), '''
You wield your sword and face the troll. With little courage you scoot forward.
The Troll comes stomping at you and you dodge enough to slash it's back.
You thrust forward, but the Troll turns around and knocks you back.
You are cornered on the rocks. He slaps the sword out of your hand and crushes you.
You died.
''')

test_world = create_world()
test_world['player']['inventory'] = ["Sword", "Armor"]
assert_equal(tunnel(test_world), '''
You wield your sword and face the Troll. Puffing out your armor, you attack.
You slash at his feet while he smacks your chest. Your armor defends the attack.
You slash again, but in a more lethal spot. You get it through the back.
It kneels and dies. You have slain the troll.
''')
assert_equal(test_world['map']['Tunnel']['about'], '''
You can move forward from this dimly lit tunnel.
''')

#bear(x)
test_world = create_world()
assert_equal(bear(test_world), '''
You stare at the bear in terror.
It rushes you and attacks.
You have no way of defending yourself and you get mauled and die.
''')

test_world = create_world()
test_world['player']['inventory'] = ["Sword"]
assert_equal(bear(test_world), '''
You unsheathe your sword and stand your ground.
The bear rushes at you and swiftly move to the side.
You thrash at it with your sword. The bear turns toward you and claws your chest.
You take a few claws to the chest, but with your sword out you are able to stab
the bear in the head. You killed the bear.
''')
assert_equal(test_world['map']['Bear']['about'], '''
The bear is slain and you may skin it.
You may move forward.
''')
test_world['player']['health'] = 2
assert_equal(bear(test_world), '''
You unsheathe your sword and stand your ground.
The bear rushes at you and swiftly move to the side.
You thrash at it with your sword. The bear turns toward you and claws your chest.
You take a few too many slashes to the chest.
You died.
''')

test_world = create_world()
test_world['player']['inventory'] = ["Sword", "Armor"]
assert_equal(bear(test_world), '''
You bring out your sword and wave it at the bear.
It charges you and tackles you, making you drop your sword.
It is biting and clawing at your chest but your armor deflects the blows.
This gives you time, you reach for your sword and stab its side.
The bear leaps off of you and you spring up and stab it one more time.
This finishes the bear.
''')
assert_equal(test_world['map']['Bear']['about'], '''
The bear is slain and you may skin it.
You may move forward.
''')

#path_e(x)
test_world = create_world()
assert_equal(path_e(test_world), '''
The witch disintegrates you immediately.
How did you even make it this far with no armor or weapon?
''')

test_world = create_world()
test_world['player']['inventory'] = ["Sword"]
assert_equal(path_e(test_world), '''
You run up sword in hand.
The witch jumps and dodges you.
You turn and slash the witches face,
but she manifested a fireball and blew it straight through you.
You died.
''')

test_world = create_world()
test_world['player']['inventory'] = ["Sword", "Armor"]
assert_equal(path_e(test_world), '''
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
''')
test_world['player']['health'] = 2
assert_equal(path_e(test_world), '''
A Witch springs out of the darkness...wielding spells.
The witch stares you down. She starts glowing then attacks.
Her spells shoot at you, but you manage to dive away.
She shoots again this time burning your arm.
You manage to dodge a few shots and you rush her.
You jab your sword through her, she turns and casts a spell at you.
Your armor withstands the blow and you pull your sword out,
before you can slash she casts a fireball that melts through your armor and you.
You died.
''')

test_world = create_world()
test_world['player']['inventory'] = ["Sword", "Armor"]
test_world['player']['follower'] = True
test_world['player']['follower num'] = 2
assert_equal(path_e(test_world), '''
A Witch springs out of the darkness...wielding spells.
Benedek jumps in front to attack first.
You bring out your sword and rush with him.
She casts a spell at your follower, and he gets struck back.
This distraction give you time to pursue.
You jab your sword through her, she turns and casts a spell at you.
Your armor withstands the blow and you pull your sword out.
You jab again kill her.
    She has a book of spells on her.
    You can read the book and learn the spells,
    however you will lose your sword.
''')
test_world['player']['health'] = 1
assert_equal(path_e(test_world), '''
A Witch springs out of the darkness...wielding spells.
Benedek jumps in front to attack first.
You bring out your sword and rush with him.
She casts a spell at your follower, and he gets struck back.
This distraction give you time to pursue.
You jab your sword through her, she turns and casts a spell at you.
Your armor withstands the blow and you pull your sword out,
before you can slash she casts a fireball that melts through your armor and you.
You died.
''')

#dragon_fight(x)
test_world = create_world()
assert_equal(dragon_fight(test_world), '''
You walk up to the dragon...nothing in hand...and you bow.
She creeps up on you and sniffs around.
She drags you to the middle of the room.
She lays back down on you and sleeps.
You slowly get crushed and suffocate.
You are dead.
''')

test_world = create_world()
test_world['player']['inventory'] = ["Sword"]
assert_equal(dragon_fight(test_world), dragon_fight_sword(test_world))

test_world = create_world()
test_world['player']['inventory'] = ["Spells"]
assert_equal(dragon_fight(test_world), dragon_fight_spells(test_world))

#dragon_fight_sword(x)
test_world = create_world()
assert_equal(dragon_fight_sword(test_world), '''
You walk in and pull out you sword.
You charge...but before you get there she
blows fire at you and disintegrates you completely.
You are dead.
''')
test_world = create_world()

test_world['player']['inventory'] = ["Sword", "Armor"]
assert_equal(dragon_fight_sword(test_world), '''
You walk in and pull out your sword.
You armor doesn't seem so strong next to her scales.
You charge and she swipes you with her tail.
Your armor breaks apart and falls right off of you.
You try to get up and move away, but she catches you and eats you.
You are dead.
''')
assert_equal(test_world['status'], 'lost')

test_world = create_world()
test_world['player']['inventory'] = ["Sword", "Armor", "Upgraded Armor", "Shield"]
test_world['player']['follower'] = True
test_world['player']['follower num'] = 2
assert_equal(dragon_fight_sword(test_world), '''
You pull out your sword, puff out your armor and move forward.
Benedek moves at your side. You both now charge.
The dragon focuses on Benedek and moves toward him.
You move around the back while she's is distracted.
She slaps you with her tail, but you block it with your shield.
You shield flies away from you, but you move forward.
you climb her and throws you off her tail onto the cave wall.
Your armor stops glowing. Benedek take the opportunity and stabs her in the chest.
You pick yourself up and run forward and jump onto her wing then to her back.
You crawl up her neck and get to head, you stab your sword through her.
She falls...You killed the dragon!
''')
assert_equal(test_world['status'], 'won')
test_world['player']['health'] = 1
assert_equal(dragon_fight_sword(test_world), '''
You pull out your sword, puff out your armor and move forward.
Benedek moves at your side. You both now charge.
The dragon focuses on Benedek and moves toward him.
You move around the back while she's is distracted.
She slaps you with her tail, but you block it with your shield.
You shield flies away from you, but you move forward.
you climb her and throws you off her tail onto the cave wall.
Your armor stops glowing. Benedek take the opportunity and stabs her in the chest.
You pick yourself up and run forward and jump onto her wing then to her back.
You crawl up her neck and get to head, but you stumble and fall.
The dragon kills Benedek then eats you.
You Died.
''')
assert_equal(test_world['status'], 'lost')

test_world = create_world()
test_world['player']['inventory'] = ["Sword", "Armor", "Upgraded Armor"]
test_world['player']['follower'] = True
test_world['player']['follower num'] = 2
assert_equal(dragon_fight_sword(test_world), '''
You pull out your sword, puff out your armor and move forward.
Benedek moves at your side. You both now charge.
The dragon focuses on Benedek and moves toward him.
You move around the back while she's is distracted.
You jump up on her tail. In one motion she grabs Benedek with her teeth
and throws you off her tail onto the cave wall.
Benedek is on the ground not moving. Your armor stops glowing.
You pick yourself up and run forward and jump onto her wing then to her back.
You crawl up her neck and get to head, you stab your sword through her.
She falls...You killed the dragon!
''')
assert_equal(test_world['status'], 'won')
test_world['player']['health'] = 2
assert_equal(dragon_fight_sword(test_world), '''
You pull out your sword, puff out your armor and move forward.
Benedek moves at your side. You both now charge.
The dragon focuses on Benedek and moves toward him.
You move around the back while she's is distracted.
You jump up on her tail. In one motion she grabs Benedek with her teeth
and throws you off her tail onto the cave wall.
Benedek is on the ground not moving. Your armor stops glowing.
You pick yourself up and run forward and jump onto her wing then to her back.
You crawl up her neck and get to head, but you stumble and fall.
The dragon kills Benedek then eats you.
You Died.
''')
assert_equal(test_world['status'], 'lost')

test_world = create_world()
test_world['player']['inventory'] = ["Sword", "Armor", "Upgraded Armor"]
assert_equal(dragon_fight_sword(test_world), '''
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
''')
assert_equal(test_world['status'], 'won')
test_world['player']['health'] = 3
assert_equal(dragon_fight_sword(test_world), '''
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
''')
assert_equal(test_world['status'], 'lost')

test_world = create_world()
test_world['player']['inventory'] = ["Sword", "Armor", "Upgraded Armor", "Shield"]
assert_equal(dragon_fight_sword(test_world), '''
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
''')
assert_equal(test_world['status'], 'won')
test_world['player']['health'] = 2
assert_equal(dragon_fight_sword(test_world), '''
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
''')
assert_equal(test_world['status'], 'lost')

test_world = create_world()
test_world['player']['inventory'] = ["Sword", "Armor"]
test_world['player']['follower'] = True
test_world['player']['follower num'] = 2
assert_equal(dragon_fight_sword(test_world), '''
You pull out your sword, puff out your armor and move forward.
Benedek moves at your side. You both now charge.
The dragon focuses on Benedek and moves toward him.
You move around out of her vision.
She clamps on Benedek with her jaw and flails him around.
You stab her from behind and she lets go of Benedek.
She whips you with her tail, knocking you back and causing your glowing armor to fade.
While you are on the ground she stand tall and takes a snap at you.
Benedek jumps in the way at the last second and takes the blow.
He dies...but with haste you get up and slide underneath the dragon.
You rapidly stab her and then roll out from under her.
She falls and dies. The Dragon is slain.
''')
assert_equal(test_world['status'], 'won')
test_world['player']['health'] = 3
assert_equal(dragon_fight_sword(test_world), '''
You pull out your sword, puff out your armor and move forward.
Benedek moves at your side. You both now charge.
The dragon focuses on Benedek and moves toward him.
You move around out of her vision.
She clamps on Benedek with her jaw and flails him around.
You stab her from behind and she lets go of Benedek.
She whips you with her tail, knocking you back and causing your glowing armor to fade.
While you are on the ground she stand tall and takes a snap at you.
Benedek jumps in the way at the last second and takes the blow.
He dies...you fall back but she stomps toward you.
She stands and blows fire on you.
You died.
''')
assert_equal(test_world['status'], 'lost')

test_world = create_world()
test_world['player']['inventory'] = ["Sword", "Armor", "Shield"]
test_world['player']['follower'] = True
test_world['player']['follower num'] = 2
assert_equal(dragon_fight_sword(test_world), '''
You pull out your sword, puff out your armor and move forward.
Benedek moves at your side. You both now charge.
The dragon focuses on you and moves toward you.
Benedek moves around out of her vision.
She clamps on you with her jaw and flails you around.
Benedek stabs her from behind and she lets go of you.
Your glowing armor fades away. She focuses on Benedek
You pick yourself up and run forward and bash her head with your shield.
Now you both stab mount her wings and slash her.
Together you stab her neck...she flies up...
you jump off, but Benedek gets crushed at the top of the cave.
The dragon falls and lays dead.
The dragon is slain.
''')
assert_equal(test_world['status'], 'won')
test_world['player']['health'] = 2
assert_equal(dragon_fight_sword(test_world), '''
You pull out your sword, puff out your armor and move forward.
Benedek moves at your side. You both now charge.
The dragon focuses on you and moves toward you.
Benedek moves around out of her vision.
She clamps on you with her jaw and flails you around.
Benedek stabs her from behind and she lets go of you.
Your glowing armor fades away. She focuses on Benedek
You pick yourself up and run forward and bash her head with your shield.
Now you both stab mount her wings and slash her.
You stumble and try to grab Benedek, but you knock him off and he lands and dies.
You fall off the other side and the dragon stand over you then eats you.
You died.
''')
assert_equal(test_world['status'], 'lost')

test_world = create_world()
test_world['player']['inventory'] = ["Sword", "Armor", "Shield"]
assert_equal(dragon_fight_sword(test_world), '''
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
''')
assert_equal(test_world['status'], 'won')
test_world['player']['health'] = 3
assert_equal(dragon_fight_sword(test_world), '''
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
''')
assert_equal(test_world['status'], 'lost')

#dragon_fight_spells(x)
test_world = create_world()
assert_equal(dragon_fight_spells(test_world), '''
You walk in and wield your spells.
You charge...but before you get there she
blows fire at you and disintegrates you completely.
You are dead.
''')

test_world['player']['inventory'] = ["Spells", "Armor"]
assert_equal(dragon_fight_spells(test_world), '''
You walk in and wield your spells.
You charge...but before you get there she
blows fire at you and melts your armor.
You try to run back, but she flies toward you and eats you.
You are dead.
''')
assert_equal(test_world['status'], 'lost')

test_world = create_world()
test_world['player']['inventory'] = ["Spells", "Armor", "Upgraded Armor"]
test_world['player']['follower'] = True
test_world['player']['follower num'] = 2
assert_equal(dragon_fight_spells(test_world), '''
You wield your spells, puff out your armor and move forward.
Benedek moves at your side. You both now charge.
The dragon focuses on Benedek and moves toward him.
You move around the back while she's is distracted.
She slaps you with her tail and you get knocked back.
you climb her and throws you off her tail onto the cave wall.
Your armor stops glowing. Benedek take the opportunity and stabs her in the chest.
You pick yourself up and run forward and aim your spells at her.
With great power you cast your spells and engulf her in pain.
You stand your ground while she slowly gets weaker.
Benedek climbs on her and finished her off.
The Dragon is slain.
''')
assert_equal(test_world['status'], 'won')
test_world['player']['health'] = 2
assert_equal(dragon_fight_spells(test_world), '''
You wield your spells, puff out your armor and move forward.
Benedek moves at your side. You both now charge.
The dragon focuses on Benedek and moves toward him.
You move around the back while she's is distracted.
She slaps you with her tail and you get knocked back.
you climb her and throws you off her tail onto the cave wall.
Your armor stops glowing. Benedek take the opportunity and stabs her in the chest.
You pick yourself up and run forward and aim your spells at her.
With great power you cast your spells and engulf her in pain.
The spells get too powerful and you get knocked back.
You and Benedek get eaten.
You died.
''')
assert_equal(test_world['status'], 'lost')

test_world = create_world()
test_world['player']['inventory'] = ["Spells", "Armor", "Upgraded Armor"]
assert_equal(dragon_fight_spells(test_world), '''
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
''')
assert_equal(test_world['status'], 'won')
test_world['player']['health'] = 3
assert_equal(dragon_fight_spells(test_world), '''
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
''')
assert_equal(test_world['status'], 'lost')

test_world = create_world()
test_world['player']['inventory'] = ["Spells", "Armor"]
test_world['player']['follower'] = True
test_world['player']['follower num'] = 2
assert_equal(dragon_fight_spells(test_world), '''
You wield your spells, puff out your armor and move forward.
Benedek moves at your side. You both now charge.
The dragon focuses on Benedek and moves toward him.
You move around the back while she's is distracted.
She slaps you with her tail and you get knocked back.
you climb her and throws you off her tail onto the cave wall.
Your armor breaks off of your body. Benedek take the opportunity and stabs her in the chest.
You pick yourself up and run forward and aim your spells at her.
With great power you cast your spells and engulf her in pain.
You stand your ground while she slowly gets weaker.
Benedek climbs on her and she slips him off and he lands on a rock that impales him.
You scream and enhance your spells which drain your power, but she slowly falls.
The Dragon is slain.
''')
assert_equal(test_world['status'], 'won')
test_world['player']['health'] = 2
assert_equal(dragon_fight_spells(test_world), '''
You wield your spells, puff out your armor and move forward.
Benedek moves at your side. You both now charge.
The dragon focuses on Benedek and moves toward him.
You move around the back while she's is distracted.
She slaps you with her tail and you get knocked back.
you climb her and throws you off her tail onto the cave wall.
Your armor breaks off of your body. Benedek take the opportunity and stabs her in the chest.
You pick yourself up and run forward and aim your spells at her.
With great power you cast your spells and engulf her in pain.
You stand your ground while she slowly gets weaker.
Benedek climbs on her and she slips him off and he lands on a rock that impales him.
With great power you cast your spells and engulf her in pain.
The spells get too powerful and you get knocked back.
She stands over you and eats you.
You died.
''')
assert_equal(test_world['status'], 'lost')

#deep_cave(x)
test_world = create_world()
assert_equal(deep_cave(test_world), '''
A Giant Spider drops down right on your head.
You have nothing to defend yourself ad you swing around in terror.
The spider ties you up...
waits 2 weeks...
Then eats you...
''')

test_world = create_world()
test_world['player']['inventory'] = ["Sword"]
assert_equal(deep_cave(test_world), '''
A Giant Spider jumps down from the top of the cave.
You pull out you sword and charge.
You get bitten once but with swift justice you
stab it in the head. The spider is killed.
''')
test_world['player']['health'] = 1
assert_equal(deep_cave(test_world), '''
A Giant Spider jumps down from the top of the cave.
You pull out you sword and charge.
You get bitten once and can't react fast enough
and get bitten again and again and again...
until you die.
''')
assert_equal(test_world['status'], 'lost')


#glowing_house(x)
test_world = create_world()
assert_equal(glowing_house(test_world), None)

#sound_c(x)
test_world = create_world()
assert_equal(sound_c(test_world), '''
Goblins jump all over you and stab you until you die.
''')

#path_f(x)
test_world = create_world()
assert_equal(path_f(test_world), world['map']['Path A']['about'])

#town(x, y)
test_world = create_world()
assert_equal(town(test_world, "Benedek"),
            '''
You chose Benedek. Good choice.
''')
assert_equal(town(test_world, "Frons"),
             '''
You chose Frons. Poor choice.
'''
)
assert_equal(town(test_world, "Adjorn"),
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
You are now standing in front of the Dragon's den.
''')
