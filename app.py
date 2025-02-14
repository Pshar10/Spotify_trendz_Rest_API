import os
from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv  # Import dotenv to load environment variables

# Load the .env file
# load_dotenv()

# Spotify API wrapper, documentation here: http://spotipy.readthedocs.io/en/latest/
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Retrieve Spotify credentials from environment variables
# client_id = os.getenv("SPOTIPY_CLIENT_ID")
# client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
def load_spotify_credentials():
    with open('/app/secrets/SPOTIPY_CLIENT_ID', 'r') as file:
        client_id = file.read().strip()
    with open('/app/secrets/SPOTIPY_CLIENT_SECRET', 'r') as file:
        client_secret = file.read().strip()

    return client_id, client_secret

client_id, client_secret = load_spotify_credentials()


if not client_id or not client_secret:
    raise ValueError("Spotify credentials not found in environment variables")


# Authenticate with Spotify using the Client Credentials flow
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

app = Flask(__name__, static_folder='public', template_folder='views')

@app.route('/')
def homepage():
    # Displays homepage
    return render_template('index.html')

@app.route('/new_releases', methods=['GET'])
def new_releases():
    # Use the country from the query parameters, if provided
    if 'country' in request.args:
        country = request.args['country']
    else:
        country = 'SE'

    # Send request to the Spotify API
    new_releases = sp.new_releases(country=country, limit=20, offset=0)

    # Return the list of new releases
    return jsonify(new_releases)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True) 

