import math


def fetch_paginated_result(query, page): 
    """
    Function which will fetch paginated results from DB
    """
    from app import db

    limit = 10
    offset = (limit*page) - limit
    mod_query = query + f" limit {limit} offset {offset}"
    data_count = db.engine.execute(f"select count(id) from orders").mappings().all()[0]['count']
    page_count = math.ceil(data_count/limit)
    results = []
    for r in db.engine.execute(mod_query):
        log_as_dict = dict(r)
        log_as_dict['created'] = str(log_as_dict['created'])
        results.append(log_as_dict)
    return {"data": results, "total_pages": page_count}