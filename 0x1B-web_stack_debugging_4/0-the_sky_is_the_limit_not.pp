# Puppet script to debug a lot of failed requests

exec { 'change ulimit':
  command => "sed -i 's/15/2000/g' /etc/default/nginx; service nginx restart",
  path    =>'/bin',
}
