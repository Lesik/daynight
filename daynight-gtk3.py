#!/usr/bin/env python3

from os.path import join;
from configparser import ConfigParser;
from xdg.BaseDirectory import load_first_config;

GTK_VERSION = "gtk-3.0";
GTK_SETTINGS = "Settings";
GTK_SETTINGS_FILE = "settings.ini";
GTK_PREF_THEME_NAME = "gtk-theme-name";
GTK_APP_PREFER_DARK = "gtk-application-prefer-dark-theme";

PREF_KEY_THEME_DARK =			"theme-dark";
PREF_KEY_THEME_LIGHT =			"theme-light";
PREF_KEY_THEME_DEFAULT =		"theme";
PREF_KEY_USE_GTK_PREFER_DARK =	"use-gtk-prefer-dark";

FILE_OPEN_WRITE = "w";

def daynight_gtk3(dark, preferences):
	gtk_config_path = join(load_first_config(GTK_VERSION), GTK_SETTINGS_FILE);
	gtkconfig = ConfigParser();
	gtkconfig.read(gtk_config_path);

	use_gtk_prefer_dark = preferences.getboolean(PREF_KEY_USE_GTK_PREFER_DARK);
	if use_gtk_prefer_dark:
		gtkconfig[GTK_SETTINGS][GTK_APP_PREFER_DARK] = str(int(dark));
		theme = preferences[PREF_KEY_THEME_DEFAULT];
	else:
		if dark:
			theme = preferences[PREF_KEY_THEME_DARK];
		else:
			theme = preferences[PREF_KEY_THEME_LIGHT];
	gtkconfig[GTK_SETTINGS][GTK_PREF_THEME_NAME] = theme;
	
	with open(gtk_config_path, FILE_OPEN_WRITE) as file_open:
		gtkconfig.write(file_open);
