# sets up a client SSH configuration file so that we can connect to a server without using a password

file_line { 'passwd_auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}

file_line { 'identity_file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '     IdentityFile ~/.ssh/school',
}
