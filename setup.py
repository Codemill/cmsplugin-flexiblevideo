from setuptools import setup, find_packages

version = __import__('cmsplugin_flexiblevideo').__version__

setup(
    name = 'cmsplugin-flexiblevideo',
    version = version,
    description = 'Plugin for Django CMS that displays a video with flexible width.',
    author = 'Ludvig Widman, CodeMill AB',
    author_email = 'opensource@codemill.se',
    url = 'http://github.com/codemill/cmsplugin-flexiblevideo',
    packages = find_packages(),
    include_package_data=True,
    install_requires = [
        'django-cms>=2.1',
    ],
)
