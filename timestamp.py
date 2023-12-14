import datetime
import sublime, sublime_plugin
 
class TimestampCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    timestamp = f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ET]: "
    self.view.insert(edit, self.view.sel()[0].begin(), timestamp)
