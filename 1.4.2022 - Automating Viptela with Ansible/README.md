This example is built using a DevNet Sandbox Environment for SD-WAN.  Choose a reservable SD-WAN sandbox.  Works on 19.2 and 20.4

Reserve a sandbox using the following link, connect to the VPN, SSH into the DevBox (10.10.20.50), and th


1. Reserve a sandbox [Cisco DevNet Sandbox for SD-WAN](https://devnetsandbox.cisco.com/RM/Topology)
2. Upon activiation, follow emailed instructions to login to VPN
3. SSH into the DevBox to perform automation task (Terminal should start in a python virtual environment)
4. Clone the respository using 'git clone https://github.com/tc45/sme_call'
5. cd into the directory 'cd sme_call'
6. cd into the directory '1.4.2022 - Automating Viptela with Ansible'
7. Ansible Examples
    - Install dependencies using pip - 'pip install -r requirements.txt'
    - Using URI Module (Native REST) to automate Viptela using Ansible
        - cd into directory 'cd Ansible_URI_module'
        - verify configuration is correct in 'inventory.json'
        - Launch playbook - 'ansible-playbook -i inventory.txt <PLAYBOOK_NAME>.yml'
        - PLAYBOOK_NAME
            - 01-vManage_Automation_using_Ansible_URI_module.yml - Basic playbook demonstrating logging in, getting a cookie, saving the cookie as a variable, and then printing the cookie.
            - 02-vManage_Automation_using_Ansible_URI_module.yml - Adding functionality to grab reboot data using stored cookie, then print the reboot data out.
            - 03-vManage_Automation_using_Ansible_URI_module.yml - Added Get list of devices, get tunnel stats, loop through devices for tunnel stats.
            - 04-vManage_Automation_using_Ansible_URI_module.yml - Added functionality 
    - Using Ansible SDK Module  to automate Viptela
        - cd into directory 'cd Ansible_Viptela_module'
        - verify configuration is correct in 'inventory.json'
        - Launch playbook - 'ansible-playbook -i inventory.txt <PLAYBOOK_NAME>.yml'
        - PLAYBOOK_NAME
            - 00-vManage_Automation_using_Ansible_Python_SDK.yml - Using ansible modules vmanage_device_facts and vmanage_policy_list_facts to pull back policy data
     
For more information on the  Viptela SDK see the [CiscoDevNet python-viptela Github repository](https://github.com/CiscoDevNet/python-viptela).
