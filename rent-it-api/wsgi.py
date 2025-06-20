import os

from rent_it_api_v1 import create_app

app = create_app()

if __name__ == "__main__":
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')