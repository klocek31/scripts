#shitty but it works
#propably gonna add more ores etc because im too lazy to use a fucking calculator


# calculates how much XP is needed until the next level
def next_level(c_level):
    if c_level <= 15 and c_level > 0:
        return (2*c_level) + 7
    elif c_level >= 16 and c_level <= 30:
        return (5*c_level) - 38
    elif c_level >= 31:
        return (9*c_level) - 158
    elif c_level == 0:
        return 7
    else:
        pass


# calculates how much total XP does a player have
def total_exp(c_level):
    if c_level <= 16 and c_level > 0:
        return pow(c_level, 2) + (6 * c_level)
    elif c_level >= 17 and c_level <= 31:
        return (2.5 * pow(c_level, 2)) - (40.5 * c_level) + 360
    elif c_level >= 32:
        return (4.5 * pow(c_level, 2)) - (162.5 * c_level) + 2220
    else:
        pass

# calculates how much XP is needed for the target lvl
def how_much_till_level(c_level, d_level):
    l_counter = int(c_level)
    xp_counter = 0
    while l_counter != d_level:
        xp_counter = xp_counter + next_level(l_counter)
        l_counter = l_counter + 1

    return xp_counter

def num_of_ores(hwtl_xp, ore):
    return how_much_till_level(c_level, d_level) / float(((ore[-1][0] + ore[-1][1]) / 2))
# lists of objects lol
o1 = ["coal_ore", [0, 2]]
o2 = ["nether_gold_ore", [0, 1]]
o3 = ["diamond_ore", "emerald_ore", [3, 7]]
o4 = ["lapis_ore", "quartz_ore", [2, 5]]
o5 = ["redstone_ore", [1, 5]]
o6 = ["monster_spawner", [15, 43]]
o7 = ["sculk", [1, 1]]
o8 = ["sculk_sensor", "sculk_shrieker", "sculk_catalyst", "calibrated_sculk_sensor", [5, 5]]

#did i mention that i cant code?


c_level = int(input("Enter your current level: "))
d_level = int(input("Enter the target level: "))
g_hwtl_xp = how_much_till_level(c_level, d_level)
g_ore = 'o' + str(input('''What are you planning on mining? (Type a number)
1. Coal Ore
2. Nether Gold Ore
3. Diamond Ore or Emerald Ore
4. Lapis Ore or Quartz Ore
5. Redstone Ore
6. Monster Spawner (why)
7. Sculk
8. Sculk Sensor, Sculk Shrieker, Sculk Catalyst or Calibrated Sculk Sensor: '''))
g_ore1 = globals()[g_ore]
import os
os.system("cls")
print(num_of_ores(g_hwtl_xp, g_ore1))