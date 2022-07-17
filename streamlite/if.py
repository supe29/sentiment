from __future__ import print_function

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET _FILE = 'client_secret GoogleCloudDemo, json'
API_NAME = "drive"
API VERSION = 'V3'
SCOPES= ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
def export_esv_file(file_path: str, parents: list-None):
if not os.path.exists(file_path):
print(f' (file _path} not found.")
return
try:
file_metadata = (
"name": os.path.basename(file_path).replace(*.csv',
••),
'mimeType": *application/vnd.google-apps.spreadsheet'
*parents": parents
}
media = MediaFileUpload(filename-file_path, mimetype='text/csv®)
response = service.files().create(
media body-media,
body=file metadata
).execute()
print (response)
except Exception as e:
print(e)
return