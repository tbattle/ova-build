# Prerequisites
## Virtual Box
https://www.virtualbox.org/
VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use. Not only is VirtualBox an extremely feature rich, high performance product for enterprise customers, it is also the only professional solution that is freely available as Open Source Software under the terms of the GNU General Public License (GPL) version 2.

## Vagrant
https://www.vagrantup.com/
Vagrant is a tool for building and managing virtual machine environments in a single workflow. With an easy-to-use workflow and focus on automation, Vagrant lowers development environment setup time, increases production parity, and makes the "works on my machine" excuse a relic of the past.
	
# OVA Build
[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://img.shields.io/badge/License-GPL%20v2-blue.svg)

## Deploying a demo of the Symphony OVA 

1. Download and unzip the project-symphony-controller.zip file into a new Vagrant folder.
2. Open a terminal window and change directory your Vagrant folder.
3. Run the command “vagrant up” (this can take up to 5-6 mins the first time)
4. Once the Vagrant has created and started you Virtual Box you can ssh in to the box.
  - Username: vagrant
  - Password: vagrant
  - IP Address: 127.0.0.1
  - Port: 2222
 

## Before you begin

Before deploying the demo, ensure that you have satisfied these prerequisites:

- OVF tool has been installed
- Python 2 has been installed
- Python pysphere library has been installed (pip install -U pysphere)
- vCenter access must be available on your system

## Deploying the demo

Here are the steps to follow to deploy the demo: 

1. Browse to Github: https://eos2git.cec.lab.emc.com/malism/ova-build
2. Clone the repository with the git clone command: `git clone https://eos2git.cec.lab.emc.com/malism/ova-build`

  This will download the following files:
  - Python deployment scripts
  - OVA deployment config file (machine_info.csv)  
  - OVA master OVA deployment script (ova_deploy.sh)
  - Symphony system definition JSON file (ssd_system_definition.json) 
  - Script to configure the Symphony system definition (ssd_set.py)

  These files are required to deploy the Symphony OVA demo.

3. Change the directory to ./ova-build/step2/deployment: `cd ova-build/step2/deployment`
4. Optionally, edit the OVA deployment configuration file (`machine_info.csv`) to add local network settings and other properties needed for your environment. More than one machine can be added to this file on separate rows.

5. Execute the master OVA deployment script (`. ova_deploy.sh <symphony-machine-name> <rackhd-machine-name> <coprhd-machine-name>`) to deploy the Symphony OVA, RackHD OVA, and CoprHD OVA into the local vCenter environment.

  For example: `. ova_deploy.sh auto-demo-symphony.mpe.lab.vce.com auto-demo-rackhd-symphony.mpe.lab.vce.com auto-demo-coprhd-symphony.mpe.lab.vce.com`
  
  Deployment of the three OVAs will take about 15 minutes.  During this time, snapshots will be taken, the VMs will be deployed, and the VMs will then be powered on.
6. Make a call to RackHD to see that it is up and running: `http://auto-demo-rackhd.mpe.lab.vce.com:8080/api/2.0/config`

7. Check the user interface for Symphony to see that it is up and running. 
  
  For example, if you deployed auto-demo-symphony, browse to this URL: `http://auto-demo-symphony.mpe.lab.vce.com:12000`
 
  At this point, you should not see any data.

7. Run `. ssd_set.sh <symphony-deploy-machine>` to configure the system definition for the demo.

  For example: `. ssd_set.sh auto-demo-symphony.mpe.lab.vce.com`

8. Look at the user interface for Symphony again to see that data has now been loaded:  `http://auto-demo-symphony.mpe.lab.vce.com:12000` 

9. Check the CoprHD site to see that it is up and running: `https://auto-demo-coprhd.mpe.lab.vce.com`

## Testing
## Contributing
## Community
## Licensing
