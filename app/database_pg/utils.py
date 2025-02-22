import os
from sqlalchemy import create_engine


def db_connect():
    db_connection = os.getenv("DB_CONNECTION")
    if db_connection is None:
        raise Exception("specify DB_CONNECTION in .env file")
    return create_engine(db_connection)


class Mixin:
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def as_clear_dict(self):
        _dict = {}
        for c in self.__table__.columns:
            if c.foreign_keys:
                continue
            val = getattr(self, c.name)
            if val:
                _dict[c.name] = val
        return _dict
