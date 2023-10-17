import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(50), unique=True)
    nombre_completo = Column(String(100))
    foto_perfil = Column(String)
    correo = Column(String)    
    biografia = Column(String)

    seguidores = relationship('Seguidores', back_populates='seguido')
    seguidos = relationship('Seguidores', back_populates='seguidor')

class Publicacion(Base):
    __tablename__ = 'publicaciones'

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    imagen = Column(String)
    pie_de_coto = Column(String, default="")    

    usuario = relationship('Usuario', back_populates='publicaciones')
    comentarios = relationship('Comentario', back_populates='publicacion')

class Comentario(Base):
    __tablename__ = 'comentarios'

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    publicacion_id = Column(Integer, ForeignKey('publicaciones.id'))
    texto = Column(String)
    

    usuario = relationship('Usuario', back_populates='comentarios')
    publicacion = relationship('Publicacion', back_populates='comentarios')

class Seguidores(Base):
    __tablename__ = 'seguidores'

    id = Column(Integer, primary_key=True)
    seguidor_id = Column(Integer, ForeignKey('usuarios.id'))
    seguido_id = Column(Integer, ForeignKey('usuarios.id'))
    

    seguidor = relationship('Usuario', foreign_keys=[seguidor_id], back_populates='seguidos')
    seguido = relationship('Usuario', foreign_keys=[seguido_id], back_populates='seguidores')


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
