#
#  ██████  ████████ ██ ██      ███████ 
# ██    ██    ██    ██ ██      ██      
# ██    ██    ██    ██ ██      █████   
# ██ ▄▄ ██    ██    ██ ██      ██      
#  ██████     ██    ██ ███████ ███████ CONFIG FILE
#     ▀▀ 
# Frederico Fávaro
#

import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # Launch apps
    Key([mod], "b", lazy.spawn('firefox'), desc="Launch Firefox"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Midia control
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 set Master 5+ unmute")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 set Master 5- unmute")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),

    # Switch between windows
    Key([mod], "j", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "k", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "l", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "semicolon", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "j", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "semicolon", lazy.layout.shuffle_right(), desc="Move window to the right"),
    
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "j", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "k", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "l", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "semicolon", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    # Toggle between split and unsplit sides of stack.y
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(),desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "d", lazy.spawn("rofi -show run")),
]

#groups = [Group(i) for i in "123456789"]
groups = [
    Group('1', label='web', matches=[Match(wm_class=["firefox"])]),
    Group('2', label='dev', matches=[Match(wm_class=["code"])]),
    Group('3', label='file', matches=[Match(wm_class=["org.gnome.Nautilus"])]),
    Group('4', label='docs'),
    Group('5', label='5'),
    Group('6', label='6'),
    Group('7', label='7'),
    Group('8', label='8'),
    Group('9', label='mid'),
    Group('0', label='conf'),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name),),
            # mod1 + shift + letter of group = switch to & move focused window to group
            #Key(
            #    [mod, "shift"],
            #    i.name,
            #    lazy.window.togroup(i.name, switch_group=True),
            #    desc="Switch to & move focused window to group {}".format(i.name),
            #),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
             Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                 desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_width=4,
        margin=[8,6,8,6],
        ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),nautilus
    # layout.Zoomy(),nautilus
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitke
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="pavucontrol"),
    ]
)

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method='block',
                    disable_drag='True'
                    ),
                widget.Sep(padding=10),
                widget.CurrentLayout(),
                widget.Sep(padding=10),
                #widget.WindowName(
                    #format='{name}',
                #),
                widget.WindowTabs(),
                widget.Sep(padding=10),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Pomodoro(prefix_inactive="Start"),
                widget.Sep(padding=10),
                widget.Volume(),
                widget.Sep(padding=10),
                widget.Clock(format="%a, %d de %b de %Y - %H:%M"),
                widget.Sep(padding=10),
                widget.Systray(),
                widget.Sep(padding=10),
                widget.QuickExit(
                    default_text='[ X ]',
                    countdown_format='[ {} ],'
                ),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
floats_kept_above = True
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "focus"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


# autostart apps
@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([script])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
