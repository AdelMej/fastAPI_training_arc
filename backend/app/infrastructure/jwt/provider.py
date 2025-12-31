from app.infrastructure.jwt.jose_encoder import JoseJWTService


def get_jwt_service():
    return JoseJWTService()
