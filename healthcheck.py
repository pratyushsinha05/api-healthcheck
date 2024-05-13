import argparse
import requests

def check_health(endpoint_url, http_method, expected_status_code):
    try:
        response = requests.request(http_method, endpoint_url)
        if response.status_code == expected_status_code:
            return True, response.status_code
        else:
            return False, response.status_code
    except requests.RequestException as e:
        return False, None

def main():
    parser = argparse.ArgumentParser(description="Health check of an API endpoint")
    parser.add_argument('--endpoint', help='API endpoint URL', required=True)
    parser.add_argument('--method', help='HTTP method (GET, POST, PUT, etc.)', required=True)
    parser.add_argument('--expected', help='Expected HTTP status code', type=int, required=True)
    args = parser.parse_args()

    # Validate HTTP method
    valid_methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS']
    if args.method.upper() not in valid_methods:
        print("Error: Invalid HTTP method. Please provide a valid HTTP method.")
        return

    # Validate expected status code
    if args.expected < 100 or args.expected >= 600:
        print("Error: Invalid expected status code. Please provide a status code in the range of 100 to 599.")
        return

    is_healthy, status_code = check_health(args.endpoint, args.method.upper(), args.expected)
    if is_healthy:
        print(f"Endpoint {args.endpoint} is healthy. Returned status code: {status_code}")
    else:
        print(f"Endpoint {args.endpoint} is unhealthy. Returned status code: {status_code}")

if __name__ == "__main__":
    main()
