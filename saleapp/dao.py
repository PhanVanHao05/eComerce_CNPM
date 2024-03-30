
from saleapp.models import Category, Product
from saleapp import app


#  doc du lieu
def load_categories():
    return Category.query.all()
    #  with open('data/categories.json', encoding='utf-8') as f:
    #     return json.load(f)


# loc du lieu
def load_products(q=None, cate_id=None, page=None):
    query = Product.query

    if q:
        query = query.filter(Product.name.contains(q))

    if cate_id:
        query = query.filter(Category.id.__eq__(cate_id))

    if page:
        page_size = app.config['PAGE_SIZE']
        start = (int(page) - 1) * page_size
        query = query.slice(start, start + page_size)

    return  query.all()



    # with open('data/products.json', encoding='utf-8') as f:
    #     products = json.load(f)
    #
    #     if q:  # nếu q khác none
    #         products = [p for p in products if p['name'].find(q) >= 0]
    #         # Nếu q có chứa name trong product thì sẽ truyền vào biến p và sau vòng lập sẽ truyền vào products
    #
    #     if cate_id:
    #         products = [p for p in products if p['category_id'].__eq__(int(cate_id))]
    #
    #     return products


def get_product_by_id(product_id):
    return Product.query.get(product_id)
    # with open('data/products.json', encoding='utf-8') as f:
    #     products = json.load(f)
    #
    #     for p in products:
    #         if p['id'] == product_id:
    #             return p


# if __name__ == '__main__':
#     print(load_categories())
