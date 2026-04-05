from typing import Optional, Any
# from ..Items import item_name_groups # need this for locations
from BaseClasses import MultiWorld, Item, Location


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    # uncomment and change only if some stages need certain characters (which should be never here)
    # if category_name in item_name_groups["character"]:
    #     # This category is the name of a champion
    #     from ..Helpers import get_option_value
    #     enabled_operators = get_option_value(multiworld, player, "enabled_operators")
    #     return category_name in enabled_operators
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:
    # Remove unwanted champions from the item pool
    if "character" in item["category"]:
        from ..Helpers import get_option_value
        enabled_operators = get_option_value(multiworld, player, "Enabled_operators")
        return item["name"] in enabled_operators  # True if they're in the yaml, false if they're not
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    return None