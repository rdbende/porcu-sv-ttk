"""Use Sun Valley ttk theme in Porcupine"""
from pathlib import Path

import sv_ttk
from porcupine import get_main_window, get_tab_manager, settings
from porcupine.settings import global_settings


def set_theme(theme) -> None:
    main_window = get_main_window()
    sv_ttk.set_theme(theme.lower())
    main_window.option_add("*Text.font", "TkFixedFont")
    main_window.option_add("*Text.highlightThickness", "0")
    main_window.option_add("*Text.borderWidth", "1")
    main_window.option_add("*Text.relief", "solid")
    main_window.option_add("*Combobox.state", "readonly")


def setup() -> None:
    main_window = get_main_window()

    global_settings.add_option("sv_theme", "Dark")
    settings.add_combobox(
        "sv_theme", "UI theme", values=["Dark", "Light"], state="readonly"
    )
    set_theme(global_settings.get("sv_theme", str))

    get_tab_manager().bind(
        "<<GlobalSettingChanged:sv_theme>>",
        lambda event: set_theme(global_settings.get("sv_theme", str)),
        add=True,
    )
