# replaces content of file
file { '/etc/default/nginx':
    ensure  => 'present',
    content => 'ULIMIT="-n 10000"'
}