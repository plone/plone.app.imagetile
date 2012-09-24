import doctest
import unittest2 as unittest
from plone.testing import layered
from plone.app.imagetile.testing import PLONE_APP_IMAGETILE_FUNCTIONAL_TESTING

import pprint
import interlude

optionflags = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)
testfiles = [
    '../tile.txt',
]


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(doctest.DocFileSuite(test,
                                     optionflags=optionflags,
                                     globs={'interact': interlude.interact,
                                            'pprint': pprint.pprint,
                                            },
                                     ),
                layer=PLONE_APP_IMAGETILE_FUNCTIONAL_TESTING)
        for test in testfiles])
    return suite
