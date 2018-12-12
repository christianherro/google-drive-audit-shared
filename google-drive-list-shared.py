#!/usr/bin/env python

from __future__ import print_function
import time
import ast

from pprint import pprint 

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

class DictQuery(dict):
  def get(self, path, default = None):
    keys = path.split("/")
    val = None

    for key in keys:
      if val:
        if isinstance(val, list):
          val = [ v.get(key, default) if v else None for v in val]
        else:
          val = val.get(key, default)
      else:
        val = dict.get(self, key, default)

      if not val:
          break;

      return val

SCOPES = 'https://www.googleapis.com/auth/drive.readonly.metadata'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
  flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
  creds = tools.run_flow(flow, store)

service = discovery.build('drive', 'v3', http=creds.authorize(Http()))
results = service.files().list(
    pageSize=1000,
    fields="nextPageToken, files(name, permissions/emailAddress, owners/emailAddress)").execute()
token = results.get('nextPageToken', None)
items = results.get('files', [])

while token is not None:
  results = service.files().list(
      pageSize=1000,
      pageToken=token,
      fields="nextPageToken, files(name, permissions/emailAddress, owners/emailAddress)").execute()
  # Store the new nextPageToken on each loop iteration
  token = results.get('nextPageToken', None)
  # Append the next set of results to the items variable
  items.extend(results.get('files', []))

# The Google Drive does not return valid JSON because the property
# names are not enclosed in double quotes, they are enclosed in
# single quotes. So, use Python AST to convert the string to an
# iterable list.
items_dict = ast.literal_eval(str(items))

# Iterate through and pretty print as JSON all the selected fields 
# (name, owner email, and email addresses that files have been shared with).
for i in range(len(items_dict)):
  pprint(items_dict[i])
