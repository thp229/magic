import random as r

##
types = ["fire","thunder","ice","earth","wind","aquatic","shadow","holy","toxic","dragon","astral","metal","nature",None]

#hello
#develop

#abilities
# ={
#versatility
#deep wounds
#airborne
#stagger

#ephemeral touch
#divine blessing
#adaptability
#tidewwalking
#withering touch
#chaotic winds
#enrage
#nimble
#fear
#molten

#}


moves = {"attack":{
#attack format name, [attack power, types, magic == 1 physical == 0 ]
#break down moves into classes
    #utility moves
    #damadge/utility
"ice barrage":[80,types[2],1],
"dark wave":[80,types[6],1],
"flare":[80,types[0],1],
"torrent":[70,types[5],1],
"shockwave":[80,types[1],1],
"fissure":[90,types[3],0],
"hurricane":[80,types[4],1],
"radiance":[70,types[7],1],
"infect":[80,types[8],1],
"rage burst":[90,types[9],0],
"ice smash":[70,types[2],0],
"flame smash":[70,types[0],0],
"tidal smash":[80,types[2],0],
"static shock":[70,types[1],0],
"mudslide":[70,types[3],1],
"aeroslash":[70,types[4],0],
"spectral slash":[70,types[6],0],
"thorns":[60,types[8],0]
}
#utility_moves
#damadge/utility_moves
}

#note that with spirits::
#index 2 = HP, 3 = Strength, 4 = Defense, 5 = Attune, 6 = Resist, 7 = Agility

#change the spirits to dictionaries rather than arrays

spirits = {
"cold scary ghost":[types[2],types[6],220,180,130,300,150,340],
"not charmander":[types[0],types[len(types)-1],250,200,150,300,160,320],
"nessie":[types[5],types[9],410,100,250,210,330,150],
"generic dragon":[types[4],types[9],230,300,250,220,190,300],
"badass divine dragon":[types[7],types[9],320,200,200,230,180,250],
"fire snake":[types[8],types[0],240,260,150,190,180,310],
"siren":[types[5],types[len(types)-1],310,120,180,280,230,280],
"nasty mothafucka":[types[8],types[len(types)-1],280,200,140,300,250,200],
"dust":[types[3],types[4],250,210,280,230,170,290],
"not pikachu":[types[1],types[len(types)-1],200,150,140,250,200,400],
"spooky":[types[6],types[len(types)-1],330,180,220,170,290,280],
"jesus":[types[7],types[len(types)-1],330,90,180,240,400,220],
"storm demon":[types[1],types[6],280,250,180,260,150,330],
"thunder bird":[types[4],types[1],250,250,190,260,200,350],
"brick dog":[types[2],types[len(types)-1],250,280,100,170,230,340]
#plus more spirits
}


def type_mod(playerX_type, playerY_type):

    type_matrix = [types,
    [0.5,1,0.5,2,2,2,1,1,1,1,1,0.5,0.5,0],
    [2,1,1,2,1,1,0.5,1,1,1,1,0.5,1,0],
    [2,1,0.5,2,0.5,1,1,1,1,1,1,2,1,0],
    [0.5,0,2,1,2,2,1,1,0.5,1,1,1,2,0],
    [1,2,2,0.5,1,1,1,1,1,1,1,1,0.5,0],
    [.5,2,2,.5,1,.5,1,1,1,1,1,1,2,0],
    [1,2,1,1,1,1,1,2,.5,2,.5,1,1,0],
    [1,.5,1,1,.5,1,2,.5,1,2,2,1,1,0],
    [2,1,1,2,1,.5,1,1,0,1,1,1,.5,0],
    [.5,2,.5,.5,1,1,.5,0,2,1,1,1,.5,0],
    [1,1,1,1,1,1,1,2,.5,2,1,2,1,0],
    [2,1,.5,2,.5,1,1,1,.5,.5,.5,.5,.5,0],
    [2,.5,2,.5,2,.5,1,1,2,1,1,1,.5,0],
    [1]*13+[0] ]

    types_to_nums = {
    "fire":1,
    "thunder":2,
    "ice":3,
    "earth":4,
    "wind":5,
    "aquatic":6,
    "shadow":7,
    "holy":8,
    "toxic":9,
    "dragon":10,
    "astral":11,
    "metal":12,
    "nature":13,
    None:14
    }

    mod_x = 1
    attack_index = type_matrix[0].index(playerX_type)
    for type in playerY_type:
        mod_x = mod_x * type_matrix[types_to_nums[type]][attack_index]
    return mod_x


