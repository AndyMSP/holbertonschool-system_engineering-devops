# Replaces content of file
file { '/etc/security/limit.conf':
    ensure  => 'present',
    content => 'holberton hard nofile 5000\nholberton soft nofile 5000'
}