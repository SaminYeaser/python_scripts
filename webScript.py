import webbrowser, sys
import pyperclip

sys.argv #[file name, rest of the address in list]

if len(sys.argv)>1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/search/' + address)