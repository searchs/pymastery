from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"Took {t2 - t1} ms")
        return result

    return wrapper


@performance
def check_duration():
    for i in range(10000000):
        i * 5


check_duration()


# User authentication
"""Create an @authenticated decorator that only allows the function
run if user1 has 'valid' set to True 
"""
user1 = {"name": "Sofia", "valid": True}


def authenticated(fn):
    """Check user validity before allowing action"""

    def wrapper(*args, **kwargs):
        if args[0]["valid"]:
            return fn(*args, **kwargs)

    return wrapper


@authenticated
def message_friends(user1):
    """Send message relating to passed user"""
    return "message sent!"


message_friends(user1)


# Test
assert message_friends(user1) == "message sent!"
