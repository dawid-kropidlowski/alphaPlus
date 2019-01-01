import pytest

from webscraper import QuoteRetrieval


def test_quoteretrieval_initializer_start_date():
    start_date = "wrong_data_type"
    with pytest.raises(ValueError):
        test_quote_retrieval_object = QuoteRetrieval(start_date=start_date)
