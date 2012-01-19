from django.core.handlers.wsgi import WSGIHandler
import os
import sys


def init_project(project_directory, *args, **kwargs):
    project_directory = os.path.abspath(project_directory)
    project_module = os.path.basename(project_directory)

    # Add the project's parent directory to the path
    parent = os.path.join(project_directory, '..')
    if parent not in sys.path:
        sys.path.append(parent)

    # Specify the settings module
    os.environ['DJANGO_SETTINGS_MODULE'] = '%s.settings' % project_module

    # Run the monitor
    from django.conf import settings
    if settings.DEBUG:
        from . import monitor
        monitor.start()

    return WSGIHandler(*args, **kwargs)
