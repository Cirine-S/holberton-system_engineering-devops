# Puppet script to debug a lot of failed requests

exec { 'change ulimit':
  command => "sudo sed -i 's/15/2000/g' /etc/default/nginx; sudo service nginx restart",
  path    => '/usr/bin',
}
