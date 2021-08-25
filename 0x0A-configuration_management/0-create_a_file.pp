file { '/tmp/holberton':
  ensure => present,
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0744',
  source => 'I love Puppet',
}
