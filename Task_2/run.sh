#!/usr/bin/env bash
set -e

docker-compose build
docker-compose up -d db redis_cache
sleep 2
docker-compose run order_app populate_db.py
docker-compose up -d order_app
