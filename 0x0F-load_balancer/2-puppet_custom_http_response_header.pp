# install and configure Nginx web server

package { 'nginx':
  ensure => installed,
}
file { '/etc/nginx/sites-available':
  ensure  => directory,
  recurse => true,
  purge   => true,
  force   => true,
}

file { '/etc/nginx/sites-enabled':
  ensure => directory,
}

file { '/var/www/html':
  ensure => directory,
}

file { '/var/www/bak':
  ensure => directory,
}

exec { 'backup_index_file':
  command     => 'mv /var/www/html/index.nginx-debian.html /var/www/bak/',
  onlyif      => '[ -f /var/www/html/index.nginx-debian.html ]',
  path        => '/usr/bin:/usr/sbin:/bin',
  refreshonly => true,
}

file {'/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

file {'/var/www/html/404.html':
  ensure  => present,
  content => 'Ceci n\'est pas une page',
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => @(EOF)
    server {
      listen 80 default_server;
      listen [::]:80 default_server;
      add_header X-Served-By $hostname;

      root /var/www/html;
      index index.html;

      location / {
        try_files $uri $uri/ =404;
      }

      location /redirect_me {
        return 301 'https://www.youtube.com/watch?v=axlUv9evU2k';
      }

      # Redirect error page
      error_page 404 /404.html;
      location = /404.html {
        internal;
        default_type text/html;
