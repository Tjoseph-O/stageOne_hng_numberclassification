import os
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from collections import OrderedDict
import requests_cache

NUMBER_KEY = "number"
IS_PRIME_KEY = "is_prime"
IS_PERFECT_KEY = "is_perfect"
PROPERTIES_KEY = "properties"
DIGIT_SUM_KEY = "digit_sum"
FUN_FACT_KEY = "fun_fact"

NUMBERS_API_BASE_URL = os.environ.get("NUMBERS_API_BASE_URL", "http://numbersapi.com")

session = requests_cache.CachedSession('numbers_api_cache')

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

    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i * i != n:
                divisors_sum += n // i
    return divisors_sum == n

def is_armstrong(n: int) -> bool:
    if n == 0:
        return True

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
        response = session.get(url, timeout=5)
        response.raise_for_status()
        return response.text.strip()

    except requests.exceptions.RequestException as e:
        print(f"Error calling Numbers API: {e}")
        return f"Error: {e}"


@api_view(['GET'])
def classify_number(request):
    number_str = request.GET.get(NUMBER_KEY, None)

    if number_str is None:
        return Response(OrderedDict([("error", True), (NUMBER_KEY, None)]), status=status.HTTP_400_BAD_REQUEST)

    try:
        number = int(number_str)
    except ValueError:
        return Response(OrderedDict([("error", True), (NUMBER_KEY, number_str)]), status=status.HTTP_400_BAD_REQUEST)

    is_prime_num = is_prime(number)
    is_perfect_num = is_perfect(number)
    is_armstrong_num = is_armstrong(number)
    is_odd = number % 2 != 0

    properties = []
    if is_armstrong_num:
        properties.append("armstrong")

    if number % 2 != 0:
        properties.append("odd")

    if number % 2 == 0:
        properties.append("even")

    success_response = OrderedDict()
    success_response[NUMBER_KEY] = number
    success_response[IS_PRIME_KEY] = is_prime_num
    success_response[IS_PERFECT_KEY] = is_perfect_num
    success_response[PROPERTIES_KEY] = properties
    success_response[DIGIT_SUM_KEY] = digit_sum(number)
    success_response[FUN_FACT_KEY] = get_fun_fact(number)

    return Response(success_response, status=status.HTTP_200_OK)