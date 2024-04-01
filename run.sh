#!/bin/bash
set -e

ENV_FILE=".env"
export $(cat $ENV_FILE | xargs)

DB_IMAGE_IMAGE="mariadb:11.3.2"
DB_CONTAINER_NAME="local_db"

PYTHON_IMAGE_NAME="sql-python-excel-prototype"
PYTHON_CONTAINER_NAME="python"
PYTHON_EXPORT_DIR="temp"

docker run --rm -d \
    --name $DB_CONTAINER_NAME \
    -e MYSQL_ROOT_PASSWORD=$DB_PASSWORD \
    -p $DB_PORT:3306 \
    -v $(pwd)/database/sample_dump.sql:/docker-entrypoint-initdb.d/dump.sql \
    $DB_IMAGE_IMAGE

# Need time for database to start before running the python script
sleep 4

rm -rf $PYTHON_EXPORT_DIR
docker build -t ${PYTHON_IMAGE_NAME} .
docker run --rm \
    --env-file .env \
    --name $PYTHON_CONTAINER_NAME \
    --network host \
    -v $(pwd)/$PYTHON_EXPORT_DIR:/$PYTHON_EXPORT_DIR \
    $PYTHON_IMAGE_NAME

docker stop $DB_CONTAINER_NAME
