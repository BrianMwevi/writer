from .base import *
if DEBUG:
	from .local_settings import *
else:
	from .production import *