# ensure file is present with proper contents
file { 'ensure file is present':
    ensure  => 'present',
    path    => '/var/www/html/wp-settings.php',
    content => file('/root/fixed_wp-settings.php')
}
