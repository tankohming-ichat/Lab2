import Lab2 as Lab2

print("Test_Lab2")


def test_min_max():
    input_arr = [1,2,3,4,5,6,7,8,9,10]
    result = Lab2.calc_min_max(input_arr)
    test_result = [1,10]
    assert (result == test_result)


def test_calc_average():
    input_arr = [1,2,3,4,5,6,7,8,9,10]
    result = Lab2.calc_average(input_arr)
    test_result = 5.5
    assert (result == test_result)


def test_calc_median_temp():
    input_arr = [1,2,3,4,5,6,7,8,9,10]
    result = Lab2.calc_median_temperature(input_arr)
    test_result = 5.5
    assert (result == test_result)
