from unittest import TestLoader, TestSuite, TextTestRunner
from Tests.Scripts.test_Login import Login

import testtools as testtools

from Tests.Scripts.test_OrderPlacement import OrderPlacement
from Tests.Scripts.test_Registration import Registration

if __name__ == "__main__":

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(Registration),
        loader.loadTestsFromTestCase(Login),
        loader.loadTestsFromTestCase(OrderPlacement),
        ))

#run test sequentially using simple TextTestRunner
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)


# #run test parallel using concurrent_suite
    concurrent_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in suite))
    concurrent_suite.run(testtools.StreamResult())