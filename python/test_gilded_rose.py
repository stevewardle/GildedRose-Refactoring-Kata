from gilded_rose import Item, GildedRose
from item_updater import (
    BasicItemUpdater,
    ConjuredItemDecorator,
    )


class TestGildedRose:
    def test_init(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        assert gilded_rose.items == items

    def test_update_items(self):
        # TODO: This is kind of a bad unit test;
        # either needs design changes or perhaps to
        # do something with mocker - we only really
        # need to know that it's calling the "update"
        # method of each item it is given
        items = [
            Item(name="foo", quality=1, sell_in=1),
            Item(name="bar", quality=1, sell_in=1),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items()
        assert gilded_rose.items[0].name == "foo"
        assert gilded_rose.items[0].quality == 0
        assert gilded_rose.items[0].sell_in == 0
        assert gilded_rose.items[1].name == "bar"
        assert gilded_rose.items[1].quality == 0
        assert gilded_rose.items[1].sell_in == 0


class TestBasicItemUpdater:
    def test_update_normal(self):
        item = Item(name="foo", sell_in=10, quality=9)
        updater = BasicItemUpdater()
        updater.update(item)
        assert item.name == "foo"
        assert item.sell_in == 9
        assert item.quality == 8

    def test_update_late(self):
        item = Item(name="foo", sell_in=0, quality=9)
        updater = BasicItemUpdater()
        updater.update(item)
        assert item.name == "foo"
        assert item.sell_in == -1
        assert item.quality == 7


class TestConjuredItemDecorator:
    def test_update_normal(self):
        item = Item(name="foo", sell_in=10, quality=9)
        updater = ConjuredItemDecorator(BasicItemUpdater())
        updater.update(item)
        assert item.name == "foo"
        assert item.sell_in == 9
        assert item.quality == 7

    def test_update_late(self):
        item = Item(name="foo", sell_in=0, quality=9)
        updater = ConjuredItemDecorator(BasicItemUpdater())
        updater.update(item)
        assert item.name == "foo"
        assert item.sell_in == -1
        assert item.quality == 5

# TODO: Complete the testing; likely also be able to
#       make the above more concise using fixtures
#       or other techniques
