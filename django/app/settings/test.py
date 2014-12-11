# -*- coding: utf-8 -*-
from base import *
import djcelery
djcelery.setup_loader()


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'test_2.db'),
    }
}

CELERY_ALWAYS_EAGER = True
# BROKER_URL = 'redis://localhost:6379/0'