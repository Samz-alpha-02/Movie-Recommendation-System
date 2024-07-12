# Movie Recommendation System

## Overview

This project is a movie recommendation system built using Python, Flask, and Select2 for an enhanced user interface. It recommends movies based on cosine similarity, allowing users to select or type a movie name and receive a list of similar movies along with their posters.

## Features

* Recommends movies based on cosine similarity.
* Allows users to select a movie from a dropdown list.
* Displays movie posters and titles.
* User-friendly interface with a search-enabled dropdown (Select2).

## Prerequisites

* Python 3.x
* Flask
* Pandas
* Scikit-learn
* Requests

## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
```

2. Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install the required packages:

```
pip install -r requirements.txt
```

## Usage

### Local Machine

1. Run the Flask app:

```
python app.py
```

2. Open your web browser and go to:

```
http://127.0.0.1:8000/
```

### Cloud Deployment Link

```
https://movie-recommendation-system-573d.onrender.com/
```

# Project Details

* `app.py`

The main Flask application file. It contains routes to handle the home page and movie recommendations. It also includes functions to load the necessary data and calculate recommendations.

* `templates/index.html`

The HTML template file for the home page. It includes the structure and styling for the user interface, incorporating Select2 for the enhanced dropdown menu.

* `static/background.jpg`

A background image used in the web page for a better visual appeal.

* `model/movie_dict.pkl`

A pickle file containing the movie data used for recommendations.

* `model/similarity.pkl`

A pickle file containing the precomputed cosine similarity matrix.

# Functions and Their Purpose

* `fetch_poster(movie_id)`

Fetches the movie poster using The Movie Database (TMDb) API.

* `download_file_from_github_release(url, file_name)`

Downloads a file from a GitHub release URL.

* `recommend(movie)`

Calculates movie recommendations based on cosine similarity.

# Flask Routes

* `/`

Renders the home page with the movie dropdown list.

* `/recommend`

Accepts a POST request with the selected movie and returns a list of recommended movies in JSON format.

# How to Use the Application

* Select or type a movie name in the dropdown box.
* Click the "Show Recommendation" button.
* The recommended movies along with their posters will be displayed on the page.

# Deployment

The application is deployed on a Cloud Platform `Render`.

You can access the application using the given Deployment Link: [Movie Recommendation System](https://movie-recommendation-system-573d.onrender.com/)

# Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push to your branch and create a pull request.

# License

This project is licensed under the MIT License.