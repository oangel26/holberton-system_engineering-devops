# Script that installs pupput-lint
package { 'puppet-lint':
  ensure   => '2.5.0',
  provider => 'gem',
  name     => 'puppet-lint',
}
