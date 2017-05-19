"""Test simple1 example"""

# Copyright BBP/EPFL 2017; All rights reserved.
# Do not distribute without further notice.

import os
import shutil
import filecmp

import nose.tools as nt

from bluepymm import tools, main
from bluepymm import prepare_and_run_combos as mm
from bluepymm import select_combos as megate


def _test_megate_output():
    matches = filecmp.cmpfiles(
        'output_megate_expected', 'output_megate',
        ['combo_model.csv', 'extNeuronDB.dat'])

    if len(matches[0]) != 2:
        print('Mismatch in files: %s' % matches[1])

    nt.assert_equal(len(matches[0]), 2)


def test_simple1_git():
    """simple1: test with git repo"""

    with tools.cd('examples/simple1'):

        if os.path.exists('tmp'):
            shutil.rmtree('tmp')

        # Run mm
        args_list = ['simple1_conf_git.json']
        args = mm.parse_args(args_list)
        mm.run(args)

        # Test output db
        # Disabled for now, there are absolute paths in db
        """
        import pandas
        import sqlite3

        scores_sqlite_filename = 'output/scores.sqlite'
        exp_scores_sqlite_filename = 'output_expected/scores.sqlite'
        with sqlite3.connect(scores_sqlite_filename) as conn:
            scores = pandas.read_sql('SELECT * FROM scores', conn)

        with sqlite3.connect(exp_scores_sqlite_filename) as conn:
            exp_scores = pandas.read_sql('SELECT * FROM scores', conn)

        if not scores.equals(exp_scores):
            print "Resulting scores db: ", scores
            print "Expected scored db:", exp_scores

        nt.assert_true(scores.equals(exp_scores))
        """

        # Run megate
        args_list = ['simple1_megate_conf.json']
        args = megate.parse_args(args_list)
        megate.run(args)

        # Test megate output
        _test_megate_output()


def test_simple1():
    """simple1: test"""

    with tools.cd('examples/simple1'):
        if os.path.exists('tmp'):
            shutil.rmtree('tmp')

        # Run mm
        args_list = ['simple1_conf.json']
        args = mm.parse_args(args_list)
        mm.run(args)

        # Test output db
        # Disabled for now, there are absolute paths in db
        """
        import pandas
        import sqlite3

        scores_sqlite_filename = 'output/scores.sqlite'
        exp_scores_sqlite_filename = 'output_expected/scores.sqlite'
        with sqlite3.connect(scores_sqlite_filename) as conn:
            scores = pandas.read_sql('SELECT * FROM scores', conn)

        with sqlite3.connect(exp_scores_sqlite_filename) as conn:
            exp_scores = pandas.read_sql('SELECT * FROM scores', conn)

        if not scores.equals(exp_scores):
            print "Resulting scores db: ", scores
            print "Expected scored db:", exp_scores

        nt.assert_true(scores.equals(exp_scores))
        """

        # Run megate
        args_list = ['simple1_megate_conf.json']
        args = megate.parse_args(args_list)
        megate.run(args)

        # Test megate output
        _test_megate_output()


def test_simple1_from_main():
    """Test example simple1 from bluepymm/main.py interface.
    """
    with tools.cd('examples/simple1'):
        if os.path.exists('tmp'):
            shutil.rmtree('tmp')

        # Run mm
        args_list = ['mm', 'simple1_conf.json']
        main(args_list)

        # TODO: test output db

        # Run megate
        args_list = ['megate', 'simple1_megate_conf.json']
        main(args_list)

        # Test megate output
        _test_megate_output()
