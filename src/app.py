from flask import Flask, request, jsonify, make_response
from binningApproach import DefaultBinningApproach 
from binningService import BinningService


app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Colplug Home Page"

@app.route('/binning')
def binning_api():
    """
    REST API to process get requests for binning service
    """
    bin_size = request.args.get('bin_size', type=int)
    min_val = request.args.get('min_val', type=int)
    max_val = request.args.get('max_val', type=int)

    input_params = ['bin_size', 'min_val', 'max_val']

    if bin_size is None or min_val is None or max_val is None:
        return make_response(jsonify({"error": "Please provide bin_size, min_val, and max_val parameters"}), 400)
    if bin_size <= 0:
        return make_response(jsonify({"error": "bin_size must be greater than 0"}), 400)
    if min_val >= max_val:
        return make_response(jsonify({"error": "min_val must be less than max_val"}), 400)

    # Provide
    approach = DefaultBinningApproach()
    service = BinningService(approach)
    response = service.process_binning_data(bin_size, min_val, max_val)
    
    return make_response(jsonify(response), 200)


if __name__ == '__main__':
    app.run(debug=True)


