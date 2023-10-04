#!/usr/bin/env python3
# pylint: disable=C0301,C0116,C0103,R0903

# Vendor         : DomTrues
# Provisioned by : Coopydood

# Import Required Modules
import os
# import time
# import subprocess
# import re 
# import json
# import sys
# import argparse

detectchoice = 0

def menu():
    global detectchoice
    # Get Terminal Size
    os.system("clear")
    spaces = ""
    i = 0
    terminal_size = os.get_terminal_size()
    while i < terminal_size.lines:
        spaces = spaces + "\n"
        i += 1
    # Menu
    print(spaces + "   Welcome to \033[94mOpenCore Configuration Assistant\033[0m")
    print("   Created by \033[1mDomTrues\033[0m\n")
    print("   This script was created with the sole purpose of simplifying\n   the process of mounting and unmounting your OpenCore.qcow2\n   so you can make any modifications necessary. \033[37m(e.g. config.plist)\n\n\033[93m   It is highly recommended that you \033[91m\033[1mBACKUP\033[0m\033[93m your OpenCore.qcow2\n   in case you mess something up.\033[0m\n")
    #print("   \033[93mAlso, please note that it is \033[91m\033[1mREQUIRED\033[0m\033[93m to have NBD installed on\n   your system.\033[0m\n")
    print("   Select an option to continue.\n")
    print("      1. Mount OpenCore ⚠\n         This will mount your OpenCore.qcow2 with read-write permissions.\n         \033[93mWill prompt you for superuser permissions, which are required.\033[0m\n")
    print("      2. Unmount OpenCore ⚠\n         This will unmount your OpenCore.qcow2 so you can boot with your modifications.\n         \033[93mWill prompt you for superuser permissions, which are required.\033[0m\n")
    print("      B. Back...")
    print("      Q. Exit\n")
    detectchoice = input("Select> ")
    if detectchoice == 1 or detectchoice == "1":
        print(spaces)
        os.system("sudo modprobe nbd")
        os.system("sudo qemu-nbd --connect=/dev/nbd0 boot/OpenCore.qcow2")
        os.system("mkdir -p boot/mnt")
        os.system("sudo mount /dev/nbd0p1 boot/mnt -o uid=$UID,gid=$(id -g)")
        print("\n   \033[92mOperation completed. \033[32m(mounted at ./boot/mnt/)\033[0m")
        input("\n   Press [ENTER] to continue...\n")
        detectchoice = 0
        menu()

    elif detectchoice == 2 or detectchoice == "2":
        print(spaces)
        os.system("sudo umount -R boot/mnt")
        os.system("sudo qemu-nbd --disconnect /dev/nbd0 2>&1 >/dev/null")
        os.system("sudo rmmod nbd")
        print("\n   \033[92mOperation completed. \033[32m(unmounted from ./boot/mnt/)\033[0m")
        input("\n   Press [ENTER] to continue...\n")
        detectchoice = 0
        menu()
    elif detectchoice == "B":
        print(spaces)
        os.system('./scripts/extras.py')
    elif detectchoice == "Q":
        exit()
    else:
        if len(detectchoice) > 1:
            print(spaces)
            print("   So... we wanna be a smartass. Well,\n   in the least respectful way possible...\n")
            print("                        /´¯¯`/)")
            print("                       /¯.../")
            print("                      /..../")
            print("                  /´¯/'..'/´¯¯`·¸")
            print("              /'/.../..../....../¨¯\\")
            print("             ('(....´...´... ¯~/'..')")
            print("              \\..............'...../")
            print("               \\....\\.........._.·´")
            print("                \\..............(")
            print("                 \\..............\\\n")
            input("   Press [ENTER] to continue...")
        detectchoice = 0
        menu()

menu()