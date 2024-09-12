from fasthtml.common import *

with open(Path(__file__).parent.parent / "secret.key", "r") as f:
    secret_key = f.read()

app = FastHTML(hdrs=(Link(rel="stylesheet", href="public/app.css", type="text/css")),
               secret_key=secret_key)
rt = app.route
