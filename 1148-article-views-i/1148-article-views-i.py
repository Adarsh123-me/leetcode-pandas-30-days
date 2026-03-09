import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    result = views[views["author_id"] == views["viewer_id"]]["author_id"].drop_duplicates()
    return result.to_frame(name="id").sort_values("id")