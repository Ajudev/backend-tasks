import math
import json
from datetime import timedelta


def fetch_results(query, page):
    from app import redis_client
    
    data = redis_client.get(f'order_page_{page}')
    if data is None:
        data = fetch_paginated_result(query, page)
        redis_client.set(f'order_page_{page}', json.dumps(data))
        redis_client.expire(f'order_page_{page}', timedelta(hours=1))
    else:
        data = json.loads(data)
    return data


def fetch_paginated_result(query, page): 
    """
    Function which will fetch paginated results from DB
    """
    from app import db

    limit = 10
    offset = (limit*page) - limit
    mod_query = query + f" limit {limit} offset {offset}"
    data_count = db.engine.execute(f"select count(id) from orders").mappings().all()[0]['count(id)']
    page_count = math.ceil(data_count/limit)
    results = []
    for r in db.engine.execute(mod_query):
        log_as_dict = dict(r)
        log_as_dict['created'] = str(log_as_dict['created'])
        results.append(log_as_dict)
    return {"data": results, "total_pages": page_count}