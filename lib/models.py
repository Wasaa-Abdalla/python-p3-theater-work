from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Audition(Base):
    __tablename__ = 'auditions'

    id = Column(Integer(), primary_key=True)
    actor = Column(String())
    location = Column(String())
    phone = Column(Integer())
    hired = Column(Boolean())
    role_id = relationship('Role', backref=backref('audition'), cascade='all, delete-orphan')

    def __repr__(self):
        return f'Audition(id={self.id}, ' + \
            f'actor={self.actor}, ' + \
            f'role_id={self.role_id})'

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer(), primary_key=True)
    character_name = Column(String())
    audition_id = Column(Integer(), ForeignKey('auditions.id'))

    def __repr__(self):
        return f'Role(id={self.id}, ' + \
            f'character_name={self.character_name}, ' + \
                f'audition_id={self.audition_id})'
