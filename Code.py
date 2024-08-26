import requests
import json

# Keywords to search for
keywords = ["open redirect", "idor", "cross site scripting"]

# GraphQL query
j = 0
while j < 20000000:
    graphql_query = {
        "operationName": "HacktivitySearchQuery",
        "variables": {
            "queryString": "*:*",
            "size": 25,
            "from": 0 + j,
            "sort": {
                "field": "disclosed_at",
                "direction": "DESC"
            },
            "index": "CompleteHacktivityReportIndexService"  # Correct index value
        },
        "query": """
        query HacktivitySearchQuery($queryString: String!, $from: Int, $size: Int, $sort: SortInput!, $index: IndexEnum!) {
            search(
                index: $index
                query_string: $queryString
                from: $from
                size: $size
                sort: $sort
            ) {
                total_count
                nodes {
                    __typename
                    ... on CompleteHacktivityReportDocument {
                        id
                        report {
                            title
                            url
                        }
                    }
                }
            }
        }
        """
    }

    # URL of the GraphQL endpoint
    graphql_endpoint = 'https://hackerone.com/graphql'

    # Send POST request with GraphQL query
    response = requests.post(graphql_endpoint, json=graphql_query)

    # Print response status code
   # print(f"Response Status Code: {response.status_code}")

    # If status code is 200, process the response
    if response.status_code == 200:
        data = response.json()

        # Print response content for debugging
        # print("Response Content:")
        # print(json.dumps(data, indent=2))  # Print formatted JSON for readability

        # Extract and print URLs from the response
        if "data" in data and "search" in data["data"]:
            for i in data["data"]["search"]["nodes"]:
                if "__typename" in i and i["__typename"] == "CompleteHacktivityReportDocument":
                    if "report" in i and "title" in i["report"] and "url" in i["report"]:
                        title = i["report"]["title"].lower()  # Convert title to lowercase for case-insensitive search
                        report_url = i["report"]["url"]

                        # Check if the title contains any of the keywords
                        if any(keyword.lower() in title for keyword in keywords):
                            print(report_url)  # Print report URL
        else:
            print("Data or search key not found in response")
    else:
        print(f"Request failed with status code: {response.status_code}")

    # Increment the page counter for pagination
    j += 25
