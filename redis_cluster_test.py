import time

from rediscluster import StrictRedisCluster


def now_time():
    t = time.time()
    return int(round(t * 1000))


def get_value():
    redis_nodes = [
        {'host': '192.168.1.100', 'port': 9261},
        {'host': '192.168.1.100', 'port': 9262},
        {'host': '192.168.1.100', 'port': 9263},
        {'host': '192.168.1.100', 'port': 9264},
        {'host': '192.168.1.100', 'port': 9261},
        {'host': '192.168.1.100', 'port': 9262},
        {'host': '192.168.1.100', 'port': 9263},
        {'host': '192.168.1.100', 'port': 9264}
    ]

    keys = ["test-key1", "test-key2",
            "test-key3", "test-key4"]

    redis_cluster_conn = StrictRedisCluster(startup_nodes=redis_nodes)
    total_spent = 0
    for key in keys:
        start = now_time()

        # has_key = redis_cluster_conn.exists(key)

        # if has_key:
        res = redis_cluster_conn.smembers(key)

        end = now_time()
        spent = end - start
        total_spent += spent
        print('spent : %s, key: %s, value : %s' % (spent, key, len(res)))

    print('total: %s' % total_spent)


get_value()
