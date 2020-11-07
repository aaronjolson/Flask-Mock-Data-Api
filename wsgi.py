import os
from .main import app

version = "1.0.0"
proc_name = "Flask_Mock_Data_API"

workers = 4

if __name__ == "__main__":
    app.run()
