#task 1
import requests
import json
from typing import Dict, List, Optional

class TransportFareFetcher:
    """Fetch public transport fares using multiple APIs with error handling."""
    
    def __init__(self, base_url: str = "https://api.example.com"):
        self.base_url = base_url
        self.transport_api_url = f"{base_url}/transport"
        self.route_api_url = f"{base_url}/routes"
        self.station_api_url = f"{base_url}/stations"
        self.timeout = 5
    
    def validate_station(self, station_code: str) -> bool:
        """Validate station using Station Validation API."""
        try:
            if not station_code or not isinstance(station_code, str):
                raise ValueError("Invalid station code format")
            
            response = requests.get(
                f"{self.station_api_url}/validate",
                params={"code": station_code},
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json().get("valid", False)
        
        except requests.exceptions.Timeout:
            print(f"Error: Station validation timeout for {station_code}")
            return False
        except requests.exceptions.ConnectionError:
            print("Error: Cannot connect to Station Validation API")
            return False
        except requests.exceptions.HTTPError as e:
            print(f"Error: HTTP error in station validation - {e.response.status_code}")
            return False
        except (ValueError, json.JSONDecodeError) as e:
            print(f"Error: Invalid station code or response format - {e}")
            return False
    
    def get_route(self, origin: str, destination: str) -> Optional[Dict]:
        """Get route information using Route API."""
        try:
            if not origin or not destination:
                raise ValueError("Origin and destination are required")
            
            response = requests.get(
                f"{self.route_api_url}/find",
                params={"from": origin, "to": destination},
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.Timeout:
            print("Error: Route API timeout")
            return None
        except requests.exceptions.ConnectionError:
            print("Error: Cannot connect to Route API")
            return None
        except requests.exceptions.HTTPError as e:
            print(f"Error: HTTP error in route API - {e.response.status_code}")
            return None
        except (ValueError, json.JSONDecodeError) as e:
            print(f"Error: Invalid input or response format - {e}")
            return None
    
    def fetch_fare(self, origin: str, destination: str, transport_type: str = "bus") -> Optional[Dict]:
        """Fetch transport fare using Transport API."""
        try:
            if not transport_type:
                raise ValueError("Transport type is required")
            
            response = requests.get(
                f"{self.transport_api_url}/fare",
                params={
                    "from": origin,
                    "to": destination,
                    "type": transport_type
                },
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.Timeout:
            print("Error: Transport API timeout")
            return None
        except requests.exceptions.ConnectionError:
            print("Error: Cannot connect to Transport API")
            return None
        except requests.exceptions.HTTPError as e:
            print(f"Error: HTTP error in transport API - {e.response.status_code}")
            return None
        except (ValueError, json.JSONDecodeError) as e:
            print(f"Error: Invalid transport type or response format - {e}")
            return None
    
    def get_complete_fare_info(self, origin: str, destination: str, transport_type: str = "bus") -> Dict:
        """Complete workflow: validate stations, get route, and fetch fare."""
        result = {
            "origin": origin,
            "destination": destination,
            "transport_type": transport_type,
            "status": "failed",
            "data": None,
            "errors": []
        }
        
        # Validate origin station
        if not self.validate_station(origin):
            result["errors"].append(f"Invalid origin station: {origin}")
            return result
        
        # Validate destination station
        if not self.validate_station(destination):
            result["errors"].append(f"Invalid destination station: {destination}")
            return result
        
        # Get route information
        route = self.get_route(origin, destination)
        if not route:
            result["errors"].append("Could not retrieve route information")
            return result
        
        # Fetch fare
        fare = self.fetch_fare(origin, destination, transport_type)
        if not fare:
            result["errors"].append("Could not retrieve fare information")
            return result
        
        result["status"] = "success"
        result["data"] = {
            "route": route,
            "fare": fare
        }
        return result


def main():
    """Main function to demonstrate fare fetching."""
    fetcher = TransportFareFetcher()
    
    # Example usage
    print("=== Public Transport Fare Fetcher ===\n")
    
    # Fetch fare for a route
    fare_info = fetcher.get_complete_fare_info("STN001", "STN002", "bus")
    
    print(json.dumps(fare_info, indent=2))
    
    if fare_info["status"] == "success":
        print("\n✓ Fare information retrieved successfully")
    else:
        print("\n✗ Errors encountered:")
        for error in fare_info["errors"]:
            print(f"  - {error}")


if __name__ == "__main__":
    main()


#task 2
import requests
from typing import Dict, Optional, Tuple

class CurrencyExchangeFetcher:
    """Fetch currency exchange rates using Forex and Conversion APIs with error handling."""
    
    def __init__(self, forex_api_url: str = "https://api.example.com/forex", 
                 conversion_api_url: str = "https://api.example.com/convert"):
        self.forex_api_url = forex_api_url
        self.conversion_api_url = conversion_api_url
        self.timeout = 5
        self.valid_currencies = {"USD", "EUR", "GBP", "INR", "JPY", "CAD", "AUD", "CHF"}
    
    def validate_currency(self, currency_code: str) -> bool:
        """Validate currency code format and existence."""
        try:
            if not currency_code or not isinstance(currency_code, str):
                raise ValueError("Invalid currency code format")
            
            currency_code = currency_code.upper()
            if len(currency_code) != 3:
                raise ValueError("Currency code must be 3 characters")
            
            if not currency_code.isalpha():
                raise ValueError("Currency code must contain only letters")
            
            return currency_code in self.valid_currencies
        
        except ValueError as e:
            print(f"Error: Currency validation failed - {e}")
            return False
    
    def validate_amount(self, amount: float) -> bool:
        """Validate exchange amount."""
        try:
            if not isinstance(amount, (int, float)):
                raise ValueError("Amount must be a number")
            
            if amount <= 0:
                raise ValueError("Amount must be greater than 0")
            
            return True
        
        except ValueError as e:
            print(f"Error: Amount validation failed - {e}")
            return False
    
    def get_exchange_rate(self, from_currency: str, to_currency: str) -> Optional[Dict]:
        """Fetch exchange rate from Forex API."""
        try:
            from_currency = from_currency.upper()
            to_currency = to_currency.upper()
            
            response = requests.get(
                f"{self.forex_api_url}/rate",
                params={"from": from_currency, "to": to_currency},
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.Timeout:
            print("Error: Forex API timeout")
            return None
        except requests.exceptions.ConnectionError:
            print("Error: Cannot connect to Forex API")
            return None
        except requests.exceptions.HTTPError as e:
            print(f"Error: HTTP error in Forex API - {e.response.status_code}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error: Invalid response format from Forex API - {e}")
            return None
    
    def convert_currency(self, amount: float, from_currency: str, to_currency: str) -> Optional[Dict]:
        """Convert amount from one currency to another using Conversion API."""
        try:
            from_currency = from_currency.upper()
            to_currency = to_currency.upper()
            
            response = requests.get(
                f"{self.conversion_api_url}/convert",
                params={
                    "amount": amount,
                    "from": from_currency,
                    "to": to_currency
                },
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.Timeout:
            print("Error: Conversion API timeout")
            return None
        except requests.exceptions.ConnectionError:
            print("Error: Cannot connect to Conversion API")
            return None
        except requests.exceptions.HTTPError as e:
            print(f"Error: HTTP error in Conversion API - {e.response.status_code}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error: Invalid response format from Conversion API - {e}")
            return None
    
    def get_complete_exchange_info(self, amount: float, from_currency: str, 
                                    to_currency: str) -> Dict:
        """Complete workflow: validate inputs, get exchange rate, and convert currency."""
        result = {
            "amount": amount,
            "from_currency": from_currency.upper(),
            "to_currency": to_currency.upper(),
            "status": "failed",
            "data": None,
            "errors": []
        }
        
        # Validate amount
        if not self.validate_amount(amount):
            result["errors"].append(f"Invalid amount: {amount}")
            return result
        
        # Validate from currency
        if not self.validate_currency(from_currency):
            result["errors"].append(f"Invalid from currency: {from_currency}")
            return result
        
        # Validate to currency
        if not self.validate_currency(to_currency):
            result["errors"].append(f"Invalid to currency: {to_currency}")
            return result
        
        # Get exchange rate
        exchange_rate = self.get_exchange_rate(from_currency, to_currency)
        if not exchange_rate:
            result["errors"].append("Could not retrieve exchange rate")
            return result
        
        # Convert currency
        conversion = self.convert_currency(amount, from_currency, to_currency)
        if not conversion:
            result["errors"].append("Could not perform currency conversion")
            return result
        
        result["status"] = "success"
        result["data"] = {
            "exchange_rate": exchange_rate,
            "conversion": conversion
        }
        return result


def main_task2():
    """Main function to demonstrate currency exchange fetching."""
    fetcher = CurrencyExchangeFetcher()
    
    # Example usage
    print("=== Currency Exchange Rate Fetcher ===\n")
    
    # Convert 100 USD to EUR
    exchange_info = fetcher.get_complete_exchange_info(100.0, "USD", "EUR")
    
    print(json.dumps(exchange_info, indent=2))
    
    if exchange_info["status"] == "success":
        print("\n✓ Exchange information retrieved successfully")
    else:
        print("\n✗ Errors encountered:")
        for error in exchange_info["errors"]:
            print(f"  - {error}")


if __name__ == "__main__":
    main()
    main_task2()


#task 3
class GitHubRepositoryFetcher:
    """Fetch GitHub repository information using GitHub REST API with input validation and error handling."""
    
    def __init__(self, api_token: Optional[str] = None):
        self.base_url = "https://api.github.com"
        self.headers = {"Accept": "application/vnd.github.v3+json"}
        if api_token:
            self.headers["Authorization"] = f"token {api_token}"
        self.timeout = 5
    
    def validate_username(self, username: str) -> bool:
        """Validate GitHub username format."""
        try:
            if not username or not isinstance(username, str):
                raise ValueError("Username must be a non-empty string")
            
            if len(username) < 1 or len(username) > 39:
                raise ValueError("Username must be between 1 and 39 characters")
            
            if not all(c.isalnum() or c == '-' for c in username):
                raise ValueError("Username can only contain alphanumeric characters and hyphens")
            
            if username.startswith('-') or username.endswith('-'):
                raise ValueError("Username cannot start or end with a hyphen")
            
            return True
        
        except ValueError as e:
            print(f"Error: Username validation failed - {e}")
            return False
    
    def validate_repo_name(self, repo_name: str) -> bool:
        """Validate repository name format."""
        try:
            if not repo_name or not isinstance(repo_name, str):
                raise ValueError("Repository name must be a non-empty string")
            
            if len(repo_name) < 1 or len(repo_name) > 100:
                raise ValueError("Repository name must be between 1 and 100 characters")
            
            return True
        
        except ValueError as e:
            print(f"Error: Repository name validation failed - {e}")
            return False
    
    def get_user_repos(self, username: str) -> Optional[List[Dict]]:
        """Fetch all repositories for a given GitHub user."""
        try:
            if not self.validate_username(username):
                return None
            
            response = requests.get(
                f"{self.base_url}/users/{username}/repos",
                headers=self.headers,
                timeout=self.timeout,
                params={"per_page": 100}
            )
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.Timeout:
            print(f"Error: GitHub API timeout while fetching repos for {username}")
            return None
        except requests.exceptions.ConnectionError:
            print("Error: Cannot connect to GitHub API")
            return None
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"Error: User {username} not found on GitHub")
            else:
                print(f"Error: HTTP error - {e.response.status_code}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error: Invalid response format from GitHub API - {e}")
            return None
    
    def get_repo_details(self, username: str, repo_name: str) -> Optional[Dict]:
        """Fetch detailed information about a specific repository."""
        try:
            if not self.validate_username(username):
                return None
            
            if not self.validate_repo_name(repo_name):
                return None
            
            response = requests.get(
                f"{self.base_url}/repos/{username}/{repo_name}",
                headers=self.headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.Timeout:
            print(f"Error: GitHub API timeout while fetching repo {username}/{repo_name}")
            return None
        except requests.exceptions.ConnectionError:
            print("Error: Cannot connect to GitHub API")
            return None
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"Error: Repository {username}/{repo_name} not found")
            else:
                print(f"Error: HTTP error - {e.response.status_code}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error: Invalid response format from GitHub API - {e}")
            return None
    
    def get_repo_contributors(self, username: str, repo_name: str) -> Optional[List[Dict]]:
        """Fetch contributors list for a repository."""
        try:
            if not self.validate_username(username):
                return None
            
            if not self.validate_repo_name(repo_name):
                return None
            
            response = requests.get(
                f"{self.base_url}/repos/{username}/{repo_name}/contributors",
                headers=self.headers,
                timeout=self.timeout,
                params={"per_page": 100}
            )
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.Timeout:
            print(f"Error: GitHub API timeout while fetching contributors")
            return None
        except requests.exceptions.ConnectionError:
            print("Error: Cannot connect to GitHub API")
            return None
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"Error: Repository {username}/{repo_name} not found")
            else:
                print(f"Error: HTTP error - {e.response.status_code}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error: Invalid response format from GitHub API - {e}")
            return None
    
    def get_complete_repo_info(self, username: str, repo_name: str) -> Dict:
        """Complete workflow: validate inputs and fetch comprehensive repository information."""
        result = {
            "username": username,
            "repo_name": repo_name,
            "status": "failed",
            "data": None,
            "errors": []
        }
        
        # Validate username
        if not self.validate_username(username):
            result["errors"].append(f"Invalid username: {username}")
            return result
        
        # Validate repository name
        if not self.validate_repo_name(repo_name):
            result["errors"].append(f"Invalid repository name: {repo_name}")
            return result
        
        # Fetch repository details
        repo_details = self.get_repo_details(username, repo_name)
        if not repo_details:
            result["errors"].append("Could not retrieve repository details")
            return result
        
        # Fetch contributors
        contributors = self.get_repo_contributors(username, repo_name)
        if not contributors:
            result["errors"].append("Could not retrieve contributors list")
            return result
        
        result["status"] = "success"
        result["data"] = {
            "repository": repo_details,
            "contributors": contributors[:10]  # Top 10 contributors
        }
        return result


def main_task3():
    """Main function to demonstrate GitHub repository fetching."""
    fetcher = GitHubRepositoryFetcher()
    
    # Example usage
    print("=== GitHub Repository Information Fetcher ===\n")
    
    # Fetch repository information
    repo_info = fetcher.get_complete_repo_info("torvalds", "linux")
    
    print(json.dumps(repo_info, indent=2))
    
    if repo_info["status"] == "success":
        print("\n✓ Repository information retrieved successfully")
    else:
        print("\n✗ Errors encountered:")
        for error in repo_info["errors"]:
            print(f"  - {error}")


if __name__ == "__main__":
    main()
    main_task2()
    main_task3()


# Task 4: News Headlines Fetching using News API
class NewsHeadlinesFetcher:
    """Fetch news headlines using News API with category-based filtering and retry mechanism."""
    
    def __init__(self, api_key: str = "demo", max_retries: int = 3):
        self.api_url = "https://newsapi.org/v2"
        self.api_key = api_key
        self.max_retries = max_retries
        self.timeout = 5
        self.categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
    
    def validate_category(self, category: str) -> bool:
        """Validate if category is supported."""
        return category.lower() in self.categories
    
    def fetch_with_retry(self, url: str, params: Dict) -> Optional[Dict]:
        """Fetch data from API with retry mechanism."""
        for attempt in range(self.max_retries):
            try:
                response = requests.get(url, params=params, timeout=self.timeout)
                response.raise_for_status()
                return response.json()
            
            except requests.exceptions.Timeout:
                print(f"Attempt {attempt + 1}: Timeout error. Retrying...")
            except requests.exceptions.ConnectionError:
                print(f"Attempt {attempt + 1}: Connection error. Retrying...")
            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 429:  # Rate limit
                    print(f"Attempt {attempt + 1}: Rate limited. Retrying...")
                else:
                    print(f"Attempt {attempt + 1}: HTTP error {e.response.status_code}")
                    return None
            except json.JSONDecodeError:
                print(f"Attempt {attempt + 1}: Invalid JSON response")
                return None
            except Exception as e:
                print(f"Attempt {attempt + 1}: Unexpected error - {e}")
        
        return None
    
    def get_top_headlines(self, category: str = "general", country: str = "us") -> Dict:
        """Fetch top headlines by category with error handling."""
        result = {
            "status": "error",
            "data": [],
            "errors": []
        }
        
        if not self.validate_category(category):
            result["errors"].append(f"Invalid category: {category}. Supported: {', '.join(self.categories)}")
            return result
        
        params = {
            "category": category.lower(),
            "country": country,
            "apiKey": self.api_key
        }
        
        response = self.fetch_with_retry(f"{self.api_url}/top-headlines", params)
        
        if not response:
            result["errors"].append("Failed to fetch headlines after retries")
            return result
        
        if response.get("status") == "error":
            result["errors"].append(response.get("message", "API returned error"))
            return result
        
        result["status"] = "success"
        result["data"] = response.get("articles", [])
        result["total_results"] = response.get("totalResults", 0)
        
        return result
    
    def search_headlines(self, query: str, sort_by: str = "publishedAt") -> Dict:
        """Search headlines by keyword with error handling."""
        result = {
            "status": "error",
            "data": [],
            "errors": []
        }
        
        if not query or not isinstance(query, str):
            result["errors"].append("Query must be a non-empty string")
            return result
        
        valid_sort_options = ["relevancy", "popularity", "publishedAt"]
        if sort_by not in valid_sort_options:
            result["errors"].append(f"Invalid sort option. Choose from: {', '.join(valid_sort_options)}")
            return result
        
        params = {
            "q": query,
            "sortBy": sort_by,
            "apiKey": self.api_key
        }
        
        response = self.fetch_with_retry(f"{self.api_url}/everything", params)
        
        if not response:
            result["errors"].append("Failed to search headlines after retries")
            return result
        
        if response.get("status") == "error":
            result["errors"].append(response.get("message", "API returned error"))
            return result
        
        result["status"] = "success"
        result["data"] = response.get("articles", [])
        result["total_results"] = response.get("totalResults", 0)
        
        return result


def main_task4():
    """Main function to demonstrate news headlines fetching."""
    fetcher = NewsHeadlinesFetcher()
    
    print("=== News Headlines Fetcher ===\n")
    
    # Fetch top headlines by category
    print("Fetching top technology headlines...\n")
    headlines = fetcher.get_top_headlines(category="technology", country="us")
    
    if headlines["status"] == "success":
        print(f"✓ Retrieved {len(headlines['data'])} headlines (Total: {headlines['total_results']})")
        for idx, article in enumerate(headlines["data"][:5], 1):
            print(f"\n{idx}. {article.get('title', 'N/A')}")
            print(f"   Source: {article.get('source', {}).get('name', 'N/A')}")
            print(f"   Published: {article.get('publishedAt', 'N/A')}")
    else:
        print("✗ Errors encountered:")
        for error in headlines["errors"]:
            print(f"  - {error}")
    
    # Search headlines
    print("\n\nSearching for COVID-19 news...\n")
    search_results = fetcher.search_headlines(query="COVID-19", sort_by="publishedAt")
    
    if search_results["status"] == "success":
        print(f"✓ Found {len(search_results['data'])} articles")
    else:
        print("✗ Search errors:")
        for error in search_results["errors"]:
            print(f"  - {error}")


if __name__ == "__main__" or True:
    try:
        main_task4()
    except Exception as e:
        print(f"Error in main_task4: {e}")


#task 5
import time
from datetime import datetime

class COVID19StatisticsFetcher:
    """Fetch COVID-19 statistics using public health API with rate-limit retry handling."""
    
    def __init__(self, api_url: str = "https://disease.sh/v3/covid-19"):
        self.api_url = api_url
        self.timeout = 10
        self.max_retries = 3
        self.retry_delay = 2
    
    def _handle_rate_limit(self, retry_count: int) -> None:
        """Handle rate limiting with exponential backoff."""
        wait_time = self.retry_delay * (2 ** retry_count)
        print(f"Rate limited. Retrying in {wait_time} seconds...")
        time.sleep(wait_time)
    
    def get_country_statistics(self, country: str) -> Dict[str, any]:
        """Fetch COVID-19 statistics for a specific country with retry logic."""
        for attempt in range(self.max_retries):
            try:
                if not country or not isinstance(country, str):
                    raise ValueError("Country must be a non-empty string")
                
                response = requests.get(
                    f"{self.api_url}/countries/{country}",
                    timeout=self.timeout
                )
                
                # Handle rate limiting
                if response.status_code == 429:
                    if attempt < self.max_retries - 1:
                        self._handle_rate_limit(attempt)
                        continue
                    else:
                        return {
                            "status": "error",
                            "errors": ["Rate limit exceeded after maximum retries"],
                            "data": None
                        }
                
                response.raise_for_status()
                data = response.json()
                return {
                    "status": "success",
                    "errors": [],
                    "data": {
                        "country": data.get("country", "N/A"),
                        "cases": data.get("cases", 0),
                        "deaths": data.get("deaths", 0),
                        "recovered": data.get("recovered", 0),
                        "active": data.get("active", 0),
                        "critical": data.get("critical", 0),
                        "tests": data.get("tests", 0),
                        "updated": data.get("updated", None)
                    }
                }
            
            except requests.exceptions.Timeout:
                error_msg = f"Timeout fetching data for {country} (attempt {attempt + 1})"
                if attempt == self.max_retries - 1:
                    return {"status": "error", "errors": [error_msg], "data": None}
                self._handle_rate_limit(attempt)
            
            except requests.exceptions.ConnectionError as e:
                error_msg = f"Connection error for {country}: {str(e)}"
                if attempt == self.max_retries - 1:
                    return {"status": "error", "errors": [error_msg], "data": None}
                self._handle_rate_limit(attempt)
            
            except requests.exceptions.HTTPError as e:
                error_msg = f"HTTP error {e.response.status_code} for {country}"
                if attempt == self.max_retries - 1:
                    return {"status": "error", "errors": [error_msg], "data": None}
                self._handle_rate_limit(attempt)
            
            except (ValueError, json.JSONDecodeError) as e:
                return {"status": "error", "errors": [f"Invalid country or response format: {e}"], "data": None}
        
        return {"status": "error", "errors": ["Failed to fetch data after retries"], "data": None}
    
    def get_multiple_countries(self, countries: List[str]) -> Dict[str, any]:
        """Fetch COVID-19 statistics for multiple countries."""
        try:
            if not countries or not isinstance(countries, list):
                raise ValueError("Countries must be a non-empty list")
            
            results = []
            for country in countries:
                result = self.get_country_statistics(country)
                results.append(result)
                time.sleep(0.5)  # Small delay between requests
            
            return {
                "status": "success",
                "errors": [],
                "data": results,
                "total_countries": len(countries)
            }
        
        except ValueError as e:
            return {"status": "error", "errors": [str(e)], "data": None}
    
    def get_global_statistics(self) -> Dict[str, any]:
        """Fetch global COVID-19 statistics with rate-limit handling."""
        for attempt in range(self.max_retries):
            try:
                response = requests.get(
                    f"{self.api_url}/all",
                    timeout=self.timeout
                )
                
                if response.status_code == 429:
                    if attempt < self.max_retries - 1:
                        self._handle_rate_limit(attempt)
                        continue
                    else:
                        return {
                            "status": "error",
                            "errors": ["Rate limit exceeded for global stats"],
                            "data": None
                        }
                
                response.raise_for_status()
                data = response.json()
                return {
                    "status": "success",
                    "errors": [],
                    "data": {
                        "cases": data.get("cases", 0),
                        "deaths": data.get("deaths", 0),
                        "recovered": data.get("recovered", 0),
                        "active": data.get("active", 0),
                        "updated": data.get("updated", None)
                    }
                }
            
            except requests.exceptions.Timeout:
                if attempt == self.max_retries - 1:
                    return {"status": "error", "errors": ["Timeout fetching global stats"], "data": None}
                self._handle_rate_limit(attempt)
            
            except requests.exceptions.ConnectionError as e:
                if attempt == self.max_retries - 1:
                    return {"status": "error", "errors": [f"Connection error: {str(e)}"], "data": None}
                self._handle_rate_limit(attempt)
            
            except requests.exceptions.HTTPError as e:
                return {"status": "error", "errors": [f"HTTP error {e.response.status_code}"], "data": None}
            
            except json.JSONDecodeError as e:
                return {"status": "error", "errors": [f"Invalid response format: {e}"], "data": None}
        
        return {"status": "error", "errors": ["Failed to fetch global stats"], "data": None}


def main_task5():
    """Main function to demonstrate COVID-19 statistics fetching."""
    fetcher = COVID19StatisticsFetcher()
    
    print("=== COVID-19 Statistics Fetcher ===\n")
    
    # Fetch global statistics
    print("Fetching global COVID-19 statistics...\n")
    global_stats = fetcher.get_global_statistics()
    
    if global_stats["status"] == "success":
        stats = global_stats["data"]
        print(f"✓ Global Statistics:")
        print(f"  Cases: {stats['cases']:,}")
        print(f"  Deaths: {stats['deaths']:,}")
        print(f"  Recovered: {stats['recovered']:,}")
        print(f"  Active: {stats['active']:,}")
    else:
        print("✗ Global stats errors:")
        for error in global_stats["errors"]:
            print(f"  - {error}")
    
    # Fetch country-based statistics
    print("\n\nFetching COVID-19 statistics by country...\n")
    countries = ["US", "India", "Brazil"]
    country_results = fetcher.get_multiple_countries(countries)
    
    if country_results["status"] == "success":
        print(f"✓ Retrieved statistics for {country_results['total_countries']} countries:")
        for result in country_results["data"]:
            if result["status"] == "success":
                data = result["data"]
                print(f"\n  {data['country']}:")
                print(f"    Cases: {data['cases']:,}")
                print(f"    Deaths: {data['deaths']:,}")
                print(f"    Recovered: {data['recovered']:,}")
            else:
                print(f"  Error fetching data: {result['errors']}")
    else:
        print("✗ Country stats errors:")
        for error in country_results["errors"]:
            print(f"  - {error}")


if __name__ == "__main__" or True:
    try:
        main_task5()
    except Exception as e:
        print(f"Error in main_task5: {e}")
1