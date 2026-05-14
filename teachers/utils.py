from django.db.models import Q
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)

from users.models import Teacher_profile


def search_query(query):

    vector = SearchVector("first_name", "last_name")
    query = SearchQuery(query)

    result = (
        Teacher_profile.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    result = result.annotate(
        headline_firstname=SearchHeadline(
            "first_name",
            query,
            start_sel='<span style="color: #E2725B;'
                      'font-style: italic;">',
            stop_sel="</span>",
        )
    )
    result = result.annotate(
        headline_lastname=SearchHeadline(
            "last_name",
            query,
            start_sel='<span style="color: #E2725B;'
                      'font-style: italic;">',
            stop_sel="</span>",
        )
    )

    return result