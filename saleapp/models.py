from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from saleapp import db, app


class Category(db.Model):
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    price = Column(Float, default=0)
    image = Column(String(100), default='https://i.pinimg.com/564x/cb/23/35/cb2335f7fce923271c84f4b5dc83cf94.jpg')
    category_id = Column(Integer, ForeignKey(Category.id), default=False)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    # #  c1 = Category(name='Mobile')
    # #  c2 = Category(name='Tablet')
    # #  c3 = Category(name='Laptop')
    # #  db.session.add_all([c3])
    #
    # import json
    #
    # with open('data/products.json', encoding='utf-8') as f:
    #     products = json.load(f)
    #     for p in products:
    #         prod = Product(**p)
    #         db.session.add(prod)
    #
    # db.session.commit()
    app.app_context().push()
