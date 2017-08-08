import sublime_plugin


class ThemeDarkCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        path = 'Preferences.sublime-settings'
        settings = sublime_plugin.sublime.load_settings(path)
        settings.set('color_scheme',
                     'Packages/gruvbox/gruvbox (Dark) (Hard).tmTheme')
        settings.set('theme',
                     'gruvbox (Dark) (Hard).sublime-theme')
        settings.set('gruvbox_accent_green',
                     True)
        settings.set('gruvbox_accent_orange',
                     False)
        settings = sublime_plugin.sublime.save_settings(path)


class ThemeLightCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        path = 'Preferences.sublime-settings'
        settings = sublime_plugin.sublime.load_settings(path)
        settings.set('color_scheme',
                     'Packages/gruvbox/gruvbox (Light) (Hard).tmTheme')
        settings.set('theme',
                     'gruvbox (Light) (Hard).sublime-theme')
        settings.set('gruvbox_accent_green',
                     False)
        settings.set('gruvbox_accent_orange',
                     True)
        settings = sublime_plugin.sublime.save_settings(path)
