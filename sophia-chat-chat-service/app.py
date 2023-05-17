from flask import Flask, request

app = Flask(__name__)

@app.route('/file', methods=['POST'])
def upload_file():
    file = request.files['file']
    print(file)

    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run()