


import os
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status





NUMBER_KEY = "number"
IS_PRIME_KEY = "is_prime"
IS_PERFECT_KEY = "is_perfect"
PROPERTIES_KEY = "properties"
DIGIT_SUM_KEY = "digit_sum"
FUN_FACT_KEY = "fun_fact"


NUMBERS_API_BASE_URL = os.environ.get("NUMBERS_API_BASE_URL", "http://numbersapi.com")

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def is_armstrong(n: int) -> bool:
    if n < 0:
        return False  

    original_n = n  
    n = abs(n) 
    num_digits = len(str(n))
    armstrong_sum = 0  
    temp_n = n

    while temp_n > 0:
        digit = temp_n % 10
        armstrong_sum += digit ** num_digits
        temp_n //= 10

    return armstrong_sum == original_n 

def digit_sum(n: int) -> int:
    return sum(int(d) for d in str(abs(n)))

def get_fun_fact(n: int) -> str:
    try:
        url = f"{NUMBERS_API_BASE_URL}/{n}/math"  
        response = requests.get(url)
        response.raise_for_status() 
        fun_fact = response.text.strip() 
        return fun_fact  

    except requests.exceptions.RequestException as e:
        print(f"Error calling Numbers API: {e}")  
        return ""  
    except Exception as e:
        print(f"Unexpected error getting fun fact: {e}")
        return ""


@api_view(['GET'])
def classify_number(request):
    number = request.GET.get('number', None)

    if number is None:
        return Response({NUMBER_KEY: None, "error": True }, status=status.HTTP_400_BAD_REQUEST)

    try:
        number = int(number) 
        
    except ValueError:
        return Response({NUMBER_KEY: number, "error": True }, status=status.HTTP_400_BAD_REQUEST)

    is_prime_num = is_prime(number)
    is_perfect_num = is_perfect(number)
    is_armstrong_num = is_armstrong(number)
    is_odd = number % 2 != 0

    properties = []
    if is_armstrong_num:
        properties.append("armstrong")
    if is_odd:
        properties.append("odd")
    else:
        properties.append("even")

    response = {
        NUMBER_KEY: number,
        IS_PRIME_KEY: is_prime_num,
        IS_PERFECT_KEY: is_perfect_num,
        PROPERTIES_KEY: properties,
        DIGIT_SUM_KEY: digit_sum(number),
        FUN_FACT_KEY: get_fun_fact(number),
    }
    return Response(response, status=status.HTTP_200_OK)