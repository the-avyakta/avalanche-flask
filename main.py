from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def handle_post_request():
    # Your POST request handling code here
    return 'POST request received successfully'

@app.errorhandler(404)
def not_found(error):
    return '404 Not Found', 404

if __name__ == '__main__':
    app.run()
