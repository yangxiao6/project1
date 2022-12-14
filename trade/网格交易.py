def use_round_func():
    i = 1.0001
    while i <= 1.001:
        i_ = round(i, 3)
        print(f"{i} :  {i_}")
        i += 0.0001


def use_float_func():
    i = 1.0001
    while i <= 1.001:
        i_ = '%.3f' % i
        i_ = float(i_)
        print(type(i_))
        print(f"{i} :  {i_}")
        i += 0.0001


use_float_func()
