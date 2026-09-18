"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000

def test_reject_negative_rates():
    with pytest.raises(ValueError):
        simulate(1000, -0.4)

def test_matches_law():
    N0 = 1000
    lam = 0.4
    dt = 0.05
    steps = 200
    t = steps * dt

    finals = [simulate(N0, lam, seed=i)[-1] for i in range(200)] #runs 200 times, each time grab final atom count
    average = np.mean(finals) #finds the average of atom counts

    expected = N0 * np.exp(-lam * t)
    assert average == pytest.approx(expected, rel=0.05) #relative difference