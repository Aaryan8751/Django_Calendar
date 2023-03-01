from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
# Create your views here.

SCOPES = ['https://www.googleapis.com/auth/calendar',
'https://www.googleapis.com/auth/calendar.readonly',
'https://www.googleapis.com/auth/userinfo.email',
'https://www.googleapis.com/auth/userinfo.profile',
'openid']

CLIENT_SECRETS_FILE = "creds.json"
REDIRECT_URI = "http://127.0.0.1:8000/rest/v1/calendar/redirect/"

API_SERVICE_NAME = 'calendar'
API_VERSION = 'v3'

@api_view(['GET'])
def GoogleCalendarInitView(request):
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES)
    flow.redirect_uri = REDIRECT_URI
    authorization_url, state = flow.authorization_url(
      # Enable offline access so that you can refresh an access token without
      # re-prompting the user for permission. Recommended for web server apps.
      access_type='offline',
      # Enable incremental authorization. Recommended as a best practice.
      include_granted_scopes='true')

  # Store the state so the callback can verify the auth server response.
    request.session['state'] = state
    return Response({"authorization_url": authorization_url})



