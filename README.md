# daynight

Do you know this situation? You're sitting at your computer at night, with a
nice dark colorscheme for your terminal, vim and mutt and a dope GTK theme. You
work late into the night and at some point, you fall asleep. You wake up in the
morning, put your laptop in your bagpack and get on your way to places. The sun
is shining through the window of your bus, tram, metro or train while you take
your laptop out of your bagpack to continue working on yesterday's
thoughts...and you don't see a thing. You might even have a matte IPS display,
but the surrounding world is just too bright. Setting the brightness to 100%
helps a bit, but you still have to squinch your eyes to read any text.

Fear not, as there is now a solution. Though in early stages (I started working
on this yesterday), `daynight` is going to help you adapting your laptop's
settings to the surrounding world. It is a simple Python script that switches
your:

- GTK theme (`gtk-application-prefer-dark-theme`)
- Xfce color scheme (theoretically working but I haven't added the file to git)
- vim background (`set background=light/dark`)
- mutt color scheme (not in git yet)

If you use other CLI applications, submit a pull request to add it to
`daynight`.

It would be cool to support Qt color schemes, though I really don't know how to
do that (and am not too excited to learn as I don't use Qt). Help appreciated.
