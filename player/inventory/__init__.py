#!/usr/bin/python3

"""

 This is to handle the players inventory in the RPG game

"""
import player


class PlayerInventory(object):

    def __init__(self):
        self.inv = []   # The players inventory
        self.Weapon = []   # The players equipped weapon
        self.Armor = []   # The players equipped armor

    def use_item(self, item):
        if item.type == 'Potion':
            self.inv.remove(item)
            player.Player.use_potion()

    def add_item(self, item):
        self.inv.append(item)

    def remove_item(self, item):
        self.inv.remove(item)

    def equip_item(self, item):
        if item.slot == 'Armor':
            if not self.Armor:
                self.inv.remove(item)
                self.Armor.append(item)
        elif item.slot == 'Weapon':
            if not self.Weapon:
                self.inv.remove(item)
                self.Weapon.append(item)

    def unequip_item(self, item):
        if item.slot == 'Armor':
            self.Armor.remove(item)
            self.inv.append(item)
        if item.slot == 'Weapon':
            self.Weapon.remove(item)
            self.inv.append(item)

