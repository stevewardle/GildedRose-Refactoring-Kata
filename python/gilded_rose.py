from catalogue import get_updater


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_items(self):
        for item in self.items:
            item_updater = get_updater(item)
            item_updater.update(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
