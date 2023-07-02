import subprocess as sb

out = sb.getstatusoutput("sudo rpm -q git")
if out[0] == 1:
        if 'not installed' in out[1]:
                out = sb.getstatusoutput('sudo yum install git -y')
                if 'complete!' in out[1]:
                        sb.call("echo 'Successfully installed git...'", shell=True)


sb.call("rm -rf /home/ec2-user/DSCWOW.TUI/", shell=True)
print("Cloning..")
sb.call("git clone https://github.com/ManthanChoudhury/DSCWOW.TUI.git",shell=True)
"""if out[0] == 0:
        sb.call("echo 'repository cloned successfully...", shell=True)
else:
        sb.call("echo 'Repository clone  failed...", shell=True)
        print(out[1])"""
