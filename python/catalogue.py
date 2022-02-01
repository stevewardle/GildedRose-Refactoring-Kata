from item_updater import (
    BasicItemUpdater,
    MaturingItemUpdater,
    EventItemUpdater,
    LegendaryItemUpdater,
    ConjuredItemUpdater,
)

# In a real world application this information could be stored
# in some sort of configuration; a file, a database or something
# else that could be easily updated for any items that already
# fit one of the predefined updater types
_DATABASE = {
    "Aged Brie": {
        "item_type": "maturing",
        },
    "Backstage passes to a TAFKAL80ETC concert": {
        "item_type": "event",
        "hype_thresholds": "10 5",
        },
    "Sulfuras, Hand of Ragnaros": {
        "item_type": "legendary",
        },
    "Conjured Mana Cake": {
        "item_type": "conjured",
        },
    }


def get_updater(item):
    """
    Return a suitable updater class for a given item.
    Items unknown to the catalogue are treated as the
    basic type of item

    """
    db_entry = _DATABASE.get(item.name, None)
    if db_entry is None:
        updater = BasicItemUpdater()

    elif db_entry["item_type"] == "maturing":
        updater = MaturingItemUpdater()

    elif db_entry["item_type"] == "event":
        hype_thresholds = list(map(
            int, db_entry["hype_thresholds"].split()))
        updater = EventItemUpdater(
            hype_thresholds=hype_thresholds)

    elif db_entry["item_type"] == "legendary":
        updater = LegendaryItemUpdater()

    elif db_entry["item_type"] == "conjured":
        updater = ConjuredItemUpdater()

    return updater
