# Python Oracle Autonomous Data Warehouse Template

This project is a flask api built with Python, Flask and Oracle Autonomous Data Warehouse to be used as a starter template.

## Built With

* [Python 3](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Docker](https://www.docker.com/)
* [Oracle Autonomous Data Warehouse](https://cloud.oracle.com/en_US/datawarehouse)

## Prerequisites

You will need the following things properly installed on your computer:

* [Git](http://git-scm.com/)
* [Docker](https://www.docker.com/)
* [Oracle Autonomous Data Warehouse Instance](https://cloud.oracle.com/en_US/datawarehouse)

## Installation

* run `git clone https://github.com/caseyr003/python-oracleadw.git`

## Setup

Getting the Autonomous Data Warehouse Wallet files
* Navigate to your ADW instance on the Oracle Cloud Infrastructure Console
* Click 'DB Connection'
* Download the Client Credentials (Wallet)
* Unzip the files and place them in the `wallet` folder in this project

Updating Python API
* Update `app.py` with the ADW credentials
* Update the `api/test` endpoint to pull relevant data using SQL

## Running

To run the project locally follow the following steps:

* change into the project directory
* `docker build -t python/oracleadw .`
* `docker run -p 5000:5000 python/oracleadw`
or for development
* `docker run -p 5000:5000 -v [LOCAL_PROJECT_PATH]:/app python/oracleadw`

## JSON API

The JSON API has sample endpoints to start development
Must configure `app.py` to connect to your Oracle DB and update the SQL query

* `http://localhost:5000/api/version`
(returns current database version)

* `http://localhost:5000/api/test`
(returns data from Oracle DB connection)
