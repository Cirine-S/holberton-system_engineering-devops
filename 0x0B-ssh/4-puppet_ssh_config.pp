# Puppet config
file_line { '/etc/ssh/ssh_config':
  line   => 'IdentityFile ~/.ssh/holberton',
}
file_line {'/etc/ssh/ssh_config':
  line   => 'PasswordAuthentication no',
}
