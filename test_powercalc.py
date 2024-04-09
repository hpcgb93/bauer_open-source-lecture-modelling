# testfunction

from Power_Calculations import apparent_power


def test_apparent_power():
    assert apparent_power(3, 4, 5, 6, 5, 4, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2)[0] == 62.05
    assert apparent_power(3, 4, 5, 6, 5, 4, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2)[1] == 39.0
