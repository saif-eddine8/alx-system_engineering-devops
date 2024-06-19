file { '/var/www/html/index.html':
  ensure  => 'file',
  content => '<html><body><h1>Holberton</h1></body></html>',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

service { 'apache2':
  ensure => 'running',
  enable => true,
  require => File['/var/www/html/index.html'],
}

