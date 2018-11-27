from mc_random import RandomSample
from datetime import datetime


def test_full_implementation():
    date = datetime(2009, 1, 15, 16, 16, 16)
    sample = RandomSample(date=date)
    assert sample.s_e == 285351376
    assert sample.seed == 1774249844
    assert sample.j_times(sample.s_e) == 77
    assert sample.rng_array() == [1773883525, 1376260681, 324244626, 616012910,
                                  1753573598, 238867782, 591860039, 64148416,
                                  12989333, 1236571744, 150838841, 1379547554,
                                  1594841833, 363535288, 643814074, 1662338174,
                                  1843118480, 1301824472, 2024723015,
                                  1640100338, 1715924041, 1979383646,
                                  1293133612, 504407049, 925629865, 879056303,
                                  257361492, 1402037236, 1031539864, 981619081,
                                  81117341, 2036123857]
    assert sample.next_x(sample.rng_array()[0]) == 1548645074
    assert sample.next_y(sample.seed) == 1530261067
    assert sample.stat_sample[0] == 874583987


def test_seed_1():
    date = datetime(2009, 1, 15, 16, 16, 16)
    sample = RandomSample(date=date)
    assert sample.s_e == 285351376
    assert sample.seed == 1774249844


def test_seed_2():
    date = datetime(2009, 7, 15, 8, 8, 8)
    sample = RandomSample(date=date)
    assert sample.s_e == 300960488
    assert sample.seed == 150009464


def test_seed_3():
    date = datetime(2010, 1, 15, 16, 16, 16)
    sample = RandomSample(date=date)
    assert sample.s_e == 316887376
    assert sample.seed == 1593377912


def test_x_generator():
    x = 1
    for _ in range(10000):
        x = RandomSample.next_x(x)
    assert x == 1919456777


def test_y_generator():
    y = 1
    for _ in range(10000):
        y = RandomSample.next_y(y)
    assert y == 2006618587


def test_samples_sorted():
    sample = RandomSample(seed=1774249844)
    assert sample.samples_sorted == [[8, 13, 70, 105, 146, 159, 177, 208, 260,
                                      274, 275, 281, 405, 417, 424, 457, 460,
                                      472, 488, 512, 518, 560, 565, 570, 608,
                                      652, 706, 708, 734, 743, 746, 765, 769,
                                      830, 923, 931, 991, 1007, 1026, 1082,
                                      1222, 1385, 1397, 1517, 1523, 1556,
                                      1564, 1570, 1664, 1725, 1760, 1794,
                                      1804, 1826, 1871, 1991, 2009, 2014,
                                      2109, 2175, 2191, 2228, 2250, 2269,
                                      2286, 2311, 2522, 2523, 2565, 2644,
                                      2646, 2686, 2692, 2704, 2765, 2773,
                                      2829, 2865, 2906, 2956], []]


def test_double_samples():
    sample = RandomSample(single=False)
    assert len(sample.samples[0]) == len(sample.samples[1])
