This example is built using a DevNet Sandbox Environment for SD-WAN.  Choose a reservable SD-WAN sandbox.  Works on 19.2 and 20.4

Reserve a sandbox using the following link, connect to the VPN, SSH into the DevBox (10.10.20.50), and th


- Reserve a sandbox [Cisco DevNet Sandbox for SD-WAN](https://devnetsandbox.cisco.com/RM/Topology)
- Upon activiation, follow emailed instructions to login to VPN
- SSH into the DevBox to perform automation task (Terminal should start in a python virtual environment)
- Clone the respository using 'git clone https://github.com/tc45/sme_call'
    ```
    git clone https://github.com/tc45/sme_call
    ```
- cd into the directory 'cd sme_call'
    ```
    cd sme_call
    ```
- cd into the directory '7.6.21 - Using vManage SDK for Python'
    ```
    cd 7.6.21 - Using vManage SDK for Python
    ```
- Install dependencies using pip - 'pip install -r requirements.txt'
    ```
    pip install -r requirements.txt
    ```
- Scripts
   - 'python3 main.py' - Will login to vManage, pull device details, print output in table format for vedges and controllers.  Script will then pull template information based on templates configured on devices.
        ```
        python3 main.py
        ```
   - 'python3 list_methods.py' - Print the methods available in the Python SDK for Viptela
        ```
        python3 list_methods.py
        ```
   
For more information on the  Viptela SDK see the [CiscoDevNet python-viptela Github repository](https://github.com/CiscoDevNet/python-viptela).
