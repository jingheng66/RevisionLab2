import RevLab2 as temperature 

def test_find_min_max():
    assert temperature.calc_min_max_temperature([10, 20, 30, 40, 50]) == [10, 50]

def test_calc_average():
    assert temperature.calc_average_temperature([10, 20, 30, 40, 50]) == 30

def test_calc_median_temperature():
    assert temperature.calc_median_temperature([10, 20, 30, 40, 50]) == 30
