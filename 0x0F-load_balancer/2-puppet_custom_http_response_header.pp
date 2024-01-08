# Create a custom header with puppet

$configure = "server {

        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;
	
	# Add a custom header
        add_header X-Served-By $HOSTNAME;


        server_name _;

	location / {
                try_files \$uri \$uri/ =404;
        }

        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }

        error_page 404 /404.html;
        location = /404.html {
                internal;
        }
}"

package { 'nginx':
ensure	=> 'installed',
}

file { '/var/www/html/index.html':
ensure	=> 'present',
content	=> 'Hello World!'
}

file { '/etc/nginx/sites-available/default':
ensure	=> 'present',
content => $configure
}

exec { 'service nginx restart':
path	=> ['/usr/sbin', '/usr/bin']
}
