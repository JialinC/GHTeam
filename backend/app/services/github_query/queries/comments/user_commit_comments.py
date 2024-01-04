from backend.app.services.github_query.github_graphql.query import QueryNode, PaginatedQuery, QueryNodePaginator
import backend.app.services.github_query.utils.helper as helper


class UserCommitComments(PaginatedQuery):
    """
    UserCommitComments constructs a paginated GraphQL query specifically for 
    retrieving user commit comments. It extends the PaginatedQuery class to handle
    queries that expect a large amount of data that might be delivered in multiple pages.
    """
    def __init__(self):
        """
        Initializes the UserCommitComments query with specific fields and arguments 
        to retrieve user commit comments including pagination handling.
        """
        super().__init__(
            fields=[
                QueryNode(
                    "user",
                    args={"login": "$user"},
                    fields=[
                        "login",
                        QueryNodePaginator(
                            "commitComments",
                            args={"first": "$pg_size"},
                            fields=[
                                "totalCount",
                                QueryNode(
                                    "nodes",
                                    fields=["createdAt"]
                                ),
                                QueryNode(
                                    "pageInfo",
                                    fields=["endCursor", "hasNextPage"]
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    @staticmethod
    def user_commit_comments(raw_data: dict):
        """
        Extracts and returns the commit comments from the raw query data.

        Args:
            raw_data (dict): The raw data returned by the GraphQL query. It's expected
                             to follow the structure: {user: {commitComments: {nodes: [{createdAt: ""}, ...]}}}.
        
        Returns:
            list: A list of dictionaries, each representing a commit comment and its associated data.
        """
        commit_comments = raw_data["user"]["commitComments"]["nodes"]
        return commit_comments

    @staticmethod
    def created_before_time(commit_comments: list, time: str):
        """
        Counts how many commit comments were created before a specific time.

        Args:
            commit_comments (list): A list of commit comment dictionaries, each containing a "createdAt" field.
            time (str): The cutoff time as a string. All comments created before this time will be counted.

        Returns:
            int: The count of commit comments created before the specified time.
        """
        counter = 0
        for commit_comment in commit_comments:
            if helper.created_before(commit_comment["createdAt"], time):
                counter += 1
            else:
                break
        return counter
