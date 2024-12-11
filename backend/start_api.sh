#! /bin/bash

pip install pandas==2.2.3
pip install fastapi==0.115
pip install uvicorn==0.32
echo "----- RUN model -----"
python3 model_api.py --host 0.0.0.0 --port 8888
