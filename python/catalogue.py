from item_updater import (
    BasicItemUpdater,
    MaturingItemUpdater,
    EventItemUpdater,
    LegendaryItemUpdater,
    ConjuredItemDecorator,
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
        "item_type": "basic",
        "conjured": True,
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
        return BasicItemUpdater()

    if db_entry["item_type"] == "basic":
        updater = BasicItemUpdater()

    elif db_entry["item_type"] == "maturing":
        updater = MaturingItemUpdater()

    elif db_entry["item_type"] == "event":
        # The event item type has extra information to
        # define the hype thresholds
        hype_thresholds = list(map(
            int, db_entry["hype_thresholds"].split()))
        updater = EventItemUpdater(
            hype_thresholds=hype_thresholds)

    elif db_entry["item_type"] == "legendary":
        updater = LegendaryItemUpdater()

    # With the base updater selected, apply any decorators
    # which modify the behaviour of the updater
    if "conjured" in db_entry and db_entry["conjured"]:
        updater = ConjuredItemDecorator(updater)

    return updater
