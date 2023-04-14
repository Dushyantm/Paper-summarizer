from article import search_arxiv
from saving_file import save_results_to_file
import datetime


def search_papers(query: str, max_results: int = 10):
    results = search_arxiv(query, max_results)
    # save_results_to_file(results, str(query) + '.pdf')
    results_dict_list = [result.__dict__ for result in results]
    
    return results_dict_list

if __name__ == '__main__':
    query = input("Enter a search query: ")
    max_results = int(input("Enter maximum number of results wanted: "))
    results = search_papers(query, max_results)
    # print(results)
