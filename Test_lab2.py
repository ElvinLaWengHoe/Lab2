import lab2

def test_find_min_max():
    input_arr = [5,67,32]

    expected_min_max_list = [5,67]

    result = lab2.find_min_max(input_arr)

    assert (result == expected_min_max_list)

def test_calc_average():
    input_arr = [5,67,32]

    expected_result = 34.666666666666664

    result = lab2.calc_average(input_arr)

    assert (result == expected_result)

def test_calc_median_temperature():
    input_arr = [5,36,67]

    expected_result = 36

    result = lab2.calc_median_temperature(input_arr)

    assert (result == expected_result)
