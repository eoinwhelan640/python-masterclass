import random
# My go at the lives config, bit too much code
# class Enemy:
#
#     def __init__(self, name="Enemy", hit_points=10, lives=1):
#         self.name = name
#         self.hit_points = hit_points
#         self.lives = lives
#         self.live_cap = hit_points
#         self.alive = True
#
#     def take_damage(self, damage):
#         remaining_points = self.hit_points - damage
#         if self.alive == False:
#             print(f"{self.name} is dead, cannot take more damage")
#         elif remaining_points >= 0:
#             self.hit_points = remaining_points
#             print(f"I took {damage} points damage and have {self.hit_points} hp left")
#         else:
#             # if we're in here, we're losing at least one life
#             lives_to_take = max(damage // self.live_cap,1)
#             # Lock the lives to be 0 min
#             self.lives = max(self.lives - lives_to_take, 0)
#             # lock our hp to be 0. If we're here the remaining points is neg so cap + neg points works
#             self.hit_points = max(self.live_cap + remaining_points, 0)
#             print(f"{self.name} Lost {lives_to_take} live(s). remaining HP {max(self.hit_points,0)}")
#             if self.lives == 0 & self.hit_points <=0:
#                 print(f"{self.name} is DEAD")
#                 self.alive = False
#
#     def __str__(self):
#         return f"Name: {self.name}, " \
#                f"lives: {self.lives}, " \
#                f"Hit points: {self.hit_points}, " \
#                f"Status: {['Alive' if self.alive ==True else 'Dead'][0]}"

class Enemy:

    def __init__(self, name="Enemy", hit_points=10, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True
        self.live_cap = hit_points

    @property
    def lives(self):
        print("using getter")
        return self._lives

    @lives.setter
    def lives(self, lives):
        print("using Setter")
        self._lives = lives


    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print(f"{self._name} took {damage} points damage and have {self._hit_points} hp left")
        else:
            self._lives -= 1
            if self._lives > 0:
                print(f"{self._name} lost a life")
                self._hit_points = self.live_cap
            else:
                print(f"{self._name} is dead")
                self._alive = False

    def __str__(self):
        return f"Name: {self._name}, lives: {self._lives}, Hit points: {self._hit_points}"

class Troll(Enemy):

    def __init__(self, name, hp=20, lives=2,weapon="stick"):
    #def __init__(self, name):
        # Would work as well
        #Enemy.__init__(self, name=name, lives= 1, hit_points)
        super().__init__(name=name, hit_points=hp, lives=lives)
        #super().__init__()
        self.weapon = weapon

    def grunt(self):
        print(f"Me {self._name}. {self._name} stomp you")


class Vampire(Enemy):
    # With hp =12 here we are saying that the hp option is dynamic, we can set it on initialisation
    def __init__(self, name, hit_points=12):
        # With lives=3 here we are hardcoding vampire lives to always be 3
        super().__init__(name, lives=3, hit_points=hit_points)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print(f"{self._name} dodges ****")
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)


class VampireKing(Vampire):

    def __init__(self, name):
        #super().__init__(name, hit_points=140)
        super().__init__(name)
        self._hit_points = 140

    # def king_shit(self,damage):
    #     print(f"{self._name} absorbs damage")
    #     return damage // 4

    def take_damage(self, damage):
        #damage = self.king_shit(damage)
        super().take_damage(damage // 4)
