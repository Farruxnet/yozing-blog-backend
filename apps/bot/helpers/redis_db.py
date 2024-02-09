from redis import Redis

redis_client = Redis(host='localhost', port=6379, password='redis123')


def get_redis_client() -> Redis:
    return redis_client
