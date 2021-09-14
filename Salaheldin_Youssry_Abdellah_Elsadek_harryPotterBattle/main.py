class Player:
    def __init__(self):
        self.health = 100
        self.energy=500
        self.shield=3
    def canUseSpell(self,spellPower):
        if spellPower>self.energy:
            return False
        return True
    def game(self,healthDec,enrgyDec,shieldDec):
        self.energy-=enrgyDec
        self.health-=healthDec
        self.shield-=shieldDec
    def canUseShield(self):
        return self.shield>0

def printGame(p1,p2):
    print("      Harry            voldmort")
    print("Health:"+str(p1.health)+"   "+str(p2.health))
    print("Energy:"+str(p1.energy)+"   "+str(p2.energy))

file1 = open('spells.txt', 'r')
Lines = file1.readlines()
vSpells = {}
hSpells={}
for line in Lines:
    all=line.split()
    if all[0]=='A':
        vSpells[all[1]]=int(all[2])
        hSpells[all[1]] = int(all[2])
    elif all[0]=='H':
        hSpells[all[1]] = int(all[2])
    elif all[0] == 'V':
        vSpells[all[1]]=int(all[2])

print(hSpells)
harry=Player()
voldmort=Player()
while True:
    if(voldmort.health==0 and harry.health==0 ):
        print("\nTie")
        break
    elif voldmort.health==0:
        print("\nHarry is the winner")
        break
    elif harry.health == 0:
        print("\nVoldmort is the winner")
        break
    game = input("Enter the two spells (harry then voldmort): \n")
    game=game.split()
    hSpell=0
    vSpell=0
    if game[0] in hSpells.keys():
        hSpell=hSpells[game[0]]
    if game[1] in vSpells.keys():
        vSpell=vSpells[game[1]]
    if not harry.canUseSpell(hSpell):
        hspell=0
    if not voldmort.canUseSpell(vSpell):
        vSpell=0
    if game[0]=='shield' and game[1]!='shield' and harry.canUseShield():
        voldmort.game(0, vSpell, 0)
        harry.game(0, 0, 1)
        printGame(harry,voldmort)
        continue
    if game[1] == 'shield' and game[0] != 'shield' and voldmort.canUseShield():
        voldmort.game(0, 0, 1)
        harry.game(0,hSpell,0)
        printGame(harry,voldmort)
        continue
    if game[1] == 'shield' and game[0] == 'shield' and voldmort.canUseShield() and harry.canUseShield():
        voldmort.game(0,0,1)
        harry.game(0,0,1)
        printGame(harry,voldmort)
        continue
    if vSpell>hSpell:
         voldmort.game(0,vSpell,0)
         harry.game(vSpell-hSpell,hSpell,0)
    else:
         voldmort.game(0, vSpell, 0)
         harry.game(0, hSpell, 0)
    printGame(harry,voldmort)

