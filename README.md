# Spotify Streaming Trends

**Name:** Arun Ganapathy   
**Date:** 9th December 2022  

## Introduction

This project aims to visualize the performance of various music artists in different genres from 2010 to 2019 and hence the trends of users too! The detailed datasets were obtained from a Kaggle-based analytics project and the Python-based 'billboard' library. The goal is to analyze the relationship between different music metrics and artist popularity, as well as to explore trends in genres and their popularity over the specified time frame.

<img src="https://github.com/arun98aol/spotify-streaming-trends/assets/49324102/0de6e0c8-081a-421e-a28f-37aec13cb833" alt="Project Image">



## Data Collection and Cleaning

Data was collected using the 'billboard' library in Python to obtain information on yearly track releases and genre classification. The data was then cleaned and processed in Jupyter Notebooks. Columns such as track_name were filtered to include only songs released in English between 2010 and 2019. Spotify data was also collected from a Kaggle data analysis project. Data inconsistencies, such as varied genre spellings, were addressed to ensure accurate analysis.

## Dataset Description

The dataset includes metrics such as artist_name, track_name, track_id, year, popularity, acousticness, danceability, duration_ms, energy, instrumentalness, key, liveness, loudness, mode, speechiness, tempo, time_signature, and valence. Each metric is defined to aid understanding.

## Project Approach/Flow

1. Data Cleaning and Validation: Data collected from multiple sources and libraries were cleaned and validated using Python.
2. Data Wrangling and Manipulation: Data massaging was performed to focus on English songs between 2010 and 2019.
3. Data Visualization: Tableau was used to create visualizations for different metrics, genres, and trends.
4. Implementation and Results: Various analyses were conducted using Tableau visualizations, and key insights were drawn.

## Results and Insights

- Metrics Correlation: Danceability, tempo, and energy showed weak correlations with popularity.
- Genre Analysis: Pop, dance, and hip-hop were the most popular genres, while others showed less popularity.
- Country Comparison: Genre popularity varied between the US and Canada, with hip-hop being more popular in the US.
- Challenges: Data collection, cleaning inconsistencies, and lack of certain data points were challenges faced during the project.

## Conclusion

The project successfully visualized music artist performance and genre popularity using a combination of data sources and visualization tools. Insights were drawn regarding metrics that influence popularity and genre trends over the specified period. Future work could involve more comprehensive streaming data analysis and international genre comparisons.

## References

- [GitHub Repository](https://github.com/arun98aol/spotify-streaming-trends)
- [Spotify Dataset](https://www.kaggle.com/datasets/leonardopena/top-spotify-songs-from-20102019-by-year)
- [Billboard Library](https://github.com/guoguo12/billboard-charts)
