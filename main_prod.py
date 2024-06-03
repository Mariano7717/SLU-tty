# SLU-tty Python version of the remote terminal session manager

# 2024june2
# initial draft of the application

# 2024june3
# "functionized everything", set some banners to clear clutter and logic below

# switch control for the desired action to perform
# connect to a ssh host
# edit add remove ssh host
# edit add remove credentials

banner_startmenu = (""
                    "|||||||||||||||||||||||||||||||||||||||||||||||||||\n"
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
                    "|||||||||||||||||||||||||||||||||||||||||||||||||||\n"
                    "")

banner_hostconnect = (""
                      "-----------------<  CONNECT     >------------------\n"
                      " Connect to host by tags or hostname               \n"
                      "---------------------------------------------------\n"
                      " find a way to list tags first and individual hosts after"
                      "")

banner_hostedit = ("-----------------<  EDIT HOSTS  >------------------\n"
                   " Edit your host information here \n"
                   "---------------------------------------------------\n"
                   "  1. Add a new host \n"
                   "  2. Add a new tag \n"
                   "  3. Edit an existing host \n"
                   "  3. Delete an existing host \n"
                   "  4. "
                   "")

banner_crededit = ("-----------------<  EDIT CREDS  >------------------\n"
                   " Edit your credentials information here \n"
                   "---------------------------------------------------\n"
                   "  1. Add a new credential \n"
                   "  2. Edit an existing credential \n"
                   "  3. Delete an existing credential \n"
                   "")



def startmenu():
    print(banner_startmenu)

    # switch case and call functions

    switch_startmenu = input()
    # wait on input

    if switch_startmenu == "1":
        (hostconnect())
    elif switch_startmenu == "2":
        (hostedit())
    elif switch_startmenu == "3":
        (credsedit())


def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def hostconnect():
    import os
    clear()
    print(banner_hostconnect)
    os.system("start cmd.exe /K ssh " % ())


def hostedit():
    clear()
    print(banner_hostedit)


def credsedit():
    clear()
    print(banner_crededit)


startmenu()
