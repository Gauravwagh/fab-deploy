DEBUG = True
TEMPLATE_DEBUG = DEBUG
# Make this unique, and don't share it with anybody.
SECRET_KEY = "a+-7nwmcbue*2l+5j4r6r4$c4d3bo0kn3ddapr7x)wt$c1%uv8"
NEVERCACHE_KEY = "892b72cc-53b7-418f-987b-97246cb946a7b7ab61d8-940b-4b90-b0e9-eebe99b3e27007f39f4d-7dd3-4230-a923-798d5cf228eb"




# DATABASES = {
#     "default": {
#         "ENGINE": "tenant_schemas.postgresql_backend",
#         "NAME": "ckiller",
#         "USER": "dbuser",
#         "PASSWORD": "consultadd",
#         "HOST": "localhost",
#         "PORT": "",
#
#     }
# }


import os
# Full filesystem path to the project.
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__ + "/../"))


# """
# dev
# """


FABRIC = {
    "SSH_USER": "root", # SSH username
    "SSH_PASS":  "Taulabs@2016", # SSH password (consider key-based authentication)
#    "SSH_KEY_PATH":  "", # Local path to SSH key file, for key-based auth
    "HOSTS": ['128.199.112.178'], # List of hosts to deploy to
    "DOMAINS": ['ck.taulabs.co'], # Domains for public site
    "VIRTUALENV_HOME":  "/var/www", # Absolute remote path for virtualenvs
    "PROJECT_NAME": "ckiller_api", # Unique identifier for project
    "REQUIREMENTS_PATH": "requirements.txt", # Path to pip requirements, relative to project
    "GUNICORN_PORT": 8001, # Port gunicorn will listen on
    "LOCALE": "en_US.UTF-8", # Should end with ".UTF-8"
    "REPO_URL": "https://gitlab.com/consultadd_inc/ckiller.git", # Git or Mercurial remote repo URL for the project
    "DB_PASS": "ckiller", # Live database password
    "ADMIN_PASS": "ckiller505", # Live admin user password
    "SECRET_KEY": SECRET_KEY,
    "NEVERCACHE_KEY": NEVERCACHE_KEY,
    "APP_REPO_URL" : ""

}





