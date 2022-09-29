#change file name
file_line { 'bashrc_proxy':
  ensure => present,
  path   => '/var/www/html',
  line   => 'require_once( ABSPATH . WPINC . \'/class-wp-locale.php' );'
  match  => 'require_once( ABSPATH . WPINC . \'/class-wp-locale.phpp' );'
}