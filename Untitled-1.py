class Soldier:
    def __init__(self, name, rank, weapon):
        self.name = name #名字
        self.rank = rank #等級
        self.weapon = weapon #武器
        self.is_alive = True

    def describe(self):
        return f"{self.rank} {self.name} with {self.weapon}"

    def attack(self, target):
        if target.is_alive:
            print(f"{self.rank} {self.name} attacks {target.rank} {target.name} with {self.weapon}!")
        else:
            print(f"{target.rank} {target.name} is already defeated.")

    def defend(self):
        print(f"{self.rank} {self.name} defends against the enemy.")

    def take_damage(self):
        self.is_alive = False
        print(f"{self.rank} {self.name} has been defeated!")

# 創建士兵
soldier1 = Soldier("小紅", "小蘭", "小綠")
soldier2 = Soldier("小王", "小李", "小黃")

# 顯示士兵資訊
print(soldier1.describe())
print(soldier2.describe())

# 士兵1攻擊士兵2
soldier1.attack(soldier2)

# 士兵2防禦
soldier2.defend()

# 士兵1再次攻擊士兵2
soldier1.attack(soldier2)

# 士兵2承受傷害
soldier2.take_damage()