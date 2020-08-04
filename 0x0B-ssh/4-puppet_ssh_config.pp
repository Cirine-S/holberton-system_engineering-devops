# Puppet config
file_line {'Use the private key':
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
}
file_line {'Refuse pwd auth':
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}
