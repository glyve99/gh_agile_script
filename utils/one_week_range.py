from datetime import datetime, timedelta

def one_week_range() -> datetime:
    '''
    One week range for fetching resources.
    '''
    
    return datetime.now() - timedelta(days=7)