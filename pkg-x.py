#turmux modules installer
import os

os.system("clear")
purple = '\x1b[38;5;165m'
purple2 = '\x1b[38;5;164m'
purple3 = '\x1b[38;5;163m'
pink = '\x1b[38;5;199m'
green = '\x1b[38;5;199m'
print(f'''{pink}
██████╗░██╗░░██╗░██████╗░  ██╗░░██╗
{purple3}██╔══██╗██║░██╔╝██╔════╝░  ╚██╗██╔╝
██████╔╝█████═╝░██║░░██╗░  ░╚███╔╝░
{purple2}██╔═══╝░██╔═██╗░██║░░╚██╗  ░██╔██╗░
██║░░░░░██║░╚██╗╚██████╔╝  ██╔╝╚██╗
{purple}╚═╝░░░░░╚═╝░░╚═╝░╚═════╝░  ╚═╝░░╚═╝

          A TOOL BY NIMSITH
               [V 0.1]
{green}
''')
print("  1) python             10) git")
print("  2) unzip              11) apt")
print("  3) toilet             12) ruby")
print("  4) php                13) wget")
print("  5) bash               14) curl")
print("  6) cmatrix            15) unzip")
print("  7) figlet             16) sl")
print("  8) apk-tools          17) nmap")
print("  9) pyfiglet")
print()
print("  98)install any other pakage")
print("  99)how to install pakages manually")
print()
print()
x=int(input("  please select an option :"))
os.system("clear")
if x==1:
    os.system("pkg install python")
if x==2:
    os.system("pkg install unzip")
if x==3:
    os.system("pkg install toilet")
if x==4:
    os.system("pkg install php")
if x==5:
    os.system("pkg install bash")
if x==6:
    os.system("pkg install cmatrix")
if x==7:
    os.system("pkg install figlet")
if x==8:
    os.system("pkg install apk-tools")
if x==9:
    os.system("pkg install pyfiglet")
if x==10:
    os.system("pkg install git")
if x==11:
    os.system("pkg install apt")
if x==12:
    os.system("pkg install ruby")
if x==13:
    os.system("pkg install wget")
if x==14:
    os.system("pkg install curl")
if x==15:
    os.system("pkg install unzip")
if x==16:
    os.system("pkg install sl")
if x==17:
    os.system("pkg install nmap")
if x==98:
    print("Oops this option is not avalable at this moment !")
    print()
    print("make sure you having a proper network connection and latest update of PKG X ")
    print()
    up=input("Do you wanna update the tool [y/n] :")
    if up=="y":
        os.system("git clone https://github.com/mrnimsith/PKG-X")
if x==99:
    print("dont worry we will help you just type the package name you wanna install :")
    print()
    y=input()
    os.system("clear")
    print("okay now just copy n paste the below command on turmux to install the tool")
    print()
    print("pkg install",y)
    print()
    z=input()
os.system("clear")
x=input("press enter to leave :(")
os.system("clear")








