import sublime_plugin


class ThemeDarkCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        path = 'Preferences.sublime-settings'
        settings = sublime_plugin.sublime.load_settings(path)
        settings.set("color_scheme",
                     "Packages/User/SublimeLinter/Tomorrow-Night (SL).tmTheme")
        settings.set("theme",
                     "Boxy Tomorrow.sublime-theme")
        settings = sublime_plugin.sublime.save_settings(path)


class ThemeLightCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        path = 'Preferences.sublime-settings'
        settings = sublime_plugin.sublime.load_settings(path)
        settings.set("color_scheme",
                     "Packages/User/SublimeLinter/Tomorrow (SL).tmTheme")
        settings.set("theme",
                     "Boxy Solarized Light.sublime-theme")
        settings = sublime_plugin.sublime.save_settings(path)

