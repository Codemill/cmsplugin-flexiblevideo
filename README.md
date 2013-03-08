# Flexible Video
Flexible Video is a plugin for Django CMS that let's you include a vimeo
or youtube video that adapts it's width to the available space. It also
features a cover image that starts the video when clicked.

## Requirements
django-cms >= 2.1

## Installation
Flexible Video can be installed with pip:

	pip install cmsplugin-flexiblevideo

## Usage
- Add cmsplugin\_flexiblevideo to INSTALLED\_APPS in your settings.py file:

		INSTALLED_APPS = (
			...
			'cmsplugin\_flexiblevideo',
			...
		)

- Run ./manage.py syncdb to add tables

- Use the plugin like any other CMS plugin

