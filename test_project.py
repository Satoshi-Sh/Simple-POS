from .project import *
import pytest 

def test_check_argv():
    # no arguments
    with pytest.raises(SystemExit) as e:
         check_argv(['read_menu.py'])
    assert e.type == SystemExit
    assert e.value.code == 1

    # invalide file format
    with pytest.raises(SystemExit) as e:
         check_argv(['read_menu.py', 'sushiya.csv'])
    assert e.type == SystemExit
    assert e.value.code == 1

    # file not found
    with pytest.raises(SystemExit) as e:
         check_argv(['read_menu.py', 'curry.json'])
    assert e.type == SystemExit
    assert e.value.code == 1
    
    # valid command
    assert check_argv(["read_menu.py","sushiya.json"]) == True

def test_chunks():
    lst = [1,2,3,4,5]
    assert chunks(lst,2) == [[1,2],[3,4],[5,'']]
    assert chunks(lst,3) == [[1,2,3],[4,5,'']]

def test_read_menu():
    assert read_menu('test.json') == ["Milk: $2.0", "Apple: $1.0"]
