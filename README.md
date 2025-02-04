# stageOne_hng_numberclassification

# Number Classification API

This API classifies numbers and provides interesting mathematical properties along with a fun fact.

## Table of Contents

- [Introduction](#introduction)
- [API Specification](#api-specification)
    - [Endpoint](#endpoint)
    - [Request](#request)
    - [Response](#response)
- [Error Handling](#error-handling)
- [Code Quality](#code-quality)
- [Deployment](#deployment)
- [Technologies Used](#technologies-used)
- [Local Development](#local-development)
- [Testing](#testing)
- [Examples](#examples)

## Introduction

This API takes an integer as input and returns its mathematical properties, including whether it's prime, perfect, Armstrong, and odd/even, the sum of its digits, and a fun fact about the number (obtained from the Numbers API).

## API Specification

### Endpoint

`GET /api/classify-number`

### Request

**Parameters:**

- `number` (required): An integer.

**Example Request:**

GET /api/classify-number?number=371

### Response

The API returns a JSON response with the following format:

**200 OK (Success):**




```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": [
    "armstrong",
    "odd"
  ],
  "digit_sum": 11,
  "fun_fact": "371 is a narcissistic number."
}

400 Bad Request (Error):

{
  "number": "",
  "error": true
}






Deployment
The API is deployed on Railway. "https://temitopejosephstageonehng.up.railway.app/api/classify-number?number="

Technologies Used
Python
Django REST Framework
requests (for making external API calls)
requests-cache (for caching external API responses - install with pip install requests-cache)



Local Development
Clone the repository:

Bash

git clone <repository_url>
Create a virtual environment (recommended):

Bash

python3 -m venv venv  # Or virtualenv venv
source venv/bin/activate  # Or venv\Scripts\activate on Windows
Install the dependencies:

Bash

pip install -r requirements.txt  # Create this file with your dependencies
Run the development server:

Bash

python manage.py runserver





    Examples
Valid Request:

Bash

curl "[https://temitopejosephstageonehng.up.railway.app/api/classify-number?number=28](https://temitopejosephstageonehng.up.railway.app/api/classify-number?number=28)"
Response:

JSON

{
  "number": 28,
  "is_prime": false,
  "is_perfect": true,
  "properties": [
    "even"
  ],
  "digit_sum": 10,
  "fun_fact": "28 is the third Granville number."
}


Invalid Request (Missing number):

Bash

curl "[https://temitopejosephstageonehng.up.railway.app/api/classify-number](https://www.google.com/search?q=https://temitopejosephstageonehng.up.railway.app/api/classify-number)"  # No number parameter
Response:

JSON

{
  "error": true,
  "number": ""
}


Invalid Request (Non-numeric number):

Bash

curl "[https://temitopejosephstageonehng.up.railway.app/api/classify-number?number=abc](https://temitopejosephstageonehng.up.railway.app/api/classify-number?number=abc)"
Response:

JSON

{
  "error": true,
  "number": "abc"
}

 
 



