def gen_id(val):
    l_1 = (val >> 16) & 0xffff
    r_1 = val & 0xffff
    for i in range(3):
        l_2 = r_1
        r_2 = l_1 ^ round((((1366 * r_1 + 150889) % 714025) / 714025.0) * 32767)
        l_1 = l_2
        r_1 = r_2
    return (r_1 << 16) + l_1


if __name__ == '__main__':
    record = set()
    for i in range(100):
        randoom_id = gen_id(i)
        assert i == gen_id(randoom_id)
        record.add(randoom_id)
    assert len(record) == 100
