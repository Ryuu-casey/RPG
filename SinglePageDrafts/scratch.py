import json

with open(f"../maps/lvls.json") as mapdata:
    worldmap = json.load(mapdata)

print(worldmap["levels"][0]["lvldata"][1]["tilemap"])
