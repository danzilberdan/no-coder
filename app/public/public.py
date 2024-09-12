from fasthtml.common import *

from app.application import rt


@rt("/public/{fname:path}.{ext:static}")
def get(fname:str, ext:str): return FileResponse(f'app/public/files/{fname}.{ext}')
