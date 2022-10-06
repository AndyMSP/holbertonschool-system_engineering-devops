# Replaces content of file
file { '/etc/default/nginx':
    ensure  => 'present',
    content => 'ULIMIT="-n 10000"'
}

# Restart nginx
exec { 'restart_nginx':
    command => '/usr/bin/service nginx restart'
}