from fasthtml.common import serve

from app import *
from app.application import app


def main():
    if os.getenv('ENV') == 'dev':
        import debugpy
        debugpy.listen(("0.0.0.0", 5678))
        print("🔍 Debugger is available on port 5678. You can attach at any time.")

    print("🚀 Starting server...")
    serve()
