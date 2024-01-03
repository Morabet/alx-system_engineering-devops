$configure = "server {

        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
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
