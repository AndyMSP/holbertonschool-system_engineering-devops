# Terminate process called 'killmenow'
exec{ 'terminate':
    command => '/usr/bin/pkill killmenow'
}