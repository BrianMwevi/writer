from .base import *

try:
	if DEBUG:
		from .local_settings import *
	else:
		from .production import *

except:
	pass