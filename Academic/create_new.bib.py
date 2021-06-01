# Enter script code
import time
keyboard.send_keys("<ctrl>+a")
keyboard.send_keys("<ctrl>+c")

time.sleep(0.02)
NewEntry = '\n'+clipboard.get_clipboard()+'\n'

with open('/home/marcelo/Documentos/the_Bib/BibScript.bib', 'a') as file:
    file.write(NewEntry)
