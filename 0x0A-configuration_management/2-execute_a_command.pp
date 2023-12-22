# create a manifest that kills a process named killmenow
# using pkill with puppet

exec { 'killmenow':
  command => '/usr/bin/pkill killmenow'
}