def stab_mod(playerX_spiritType,playerX_attackType):
    if playerX_attackType in playerX_spiritType:
        return 1.5
    else:
        return 1

def damageX_onto_Y():

    #playerX attacking playerY , calculate damadge done by player X onto Y

    #D = (2 * Attack Power * (Strength/Defense))/5 * modifier
    #Defense = need playerY_spirit_defense_Stat
    #Strength = need playerX_strength_Stat
    #Attack Power = first index of currently chosen attack type <int power>
    #modifer = type_mod * stab_mod
        #type_mod
            #need playerX_attack_type
            #need playerY_spirit_type

        #stab_mod
            #need playerX_attack_type
            #need playerX_spirit_type

    #in order for this function to work, player1 must have set an attack

    #also must have set an active spirit

    #gather player spirit stats
    defense = player2.get_spirit()[4]
    strength = player1.get_spirit()[3]
    attunement = player1.get_spirit()[5]
    resistance = player2.get_spirit()[6]
    #gather player attack data
    try:
        att_power = player1.get_player_attack()[0]
        att_type = player1.get_player_attack()[1]
    except:
        print("Player 1 must have an attack choosen.")
        print()
        return

    #gather bh player spirit types
    spirit_type1 = player1.return_player_spiritTypes()
    spirit_type2 = player2.return_player_spiritTypes()

    #calculate mods
    T_mod = type_mod(att_type,spirit_type2)
    S_mod = stab_mod(spirit_type1,att_type)
    final_mods = T_mod * S_mod

    #final damage calculation
    if player1.get_player_attack()[2] == 0:
        str_over_def = strength/defense
        D = ((2 * att_power * str_over_def)/5)*final_mods
        return int(D)
    else:
        att_over_res = attunement/resistance
        D = ((2 * att_power * att_over_res)/5)*final_mods
        return int(D)

def damageY_onto_X():
    defense = player1.get_spirit()[4]
    strength = player2.get_spirit()[3]
    attunement = player2.get_spirit()[5]
    resistance = player1.get_spirit()[6]
    try:
        att_power = player2.get_player_attack()[0]
        att_type = player2.get_player_attack()[1]
    except:
        print("Player 2 must have an attack chosen.")
        print()
        return

    spirit_type1 = player2.return_player_spiritTypes()
    spirit_type2 = player1.return_player_spiritTypes()

    T_mod = type_mod(att_type,spirit_type2)
    S_mod = stab_mod(spirit_type1,att_type)
    final_mods = T_mod * S_mod
    #final damage calculation
    if player2.get_player_attack()[2] == 0:
        str_over_def = strength/defense
        D = ((2 * att_power * str_over_def)/5)*final_mods
        return int(D)
    else:
        att_over_res = attunement/resistance
        D = ((2 * att_power * att_over_res)/5)*final_mods
        return int(D)


def check_agility():
    if player1.get_spirit()[7] > player2.get_spirit()[7]:
        return True
        #so return True means that player1 goes first
        #their damadge happens before the death check
    elif player1.get_spirit()[7] < player2.get_spirit()[7]:
        return False
    else:
        return r.choice([True,False])
        #otherwise player 2 goes first


list_moves = list(moves["attack"].keys())

