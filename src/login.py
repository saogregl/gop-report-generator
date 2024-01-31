import requests
import os
from dotenv import load_dotenv

def login(): 
    """
    Login to the GOP website and returns the session object.

    Returns:
        requests.Session: The session object.
    """
    load_dotenv()
    s = requests.Session()
    url = "https://gop.jacto.srv.br/login"
    username = os.getenv("GOP_USER")
    password = os.getenv("GOP_PASSWORD")
    s.auth = (username, password)

    #Read the credentials from the .env file
    #credential
    data = {"usuario.login": username, "usuario.senha": password}
    resp = s.post(url, data)

    return s