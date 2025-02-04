from mangum import Mangum
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx
import math

app = FastAPI(title="Number Classification API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_armstrong(num: int) -> bool:
    str_num = str(abs(num))
    power = len(str_num)
    return abs(num) == sum(int(digit) ** power for digit in str_num)

def is_prime(num: int) -> bool:
    num = abs(num)
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect(num: int) -> bool:
    num = abs(num)
    if num <= 1:
        return False
    return sum(i for i in range(1, num) if num % i == 0) == num

def get_digit_sum(num: int) -> int:
    return sum(int(digit) for digit in str(abs(num)))

async def get_fun_fact(num: int) -> str:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"http://numbersapi.com/{abs(num)}/math")
            if response.status_code == 200:
                return response.text
            return f"{num} is a number with interesting properties."
    except:
        return f"{num} is a number with interesting properties."

@app.get("/api/classify-number")
async def classify_number(number: str):
    try:
        # Try to convert to float first to handle decimal points
        num_float = float(number)
        # Convert to integer by truncating
        num = int(num_float)
        
        # Generate properties
        properties = []
        if is_armstrong(num):
            properties.append("armstrong")
        properties.append("odd" if num % 2 else "even")

        # Get fun fact
        fun_fact = await get_fun_fact(num)

        return {
            "number": num,
            "is_prime": is_prime(num),
            "is_perfect": is_perfect(num),
            "properties": properties,
            "digit_sum": get_digit_sum(num),
            "fun_fact": fun_fact
        }
    except (ValueError, TypeError):
        # Raise HTTPException with 400 status code for invalid input
        raise HTTPException(
            status_code=400,
            detail={
                "number": number,
                "error": True
            }
        )
    except Exception as e:
        # Raise HTTPException with 400 status code for other errors
        raise HTTPException(
            status_code=400,
            detail={
                "number": number,
                "error": True
            }
        )

handler = Mangum(app)