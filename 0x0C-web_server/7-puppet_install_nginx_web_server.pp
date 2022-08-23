# Install and configure nginx on server

# Ensure nginx is installed
package{ 'nginx':
    ensure   => latest,
    provider => apt
}

# Ensure default config file is gone
file{ '/etc/nginx/sites-enabled/default':
    ensure => absent
}

# Ensure tacobell directory is present in www
file{ '/var/www/tacobell':
    ensure => directory
}

# Ensure tacobell index file is present
file{ '/var/www/tacobell/index.html':
    ensure  => 'present',
    content => "Hello World\n"
}

# Ensure custom 404 page is present
file{ '/var/www/tacobell/custom_404.html':
    ensure  => 'present',
    content => "Ceci n'est pas une page done with puppet\n"
}

# Server config file
file{ '/etc/nginx/conf.d/tacobell.conf':
    ensure  => 'present',
    content =>
    "server{
	listen 80;
	root /var/www/tacobell;
	index index.html;

	location /redirect_me {
		return 301 http://churger.tech/;
	}

	error_page 404 /custom_404.html;
	location = /custom_404.html {
		root /var/www/tacobell;
		internal;
	}

}"
}