import time

import redis


def now_time():
    t = time.time()
    return int(round(t * 1000))


def get_value():
    r = redis.Redis(host='192.168.1.100', port=9261)

    keys = ["test-key1", "test-key2",
            "test-key3", "test-key4"]

    total_spent = 0
    for key in keys:
        start = now_time()

        res = r.smembers(key)

        end = now_time()
        spent = end - start
        total_spent += spent
        print('spent : %s, key: %s, res : %s' % (spent, key, len(res)))

    print('total: %s' % total_spent)


get_value()
