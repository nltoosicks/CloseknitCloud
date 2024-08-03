from app import create_app, db
from app.models import User

# Uncomment these imports if Photo and Video models exist in your models.py
# from app.models import Photo, Video

app = create_app()

with app.app_context():
    db.create_all()
    print("Database tables created.")
