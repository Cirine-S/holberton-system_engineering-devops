# Puppet manifest to login with the holberton user and open a file without any error message.

exec {'fix hard':
path    => '/usr/bin/',
command => "sudo sed -i 's/^holberton hard nofile.*/holberton hard nofile 2000/g' /etc/security/limits.conf",
}

exec {'fix soft':
path    => '/usr/bin/',
command => "sudo sed -i 's/^holberton soft nofile.*/holberton soft nofile 2000/g' /etc/security/limits.conf",
}