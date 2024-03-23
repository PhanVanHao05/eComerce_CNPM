from flask import Flask, render_template, request, redirect
import dao

app = Flask(__name__)


@app.route('/')
def index():
    #  từ điền - key value cho request / tham số truy vấn (query parameters)
    q = request.args.get('q')
    #  q là lấy chuỗi nhật từ client
    cate_id = request.args.get('category_id')
    # cate_id chứa id cho danh mục khi client click vào

    products = dao.load_products(q, cate_id)
    return render_template('index.html', products=products)


@app.route('/products/<int:id>')
def details(id):
    product = dao.get_product_by_id(id)
    return render_template('product-details.html', product=product)


@app.context_processor
def common_attributes():
    return {
        'categories': dao.load_categories()
    }


@app.route('/login', methods=['get', 'post'])
def login_my_user():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

    if username.__eq__('admin') and password.__eq__('123'):
        return redirect('/')
    return render_template('login.html')


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
