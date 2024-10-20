from dataclasses import dataclass

from tasker.utils import meta_attr

from .icon import Icon


@meta_attr
def meta_icon(value):
    return Icon(value)


class Misc(Icon, metaclass=meta_icon):
    HUE = 'cust_ambilwarna_hue'

    BEAR = 'cust_animal_bear'
    BUG = 'cust_animal_bug'
    FOX = 'cust_animal_fox'
    HIPPO = 'cust_animal_hippo'
    PANDA = 'cust_animal_panda'
    PENGUIN = 'cust_animal_penguin'

    TASKER = 'cust_app_icon'

    EDIT = 'cust_appshort_edit'
    LOG = 'cust_appshort_log'
    SETTING = 'cust_appshort_settings'

    BATTERY = 'cust_battery'
    CHARGING = 'cust_charging'

    TASKER_BLACK = 'cust_bolt_black'
    TASKER_WHITE = 'cust_bolt_white'

    HOLO_DARK = 'cust_button_holo_dark'

    SEARCH = 'cust_choose_blue'
    COFFEE = 'cust_coffee'
    COOKIE = 'cust_cookie'
    EMAIL = 'cust_email'
    FLAG = 'cust_flag'

    DONUT = 'cust_icon_donut'
    GINGERBREAD = 'cust_icon_gingerbread'

    LOCK = 'cust_lock'

    PANEL_HOLO_DARK = 'cust_menu_dropdown_panel_holo_dark'
    PANEL_HOLO_LIGHT = 'cust_menu_dropdown_panel_holo_light'

    PROFILE_ENTER_DARK = 'cust_profile_enter_dark'
    PROFILE_ENTER_LIGHT = 'cust_profile_enter_light'
    PROFILE_EXIT_DARK = 'cust_profile_exit_dark'
    PROFILE_EXIT_LIGHT = 'cust_profile_exit_light'

    SATELLITE = 'cust_satellite'
    SCRUBBER_NORMAL = 'cust_scrubber_normal'
    STAR = 'cust_star'
    USB = 'cust_usb'
    WARNING = 'cust_warning'
    ZIP = 'cust_zip'
