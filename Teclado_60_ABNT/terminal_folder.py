# Open terminal in the current folder (not in a subfolder selected in the current folder)
import time
import os
lastPath = window.get_active_title()
if lastPath == '\\':
  os.system("gnome-terminal 'cd'")
else:
  keyboard.send_keys("<ctrl>+<shift>+a")
  keyboard.send_keys("<ctrl>+i")
  keyboard.send_key("<tab>",4)
  time.sleep(0.1)
  keyboard.send_key("<tab>+<shift>",1)
  time.sleep(0.1)
  keyboard.send_keys("<ctrl>+i")
  terminalPath = 'cd '+clipboard.get_selection()+'\t'+lastPath
  keyboard.send_keys("<alt>+<f4>")
  keyboard.send_keys("<ctrl>+<alt>+t")
  keyboard.send_keys(terminalPath)
  keyboard.send_keys("<enter>")