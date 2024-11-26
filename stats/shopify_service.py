
import requests
from django.conf import settings

# Shopify API Base URL
BASE_URL = f"https://{settings.SHOPIFY_API_KEY}:{settings.SHOPIFY_PASSWORD}@{settings.SHOPIFY_STORE_URL}"

def get_shopify_data():
    # Fetch orders
    orders_url = f"{BASE_URL}/admin/api/2023-04/orders.json"
    response = requests.get(orders_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching orders from Shopify: {response.status_code}")

def get_abandoned_checkouts():
    # Fetch abandoned checkouts
    abandoned_checkouts_url = f"{BASE_URL}/admin/api/2023-04/checkouts.json"
    response = requests.get(abandoned_checkouts_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching abandoned checkouts from Shopify: {response.status_code}")

def get_product_views():
    # Fetch product views (if available through Shopify Analytics API for Shopify Plus)
    product_views_url = f"{BASE_URL}/admin/api/2023-04/analytics/reports/product_views.json"
    response = requests.get(product_views_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching product views from Shopify: {response.status_code}")

def get_carts():
    # Fetch active carts (if accessible)
    carts_url = f"{BASE_URL}/admin/api/2023-04/carts.json"
    response = requests.get(carts_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching carts from Shopify: {response.status_code}")

from google.cloud import bigquery

def save_to_bigquery(data, table_id):
    client = bigquery.Client()
    dataset_id = settings.BIGQUERY_DATASET_ID
    table_ref = client.dataset(dataset_id).table(table_id)
    table = client.get_table(table_ref)

    errors = client.insert_rows_json(table, data)
    if errors:
        raise Exception(f"Error inserting data into BigQuery: {errors}")

def fetch_all_shopify_stats():
    # Fetch all relevant statistics from Shopify
    stats = {
        'orders': get_shopify_data(),
        'abandoned_checkouts': get_abandoned_checkouts(),
        'product_views': get_product_views(),
        'carts': get_carts(),
    }
    return stats
