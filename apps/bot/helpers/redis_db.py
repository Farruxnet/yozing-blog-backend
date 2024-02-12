from redis import Redis

redis_client = Redis(host='localhost', port=6379, password='redis123')


def get_otp_from_redis(otp: str) -> dict:
    redis_data = redis_client.hgetall(name=f'otp_{otp}')
    decoded_data = {key.decode(): value.decode() for key, value in redis_data.items()}
    redis_client.delete(f'otp_{otp}')
    return decoded_data


def save_otp_to_redis(random_otp: int, message: str):
    for i in redis_client.keys(pattern=f"otp_*_{message.chat.id}"):
        redis_client.delete(i.decode('utf-8'))
    key = f'otp_{random_otp}_{message.chat.id}'
    value = f'{random_otp}'
    redis_client.set(name=key, ex=60, value=str(value))
