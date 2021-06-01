import webbrowser
import time
keyboard.send_keys("<ctrl>+c")
time.sleep(0.1)
searchPar = clipboard.get_clipboard()# search parameter


#paperURL= "https://sci-hub.se"+clipboard.get_selection()
webbrowser.open("https://scholar.google.com.br/scholar?hl=pt-BR&as_sdt=0%2C5&q="+searchPar +"&btnG=")

