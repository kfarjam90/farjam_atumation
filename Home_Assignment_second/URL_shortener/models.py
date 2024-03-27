from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///urls.db')
Base = declarative_base()

# Define the URL and Stats models
class URL(Base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True)
    shortcode = Column(String(6))
    url = Column(String, nullable=False)

    def __repr__(self):
        return f"URL(id={self.id}, shortcode='{self.shortcode}', url='{self.url}')"

class Stats(Base):
    __tablename__ = 'stats'

    id = Column(Integer, primary_key=True)
    shortcode = Column(String(6))
    created = Column(DateTime)
    last_redirect = Column(DateTime)
    redirect_count = Column(Integer, default=0)

    def __repr__(self):
        return f"Stats(id={self.id}, shortcode='{self.shortcode}', created='{self.created}', last_redirect='{self.last_redirect}', redirect_count={self.redirect_count})"

# Create the database tables
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)
