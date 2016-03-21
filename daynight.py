#!/usr/bin/env python3

from debug import *;
from os.path import join;
from importlib import import_module;
from configparser import ConfigParser;
from xdg.BaseDirectory import xdg_config_home, load_first_config;

DAYNIGHT = "daynight";
DAYNIGHT_CONFIG_DIR = "daynight";
DAYNIGHT_CONFIG_FILE = "daynight";
PREF_LIST_SEPARATOR = ",";
MODULE_SEPARATOR = "-";
FUNCTION_SEPARATOR = "_";

PREF_KEY_COMPONENTS =		"components";

COMPONENT_GTK = "gtk";
COMPONENT_VIM = "vim";
COMPONENT_XFCE4TERM = "xfce4-terminal";
COMPONENT_MUTT = "mutt";

daynight_config_path = load_first_config(DAYNIGHT_CONFIG_DIR);
if not daynight_config_path:
	raise FileNotFoundError("Config folder missing");

config = ConfigParser();
if not config.read(join(daynight_config_path, DAYNIGHT_CONFIG_FILE)):
	raise FileNotFoundError("Config file missing");

pref_daynight = config[DAYNIGHT];
components = pref_daynight[PREF_KEY_COMPONENTS].split(PREF_LIST_SEPARATOR);

if len(components) != len(set(components)):
	warn("Possible duplicates in config, you probably don't want this.");

for component in components:
	component = component.strip();		# remove spaces after comma "foo, bar"
	try:
		# this is risky and hacky but theoretically should be safe (try/catch)
		pref_component = config[component];
		module_name = MODULE_SEPARATOR.join((DAYNIGHT, component));
		module = import_module(module_name);
		function_name = FUNCTION_SEPARATOR.join((DAYNIGHT, component)) \
						.replace(MODULE_SEPARATOR, FUNCTION_SEPARATOR);
						# yes I hate this too but I really want to keep the key
						# as "xfce4-terminal" and not change it to something
						# like "xfce4term" to avoid confusion
		function = getattr(module, function_name);
		function(True, pref_component);
	except KeyError as e:
		print("An exception occured while parsing", component);
		raise e;
		break;
