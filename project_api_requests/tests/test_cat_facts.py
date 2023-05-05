from unittest.mock import Mock
from lib.cat_facts import *

def test_using_API_to_get_the_cat_facts():
    response_mock = Mock
    response_mock.json.return_value = {"fact":"The term \u201cpuss\u201d is the root of the principal word for \u201ccat\u201d in the Romanian term pisica and the root of secondary words in Lithuanian (puz) and Low German\u00a0puus. Some scholars suggest that \u201cpuss\u201d could be imitative of the hissing sound used to get a cat\u2019s attention. As a slang word for the female pudenda, it could be associated with the connotation of a cat being soft, warm, and fuzzy."}
    assert response_mock.provide() == "Cat fact: cats are awesom"