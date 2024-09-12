from fasthtml.common import *
from fasthtml.oauth import GoogleAppClient
import requests

from app.application import rt


google_client = GoogleAppClient(
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
)
google_login_link = google_client.login_link(redirect_uri=os.getenv('DOMAIN', 'http://127.0.0.1:5001') + '/login/google/callback')


@rt('/login/google/callback')
async def get(code: str, session):
    token_url = "https://accounts.google.com/o/oauth2/token"
    data = {
        "code": code,
        "client_id": google_client.client_id,
        "client_secret": google_client.client_secret,
        "redirect_uri": google_client.redirect_url,
        "grant_type": "authorization_code",
    }
    response = requests.post(token_url, data=data)
    access_token = response.json().get("access_token")
    user_info = requests.get("https://www.googleapis.com/oauth2/v1/userinfo", headers={"Authorization": f"Bearer {access_token}"})
    email = user_info.json().get("email")
    session['email'] = email

    return RedirectResponse('/')


@rt('/login')
def get():
    return Main(
        Div(
            Div(
                H1(f"Login to {os.getenv('APP_NAME', 'MyApp')}", cls="text-2xl font-bold mb-6"),
                A(
                    Span(cls="icon-[devicon--google] mr-2"),
                    "Login with Google",
                    href=google_login_link,
                    cls="bg-gray-200 hover:bg-gray-300 text-gray-800 font-bold py-2 px-4 rounded flex items-center justify-center border border-gray-300 w-full max-w-[30rem]"
                ),
                cls="bg-white shadow-lg px-8 py-10 w-full sm:w-1/2 min-w-[10rem] h-full flex flex-col justify-center"
            ),
            cls="flex items-center justify-end h-screen"
        ),
        cls="bg-gray-100 h-screen"
    )
