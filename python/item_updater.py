from abc import ABC, abstractmethod


class ItemUpdater(ABC):
    ITEM_QUALITY_DECAY_RATE = 1
    ITEM_QUALITY_MAX = 50
    ITEM_QUALITY_MIN = 0
    ITEM_SELL_IN_DECAY_RATE = 1

    def update(self, item):
        self.update_sell_in(item)
        self.update_quality(item)

    def update_sell_in(self, item):
        item.sell_in -= self.ITEM_SELL_IN_DECAY_RATE

    @abstractmethod
    def update_quality(self, item):
        pass


class BasicItemUpdater(ItemUpdater):
    def update_quality(self, item):
        if item.quality > self.ITEM_QUALITY_MIN:
            item.quality -= self.ITEM_QUALITY_DECAY_RATE
        if (item.sell_in < 0
                and item.quality > self.ITEM_QUALITY_MIN):
            item.quality -= self.ITEM_QUALITY_DECAY_RATE


class ConjuredItemUpdater(ItemUpdater):
    def update_quality(self, item):
        if item.quality > self.ITEM_QUALITY_MIN:
            item.quality -= self.ITEM_QUALITY_DECAY_RATE*2
        if (item.sell_in < 0
                and item.quality > self.ITEM_QUALITY_MIN):
            item.quality -= self.ITEM_QUALITY_DECAY_RATE*2


class MaturingItemUpdater(ItemUpdater):
    def update_quality(self, item):
        if item.quality < self.ITEM_QUALITY_MAX:
            item.quality += self.ITEM_QUALITY_DECAY_RATE
        if (item.sell_in < 0
                and item.quality < self.ITEM_QUALITY_MAX):
            item.quality += self.ITEM_QUALITY_DECAY_RATE


class LegendaryItemUpdater(ItemUpdater):
    def update_sell_in(self, item):
        pass

    def update_quality(self, item):
        pass


class EventItemUpdater(ItemUpdater):
    def __init__(self, hype_thresholds=[]):
        # The thresholds are the days remaining before the event
        # at which the increase in value becomes greater
        self.hype_thresholds = hype_thresholds

    def update_quality(self, item):
        if item.quality < self.ITEM_QUALITY_MAX:
            item.quality += self.ITEM_QUALITY_DECAY_RATE
            # Increase the value an additional time for each
            # threshold we have already passed
            for hype in self.hype_thresholds:
                if (item.sell_in < hype
                        and item.quality < self.ITEM_QUALITY_MAX):
                    item.quality += self.ITEM_QUALITY_DECAY_RATE
        if item.sell_in < 0:
            item.quality = self.ITEM_QUALITY_MIN
