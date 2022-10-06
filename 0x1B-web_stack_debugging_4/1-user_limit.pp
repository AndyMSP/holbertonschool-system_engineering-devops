# Replaces content of file
file { '/etc/security/limits.conf':
    ensure  => 'present',
    content => '
holberton hard nofile 5000
holberton soft nofile 5000
'
}
