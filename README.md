# Number Classification API

## Overview
This API classifies numbers based on mathematical properties such as primality, Armstrong status, parity (odd/even), and perfection. It also fetches a fun fact about the number from the Numbers API.

## Features
- Check if a number is prime, Armstrong, or perfect.
- Determine if a number is odd or even.
- Calculate the sum of the digits of the number.
- Retrieve a fun fact from the Numbers API.
- Handles CORS requests.

## Technologies Used
- **FastAPI** - For building the API.
- **Uvicorn** - For running the application.
- **Httpx** - For making external API requests.
- **Python** - Core programming language.

## Installation
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd number-classification-api
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the API Locally
Start the FastAPI application using Uvicorn:
```sh
uvicorn main:app --reload
```
The API will be accessible at `http://127.0.0.1:8000`.

## API Endpoint
### Classify a Number
**Endpoint:** `GET /api/classify-number?number=<integer>`

#### Example Request:
```sh
curl -X GET "http://127.0.0.1:8000/api/classify-number?number=371"
```

#### Example Response:
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

## Deployment (AWS Lambda Function URL)
This API is deployed using AWS Lambda with **Lambda Function URLs**.

### Steps to Deploy:
1. **Package the application**:
   ```bash
   Compress-Archive venv\Lib\site-packages\* lambda.zip 
   Compress-Archive .\main.py -Update lambda.zip
   ```
2. **Create an AWS Lambda function**.
3. **Upload `lambda.zip`** as the Lambda function's code.
4. **Set up Lambda Function URL**:
   - Enable Function URL in the AWS Lambda console.
   - Set Auth Type to `NONE` for public access.
   - **Enable CORS**:
5. **Test the Lambda Function URL**:
   ```bash
   curl -X GET "https://your-lambda-url/api/classify-number?number=153"
   ```

## Error Handling
- If the input is not a valid number:
  ```json
  {
      "number": "abc",
      "error": true
  }
  ```
- All valid numbers (including negative and floating-point) return 200 status code

## License
This project is licensed under the MIT License.

## Contributing
If you find any issues or have suggestions, feel free to open an issue or submit a pull request or reach out to me.
* **Ameh Richard Atodo** [@RichardAtodo](https://x.com/RichardAtodo)