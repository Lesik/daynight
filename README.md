# daynight

Do you know this situation? You're sitting at your computer at night, with a
nice dark colorscheme for your terminal, vim and mutt and a dope GTK theme. You
work late into the night and at some point, you fall asleep. You wake up in the
morning, put your laptop in your backpack and get on your way to places. The sun
is shining and you take your laptop out of your bagpack to continue working on
yesterday's thoughts, but you can't see a thing. You might even have a matte
IPS display, but the surrounding world is just too bright. Setting the
brightness to 100% helps a bit, but you still have to squinch your eyes to read
any text.

Fear not, as there is now a solution. Though in early stages (I started working
on this yesterday, 19.03.2016), `daynight` helps you adapting your laptop's
settings to the surrounding world. It is a simple Python script that switches
your:

- GTK theme (`gtk-application-prefer-dark-theme`)
- vim background (`set background=light/dark`)

Planned additions (WIP):

- Xfce color scheme (theoretically working but I haven't added the file to git)
- mutt color scheme (easy to do and will be done soon)

Planned additions (no progress):

- Qt
- you tell me?

If you use other CLI applications, submit a pull request to add it to
`daynight`.

It would be cool to support Qt color schemes, though I really don't know how to
do that (and am not too excited to learn as I'm a GTK person). Help appreciated.

## Modules and configuration
The configuration file can be found at `~/.config/daynight/daynight`.

### `daynight-vim`
`daynight` changes the `background` variable in vim. All vim sessions need to
be restarted for this change to take effect, but that isn't a big problem as
you probably don't use `daynight` more than twice a day.

I was thinking about also allowing changing the vim colorscheme, but then
discarded that thought. Please set the `use-background` config to true.

Here is an example configuration for `daynight-vim` which will set the
`background` variable of vim to dark or light:
```
[daynight]
components = vim

[vim]
use-background = 1
```

#### daynight-gtk3
There are two ways of changing the GTK from dark to bright and back:
- through the gtk-application-prefer-dark-theme switch
- through completely changing GTK themes

The first approach is better and should be used everywhere, but not all themes
support it yet. A good theme that supports the first way is Numix-Solarized.

`daynight` supports both ways. Here is an example config for the first way:
```
[daynight]
components = gtk3

[gtk3]
use-gtk-prefer-dark = 1
theme = Numix-Solarized
```

Here's one for the second approach:
```
[daynight]
components = gtk3

[gtk3]
use-gtk-prefer-dark = 0
theme-dark = Clearlooks-Dark
theme-light = Clearlooks
```

As you can see, the `use-gtk-prefer-dark` key is mandatory. You can probably
also mix these two approaches together, but keep in mind that `daynight` will
only execute one of them, as defined by the `use-gtk-prefer-dark` key.

### bugs
Currently any commented lines you might have in your
`~/.config/gtk-3.0/settings.ini` file will vanish after running `daynight`.

### hacking
It is easy to contribute to `daynight`.

The main file is `daynight.py`. It loads the config in
`~/.config/daynight/daynight` and analyzes the `components` key. For each of
the components, for example `my-component-1` (this could be vim, gtk3, mutt,
etc.), it scans the corresponding (read: same name) section
(in our example `[my-component-1]`) in the config (the section necessarily has
to exist). It then imports a python file called `daynight-my-component-1.py`,
in which it runs a function called `daynight_my_component_1()`. The function
receives two arguments, the first one being the state to which the theme/colors
should be changed (boolean variable, `True` if dark) and the second one being a
`configparser.SectionProxy` containing the "corresponding section" of the
config file mentioned earlier. For consistency, the received arguments should
be called `dark` and `preferences`.

A less abstract example: To add mate-terminal support to `daynight`, you'd have
to create a file called `daynight-mate-terminal.py` containing the function
`daynight_mate_terminal(dark, preferences)`, which is then responsible for
doing everything that is needed to change the theme/colors.

Please use tabs for indentation. I know that PEP says otherwise, but I believe
that it's part of a programmer's freedom to have a custom indent width, which
is not possible when using a fixed space indent. I personally have my tabs set
to 4 space characters.

`ClassNamesInCamelCase, function_names_with_underscores(), same_for_variables`

For consistency, please end code lines with a semicolon (`;`), even though this
is not necessary in Python. No lines are allowed to exceed 79 characters
(from a tab-is-4-spaces perspective).

To warn the user, use the `warn()` function from `debug.py`, supplying the
warning message as argument. Similarly, use `err()` for errors.
