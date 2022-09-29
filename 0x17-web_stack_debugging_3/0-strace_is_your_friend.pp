# replace bad part of file
exec { 'rename_phpp_to_php':
    command => '/bin/sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php'
}