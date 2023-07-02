import subprocess as sb
from time import sleep
import os
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager

def launch_instances(name, nodecount):
	sb.call("terraform -chdir='./terraform/' init", shell=True)
	sb.call(f"terraform -chdir='./terraform/' apply --auto-approve -var name={name} -var nodecount={nodecount}  ", shell=True)
	sleep(30)

def configure_namenode_hadoop():
	ip = '0.0.0.0'
	print("Launching EC2 instance...")
	launch_instances('namenode', 1)
	#sb.call("terraform -chdir='./terraform/' init", shell=True)
	#sb.call("terraform -chdir='./terraform/' apply -var name='namenode' -var nodecount=1  ", shell=True)
	#dl = DataLoader()
	#im = InventoryManager(loader=dl, sources=['./playbooks/hadoop/inventory'])
	master_ip = im.list_hosts()[0]
	#master_ip = input("Enter Master IP: ")
	print("Configuring Namenode...")
	sb.call(f'ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i ./playbooks/hadoop/inventory --become --become-method=sudo --become-user=root --private-key=./playbooks/hadoop/hadoop.pem ./playbooks/hadoop/namenode.yml', shell=True)

def configure_datanodes_hadoop():
	print("Launching EC2 instance...")
	launch_instances('datanode', input('datanode count: '))
	#sb.call("terraform -chdir='./terraform/' init", shell=True)
	#sb.call(f"terraform -chdir='./terraform/' apply -var name='datanode' -var nodecount={input('datanodes count: ')} ", shell=True)
	#dl = DataLoader()
	#im = InventoryManager(loader=dl, sources=['./playbooks/hadoop/inventory'])
	#master_ip = im.list_hosts()[0]
	master_ip = input("masterIP address: ")
	print("Configuring Datanode...")
	sb.call(f'ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i ./playbooks/hadoop/inventory -e namenode={master_ip} --become --become-method=sudo --become-user=root --private-key=./playbooks/hadoop/hadoop.pem ./playbooks/hadoop/datanode.yml', shell=True)

def configure_cluster(ips):
	launch_instances('node', 3)
	print("Configuring Namenode...")
	sb.call(f'ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i ./playbooks/hadoop/inventory --become --become-method=sudo --become-user=root --private-key=./playbooks/hadoop/hadoop.pem ./playbooks/hadoop/namenode.yml', shell=True)

	dl = DataLoader()
	im = InventoryManager(loader=dl, sources=['./playbooks/hadoop/inventory'])
	master_ip = im.list_hosts()[0]
	print("Configuring Datanode...")
	sb.call(f'ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i ./playbooks/hadoop/inventory -e namenode={master_ip} --become --become-method=sudo --become-user=root --private-key=./playbooks/hadoop/hadoop.pem ./playbooks/hadoop/datanode.yml', shell=True)

def hadoop():
	while True:
		os.system('tput setaf 10')
		print("""
			-----------------------------------------------------
				Hadoop:
			-----------------------------------------------------	
				1. Configure Hadoop Namenode
				2. Configure Hadoop Datanode
				3. Configure the Whole Cluster
				4. Show Report
				5. Main Menu
			-----------------------------------------------------
			""")
		os.system("tput setaf 2")
		ch  = ""
		while ch == "":
			ch = input("Enter choice : ")
		ch = int(ch)
		
		os.system('tput setaf 7')
		if ch == 1:
			configure_namenode_hadoop()
		elif ch == 2:
			configure_datanodes_hadoop()
		elif ch == 3:
			ips = list(input('Enter IPs of Datanodes separated by space : ').split(" "))
			configure_cluster(ips)
		elif ch == 4:
			os.system("hadoop dfsadmin -report")
		elif ch == 5:
			os.system("clear")
			break
		else:
			os.system("tput setaf 1")
			print("Invalid Input!")