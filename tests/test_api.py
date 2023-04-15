import requests
import json

#Get all books
def test_get_all_books():
    url = "https://demoqa.com/BookStore/v1/Books"
    response = requests.get(url)
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    assert len(response.json()) > 0

#Add new book
def test_add_new_book():
    url = "https://demoqa.com/BookStore/v1/Books"
    headers = {"Content-Type": "application/json"}
    data = {
        "isbn": "9781449325862",
        "title": "Python Testing with pytest",
        "subtitle": "Simple, Rapid, Effective, and Scalable",
        "author": "Brian Okken",
        "published": "2017-03-28T00:00:00.000Z",
        "publisher": "O'Reilly Media",
        "pages": 200,
        "description": "The pytest testing framework helps you write tests quickly and keep them readable and maintainable—with no boilerplate code. Using a robust yet simple fixture model, it’s just as easy to write small tests with pytest as it is to scale up to complex functional testing for applications, packages, and libraries.",
        "website": "https://www.oreilly.com/library/view/python-testing-with/9781449325862/",
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    assert response.status_code == 201, f"Expected 201 but got {response.status_code}"
    assert response.json()["title"] == data["title"], "Unexpected title in response body"

#Find book by ISBN
def test_get_book_by_isbn():
    url = "https://demoqa.com/BookStore/v1/Book"
    params = {"ISBN": "9781449325862"}
    response = requests.get(url, params=params)
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
