<div class='tableauPlaceholder' id='viz1693245697996' style='position: relative'><noscript><a href='https:&#47;&#47;github.com&#47;arun98aol&#47;spotify-streaming-trends&#47;tree&#47;main'><img alt='D0 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;IF&#47;IFP_1&#47;D0&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='IFP_1&#47;D0' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;IF&#47;IFP_1&#47;D0&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1693245697996');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>

# Spotify Streaming Trends

**Name:** Arun Ganapathy   
**Date:** 9th December 2022  

## Introduction

This project aims to visualize the performance of various music artists in different genres from 2010 to 2019 and hence the trends of users too! The detailed datasets were obtained from a Kaggle-based analytics project and the Python-based 'billboard' library. The goal is to analyze the relationship between different music metrics and artist popularity, as well as to explore trends in genres and their popularity over the specified time frame.

<img src="https://github.com/arun98aol/spotify-streaming-trends/blob/main/mainpage.png" alt="Alt text" title="Optional title">


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
