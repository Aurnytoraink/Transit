python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'transit.in',
  output: 'transit',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

transit_sources = [
  'main.py',
  'window.py',
]

install_data(transit_sources, install_dir: moduledir)
