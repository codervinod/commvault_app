__author__ = "Vinod.Gupta@nutanix.com"

PROTO = 'http://'
BASE_PORT = 81
LOGIN_PATH = 0

COMMVAULT_PATHS = (
    '/SearchSvc/CVWebService.svc/Login',
)

LOGIN_BODY = '<DM2ContentIndexing_CheckCredentialReq mode="Webconsole" username="<<username>>" password="<<password>>" />' # noqa
