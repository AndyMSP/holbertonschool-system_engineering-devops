# replace bad part of file

exec { 'rename .phpp to .php':
    command => sed 's/.phpp/.php/' /var/www/html/wp-settings.php
}