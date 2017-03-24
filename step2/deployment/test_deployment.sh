export my_symphony_fqdn=$1
export my_rackhd_fqdn=$2
export my_coprhd_fqdn=$3

py.test -v test_deployment.py --html /var/www/mvp_testing.html --self-contained-html

unset my_symphony_fqdn
unset my_rackhd_fqdn
unset my_coprhd_fqdn