import time
import os
import subprocess as sb
import time

def Lvm():                            #Creates lvm partition
    ch=input("Do you want to know the hard disk information:[Y/N]\n")
    if ch=="Y" or ch=="y":
      sb.call("fdisk -l",shell=True)
      time.sleep(2)

    hdname=input("\nEnter the hard disk name: \n")
    sb.call("pvcreate {}".format(hdname),shell=True)

    ch1=input("Do you want to see the physical volume info:[Y/N]\n")
    if ch1=="Y" or ch1=="y":
      sb.call("pvdisplay {}".format(hdname),shell=True)
      time.sleep(2)

    vname=input("Enter the vg name: \n")
    sb.call("vgcreate {} {}".format(vname,hdname),shell=True)

    ch2 = input("Do you want to see the volume group info:[Y/N]\n")
    if ch2 == "Y" or ch2 == "y":
      sb.call("vgdisplay {}".format(vname), shell=True)
      time.sleep(2)

    lv=input("Enter the name of lv: \n")
    size=input("Enter the size of lv: \n")
    sb.call("lvcreate --size {} --name {} {}".format(size,lv,vname),shell=True)

    ch3 = input("Do you want to see the lvm info:[Y/N]\n")
    if ch3 == "Y" or ch3 == "y":
      sb.call("lvdisplay {}/{}".format(vname,lv), shell=True)
      time.sleep(2)

    sb.getoutput("mkfs.ext4 /dev/{}/{}".format(vname,lv))

    dir=input("Enter the directory name: \n")
    sb.call("mkdir /{}".format(dir),shell=True)
    sb.call("mount /dev/{}/{}  /{}".format(vname,lv,dir),shell=True)
    time.sleep(1)

    ch4 = input("Do you want to see the hard disk info:[Y/N]\n")
    if ch4 == "Y" or ch4 == "y":
      sb.call("df -h", shell=True)

def increase():
    path=input("Enter the path of lv: \n")
    size1=input("Enter the size: \n")
    sb.call("lvextend --size +{} /dev/{}".format(size1,path),shell=True)
    sb.call("resize2fs {}".format(path),shell=True)
    sb.call("df -h",shell =True)

def decrease():
    m=input("Enter the mount point: \n")
    sb.call("umount {}".format(m),shell=True)
    vname=input("Enter the vg name:\n")
    lv=input("Enter the name of lv: \n")
    sb.call("e2fsck -f /dev/mapper/{}-{}".format(vname,lv),shell=True)
    sb.call("resize2fs /dev/mapper/{}-{}".format(vname,lv),shell=True)
    size2=input("Enter the size to be reduced: \n")
    sb.call("lvreduce --size -{} /dev/mapper/{}-{}".format(size2,vname,lv),shell=True)
    sb.call("mount /dev/{}/{}".format(vname,m),shell=True)
   
   
def partition():
    ch=input("Do you want to know the hard disk information:[Y/N]\n")
    if ch=="Y" or ch=="y":
      sb.call("fdisk -l",shell=True)
      time.sleep(2)
    
    hd=input("Enter the hard disk you want to use for partition: \n")
    s=input("Enter the size of the partition: \n")
    mount=input("Folder name/Mount Point: \n")
    sb.getoutput("fdisk {}".format(hd))
    time.sleep(1)
    os.system("echo p\n")
    time.sleep(1)
    os.system("echo n\n")
    time.sleep(1)
    time.sleep(1)
    os.system("echo $s\n")
    time.sleep(1)
    os.system("echo w\n")
    sb.getoutput("udevadm settle")
    sb.getoutput("mkfs.ext4  {}".format(hd))
    sb.getoutput("mkdir /{}".format(mount))
    sb.getoutput("mount {}/{}".format(hd,mount))
    sb.call("df -h",shell=True)
    
def change_permission():
    dir=input("Enter the path of the file: \n")
    sb.getoutput("ls  -l {}".format(dir))
    person=input("Whose permission you want to change? -To change owner permission PRESS o\n  -To change user permission PRESS u\n -To change group permission PRESS g\n")
    permissions=input("List of permissions:\n  r(read) \n  w(write) \n x(execute)\n")
    sign=input("To remove permission press '-'\n To add permission press '+'\n")
    sb.call("chmod {}{}{}".format(person,sign,permissions),shell=True)
    
