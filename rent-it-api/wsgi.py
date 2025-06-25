"""Provides the WSGI entry point for running the rent-it-api application."""

import os

from rent_it_api import create_app

app = create_app()

if __name__ == "__main__":
    server_port = os.environ.get('PORT', '8090')
    app.run(debug=False, port=server_port, host='0.0.0.0')