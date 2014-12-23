import sublime, sublime_plugin

class NestCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
      if region.empty():
        continue
      text = self.view.substr(region)
      # if '<!--' not in text:
      if text.startswith("<!--"):
        # print('Uncomment Please')
        text = text[4:]
        text = text[:-3]
        text = text.replace('<!~~', '<!--')
        text = text.replace('~~>', '-->')
        self.view.replace(edit, region, text)
      else:
        # print('Comment these nested comments')
        text = text.replace('<!--', '<!~~')
        text = text.replace('-->', '~~>')
        self.view.replace(edit, region, text)
        self.view.insert(edit, self.view.sel()[0].begin(), "<!--")
        self.view.insert(edit, self.view.sel()[0].end(), "-->")

#http://www.sublimetext.com/forum/viewtopic.php?f=6&t=10984