from abc import ABC, abstractmethod


class ItemUpdater(ABC):
    """
    Abstract base class which updates items
    """
    ITEM_QUALITY_DECAY_RATE = 1
    ITEM_QUALITY_MAX = 50
    ITEM_QUALITY_MIN = 0
    ITEM_SELL_IN_DECAY_RATE = 1

    def update(self, item):
        self.update_sell_in(item)
        self.update_quality(item)
        self.cap_quality(item)

    def update_sell_in(self, item):
        item.sell_in -= self.ITEM_SELL_IN_DECAY_RATE

    def cap_quality(self, item):
        if item.quality > self.ITEM_QUALITY_MAX:
            item.quality = self.ITEM_QUALITY_MAX

        elif item.quality < self.ITEM_QUALITY_MIN:
            item.quality = self.ITEM_QUALITY_MIN

    @abstractmethod
    def update_quality(self, item):
        pass


class BasicItemUpdater(ItemUpdater):
    """
    A Basic item decays at the regular rate but then
    at double the rate after its sell date passes
    """
    def update_quality(self, item):
        item.quality -= self.ITEM_QUALITY_DECAY_RATE
        if item.sell_in < 0:
            item.quality -= self.ITEM_QUALITY_DECAY_RATE


class ConjuredItemUpdater(ItemUpdater):
    """
    A Conjured item decays at the regular rate but then
    at double the rate after its sell date passes
    """
    def update_quality(self, item):
        item.quality -= self.ITEM_QUALITY_DECAY_RATE*2
        if item.sell_in < 0:
            item.quality -= self.ITEM_QUALITY_DECAY_RATE*2


class MaturingItemUpdater(ItemUpdater):
    """
    A Maturing item increases in value at the regular
    decay rate but then at double the rate after its sell
    date passes
    """
    def update_quality(self, item):
        item.quality += self.ITEM_QUALITY_DECAY_RATE
        if item.sell_in < 0:
            item.quality += self.ITEM_QUALITY_DECAY_RATE


class LegendaryItemUpdater(ItemUpdater):
    """
    A Legendary item retains its value and has no sell
    date requirements
    """
    def update_sell_in(self, item):
        pass

    def update_quality(self, item):
        pass

    def cap_quality(self, item):
        pass


class EventItemUpdater(ItemUpdater):
    """
    An Event item increases in value at a gradually building
    rate until the sell date at which point it becomes worthless
    """
    def __init__(self, hype_thresholds=[]):
        # The thresholds are the days remaining before the event
        # at which the increase in value becomes greater
        self.hype_thresholds = hype_thresholds

    def update_quality(self, item):
        item.quality += self.ITEM_QUALITY_DECAY_RATE
        # Increase the value an additional time for each
        # threshold we have already passed
        for hype in self.hype_thresholds:
            if item.sell_in < hype:
                item.quality += self.ITEM_QUALITY_DECAY_RATE
        if item.sell_in < 0:
            item.quality = self.ITEM_QUALITY_MIN
