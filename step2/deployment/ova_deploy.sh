# Deploy Symphony
echo
echo "*** Deploy Symphony *** "
echo "*** Deploy Symphony *** "
echo "*** Deploy Symphony *** "
echo
#python ova-deploy-read-info.py --myOVA_URL http://10.3.61.214/builds/symphony-ova-build-step2-master_stable/Symphony.ova --myVM_FQDN $1
#python create-snapshot-read-info.py --myVM_FQDN $1
python revert-snapshot-read-info.py --myVM_FQDN $1
python power-on-read-info.py --myVM_FQDN $1

# Deploy RackHD
echo
echo "*** Deploy RackHD *** "
echo "*** Deploy RackHD *** "
echo "*** Deploy RackHD *** "
echo
#python ova-deploy-rackhd-read-info.py --myOVA_URL http://10.3.61.214/builds/rackhd_ova_stable/rackhd-ubuntu-16.04-2.0.0.ova --myVM_FQDN $2
#python create-snapshot-read-info.py --myVM_FQDN $2
python revert-snapshot-read-info.py --myVM_FQDN $2
python power-on-read-info.py --myVM_FQDN $2

# Deploy CoprHD
echo
echo "*** Deploy CoprHD *** "
echo "*** Deploy CoprHD *** "
echo "*** Deploy CoprHD *** "
echo
#python ova-deploy-coprhd-read-info.py --myOVA_URL http://10.3.61.214/builds/coprhd_ova_stable/CoprHD.x86_64-3.6.0.0.990.ovf --myVM_FQDN $3
#python create-snapshot-read-info.py --myVM_FQDN $3
python revert-snapshot-read-info.py --myVM_FQDN $3
python power-on-read-info.py --myVM_FQDN $3

# Disable RackHD Authentication
echo
echo "*** Disable RackHD Authentication *** "
echo "*** Disable RackHD Authentication *** "
echo "*** Disable RackHD Authentication *** "
echo
python rackhd-disable-auth.py --myVM_FQDN $2

# Verify RackHD Deployment
echo
echo "*** Verify RackHD Deployment *** "
echo "*** Verify RackHD Deployment *** "
echo "*** Verify RackHD Deployment *** "
echo
python rackhd_verification.py --myVM_FQDN $2

# Verify Symphony Deployment
echo
echo "*** Verify Symphony Deployment *** "
echo "*** Verify Symphony Deployment *** "
echo "*** Verify Symphony Deployment *** "
echo
python symphony_verification.py --myVM_FQDN $1

# Verify CoprHD Deployment
echo
echo "*** Verify CoprHD Deployment *** "
echo "*** Verify CoprHD Deployment *** "
echo "*** Verify CoprHD Deployment *** "
echo
python coprhd_verification.py --myVM_FQDN $3

# Test Suites
. test_deployment.sh $1 $2 $3

# Create Links
echo "<h1 style=\"color: #5e9ca0;\">Symphony Deployment:</h1>" > Product_Links.html
echo "<h2>&nbsp; &nbsp; Symphony Consul:&nbsp;<a href=\"http://$1:8500\">http://$1:8500</a></h2>" >> Product_Links.html
echo "<h2>&nbsp; &nbsp; Symphony Configuration Insight:&nbsp;<a href=\"http://$1:12000\">http://$1:12000</a></h2>" >> Product_Links.html
echo "<h2>&nbsp; &nbsp; Symphony Log Collection:&nbsp;<a href=\"http://$1:8082\">http://$1:8082</a></h2>" >> Product_Links.html
echo "<h2>&nbsp; &nbsp; Symphony RabbitMQ:&nbsp;<a href=\"http://$1:15672\">http://$1:15672</a></h2>" >> Product_Links.html
echo "<h2>&nbsp; &nbsp; Symphony RCM Fitness:&nbsp;<a href=\"http://$1:19080/rcm-fitness-ui\">http://$1:19080/rcm-fitness-ui</a></h2>" >> Product_Links.html
echo "<h2>&nbsp;</h2>" >> Product_Links.html
echo "<h1 style=\"color: #5e9ca0;\">RackHD Deployment:</h1>" >> Product_Links.html
echo "<h2>&nbsp; &nbsp; RackHD API:&nbsp;<a href=\"http://$2:8080/api/2.0/config\">http://$2:8080/api/2.0/config</a></h2>" >> Product_Links.html
echo "<p>&nbsp;</p>" >> Product_Links.html
echo "<h1 style=\"color: #5e9ca0;\">CoprHD Deployment:</h1>" >> Product_Links.html
echo "<h2>&nbsp; CoprHD Login Page:&nbsp;<a href=\"https://$3\">https://$3</a></h2>" >> Product_Links.html
