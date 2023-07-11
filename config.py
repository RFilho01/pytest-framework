import logging

APP_URL = "http://localhost:8080"
ADMIN_USER = "admin"
ADMIN_PASSWORD = "admin"

LOG = logging.getLogger()

class HideSensitiveData(logging.Filter):
    
    def filter(self, record):
        record.msg = str(record.msg).replace(ADMIN_PASSWORD, "********")
        return True
    
LOG.addFilter(HideSensitiveData())