def change_owner():
    owner=input("Enter the new owner name: \n")
    file=input("Enter the file name: \n")
    sb.call("chown {} {}".format(owner,file),shell=True)
  
def web_server():
    out = sb.getstatusoutput("rpm -q httpd")
    if out[0]==1:
      if 'not installed' in out[1]:
        out=sb.getstatusoutput('yum install httpd -y')
        if 'complete!' in out[1]:
          print("Succesfully installed \n")
    else:
      out = sb.getstatusoutput('yum install httpd -y')
      if 'complete!' in out[1]:
        print("Succesfully installed \n")
                              
def webpage():
     f= input("Enter the file name: \n")
     fh = open("/var/www/html/{}".format(f), "+w")
     lines_of_text = []
     input=input("Enter the content of webpage:  \n")
     for i in input:
        lines_of_text=lines_of_text.append(i)
     fh.writelines(lines_of_text)
     fh.close()

def fileHandling(ch1):
    if ch1==1:
      dir=input("Enter the directory name: \n")
      sb.getstatusoutput("mkdir {}".format(dir))
      time.sleep(5)

    elif ch1==2:
      dir=input("Enter the name of the directory you want to delete: \n")
      sb.call("rmdir {}".format(dir),shell="True")
      time.sleep(5)
      
    elif ch1==3:
      file=input("Enter the file name along with the path : \n")
      contents=input("Enter the contents of the file: \n")
      f= open("{}".format(file),"w+")
      f.write(contents)
      f.close()
      time.sleep(5)
      
    elif ch1==4:
      file=input("Enter the file name along with path : \n")
      sb.call("rm {}".format(file),shell=True)
      time.sleep(5)
  
    elif ch1==5:
      file=input("Enter the file name along with path : \n")
      sb.call("cat {}".format(file),shell=True)
      time.sleep(5)
      
    elif ch1==6:
      dir=input("Enter the path of the directory: \n")
      sb.call("ls {}".format(dir),shell=True)
      time.sleep(5)
      
    elif ch1==7:
      dir=input("Enter the path of the directory: \n")
      sb.call("ls  -l {}".format(dir),shell=True)
      time.sleep(5)
      
    elif ch1==8:
      change_permission()
      time.sleep(5)
      
    elif ch1==9:
      change_owner()
      time.sleep(5)

    elif ch1==10:
      exit()
    
    else:
      os.system("tput setaf 1 | echo 'Sorry Not Supported!!'")
      exit()
    return 'success'

def linux(T, ip):
    ch = 0
    while ch != 4:
        os.system('tput setaf 10')
        print("""
            -----------------------------------------------------
                Linux:
            -----------------------------------------------------   
                1. date
                2. calender
                3. Show IP
                4. File handling
                5. Storage
                6. Networking
                7. Configure servers/Downloading softwares
                8. User Adminstration
                9. Main Menu
            -----------------------------------------------------
            """)
        os.system("tput setaf 2")
        ch  = ""
        while ch == "":
            ch = input("Enter choice : ")
        ch = int(ch)
            
        os.system('tput setaf 7')

        if ch == 1:
            os.system("tput setaf 3")
            if T == 'local':
                    os.system("date")
            else:
                    os.system("ssh  {} date".format(ip))
            input()
        elif ch == 2:
            os.system("tput setaf 3")
            if T == 'local':
                os.system("cal")
            else:
                os.system("ssh {} cal".format(ip))
            input()

        elif ch == 3:
            os.system("tput setaf 3")
            if  T == 'local':
                os.system("ifconfig")
            else:
                os.system("ssh {} ifconfig enp0s3".format(ip))
            input()
        elif ch == 4:
            os.system("clear")
            os.system("tput setaf 12")
            print("""
                  --------------------------------------
                  Press 1:Create a directory
                  Press 2:Remove the directory
                  Press 3:Create file 
                  Press 4:Delete the file
                  Press 5:View the contents of file
                  Press 6:To view list of files present in a directory
                  Press 7:To view the permissions given to a directory/file              
                  Press 8:To change the given permissions to file
                  Press 9:To change the owner of file
                  Press 10:To exit
                  --------------------------------------
                """)
            os.system("tput setaf 7")
            ch1=input("What is your choice?\n")
            fileHandling(int(ch1))

        elif ch == 9:
            os.system("clear")
            break

        else:
            os.system("tput setaf 1")
            print("Invalid Input!")
            


