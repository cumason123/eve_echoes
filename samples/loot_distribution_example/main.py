import json

from eve_echoes.loot_distribution import LootDistribution

if __name__ == "__main__":
    members = ["DONTSHOOT", "jaminLagoon", "eisenhorn"]
    loot = {
        "Corpum C-Type Medium Pulse Lasers": 12,
        "Corpum C-Type Medium Beam Lasers": 5,
        "Corpum C-Type Small Pulse Lasers": 16,
        "Corpum C-Type Small Beam Lasers": 3,
        "Corpum C-Type Medium Armor Repairer": 19,
    }
    loot = LootDistribution(members, loot)
    organized_loot = loot.distribute()
    print(json.dumps(organized_loot, indent=4))
