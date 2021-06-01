import webbrowser
import time
keyboard.send_keys("<ctrl>+l")
time.sleep(0.1)
keyboard.send_keys("<ctrl>+c")
time.sleep(0.1)
#paperURL= "https://sci-hub.se"+clipboard.get_selection()
webbrowser.open("https://sci-hub.se/"+clipboard.get_clipboard())
time.sleep(0.1)
keyboard.send_key("<tab>",2)
time.sleep(0.1)
keyboard.send_keys("<enter>")

