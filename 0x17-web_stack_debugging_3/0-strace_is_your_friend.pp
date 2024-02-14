# fix the apache2 server

$file_path='/var/www/html/wp-settings.php'
$old_value='class-wp-locale.phpp'
$new_value='class-wp-locale.php'

# reading the file contents
$content=file($file_path)

# update the file content using this ruby code
# $updated_content=inline_template("<%= @content.gsub(/#{@old_value}/, '#{@new_value}') %>")
$updated_content=regsubst($content , $old_value, $new_value, 'G')


file{ 'update_settings':
ensure  => present,
path    => $file_path,
content => $updated_content
}

# notify to restart Apache
service{ 'apache2':
ensure    => running,
subscribe => File[ 'update_settings' ]
}
