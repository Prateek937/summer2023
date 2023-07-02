import os
import linux_basic as linux
import docker
import aws
import hadoop
import apache_web


os.system("tput setaf 6")
os.system("clear")
operating_sys = input("Where u want to run prog ? (local/Remote) : ")
if operating_sys == 'remote':
    ip = input("Enter remote IP : ")
else:
    ip = 0
print("{}:{}".format(operating_sys, ip))


while True:
    os.system('tput setaf 5')
    print("""
        Main Menu:
        -----------------------------------------------------
            1. Linux
            2. Docker
            3. Hadoop
            4. AWS Cloud
            5. Apache httpd Server
            6. Exit 
        -----------------------------------------------------   
        """)
    os.system("tput setaf 2")
    choice  = ""
    while choice == "":
        choice = input("Enter choice : ")
    
    choice = int(choice)

    if operating_sys == "remote" or operating_sys == "local":
        if choice == 1:
            os.system("clear")
            linux.linux(operating_sys, ip)

        elif choice == 2:
            os.system("clear")
            docker.docker(operating_sys, ip)

        elif choice == 3:
            os.system("clear")
            hadoop.hadoop()

        elif choice == 4:
            os.system("clear")
            aws.aws()

        elif choice == 5:
            os.system("clear")
            apache_web.webserver()

        elif choice == 6:
            exit()

        else:
            os.system("tput setaf 1")
            print("Invalid Input! ")
