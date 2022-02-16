# puppet scripts taht executes command to correct error
exec { 'error_correction':
  command => 'sed -i \'s/class-wp-locale.phpp/class-wp-locale.php/g\' /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
}
