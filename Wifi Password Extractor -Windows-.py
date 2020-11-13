import subprocess

WifiCommand = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n') #excute netsh wlan show profiles command


#NamesMsg = "Here is your Wifi Networks!\n"

WifiNames = [line.split(':')[1][1:-1] for line in WifiCommand if "All User Profile" in line] #organizing the result


#print(WifiCommand)

for Wifi in WifiNames:


    PasswordCommand = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', Wifi, 'key=clear']).decode('utf-8').split('\n') #excute netsh wlan show profiles (wifiname) key=clear
    PasswordCommand = [line.split(':')[1][1:-1] for line in PasswordCommand if "Key Content" in line] #organizing the result
    try:
        print(f'Name: {Wifi}, Password: {PasswordCommand[0]}') #printing out the whole results
    except Error:
        Print(f'Name: {Wifi}, Password: There is no Stored-Password') #Error if can't read or find the Password



    #PasswordMsg = 'Here is your Passwords !\n'

#print (PasswordMsg, PasswordCommand)
