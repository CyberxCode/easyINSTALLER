#! usr/bin/python
#A,#K
import os
import redhat
def easyINSTLLER():
    try:
        print ('''
                           \033[1;32m+ -- -- +=[esayINSTALLER]=+ -- -- +\033[1;m
         \033[1;32m+ -- -- +=[ Author: CyberCode | Homepage: www.fb.com/hbd0309]=+ -- -- +\033[1;m
                 \033[1;32m+ -- -- +=[Make your distro better. ]=+ -- -- +\033[1;m

1) RedHat/Fedora/CentOS...
2) Debian/Ubuntu/Mint...

            ''')
        def category():#List of programs
            print("""
        1)compiz
        2)emerald
        3)Fusion icon
        4)Font manager
        5)Conky
                  """)
            options=input("\:")
            try:
                if options in range(1,6):
                    return(options)
                else:
                    print("number you entered is incorrect please try again.")
            except ValueError:
                print("ValueError")

        while True:#Verification and install Programmes
            #os.system("sudo -s")
            distronum=input("Please choose your distro number: ")
            try:
                if distronum in range(1,3):
                    if distronum  == 1:#RedHat
                        options=category()
                        if options == 1:
                            redhat.compiz()
                        elif options==2:
                            redhat.emerald()
                        elif options==3:
                            redhat.Fusion_icon()
                        elif options==4:
                            redhat.font_manager()
                        elif options==5:
                            redhat.conky()
                        else:
                            print("number you entered is incorrect please try again.")
                    elif distronum ==2:#Debian
                        debian.PPA()
                        category()
                        if options == 1:
                            debian.compiz()
                        elif options==2:
                            debian.emerald()
                        elif options==3:
                            debian.Fusion_icon()
                        elif options==4:
                            debian.font_manager()
                        elif options==5:
                            debian.conky()
                        else:
                            print("number you entered is incorrect please try again.")
                    else:
                        print("number you entered is incorrect please try again.")
                else:
                    print("number you entered is incorrect please try again.")
            except ValueError:
                print("ValueError")

    except IOError:
        print("Hello")
easyINSTLLER()
