#!/usr/bin/env python3

from os.path import expanduser;

FILE_OPEN_READ = "r";
FILE_OPEN_WRITE = "w";
FILE_OPEN_APPEND = "a";

VIM_SOURCE_LINE = "so ~/.vim/daynight";
VIM_BACKGROUND_LINE = "set background={0}";

BACKGROUND_DARK = "dark";
BACKGROUND_LIGHT = "light";

PREF_KEY_USE_BACKGROUND = 		"use-background";

def daynight_vim(dark, preferences):
	vim_config_path = expanduser("~/.vimrc");
	vim_bg_config_path = expanduser("~/.vim/daynight");
	
	# add VIM_SOURCE_LINE to vimrc if not yet there
	with open(vim_config_path, FILE_OPEN_READ) as file_open:
		if not VIM_SOURCE_LINE in file_open.read():
			with open(vim_config_path, FILE_OPEN_APPEND) as file_open:
				file_open.write(VIM_SOURCE_LINE);
	
	with open(vim_bg_config_path, FILE_OPEN_WRITE) as file_open:
		if preferences[PREF_KEY_USE_BACKGROUND]:
			background = BACKGROUND_DARK if dark else BACKGROUND_LIGHT;
			file_open.write(VIM_BACKGROUND_LINE.format(background));
