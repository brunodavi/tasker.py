from dataclasses import dataclass

from .icon import Icon


@dataclass
class Misc(Icon):
    HUE: str = "cust_ambilwarna_hue"

    BEAR: str = "cust_animal_bear"
    BUG: str = "cust_animal_bug"
    FOX: str = "cust_animal_fox"
    HIPPO: str = "cust_animal_hippo"
    PANDA: str = "cust_animal_panda"
    PENGUIN: str = "cust_animal_penguin"

    TASKER: str = "cust_app_icon"

    EDIT: str = "cust_appshort_edit"
    LOG: str = "cust_appshort_log"
    SETTING: str = "cust_appshort_settings"

    BATTERY: str = "cust_battery"
    CHARGING: str = "cust_charging"

    TASKER_BLACK: str = "cust_bolt_black"
    TASKER_WHITE: str = "cust_bolt_white"

    HOLO_DARK: str = "cust_button_holo_dark"

    SEARCH: str = "cust_choose_blue"
    COFFEE: str = "cust_coffee"
    COOKIE: str = "cust_cookie"
    EMAIL: str = "cust_email"
    FLAG: str = "cust_flag"

    DONUT: str = "cust_icon_donut"
    GINGERBREAD: str = "cust_icon_gingerbread"

    LOCK: str = "cust_lock"

    PANEL_HOLO_DARK: str = "cust_menu_dropdown_panel_holo_dark"
    PANEL_HOLO_LIGHT: str = "cust_menu_dropdown_panel_holo_light"

    PROFILE_ENTER_DARK: str = "cust_profile_enter_dark"
    PROFILE_ENTER_LIGHT: str = "cust_profile_enter_light"
    PROFILE_EXIT_DARK: str = "cust_profile_exit_dark"
    PROFILE_EXIT_LIGHT: str = "cust_profile_exit_light"

    SATELLITE: str = "cust_satellite"
    SCRUBBER_NORMAL: str = "cust_scrubber_normal"
    STAR: str = "cust_star"
    USB: str = "cust_usb"
    WARNING: str = "cust_warning"
    ZIP: str = "cust_zip"
