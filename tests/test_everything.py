"""Lets just dump them all into one place.

NOTE I expect that these tests will take several minutes because
of BRef rate limiting.

TODO these are totally wrong now.
"""

import mlb_graphical_standings as m

def test_division_info():
    assert m.extract_divisions(2014) == {
        'AL_East': ['BAL', 'NYY', 'TOR', 'TBR', 'BOS'],
        'AL_Central': ['DET', 'KCR', 'CLE', 'CHW', 'MIN'],
        'AL_West': ['LAA', 'OAK', 'SEA', 'HOU', 'TEX'],
        'NL_East': ['WSN', 'ATL', 'NYM', 'MIA', 'PHI'],
        'NL_Central': ['STL', 'PIT', 'MIL', 'CIN', 'CHC'],
        'NL_West': ['LAD', 'SFG', 'SDP', 'COL', 'ARI']
    }

    assert m.extract_divisions(1989) == {
        'AL_East': ['TOR', 'BAL', 'BOS', 'MIL', 'NYY', 'CLE', 'DET'],
        'AL_West': ['OAK', 'KCR', 'CAL', 'TEX', 'MIN', 'SEA', 'CHW'],
        'NL_East': ['CHC', 'NYM', 'STL', 'MON', 'PIT', 'PHI'],
        'NL_West': ['SFG', 'SDP', 'HOU', 'LAD', 'CIN', 'ATL']
    }

    assert m.extract_divisions(2024) == {
        'AL_East': ['NYY', 'BAL', 'BOS', 'TBR', 'TOR'],
        'AL_Central': ['CLE', 'MIN', 'KCR', 'DET', 'CHW'],
        'AL_West': ['HOU', 'SEA', 'TEX', 'OAK', 'LAA'],
        'NL_East': ['PHI', 'ATL', 'NYM', 'WSN', 'MIA'],
        'NL_Central': ['MIL', 'CHC', 'STL', 'CIN', 'PIT'],
        'NL_West': ['LAD', 'ARI', 'SDP', 'SFG', 'COL']
    }
