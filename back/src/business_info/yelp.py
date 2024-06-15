from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import os

class YelpHandler:
    def __init__(self, api_key):
        self.api_key = api_key

    def call_api(self, location): # Location must be string
        # Define the GraphQL endpoint
        url = 'https://api.yelp.com/v3/graphql'

        # Define the GraphQL query
        query = gql(f"""query Restaurant {{
        search(
            term: "dog friendly"
            sort_by: "distance"
            open_now: true
            categories: "restaurant"
            location: "{location}"
            limit: 1
        ) {{
            business {{
            id
            name
            coordinates {{
                latitude
                longitude
            }}
            url
            distance
            photos
            price
            phone
            rating
            }}
            total
        }}
        }}
        """)

        transport = RequestsHTTPTransport(
            url=url,
            headers={'Authorization': f'Bearer {self.api_key}'},
            use_json=True,
        )

        # Create a GraphQL client using the defined transport
        client = Client(transport=transport, fetch_schema_from_transport=True)
        result = client.execute(query)
        return result
