import pytest
import json
from eve_echoes.loot_distribution import LootDistribution


def test_loot_generated_evenly():
    members = ["DONTSHOOT", "DONTSHOOT1", "DONTSHOOT2"]
    test_loot = {"medium lasers": 39, "small laser": 1}
    loot = LootDistribution(members, test_loot)
    distributed_loot = loot.distribute()

    size_set = set()
    for member in members:
        assert member in distributed_loot, "member not in distributed loot?"
        size_set.add(distributed_loot.get(member)["size"])

    assert size_set == set([13, 14])


def test_not_enough_loot():
    members = ["DONTSHOOT", "DONTSHOOT1", "DONTSHOOT2", "DONTSHOOT3"]
    test_loot = {"medium laser": 1, "small laser": 1}
    loot = LootDistribution(members, test_loot)
    distributed_loot = loot.distribute()

    print(json.dumps(distributed_loot, indent=2))
