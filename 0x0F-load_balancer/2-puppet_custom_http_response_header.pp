# automate task 0 with puppet
exec {'automate task0':
  command  => 'sudo apt -y update
sudo apt-get -y install nginx
sudo chmod 777 /var/www/html/index.nginx-debian.html
echo "Holberton School" > /var/www/html/index.nginx-debian.html
echo "server {                                                                  
    listen 80;                                                                  
    listen [::]:80 default_server;                                              
    root   /var/www//html;                                                      
    index index.nginx-debian.html index.nginx-debian.html;
    add_header X-Served-By $HOSTNAME;                    
                                                                     
}" > /etc/nginx/sites-available/default
sudo service nginx restart',
  provider  => shell,
}