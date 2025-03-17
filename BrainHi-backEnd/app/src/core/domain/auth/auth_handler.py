
import time
from typing import Dict

import jwt
from decouple import config

from src.core.domain.dtos.user_dto import UserDTO


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


# function used for signing the JWT string
def signJWT(user: UserDTO) -> str:
    payload = {
          "id": user.id,
           "name": f"{user.firstName} {user.lastName}",
           "iat": time.time(),
           "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}