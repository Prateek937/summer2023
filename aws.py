import os


def create_instance():
    imageid = input("AMI Image ID: ")
    instancetype = input("Instance type: ")
    subnetid = input("Subnet ID: ")
    securityid = input("Security Group ID: ")
    keyname = input("Key Name: ")

    os.system("aws ec2 run-instances --image-id {} --instance-type {} --count 1 --subnet-id {} --security-group-ids {} --key-name {}".format(imageid, instancetype, subnetid, securityid, keyname))


def start_instance():
    iid = input("Instance ID: ")
    os.system("aws ec2 start-instances --instance-ids {}".format(iid))


def stop_instance():
    ids = input("Instance ID: ")
    os.system("aws ec2 stop-instances --instance-ids {}".format(ids))


def create_volume():
    size = input("Size of volume in GB: ")
    zone = input("Enter zone ex:-ap-south-1a/b/c: ")
    
    os.system("aws ec2 create-volume --volume-type gp2  --size {} --availability-zone {}".format(size, zone))


def attach_volume():
    volId = input("Volume ID: ")
    instanceId = input("Instance ID: ")
    device = input("/dev/xvd[a-z]: ")
    os.system("aws ec2 attach-volume --device {} --volume-id {} --instance-id {}".format(device, volId, instanceId))


def iam():
    iamname = input("User-name: ")
#    permissionboundary = input("Permission boundary for User:")
    os.system("aws iam create-user --user-name {} ".format(iamname))


def snapshot():
    volumeid = input("Volume ID: ")
    description = input("Description: ")
    os.system("aws ec2 create-snapshot --volume-id {} --description {} ".format(volumeid, description))


def s3():
    bucketName = input("Bucket Name: ")
    region = input("Region: ")
    os.system("aws s3 mb s3://{} --region {}".format(bucketName, region))





def aws():
    ch = 0
    while ch != 12:
        os.system('tput setaf 4')
        print("""
                -----------------------------------------------------
                    Welcome to AWS Cloud!:
                -----------------------------------------------------
                    1. Configure AWS CLI
                    2. Launch EC2 Instance
                    3. Start Instance
                    4. Stop Instance    
                    5. Create EBS Volume
                    6. Attach EBS Volume 
                    7. Create IAM User
                    8. Create S3 Bucket
                    9. Create Snapshot of Instance
                   10. Configure Cloud Front
                   11. Cloud Watch
                   12. Main Menu
                -----------------------------------------------------
            """)
        os.system("tput setaf 2")
        ch  = ""
        while ch == "":
            ch = input("Enter choice : ")
        
        ch = int(ch)

        if ch == 1:
            os.system("aws configure")
        elif ch == 2:
            create_instance()
        elif ch == 3:
            start_instance()
        elif ch == 4:
            stop_instance()
        elif ch == 5:
            create_volume()
        elif ch == 6:
            attach_volume()
        elif ch == 7:
            iam()
        elif ch == 8:
            s3()
        elif ch == 9:
            snapshot()
        elif ch == 10:
            os.system("aws cloudfront create-distribution  --origin-domain-name webserveraws-lw.s3.amazonaws.com  --default-root-object  index.html")
        elif ch == 11:
            os.system("aws cloudwatch put-dashboard --dashboard-name  WatchClould-1 --dashboard-body  {\"widgets\":[]}")
        elif ch == 12:
            os.system("clear")
            break
        else:
            os.system('tput setaf 1')
            print("Invalid Input!")
