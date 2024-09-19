from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

file_tags = db.Table('file_tags',
    db.Column('file_id', db.Integer, db.ForeignKey('file.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

pond_tags = db.Table('pond_tags',
    db.Column('pond_id', db.Integer, db.ForeignKey('pond.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    path = db.Column(db.String(255), nullable=False)
    tags = db.relationship('Tag', secondary=file_tags, back_populates='files')
    folder_id = db.Column(db.Integer, db.ForeignKey('folder.id'), nullable=True)

class Folder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('folder.id'), nullable=True)
    parent = db.relationship('Folder', remote_side=[id], backref=db.backref('children', lazy='dynamic'))
    files = db.relationship('File', backref='folder', lazy='dynamic')

class Pond(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    tags = db.relationship('Tag', secondary=pond_tags, back_populates='ponds')

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    files = db.relationship('File', secondary=file_tags, back_populates='tags')
    ponds = db.relationship('Pond', secondary=pond_tags, back_populates='tags')