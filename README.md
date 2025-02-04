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

