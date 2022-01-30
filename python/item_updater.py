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
