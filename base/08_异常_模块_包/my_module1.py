__all__ = ['test_a']

def test_a(x, y):
    a = x + y
    print(f"我是模块1，方法:test_a，打印结果是{a}")
    return


def test_b(x, y):
    a = x - y
    print(f"我是模块1，方法:test_b，打印结果是{a}")
    return


def test(x, y):
    a = x + y
    print(f"我是模块1，方法:test，打印结果是{a}")
    return a
