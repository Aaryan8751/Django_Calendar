# Django_Calendar

Problem: In this assignment you have to implement google calendar
integration using django rest api. You need to use the OAuth2 mechanism to
get users calendar access. Below are detail of API endpoint and
corresponding views which you need to implement
/rest/v1/calendar/init/ -> GoogleCalendarInitView()
This view should start step 1 of the OAuth. Which will prompt user for
his/her credentials
/rest/v1/calendar/redirect/ -> GoogleCalendarRedirectView()
This view will do two things
1. Handle redirect request sent by google with code for token. You
need to implement mechanism to get access_token from given
code
2. Once got the access_token get list of events in users calendar


### References

https://developers.google.com/calendar/caldav/v2/auth

https://www.djangoproject.com/

https://docs.djangoproject.com/en/4.1/ref/request-response/

https://developers.google.com/identity/protocols/oauth2/web-server

https://developers.google.com/calendar/api/v3/reference

https://developers.google.com/calendar/api/v3/reference/events/list

https://stackoverflow.com/questions/57589526/what-and-how-to-pass-credential-using-using-python-client-library-for-gcp-comput
