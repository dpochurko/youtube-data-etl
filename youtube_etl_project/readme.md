# YouTube Trending Videos ETL Pipeline

This project fetches trending YouTube video data using the YouTube Data API v3, processes the data with Pandas, and stores it in a PostgreSQL database. It is optionally automated using Apache Airflow or a cron job.

## Features
- Extract trending YouTube videos
- Transform & clean data (filter zero views, validate structure)
- Load data into PostgreSQL
- Automated daily with Airflow or cron
- Written entirely in Python

## Tech Stack
- Python
- PostgreSQL
- YouTube API
- Pandas
- SQLAlchemy
- Airflow (optional)

## To Run
1. Clone the repo
2. Set up a `.env` with your YouTube API key and DB credentials
3. Run `youtube_etl.py`