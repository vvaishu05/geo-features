import requests, os
import geopandas as gpd
from decouple import Config
from pathlib import Path

# Load environment variables
BASE_DIR = Path(__file__).resolve().parent
env_file_path = BASE_DIR.parent / '.env'
if os.path.exists(env_file_path):
	config = Config(str(env_file_path))
else:
	config = os.environ

# Load the dataset
gdf = gpd.read_file(
	config('GEOJSON_PATH', default=os.path.join(BASE_DIR.parent, 'municipalities_nl.geojson')))

# API endpoint for JWT token and features insertion
token_url = 'http://localhost:8000/api/token/'
post_url = 'http://localhost:8000/api/features/'

# Get JWT token for user
token_response = requests.post(
	token_url, json={"username": config('DB_USER'), "password": config('DB_PASSWORD')})
token = token_response.json()["access"]

# Iterate through GeoDataFrame and post each feature
for idx, row in gdf.iterrows():
	feature = {
		"name": row['name'],
		"geom": row['geometry'].__geo_interface__
	}
	response = requests.post(post_url, json=feature, headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"})
	if response.status_code == 201:
		print(f'Successfully posted feature {idx + 1}')
	else:
		print(f'Failed to post feature {idx + 1}: {response.content}')
