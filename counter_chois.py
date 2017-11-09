from collections import Counter
import numpy as np




def counter_rand(map_num, cho_data, cho_counter, end_cho):
    """

    :param map_num:
    :param cho_data:
    :param cho_counter:
    :param end_cho:
    :return:
    """
    choise_data = cho_data
    for _ in map_num:

        try:
            cho_num = np.random.choice(choise_data)
            cho_counter[cho_num] += 1
            yield cho_num
            if cho_counter[cho_num] >= end_cho:
                choise_data.remove(cho_num)
        except ValueError:
            raise ValueError('计数器的截止数太小！')


if __name__ == '__main__':
    map_num = [i for i in range(1, 101)]
    cho_data = [i for i in range(1, 6)]
    cho_counter = Counter()
    end_cho = 20
    rt = [i for i in counter_rand(map_num, cho_data, cho_counter, end_cho)]

    print(sorted(rt))
    # print(rc)
