echo "<h1 style=\"color: #5e9ca0;\">Symphony Deployment:</h1>" > /var/www/Product_Links.html
echo "<h2>&nbsp; &nbsp; Symphony Consul:&nbsp;<a href=\"http://$1:8500\">http://$1:8500</a></h2>" >> /var/www/Product_Links.html
echo "<h2>&nbsp; &nbsp; Symphony Configuration Insight:&nbsp;<a href=\"http://$1:12000\">http://$1:12000</a></h2>" >> /var/www/Product_Links.html
echo "<h2>&nbsp; &nbsp; Symphony Log Collection:&nbsp;<a href=\"http://$1:8082\">http://$1:8082</a></h2>" >> /var/www/Product_Links.html
echo "<h2>&nbsp; &nbsp; Symphony RabbitMQ:&nbsp;<a href=\"http://$1:15672\">http://$1:15672</a></h2>" >> /var/www/Product_Links.html
echo "<h2>&nbsp; &nbsp; Symphony RCM Fitness:&nbsp;<a href=\"http://$1:19080/rcm-fitness-ui\">http://$1:19080/rcm-fitness-ui</a></h2>" >> /var/www/Product_Links.html
echo "<h2>&nbsp;</h2>" >> /var/www/Product_Links.html
echo "<h1 style=\"color: #5e9ca0;\">RackHD Deployment:</h1>" >> /var/www/Product_Links.html
echo "<h2>&nbsp; &nbsp; RackHD API:&nbsp;<a href=\"http://$2:8080/api/2.0/config\">http://$2:8080/api/2.0/config</a></h2>" >> /var/www/Product_Links.html
echo "<p>&nbsp;</p>" >> /var/www/Product_Links.html
echo "<h1 style=\"color: #5e9ca0;\">CoprHD Deployment:</h1>" >> /var/www/Product_Links.html
echo "<h2>&nbsp; &nbsp; CoprHD Login Page:&nbsp;<a href=\"https://$3\">https://$3</a></h2>" >> /var/www/Product_Links.html