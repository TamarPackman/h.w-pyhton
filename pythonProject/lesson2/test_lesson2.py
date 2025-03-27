import pytest
from library import  Library
from book import  Book
def test_add_book():
    l=Library()
    b=Book("jvort","libi klain")
    prevLen=len(l.books)
    l.add_book(b)
    newLen=len(l.books)
    assert  prevLen+1==newLen
@pytest.mark.add_user
def test_add_user():
    l=Library()
    try:
     l.add_user("")
    except ValueError as e:
        assert e.__eq__("Username must not be empty.")

def test_check_out_book():
    l=Library()
    b=Book("jvort","libi klain")
    try:
     l.check_out_book("tami",b)
    except ValueError as e:
        assert e.__eq__("Username must not be empty.")

#@pytest.mark.skip(reason="not work yet")
def test_return_book():
    l = Library()
    b = Book("jvort", "libi klain")
    l.add_user("tami")
    l.add_book(b)
    prevLen = len(l.checked_out_books)
    l.check_out_book("tami",b)
    l.return_book("tami",b)
    newLen=len(l.checked_out_books)
    assert prevLen == newLen

def test_search_book():
    l=Library()
    b = Book("jvort", "libi klain")
    l.add_book(b)
    book= l.search_books("jk")
    assert book==[]





