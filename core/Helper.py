import hashlib
import uuid

def random_str() -> str:
    """
    随机生成字符串
    :return:
    """
    only = hashlib.md5(str(uuid.uuid1()).encode("UTF-8")).hexdigest()
    return str(only)