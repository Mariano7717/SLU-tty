# SLU-tty Python version of the remote terminal session manager

# 2024june6
# initial draft of the application

# switch control for the desired action to perform
# connect to a ssh host
# edit add remove ssh host
# edit add remove credentials

def startmenu():
    banner = ("|||||||||||||||||||||||||||||||||||||||||||||||||||\n"
              "|----------------<   SLU-tty    >-----------------|\n"
              "|----------------<  START MENU  >-----------------|\n"
              "|SSH hosts Listing and Unified credential manager |\n"
              "|-------------------------------------------------|\n"
              "|                                                 |\n"
              "| Select the option that applies and hit ENTER    |\n"
              "| 1. Connect to a host                            |\n"
              "| 2. Edit hosts                                   |\n"
              "| 3. Edit credentials                             |\n"
              "|                                                 |\n"
              "|||||||||||||||||||||||||||||||||||||||||||||||||||\n")

    print(banner)

    # switch case and call functions

    switch_startmenu = input()
    # wait on input

    if switch_startmenu == "1":
        (hostconnect())
    elif switch_startmenu == "2":
        (edithost())
    elif switch_startmenu == "3":
        (editcreds())


def hostconnect():
    import os
    os.system("start cmd.exe")

def edithost():
    print("-----------------<  EDIT HOSTS  >------------------\n"
          " Edit your host information here \n"
          "---------------------------------------------------\n")
def editcreds():
    print("-----------------<  EDIT CREDS  >------------------\n"
          " Edit your Credentials information here \n"
          "---------------------------------------------------\n")

startmenu()
