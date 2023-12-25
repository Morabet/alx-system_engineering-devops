# sets up a client SSH configuration file so that we can connect to a server without using a password

file { 'passwd auth':
  ensure => present,
  path   => '~/.ssh/school',
  line   => '    PasswordAuthentication no',
}

file { 'identity file':
  ensure => present,
  path   => '~/.ssh/school',
  line   => '     IdentityFile ~/.ssh/school',
}
