# configure nginx to receive large mounts of REQUESTS

exec { 'sed':
    command => 'sed -i "s/15/4096/" /etc/default/nginx',
    path    => 'usr/local/bin/:/bin/'
}

exec { 'restart':
    command => 'nginx restart',
    path    => '/etc/init.d'
}
