import sublime_plugin


class ProxySwitcherCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        PROXY = 'http://wwwproxy.se.axis.com:3128'
        KEY = 'http_proxy'
        PATH = 'Package Control.sublime-settings'

        settings = sublime_plugin.sublime.load_settings(PATH)


        if settings.get(KEY):
            settings.set(KEY, "")
        else:
            settings.set(KEY, PROXY)
        settings = sublime_plugin.sublime.save_settings(PATH)
