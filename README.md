# API Health Check

Perform health checks on API endpoints with this Python script. Simply specify the URL, HTTP method, and expected status code to monitor the health of your APIs.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/api-healthcheck.git
    ```

2. Navigate to the project directory:

    ```bash
    cd api-healthcheck
    ```

3. Install dependencies (if required):

    ```bash
    pip install -r requirements.txt
    ```

4. Run the script:

    ```bash
    python healthcheck.py --endpoint <API_URL> --method <HTTP_METHOD> --expected <EXPECTED_STATUS_CODE>
    ```

Replace `<API_URL>`, `<HTTP_METHOD>`, and `<EXPECTED_STATUS_CODE>` with the appropriate values for your API endpoint.

## Parameters

- `--endpoint`: The URL of the API endpoint.
- `--method`: The HTTP method to use (GET, POST, PUT, etc.).
- `--expected`: The expected HTTP status code.

## Example

```bash
python healthcheck.py --endpoint http://example.com/api --method GET --expected 200