class Player:
    def __init__(self):
        self.playerX_team = {}
        self.playerX_spirit = []
        self.playerX_attack = []
        self.playerX_switch_or_attack = 0

    def set_spirits(self):
        for x in range(5):
            if x != 0:
                spirit_choice = input("Choose spirit #"+str(x+1)+ "\n" + "<or press E.N.T.E.R. if finished building team>"+": ")
            else:
                spirit_choice = input("Choose spirit #"+str(x+1)+": ")
            self.playerX_team[spirit_choice.lower()] = spirits[spirit_choice.lower()]
            print()
            print("You choose",spirit_choice.title())
            moves = []
            for y in range(4):
                move_choice = input("Choose a move: ")
                while True:
                    if move_choice not in moves and move_choice in list_moves:
                        break
                    else:
                        print("Choose a new move.")
                        print()
                        move_choice = input("Choose a move: ")
                moves.append(move_choice.lower())
            self.playerX_team[spirit_choice].append(moves)
            print()

    def get_spirit(self):
        if len(self.playerX_spirit) == 0:
            return None
        else:
            return self.playerX_spirit

    def attack_or_switch(self):
        choice = input("Attack or Switch?: ")
        print()
        if choice.lower() == "attack":
            self.set_player_attack()
            self.playerX_switch_or_attack = 0
        elif choice.lower() == "switch":
            self.switch_spirits()
            self.playerX_switch_or_attack = 1

    def return_player_spiritTypes(self):
        #input: current spirit chosen by the player
        #output: their c
        return self.playerX_spirit[:2]


    def set_player_attack(self):

        attack_list = ""
        i = 0
        for attack_names in self.playerX_spirit[len(self.playerX_spirit)-1]:
            attack_list += "<"+str(i+1)+">" + attack_names.title() + "  "
            i += 1
        print(attack_list)
        print()

        attack_choice = input("Choose an attack: ")
        if attack_choice.lower() in self.playerX_spirit[len(self.playerX_spirit)-1]:
            self.playerX_attack = moves["attack"][attack_choice]
        else:
            print("Move not available.")
            print()
            while True:
                attack_choice = input("Choose an attack: ")
                if attack_choice.lower() in self.playerX_spirit[len(self.playerX_spirit)-1]:
                    self.playerX_attack = moves["attack"][attack_choice]
                    break

                else:
                    print("Move not available.")
                    print()

    def reset_player_attack(self):
        self.playerX_attack = []

    def get_player_attack(self):
        if len(self.playerX_attack) == 0:
            return None
        else:
            return self.playerX_attack

    def switch_spirits(self):
        spirit_list = ""
        for spirit_names in list(self.playerX_team.keys()):
            spirit_list += " >"+spirit_names.title() +"   "+"HP:" + str(self.playerX_team[spirit_names][2]) + "\n"
        print(spirit_list)
        print()
        spirit_choice = input("Choose a spirit: ")
        if spirit_choice in self.playerX_team.keys():
            self.playerX_spirit = self.playerX_team[spirit_choice]
        else:
            print("Spirit not available.")
            print()
            while True:
                spirit_choice = input("Choose a spirit: ")
                if spirit_choice in self.playerX_team.keys():
                    self.playerX_spirit = self.playerX_team[spirit_choice]
                    break
                else:
                    print("Spirit not available.")
                    print()

    def death_check(self):
        if self.playerX_spirit[2] <= 0:
            return True
        else:
            return False

    def remove_dead_spirit(self):
        for key in list(self.playerX_team.keys()):
            if self.playerX_team[key] == self.playerX_spirit:
                del self.playerX_team[key]

    def player_lose(self):
        if len(self.playerX_team.keys()) == 0:
            return True
        else:
            return False


def print_spirit_stats(spirit_list):

    stats = ""
    stats += "\n"
    stats += "Types:" + "\n"
    for x in spirit_list[:2]:
        if x is not None:
            stats += " >"+x.title() + "\n"
        else:
            stats += ""
    stats += "\n"
    stats += " HP:" + str(spirit_list[2]) + "\n"
    stats += " Strength:" + str(spirit_list[3]) + "\n"
    stats += " Defense:" + str(spirit_list[4]) + "\n"
    stats += " Attunement:" + str(spirit_list[5]) + "\n"
    stats += " Resistance:" + str(spirit_list[6]) + "\n"
    stats += " Agility:" + str(spirit_list[7]) + "\n"
    stats += "\n"
    stats += "\n"
    return stats


def title():
    spirit_names = "" + "\n"
    spirit_names += ">>>>S.p.i.r.i.t.s.<<<<" + "\n" + "\n"
    for x,values in spirits.items():
        spirit_names += "*" + x.title() + "\n"
        spirit_names += print_spirit_stats(values)

    moves_names = ""
    moves_names += ">>>>M.o.v.e.s.<<<<" + "\n" + "\n" + "   << A t t a c k s >>" + "\n" + "\n"

    i = 0
    for x in moves["attack"].keys():
        if i % 2 == 0:
            moves_names += " * " + x.title()
        else:
            moves_names += format(" * "+x.title(), "<75s") + "\n"
        i += 1

    print(spirit_names)
    print()
    print(moves_names)


def start_game():
    title()
    print("----Player 1----")

    try:
        player1.set_spirits()
    except:
        print()

    empty_space = ""
    for x in range(7):
        empty_space += " " + "\n"
    print(empty_space)

    title()
    print("----Player 2----")
    try:
        player2.set_spirits()
    except:
        print()

    empty_space = ""
    for x in range(7):
        empty_space += " " + "\n"
    print(empty_space)

    #set spirits

    print("Choose your starting spirits!")
    print()
    print("----Player 1 <<S.p.i.r.i.t.s.>>----")
    print()
    player1.switch_spirits()

    print()
    print("----Player 2 <<S.p.i.r.i.t.s.>>----")
    print()
    player2.switch_spirits()

    print()
    print()
    print("------------------------")
    print("| Let The Games Begin! |")
    print("------------------------")


