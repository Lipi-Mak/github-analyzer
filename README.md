# GitHub Profile Analyzer

A web-based GitHub Profile Analyzer built using **Python**, **Flask**, and the **GitHub REST API**. This application analyzes a GitHub user's public repositories and generates a profile score along with meaningful insights and personalized recommendations.

## Features

* Analyze any public GitHub profile
* Calculate an overall GitHub profile score
* Display:

  * Total public repositories
  * Programming languages used
  * Total stars received
  * Total forks
  * Recently updated repositories
* Generate profile insights
* Provide personalized recommendations for improving a GitHub profile
* Simple and responsive user interface built with HTML and CSS

## Technologies Used

* Python
* Flask
* GitHub REST API
* HTML
* CSS

## Project Structure

```
github-analyzer/
│
├── app.py
├── analyzer.py
├── github_api.py
├── scoring.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## Installation

1. Clone the repository.

```
git clone https://github.com/Lipi-Mak/github-analyzer.git
```

2. Navigate into the project folder.

```
cd github-analyzer
```

3. Install the required dependencies.

```
pip install -r requirements.txt
```

4. Run the application.

```
python app.py
```

## Live Demo

https://your-app.onrender.com

## How It Works

The application fetches a user's public repositories using the GitHub REST API. It then analyzes various profile metrics, including repository count, programming language diversity, repository popularity (stars and forks), repository descriptions, and recent activity. Based on these metrics, the application computes a GitHub profile score and generates insights along with recommendations.

## Learning Outcomes

This project helped strengthen my understanding of:

* Flask web development
* REST API integration
* Modular Python programming
* HTML and CSS
* Code organization
* Software project structure
* GitHub workflows
