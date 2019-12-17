import json

with open(f"../maps/lvls02.json") as mapdata:
    worldmap = json.load(mapdata)

print(worldmap["Foyer"]["doorways"])