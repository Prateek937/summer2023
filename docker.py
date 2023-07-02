import os
from time import sleep
import subprocess as sb 

def docker_install(T):
    output = sb.getstatusoutput('rpm -q docker')
    if output[0] == 1:
        if 'not installed' in output[1]:
            sleep(1)
            os.system('tput setaf 3')
            sb.call("echo 'Downloading docker, please wait ...'", shell=True)
            sb.call("yum install docker -y", shell=True)
            sleep(1)
            sb.call("echo 'Enabling container services...'", shell=True)
            sb.getstatusoutput("systemctl enable docker")
            sb.getstatusoutput("systemctl start docker")

            os.system('tput setaf 2')
            print('Docker-ce successfully Installed and Starded !')
                    
    else:
        sleep(1)
        os.system('tput setaf 6')
        print('Docker already installed !\n Starting container Services..')
        sb.getstatusoutput("systemctl start docker")
        print('Service stated successfully! ')

def status(T, ip):
    os.system('tput setaf 3')
    if T == 'local':
        sb.call("systemctl status docker", shell = True)
    else:
        os.system('ssh root@{} systemctl status docker'.format(ip))
def pull_docker_images(T, ip, img_name):
    os.system('tput setaf 3')
    if T == 'local':
        sb.call("docker pull {}".format(img_name), shell=True)
    else:
        os.system("ssh {} docker pull {}".format(ip, img_name))

def show_docker_images(T, ip):
    os.system('tput setaf 3')
    if T == 'local':
        sb.call("docker images", shell=True)
    else:
        os.system("ssh {} docker images".format(ip))

def display_all_containers(T, ip):
    os.system('tput setaf 3')
    if  T == 'local':
        sb.call("docker ps -a", shell=True)
    else:
        os.system("ssh {} docker ps -a".format(ip))

def run_docker_container(T,ip, os_name,version, title):
    os.system('tput setaf 3')
    if T == 'local':
        sb.call("docker run -it --privileged --name {} {}:{}".format(title, os_name, version), shell=True)
    else:
        os.system("ssh -t {} docker run -it --name {} {}".format(ip, title, os_name))

def run_detached_container(T,image, version, os_name):
    os.system('tput setaf 3')
    sb.call("docker run -dit --privileged --name {} {}".format(os_name, image+':'+version), shell = True)

def remove_all_containers(T, ip):
    os.system('tput setaf 3')
    if T == 'local':
        sb.call("docker rm `docker ps -a -q`", shell=True)
    else:
        sb.call('ssh {} "docker rm `docker ps -a -q`"'.format(ip), shell = True)

def remove_one_container(T, ip, id):
    os.system('tput setaf 3')
    if T == 'local':
        os.system("docker rm id {}".format(id))
        print("Successfully Removed {}".format(id))
    else:
        os.system("ssh {} docker rm id {}".format(ip, id))
        os.system("ssh {} echo 'Successfully Removed!'".format(ip))    

def docker_info(T, ip):
    os.system('tput setaf 3')
    if T == 'local':
        sb.call("docker info", shell = True)
    else:
        os.system("ssh {} docker info".format(ip))        



def docker(T, ip):
    ch = 0
    while ch != 12:
        os.system('tput setaf 4')
        print("""
                -----------------------------------------------------
                    Welcome to Docker!:
                -----------------------------------------------------
                    1. Install Docker-ce
                    2. Check Status of Docker
                    3. Docker Information     
                    4. Show Docker Images
                    5. Pull a Docker Image 
                    6. Show all Containers
                    7. Run Docker Container
                    8. Run Detached Container
                    9. Remove One Container
                   10. Remove all Containers
                   11. Main Menu
                -----------------------------------------------------
            """)
        os.system("tput setaf 2")
        ch  = ""
        while ch == "":
            ch = input("Enter choice : ")
        
        ch = int(ch)


        if ch == 1:
            docker_install(T)

        elif ch == 2:
            status(T, ip)

        elif ch == 3:
            docker_info(T, ip)

        elif ch == 4:
            show_docker_images(T, ip)

        elif ch == 5:
            img_name = input('Enter image name: ')
            pull_docker_images(T, ip,  img_name)

        elif ch == 6:
            display_all_containers(T, ip)

        elif ch == 7:
            image = input('Enter Image name: ')
            version = input('Enter os version :')
            os_name = input('Enter OS  name : ')
            run_docker_container(T, ip, image, version, os_name)

        elif ch == 8:
            os_name = input('Enter Image name: ')
            version = input('Enter os version :')
            title = input('Enter OS  name : ')
            run_docker_container(T, ip, os_name,version,title)

        elif ch == 9:
            id = input("Enter the  os name/ID: ")
            remove_one_container(T, ip, id)
        elif ch == 10:
            remove_all_containers(T, ip)
        elif ch == 11:
            os.system("clear")
            break
        else:
            os.system("tput setaf 1")
            print("Invalid Input!")


