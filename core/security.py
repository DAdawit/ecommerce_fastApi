from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hasshed_password(password):
    return pwd_context.hash(password)
