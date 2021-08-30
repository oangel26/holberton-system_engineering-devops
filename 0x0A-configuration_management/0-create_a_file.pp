# Script that creates 'holberton' file in /tmp
file { '/tmp/holberton':
  path    => '/tmp/holberton',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
}
