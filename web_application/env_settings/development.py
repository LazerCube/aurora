import os
from web_application.settings import *

DEBUG = True

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'web_application', 'fixtures'),
)


# Allow all host headers
ALLOWED_HOSTS = ['*']