########################################################
#######            main game loop                #######
########################################################

player1 = Player()
player2 = Player()
start_game()

while True:
    print("-----Player 1-----")
    print()
    player1.attack_or_switch()
    print("-----Player 2-----")
    print()
    player2.attack_or_switch()

    #both players decide to attack that turn
    if player1.playerX_switch_or_attack == 0 and player2.playerX_switch_or_attack == 0:
        #calculate the damdage done
        player1_damage_done = damageX_onto_Y()
        player2_damage_done = damageY_onto_X()
        if check_agility() == True:
            player2.get_spirit()[2] -= player1_damage_done
            print("Player 2 takes",player1_damage_done,"damage.")
            print("Player 2 has",player2.get_spirit()[2],"HP remaining.")
            print()
            if player2.death_check() == True:
                print("Player 2 spirit has died.")
                player2.remove_dead_spirit()
                if player2.player_lose() == True:
                    print("Player 1 Wins!")
                    break
                else:
                    print("-----Player 2 <<Switch Sprits>>-----")
                    print()
                    player2.switch_spirits()
            else:
                player1.get_spirit()[2] -= player2_damage_done
                print("Player 1 takes",player2_damage_done,"damage.")
                print("Player 1 has",player1.get_spirit()[2],"HP remaining.")
                print()
                if player1.death_check() == True:
                    print("Player 1 spirit has died.")
                    player1.remove_dead_spirit()
                    if player1.player_lose() == True:
                        print("Player 2 Wins!")
                        break
                    else:
                        print("-----Player 1 <<Switch Spirits>>-----")
                        print()
                        player1.switch_spirits()
        else:
            player1.get_spirit()[2] -= player2_damage_done
            print("Player 1 takes",player2_damage_done,"damage.")
            print("Player 1 has",player1.get_spirit()[2],"HP remaining.")
            print()
            if player1.death_check() == True:
                print("Player 1 spirit has died.")
                player1.remove_dead_spirit()
                if player1.player_lose() == True:
                    print("Player 2 Wins!")
                    break
                else:
                    print("-----Player 1 <<Switch Spirits>>-----")
                    player1.switch_spirits()
            else:
                player2.get_spirit()[2] -= player1_damage_done
                print("Player 2 takes",player1_damage_done,"damage.")
                print("Player 2 has",player2.get_spirit()[2],"HP remaining.")
                print()
                if player2.death_check() == True:
                    print("Player 2 spirit has died.")
                    player2.remove_dead_spirit()
                    if player2.player_lose() == True:
                        print("Player 1 Wins!")
                        break
                    else:
                        print("-----Player 2 <<Switch Sprits>>-----")
                        player2.switch_spirits()

    #player1 decides to attack and player2 decides to switch
    elif player1.playerX_switch_or_attack == 0 and player2.playerX_switch_or_attack == 1:
        player1_damage_done = damageX_onto_Y()
        player2.get_spirit()[2] -= player1_damage_done
        print("Player 2 takes", player1_damage_done,"damage")
        print("Player 2 has", player2.get_spirit()[2],"HP remaining.")
        print()
        if player2.death_check() == True:
            print("Player 2 spirit has died.")
            player2.remove_dead_spirit()
            if player2.player_lose() == True:
                print("Player 1 Wins!")
                break
            else:
                print("-----Player 2 <<Switch Sprits>>-----")
                print()
                player2.switch_spirits()

    elif player1.playerX_switch_or_attack == 1 and player2.playerX_switch_or_attack == 0:
        player2_damage_done = damageY_onto_X()
        player1.get_spirit()[2] -= player2_damage_done
        print("Player 1 takes", player2_damage_done,"damage")
        print("Player 1 has", player1.get_spirit()[2],"HP remaining.")
        print()
        if player1.death_check() == True:
            print("Player 1 spirit has died.")
            player1.remove_dead_spirit()
            if player1.player_lose() == True:
                print("Player 2 Wins!")
                break
            else:
                print("-----Player 1 <<Switch Sprits>>-----")
                print()
                player1.switch_spirits()
    else:
        print("Both players switch!")
        #announce who switches to what
