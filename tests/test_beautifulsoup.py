from usefulpackages.beautifulsoup import get_movies_list

def test_type():
    assert type(get_movies_list()) == list
