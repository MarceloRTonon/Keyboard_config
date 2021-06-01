import webbrowser
import time
keyboard.send_keys("<ctrl>+c")
time.sleep(0.01)
searchPar = clipboard.get_clipboard()# search parameter
time.sleep(0.01)
keyboard.send_keys("<ctrl>+l")
time.sleep(0.01)
keyboard.send_keys("<ctrl>+c")
time.sleep(0.01)
#paperURL= "https://sci-hub.se"+clipboard.get_selection()
webbrowser.open("https://sci-hub.se/"+clipboard.get_clipboard())
time.sleep(0.01)
keyboard.send_key("<tab>",2)
time.sleep(0.1)
keyboard.send_keys("<enter>")
webbrowser.open("https://scholar.google.com.br/scholar?hl=pt-BR&as_sdt=0%2C5&q="+searchPar +"&btnG=")
