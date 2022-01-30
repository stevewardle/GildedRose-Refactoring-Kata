# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class ItemUpdater(ABC):
    def update(self, item):
        self.update_sell_in(item)
        self.update_quality(item)

    @abstractmethod
    def update_sell_in(self, item):
        pass

    @abstractmethod
    def update_quality(self, item):
        pass


class BasicItemUpdater(ItemUpdater):
    def update_sell_in(self, item):
        item.sell_in -= 1

    def update_quality(self, item):
        if item.quality > 0:
            item.quality -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1


class MaturingItemUpdater(ItemUpdater):
    def update_sell_in(self, item):
        item.sell_in -= 1

    def update_quality(self, item):
        if item.quality < 50:
            item.quality += 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1


class LegendaryItemUpdater(ItemUpdater):
    def update_sell_in(self, item):
        pass

    def update_quality(self, item):
        pass


class EventItemUpdater(ItemUpdater):
    def update_sell_in(self, item):
        item.sell_in -= 1

    def update_quality(self, item):
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 10 and item.quality < 50:
                item.quality += 1
            if item.sell_in < 5 and item.quality < 50:
                item.quality += 1
        if item.sell_in < 0:
            item.quality = 0


class GildedRose:

    updater_mapping = {
        "Aged Brie": MaturingItemUpdater(),
        "Backstage passes to a TAFKAL80ETC concert": EventItemUpdater(),
        "Sulfuras, Hand of Ragnaros": LegendaryItemUpdater(),
        }

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item_updater = self.updater_mapping.get(
                item.name, BasicItemUpdater())
            item_updater.update(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
