Usage:

	# dispatch.wsgi
	from wsgitools import init_project
	application = init_project('/path/to/django_project')
	
	optional:
	application = init_project('/path/to/django_project', 
							   settings='path.to.settings')
