import argparse

def _parse_console_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("search_query",
                        help="Keywords to be searched in papers.", 
                        type =str)
    parser.add_argument("max_papers",
                        help="Maximum number of papers to retrieve.", 
                        type = int)
    parser.add_argument("save_dir",
                        help="directory where to store summaries",
                        type=str)
    args  = parser.parse_args()
    return args.query, args.max_papers, args.save_dir