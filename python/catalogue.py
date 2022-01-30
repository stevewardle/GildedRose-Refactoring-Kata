from collections import defaultdict
from item_updater import (
    BasicItemUpdater,
    MaturingItemUpdater,
    EventItemUpdater,
    LegendaryItemUpdater)

# In a real world application this information could be stored
# in some sort of configuration; a file; a database or something
# else that could be easily updated for any items that already
# fit one of the predefined updater types

UPDATER_MAPPING = defaultdict(BasicItemUpdater)
UPDATER_MAPPING.update({
    "Aged Brie": MaturingItemUpdater(),
    "Backstage passes to a TAFKAL80ETC concert": EventItemUpdater(),
    "Sulfuras, Hand of Ragnaros": LegendaryItemUpdater(),
    })
