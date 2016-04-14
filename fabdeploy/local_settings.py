DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Make this unique, and don't share it with anybody.
SECRET_KEY = '^*4supq(6-4z53-cwy%czely13k_)t9(43g9ba^*qqstf9z&n8'
NEVERCACHE_KEY = "892b72cc-53b7-418f-987b-97246csddb946a7b7addsadasvvxb61d8-940b-4b90-b0e9-eebefdds99b3e27007f39f4d-7dd3-4230-a923-798d5cf228eb"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT_DIR, 'db.sqlite3'),
    }
}

import os
# Full filesystem path to the project.
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__ + "/../"))


# """
# dev
# """


FABRIC = {
    "SSH_USER": "user", # SSH username
    "SSH_PASS":  "******", # SSH password (consider key-based authentication)
#    "SSH_KEY_PATH":  "", # Local path to SSH key file, for key-based auth
    "HOSTS": ['122.265.852.25'], # List of hosts to deploy to
    "DOMAINS": ['xyz.com'], # Domains for public site
    "VIRTUALENV_HOME":  "/var/www", # Absolute remote path for virtualenvs
    "PROJECT_NAME": "fabdeploy", # Unique identifier for project
    "REQUIREMENTS_PATH": "requirements.txt", # Path to pip requirements, relative to project
    "GUNICORN_PORT": 8001, # Port gunicorn will listen on
    "LOCALE": "en_US.UTF-8", # Should end with ".UTF-8"
    "REPO_URL": "https://github.com/Gauravwagh/fab-deploy.git", # Git or Mercurial remote repo URL for the project
    "DB_PASS": "dbpassword", # Live database password
    "ADMIN_PASS": "adminpassword", # Live admin user password
    "SECRET_KEY": SECRET_KEY,
    "NEVERCACHE_KEY": NEVERCACHE_KEY,
    "APP_REPO_URL" : ""

}





