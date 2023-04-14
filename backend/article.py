import arxiv


def search_arxiv(query,max_results):
    search = arxiv.Search(query=query, max_results=max_results, sort_by=arxiv.SortCriterion.SubmittedDate)
    summaries = []
    for result in search.results():
        summaries.append(result)
    return summaries
