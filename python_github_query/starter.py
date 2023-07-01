import os
import json
from python_github_query.github_graphql.query import QueryNodePaginator, QueryNode, Query, PaginatedQuery
from python_github_query.github_graphql.authentication import PersonalAccessTokenAuthenticator
from python_github_query.github_graphql.client import Client
from python_github_query.queries.login import UserLoginViewer, UserLogin
from python_github_query.queries.metrics import UserMetrics
from python_github_query.queries.commits import UserCommits
from python_github_query.queries.comments import UserComments
from python_github_query.queries.contributions import UserContributions
from python_github_query.queries.repositories import UserRepositories

if __name__ == '__main__':
    client = Client(
        host="api.github.com", is_enterprise=False,
        authenticator=PersonalAccessTokenAuthenticator(token=os.environ.get("GITHUB_PERSONAL_ACCESS_TOKEN"))
    )

    # enterprise_client = Client(
    #     host="github.ncsu.edu", is_enterprise=True,
    #     authenticator=PersonalAccessTokenAuthenticator(token=os.environ.get("GITHUB_ENTERPRISE_PERSONAL_ACCESS_TOKEN"))
    # )

    path1 = "https://api.github.com/graphql"
    header1 = client._generate_headers()
    # path2 = "https://github.ncsu.edu/api/graphql"
    # header2 = enterprise_client._generate_headers()

    # UserLoginViewer
    response = client.execute(query=UserLoginViewer(), substitutions={})
    print(response)

    # response = enterprise_client.execute(query=UserLoginViewer(), substitutions={})
    # print(response)

    # UserLogin
    response = client.execute(query=UserLogin(), substitutions={"user": "JialinC"})
    print(response)

    # response = enterprise_client.execute(query=UserLogin(), substitutions={"user": "jcui9"})
    # print(response)

    # UserMetrics
    response = client.execute(query=UserMetrics(), substitutions={"user": "JialinC"})
    print(response)

    # response = enterprise_client.execute(query=UserMetrics(), substitutions={"user": "jcui9"})
    # print(response)

    # UserCommits
    response = client.execute(query=UserCommits(), substitutions={"user": "JialinC",
                                                                  "start": "2020-02-07T18:11:20Z",
                                                                  "end": "2021-02-07T18:11:20Z"})
    print(response)

    # response = enterprise_client.execute(query=UserCommits(), substitutions={"user": "jcui9",
    #                                                                          "start": "2020-02-07T18:11:20Z",
    #                                                                          "end": "2021-02-07T18:11:20Z"}
    # print(response)

    # UserComments
    for response in client.execute(query=UserComments(),
                                   substitutions={"user": "JialinC", "pg_size": 10, "comment_type": "commitComments"}):
        print(response)
    for response in client.execute(query=UserComments(),
                                   substitutions={"user": "JialinC", "pg_size": 10, "comment_type": "gistComments"}):
        print(response)
    for response in client.execute(query=UserComments(),
                                   substitutions={"user": "JialinC", "pg_size": 10, "comment_type": "issueComments"}):
        print(response)
    for response in client.execute(query=UserComments(),
                                   substitutions={"user": "JialinC", "pg_size": 10,
                                                  "comment_type": "repositoryDiscussionComments"}):
        print(response)

    # for response in enterprise_client.execute(query=UserComments(),
    #                                           substitutions={"user": "jcui9", "pg_size": 2, "comment_type": "commitComments"}):
    #     print(response)
    # for response in enterprise_client.execute(query=UserComments(),
    #                                           substitutions={"user": "jcui9", "pg_size": 2, "comment_type": "gistComments"}):
    #     print(response)
    # for response in enterprise_client.execute(query=UserComments(),
    #                                           substitutions={"user": "jcui9", "pg_size": 2, "comment_type": "issueComments"}):
    #     print(response)
    # for response in enterprise_client.execute(query=UserComments(),
    #                                           substitutions={"user": "jcui9", "pg_size": 2, "comment_type": "repositoryDiscussionComments"}):
    #     print(response)

    # UserContributions
    for response in client.execute(query=UserContributions(),
                                   substitutions={"user": "JialinC", "pg_size": 10, "contribution_type": "gists"}):
        print(response)
    for response in client.execute(query=UserContributions(),
                                   substitutions={"user": "JialinC", "pg_size": 10,
                                                  "contribution_type": "repositoryDiscussions"}):
        print(response)
    for response in client.execute(query=UserContributions(),
                                              substitutions={"user": "JialinC", "pg_size": 10,
                                                             "contribution_type": "pullRequests"}):
        print(response)
    for response in client.execute(query=UserContributions(),
                                              substitutions={"user": "JialinC", "pg_size": 10,
                                                             "contribution_type": "issues"}):
        print(response)

    # for response in enterprise_client.execute(query=UserContributions(),
    #                                substitutions={"user": "jcui9", "pg_size": 2, "contribution_type": "gists"}):
    #     print(response)
    # for response in enterprise_client.execute(query=UserContributions(),
    #                                substitutions={"user": "jcui9", "pg_size": 2,
    #                                               "contribution_type": "repositoryDiscussions"}):
    #     print(response)
    # for response in enterprise_client.execute(query=UserContributions(),
    #                                substitutions={"user": "jcui9", "pg_size": 2, "contribution_type": "pullRequests"}):
    #     print(response)
    # for response in enterprise_client.execute(query=UserContributions(),
    #                                substitutions={"user": "jcui9", "pg_size": 2,
    #                                               "contribution_type": "issues"}):
    #     print(response)

    # UserRepositories
    for response in client.execute(query=UserRepositories(), substitutions={"user": "JialinC",
                                                                            "pg_size": 5,
                                                                            "is_fork": True,
                                                                            "ownership": "OWNER",
                                                                            "order_by": {"field": "CREATED_AT", "direction": "ASC"}}):
        print(response)

    print("True", "COLLABORATOR")
    for response in client.execute(query=UserRepositories(), substitutions={"user": "JialinC",
                                                                            "pg_size": 5,
                                                                            "is_fork": True,
                                                                            "ownership": "COLLABORATOR",
                                                                            "order_by": {"field": "CREATED_AT",
                                                                                         "direction": "ASC"}}):
        print(response)

    print("False", "OWNER")
    for response in client.execute(query=UserRepositories(), substitutions={"user": "JialinC",
                                                                            "pg_size": 5,
                                                                            "is_fork": False,
                                                                            "ownership": "OWNER",
                                                                            "order_by": {"field": "CREATED_AT",
                                                                                         "direction": "ASC"}}):
        print(response)

    print("False", "COLLABORATOR")
    for response in client.execute(query=UserRepositories(), substitutions={"user": "JialinC",
                                                                            "pg_size": 5,
                                                                            "is_fork": False,
                                                                            "ownership": "COLLABORATOR",
                                                                            "order_by": {"field": "CREATED_AT",
                                                                                         "direction": "ASC"}}):
        print(response)

    # print("True", "OWNER")
    # for response in enterprise_client.execute(query=UserRepositories(), substitutions={"user": "jcui9",
    #                                                                         "pg_size": 5,
    #                                                                         "is_fork": True,
    #                                                                         "ownership": "OWNER",
    #                                                                         "order_by": {"field": "CREATED_AT",
    #                                                                                      "direction": "ASC"}}):
    #     print(response)
    #
    # print("True", "COLLABORATOR")
    # for response in enterprise_client.execute(query=UserRepositories(), substitutions={"user": "jcui9",
    #                                                                         "pg_size": 5,
    #                                                                         "is_fork": True,
    #                                                                         "ownership": "COLLABORATOR",
    #                                                                         "order_by": {"field": "CREATED_AT",
    #                                                                                      "direction": "ASC"}}):
    #     print(response)
    #
    # print("False", "OWNER")
    # for response in enterprise_client.execute(query=UserRepositories(), substitutions={"user": "jcui9",
    #                                                                         "pg_size": 5,
    #                                                                         "is_fork": False,
    #                                                                         "ownership": "OWNER",
    #                                                                         "order_by": {"field": "CREATED_AT",
    #                                                                                      "direction": "ASC"}}):
    #     print(response)
    #
    # print("False", "COLLABORATOR")
    # for response in enterprise_client.execute(query=UserRepositories(), substitutions={"user": "jcui9",
    #                                                                         "pg_size": 5,
    #                                                                         "is_fork": False,
    #                                                                         "ownership": "COLLABORATOR",
    #                                                                         "order_by": {"field": "CREATED_AT",
    #                                                                                      "direction": "ASC"}}):
    #     print(response)
