from typing import Optional, Any
from BaseClasses import MultiWorld


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
        enabled_6_star = get_option_value(multiworld, player, "whitelist_6_star")
        enabled_5_star = get_option_value(multiworld, player, "whitelist_5_star")
        enabled_4_star = get_option_value(multiworld, player, "whitelist_4_star")
        enabled_3_star = get_option_value(multiworld, player, "whitelist_3_star")
        enabled_low_star = get_option_value(multiworld, player, "whitelist_low_star")
        if get_option_value(multiworld, player, "blacklist_or_whitelist_operators"):
            return item["name"] in enabled_6_star or item["name"] in enabled_5_star or item["name"] in enabled_4_star or item["name"] in enabled_3_star or item["name"] in enabled_low_star  # True if they're in the yaml, false if they're not
        else: 
            return not (item["name"] in enabled_6_star or item["name"] in enabled_5_star or item["name"] in enabled_4_star or item["name"] in enabled_3_star or item["name"] in enabled_low_star)
    return None


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
