"""
Arquivo que contém o modelo para o banco de dados
ORM => Ferramenta que abstrai o sql usando a própria linguagem para interagir com o banco
"""
from ..Main import app
from abc import ABC, abstractmethod
from ..Main import database as db


class Representation(ABC):
    @abstractmethod
    def __repr__(self):
        ...


class User(Representation):
    __tablename__: str = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    def __init__(self, username: str, password: str, name: str, email: str) -> None:
        self.__username: str = username
        self.__password: str = password
        self.__name: str = name
        self.__email: str = email

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    def __repr__(self):
        return f"<User {self.__username}>"


class Post(Representation):
    __tablename__: str = "posts"
    content = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", foreign_keys=user_id)

    def __init__(self, content: str, id_user: str) -> None:
        self.__content : str = content
        self.__user_id: str = id_user


    @property
    def content(self):
        return self.__content

    @property
    def user_id(self):
        return self.__user_id

    def __repr__(self):
        return f"<id {self.user_id}>"


class Follow(Representation):
    __tablename__: str = "follow"
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    id_follower = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", foreign_keys=id_user)
    follower = db.relationship("User", foreign_keys=id_follower)

    def __init__(self, username: str, id_follower: str, id_user: str) -> None:
        self.__id: str = id
        self.__id_follower : str = id_follower
        self.__id_user: str = id_user

    @property
    def id(self):
        return self.__id

    @property
    def id_follower(self):
        return self.__id_follower

    @property
    def id_user(self):
        return self.__id_user

    def __repr__(self):
        return f"<id {self.__id}>"
