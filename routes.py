from flask import Blueprint, Flask, render_template, jsonify
 
home_bp = Blueprint('home', __name__, template_folder='templates')
api_bp = Blueprint('api', __name__)
 
@home_bp.route('/')
def index():
    return render_template('index.html')


@home_bp.route('/home', methods=['GET'])
def home():
    return index()


@api_bp.route('/data/get-trend-data', methods=['GET'])
def customer_review_services():
    response = {
        'status': 'Success',
        'data': {}
    }
    labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    data = [15000, 18500, 22000, 19800, 25400, 28300, 16080]

    response['data']['labels'] = labels
    response['data']['data'] = data

    return jsonify(response)


@api_bp.route('/data/get-funnel-data', methods=['GET'])
def funnel_data():
    response = {
        'status': 'Success',
        'data': {}
    }
    labels = ['Website Visits', 'Browse Vehicles', 'Test Drive Book', 'Lead Generated', 'Deal Closed']
    data = [125480, 89200, 42600, 3240, 1296]

    response['data']['labels'] = labels
    response['data']['data'] = data

    return jsonify(response)

 
if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')