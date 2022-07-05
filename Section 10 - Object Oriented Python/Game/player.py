# class Player(object):
#
#     def __init__(self, name):
#         self.name = name
#         self._lives = 3
#         self._level = 1
#         self.score = 0
#
#     def _get_lives(self):
#         print('USING GETTER')
#         return self._lives
#
#     def _set_lives(self, internal_lives):
#         print('USING SETTER')
#         if internal_lives >= 0:
#             self._lives = internal_lives
#         else:
#             print("Lives cannot be negative")
#             self._lives = 0
#
#     def _get_level(self):
#         print("CALLING LEVEL GETTER")
#         return self._level
#
#     def _set_level(self, level):
#         print("CALLING LEVEL SETTER")
#         print(f"LEVEL IS {level}")
#         print(f"At start, self._level is {self._level}")
#         if level > 0:
#             delta = level - self._level
#             self.score += delta * 1000
#             self._level = level
#         else:
#             print("Level can't be less than 1")
#         print(f"At end, self._level is {self._level}")
#
#     lives = property(_get_lives, _set_lives)
#     level = property(_get_level, _set_level)
#
#     def __str__(self):
#         return f"Name: {self.name}, Lives: {self.lives}, Level: {self._level}, Score: {self.score}"

class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        print('USING GETTER')
        return self._lives

    def _set_lives(self, internal_lives):
        print('USING SETTER')
        if internal_lives >= 0:
            self._lives = internal_lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    def _get_level(self):
        print("CALLING LEVEL GETTER")
        return self._level

    def _set_level(self, level):
        print("CALLING LEVEL SETTER")
        print(f"LEVEL IS {level}")
        print(f"At start, self._level is {self._level}")
        if level > 0:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print("Level can't be less than 1")
        print(f"At end, self._level is {self._level}")

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return f"Name: {self.name}, Lives: {self.lives}, Level: {self._level}, Score: {self._score}"