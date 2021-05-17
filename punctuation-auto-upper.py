import sublime
import sublime_plugin
import re

MAP_PUNCTUATION = {
    //"\ ": "　",
    "“": '"',
    "”": '"',
    "\!": "！",
    "\$": "￥",
    "\^": "……",
    "\(": "（",
    "\)": "）",
    "\--": "——",
    "\[": "【",
    "\]": "】",
    "\;": "；",
    "\'": "’",
    "\:": "：",
    "\,": "，",
    "\.": "。",
    "\,": "、",
    "\?": "？",
}


def changeContent(content):
    for x in MAP_PUNCTUATION.items():
        content = re.sub(x[0], x[1], content)
    return content


class PunctuationAutoUpperCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        r = sublime.Region(0, self.view.size())
        content = self.view.substr(r)
        self.view.replace(edit, r, changeContent(content))


class PunctuationAutoUpperListener(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        if not "punctuation-auto-upper.py" in view.file_name():
            view.run_command("punctuation_auto_upper")
