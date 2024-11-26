
from celery import shared_task
from .shopify_service import fetch_all_shopify_stats, save_to_bigquery

@shared_task
def fetch_and_save_all_shopify_stats():
    stats = fetch_all_shopify_stats()

    # Save each stat type to its respective BigQuery table
    save_to_bigquery(stats['orders'], 'orders_table')
    save_to_bigquery(stats['abandoned_checkouts'], 'abandoned_checkouts_table')
    save_to_bigquery(stats['product_views'], 'product_views_table')
    save_to_bigquery(stats['carts'], 'carts_table')
