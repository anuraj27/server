from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from django.urls import reverse

# Initialize the OAuth flow
def get_oauth_flow():
    # Pass the corrected configuration from settings
    flow = Flow.from_client_config(
        settings.OAUTH_CONFIG,  # Use the corrected structure here
        scopes=settings.SCOPES,
        redirect_uri=settings.REDIRECT_URI
    )
    return flow

# Route to initiate login
def login(request):
    """Start OAuth 2.0 flow."""
    flow = get_oauth_flow()
    authorization_url, state = flow.authorization_url(
        access_type='offline',  # Get a refresh token
        include_granted_scopes='true'
    )
    # Store state for CSRF protection
    request.session['state'] = state
    return redirect(authorization_url)

# Callback route for Google OAuth
def callback(request):
    """Handle callback from Google's OAuth server."""
    try:
        # Verify the state to protect against CSRF
        if request.session.get('state') != request.GET.get('state'):
            return HttpResponse("Error: State mismatch", status=400)

        # Fetch the access token
        flow = get_oauth_flow()
        flow.fetch_token(authorization_response=request.build_absolute_uri())
        credentials = flow.credentials

        # Store credentials in session (or save them to your DB)
        request.session['credentials'] = {
            'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes,
        }

        return redirect(reverse('dashboard'))
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}", status=500)

# Protected route for logged-in users
def dashboard(request):
    """Display user dashboard."""
    credentials_data = request.session.get('credentials')
    if not credentials_data:
        return redirect(reverse('login'))

    credentials = Credentials(**credentials_data)

    # Example: Display access token
    return HttpResponse(f"Access token: {credentials.token}")

# Logout route
def logout(request):
    """Logout user by clearing session."""
    request.session.clear()
    return redirect(reverse('login'))
