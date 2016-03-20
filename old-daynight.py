#!/usr/bin/env python3

from configparser import ConfigParser;
from xdg.BaseDirectory import xdg_config_home, load_first_config;
from os import system;
from os import environ;
from os.path import join, expanduser;

DEBUG = 0;

GTK_VERSION = "gtk-3.0";
GTK_SETTINGS = "Settings";
GTK_SETTINGS_FILE = "settings.ini";
GTK_APPLICATION_PREFER_DARK_THEME = "gtk-application-prefer-dark-theme";
FILE_OPEN_WRITE = "w";

gtk_config_path = join(load_first_config(GTK_VERSION), GTK_SETTINGS_FILE);

gtkconfig = ConfigParser();
gtkconfig.read(gtk_config_path);

# we receive a string ('0' or '1'), so cast it to int (0 or 1) and then bool
prefer_dark_theme = not bool(int(gtkconfig[GTK_SETTINGS]
										  [GTK_APPLICATION_PREFER_DARK_THEME]));

# other way around, we have bool (True or False), cast it to int (0 or 1)
# but ConfigParser wants strings, so cast it to string ('0' or '1')
gtkconfig[GTK_SETTINGS] \
		 [GTK_APPLICATION_PREFER_DARK_THEME] = str(int(prefer_dark_theme));

with open(gtk_config_path, FILE_OPEN_WRITE) as file_open:
	gtkconfig.write(file_open);

if DEBUG:
	print("Path:", gtk_config_path);
	print(GTK_APPLICATION_PREFER_DARK_THEME, "was", prefer_dark_theme);
	print("Now is", str(int(not prefer_dark_theme)));

variant = "dark" if prefer_dark_theme else "light"

system("xfce4-terminal-colorscheme solarized-{0}".format(variant));

XDG_DATA_HOME = "XDG_DATA_HOME";

vim_config_path = expanduser("~/.vim/background");
with open(vim_config_path, FILE_OPEN_WRITE) as file_open:
	file_open.write("set background={0}".format(variant));
