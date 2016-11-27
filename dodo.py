PACKAGE = '_PACKAGE_NAME_'

def task_prepenv():
    """Prepare environment for other commands."""
    return {
        'actions': ['ppp .'],
        'file_dep': [],
        'task_dep': [],
        'targets': [],
        'clean': ['rm -fr __pycache__ {}/__pycache__ .doit.db .cache'.format(PACKAGE)],
        'verbosity': 2,
        }

def task_docs_build():
    """Builds documentation."""
    return {
        'actions': ['cd docs && make html'],
        'file_dep': [],
        'task_dep': ['prepenv'],
        'targets': [],
        'clean': ['rm -fr docs/build'],
        'verbosity': 2,
        }

