#!/usr/bin/python3


class Items(object):
    def __init__(self, itemlvl, **kw_gsp):
        self.itemlvl = itemlvl
        super().__init__(**kw_gsp)


class Equipment(Items):
    def __init__(self, **kw_gsp):
        super().__init__(**kw_gsp)
        pass


class Weapons(Equipment):
    def __init__(self, **kw_gsp):
        super().__init__(**kw_gsp)
        self.slot = 'Weapon'
        pass


class Melee(Weapons):
    def __init__(self, **kw_gsp):
        super().__init__(**kw_gsp)
        self.type = 'melee'
        pass


class Sword(Melee):
    def __init__(self, **kw_gsp):
        super().__init__(**kw_gsp)
        self.damage = 10
        pass


class Ranged(Weapons):
    def ___init__(self, **kw_gsp):
        super().__init__(**kw_gsp)
        self.type = 'ranged'
        pass


class Armor(Equipment):
    def __init__(self, **kw_gsp):
        super().__init__(**kw_gsp)
        self.slot = 'Armor'
        pass


class Potion(Items):
    def __init__(self, **kw_gsp):
        super().__init__(**kw_gsp)
        self.type = 'Potion'
        pass
