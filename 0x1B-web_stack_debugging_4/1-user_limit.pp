# Puppet manifest to login with the holberton user and open a file without any error message.

exec {'holberton hard':
path     => '/usr/bin/',
command  => "sudo sed -i 's/^holberton hard /holberton hard nofile 2000/g' /etc/security/limits.conf",
}

exec {'holberton soft':
path     => '/usr/bin/',
command  => "sudo sed -i 's/^holberton soft /holberton soft nofile 2000/g' /etc/security/limits.conf",
}