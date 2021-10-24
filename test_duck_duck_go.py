import requests
import pytest

ddg_url = "https://api.duckduckgo.com"


@pytest.fixture()
def unique_presidency_last_names():
    return {
        "Washington",
        "Adams",
        "Jefferson",
        "Madison",
        "Monroe",
        "Adams",
        "Jackson",
        "Van Buren",
        "Harrison",
        "Tyler",
        "Polk",
        "Taylor",
        "Fillmore",
        "Pierce",
        "Buchanan",
        "Lincoln",
        "Johnson",
        "Grant",
        "Hayes",
        "Garfield",
        "Arthur",
        "Cleveland",
        "Harrison",
        "Cleveland",
        "McKinley",
        "Roosevelt",
        "Taft",
        "Wilson",
        "Harding",
        "Coolidge",
        "Hoover",
        "Roosevelt",
        "Truman",
        "Eisenhower",
        "Kennedy",
        "Johnson",
        "Nixon",
        "Ford",
        "Carter",
        "Reagan",
        "Bush",
        "Clinton",
        "Bush",
        "Obama",
        "Trump",
        "Biden"
    }


def test_duck_duck_go_presidents_query(unique_presidency_last_names):
    # Make request querying presidents
    query = "/?q=presidents of the united states&format=json"
    res = requests.get(ddg_url + query)
    # Extract 'RelatedTopics' field and store as string all lower case
    lowercase_data = str(res.json()['RelatedTopics']).lower()

    # Iterate presidents
    for last_name in unique_presidency_last_names:
        # Check lower case name in data
        assert last_name.lower() in lowercase_data
