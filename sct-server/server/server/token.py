__author__ = 'willispinaud'

from itsdangerous import URLSafeTimedSerializer

from server import cfg


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(cfg.SECRET_KEY)
    return serializer.dumps(email, salt=cfg.SECURITY_PASSWORD_SALT)


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(cfg.SECRET_KEY)
    try:
        email = serializer.loads(
            token,
            salt=cfg.SECURITY_PASSWORD_SALT,
            max_age=expiration
        )
    except:
        return False
    return email
