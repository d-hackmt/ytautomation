## code owner SUNNY SAVITA SIR , 
# a code to fetch all the python library versions.

import importlib.metadata
packages = [
    # crosss fade 
'pydub',
'ffmpeg-python',

# beat matching 
'librosa',
'numpy',
'scipy',

#frontend
'streamlit',

# software
'fastapi',
'uvicorn[standard]',
'python-multipart',
'Pillow',
'requests',
'aiofiles',

# experiment notebook
'ipykernel',

'matplotlib',
    "uvicorn",
]
for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} (not installed)")

# # serve static & templates
# app.mount("/static", StaticFiles(directory="../static"), name="static")
# templates = Jinja2Templates(directory="../templates")