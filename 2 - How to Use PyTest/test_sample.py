def test_example():
    assert 1+1 == 2
def test_name2(page):
    page.goto('https://google.com')
    assert "Google" in page.title()
    