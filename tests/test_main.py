def _get_decorated_lines(results):
    """Return the long, decorated lines."""
    return list(filter(lambda x: "=====" in x, results.stdout.__str__().split('\n')))


def test_it_does_not_seem_to_influence_results(tmp_tree_of_tests):
    """Check that the tests itself are not influenced."""
    results = tmp_tree_of_tests.runpytest('--vim-quickfix')
    results.assert_outcomes(passed=2, failed=1)


def test_it_shorten_the_lines(tmp_tree_of_tests):
    """Check that the output lines are indeed shorter."""
    results = tmp_tree_of_tests.runpytest('')
    decorated_lines = _get_decorated_lines(results)

    results_fixed = tmp_tree_of_tests.runpytest('--vim-quickfix')
    decorated_lines_fixed = _get_decorated_lines(results_fixed)

    for (index, _) in enumerate(decorated_lines):
        assert len(decorated_lines_fixed[index]) + 10 == len(decorated_lines[index])
