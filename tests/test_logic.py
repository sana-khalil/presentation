from presentation.logic import retrieveimage

def test_retrieveimage():
    actual = retrieveimage('data/blur.jpg')
    expected = '[[ 71  72  72 ... 219 218 218]' \
               '[ 70  71  72 ... 219 219 218]' \
               '[ 68  70  71 ... 220 219 218]' \
               '...' \
               '[ 49  47  44 ... 103 102 102]' \
               '[ 49  46  44 ... 102 102 103]' \
               '[ 48  46  43 ... 100 101 102]]'
    assert actual == expected
