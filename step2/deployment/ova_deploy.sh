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

# Do Someting Here for CoprHD
# Verify CoprHD Deployment
echo
echo "*** Verify CoprHD Deployment *** "
echo "*** Verify CoprHD Deployment *** "
echo "*** Verify CoprHD Deployment *** "
echo
python coprhd_verification.py --myVM_FQDN $3
