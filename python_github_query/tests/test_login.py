import os
import pytest
from python_github_query.github_graphql.authentication import PersonalAccessTokenAuthenticator
from python_github_query.github_graphql.client import Client
from python_github_query.queries.login import UserLoginViewer, UserLogin


@pytest.fixture(scope="class")
def graphql_client():
    # Set up the GraphQL client
    client = Client(
        host="api.github.com", is_enterprise=False,
        authenticator=PersonalAccessTokenAuthenticator(token=os.environ.get("GITHUB_PERSONAL_ACCESS_TOKEN"))
    )

    enterprise_client = Client(
        host="github.ncsu.edu", is_enterprise=True,
        authenticator=PersonalAccessTokenAuthenticator(token=os.environ.get("GITHUB_ENTERPRISE_PERSONAL_ACCESS_TOKEN"))
    )
    yield [client, enterprise_client]


@pytest.mark.usefixtures("graphql_client")
class TestLogin:
    def test_user_login_viewer_public(self, graphql_client):
        client = graphql_client[0]
        response = client.execute(
            query=UserLoginViewer.query, substitutions={}
        )

        expected_data = {
            'viewer': {
                'login': 'JialinC'
            }
        }
        assert response == expected_data

    def test_user_login_viewer_enterprise(self, graphql_client):
        client = graphql_client[1]
        response = client.execute(
            query=UserLoginViewer.query, substitutions={}
        )

        expected_data = {
            'viewer': {
                'login': 'jcui9'
            }
        }
        assert response == expected_data

    def test_user_login_public(self, graphql_client):
        client = graphql_client[0]
        response = client.execute(
            query=UserLogin.query, substitutions={"user": "JialinC"}
        )

        expected_data = {
            'user': {
                'login': 'JialinC',
                'name': 'Jialin Cui',
                'email': '',
                'createdAt': '2018-04-20T04:37:16Z'}
        }
        assert response == expected_data

    def test_user_login_enterprise(self, graphql_client):
        client = graphql_client[1]
        response = client.execute(
            query=UserLogin.query, substitutions={"user": "jcui9"}
        )

        expected_data = {
            'user': {
                'login': 'jcui9',
                'name': 'jcui9',
                'email': 'jcui9@ncsu.edu',
                'createdAt': '2019-09-11T17:08:06Z'
            }
        }
        assert response == expected_data


