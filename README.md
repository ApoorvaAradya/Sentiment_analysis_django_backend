# Sentiment Analysis API

A simple backend service that performs sentiment analysis on text using Django, Django REST framework, and VADER sentiment analysis library.

## Requirements

- Python 3.x
- Django
- Django REST framework
- vaderSentiment

## Installation

1. **Clone the repository:**
   git clone <repository-url>
   cd sentiment_analysis

##Usage
Send a POST request to http://127.0.0.1:8000/analysis/analyze/ with JSON payload.
Positive Sentiment Example:
curl -X POST http://127.0.0.1:8000/analysis/analyze/ -H "Content-Type: application/json" -d '{"text": "I love this product!"}'

Negative Sentiment Example:
curl -X POST http://127.0.0.1:8000/analysis/analyze/ -H "Content-Type: application/json" -d '{"text": "I am very disappointed with the service."}'


