# replace bad part of file

exec { 'rename .phpp to .php':
    command => '/bin/sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
    provider => shell
}
