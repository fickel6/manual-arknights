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
    from ..Helpers import get_option_value
    if "6 star" in item["category"]:
        enabled_6_star = get_option_value(multiworld, player, "listing_6_star")
        # print(enabled_6_star)
        return item["name"] in enabled_6_star if get_option_value(multiworld, player, "blacklist_or_whitelist_operators") else not item["name"] in enabled_6_star
    if "5 star" in item["category"]:
        enabled_5_star = get_option_value(multiworld, player, "listing_5_star")
        return item["name"] in enabled_5_star if get_option_value(multiworld, player, "blacklist_or_whitelist_operators") else not item["name"] in enabled_5_star
    if "4 star" in item["category"]:
        enabled_4_star = get_option_value(multiworld, player, "listing_4_star")
        return item["name"] in enabled_4_star if get_option_value(multiworld, player, "blacklist_or_whitelist_operators") else not item["name"] in enabled_4_star
    if "3 star" in item["category"]:
        enabled_3_star = get_option_value(multiworld, player, "listing_3_star")
        return item["name"] in enabled_3_star if get_option_value(multiworld, player, "blacklist_or_whitelist_operators") else not item["name"] in enabled_3_star
    if "low star" in item["category"]:
        enabled_low_star = get_option_value(multiworld, player, "listing_low_star")
        return item["name"] in enabled_low_star if get_option_value(multiworld, player, "blacklist_or_whitelist_operators") else not item["name"] in enabled_low_star
    return None


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
