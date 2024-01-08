# Create a custom header with puppet

$configure = "server {

        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;
	
	# Add a custom header
        add_header X-Served-By '$HOSTNAME';

        server_name _;

	location / {
                try_files \$uri \$uri/ =404;
        }

}"

package { 'nginx':
ensure  => 'installed',
}


file { '/etc/nginx/sites-available/default':
ensure  => 'present',
content => $configure
}

exec { 'service nginx restart':
path    => ['/usr/sbin', '/usr/bin']
}
