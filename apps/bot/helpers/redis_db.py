from redis import Redis

redis_client = Redis(host='localhost', port=6379, password='redis123')


def get_otp_from_redis(otp: str) -> dict:
    redis_data = redis_client.hgetall(name=f'otp_{otp}')
    decoded_data = {key.decode(): value.decode() for key, value in redis_data.items()}
    redis_client.delete(f'otp_{otp}')
    return decoded_data
