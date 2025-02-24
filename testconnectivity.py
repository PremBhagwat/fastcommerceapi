from config_db import engine

try:
    with engine.connect() as conn:
        print("connection done")
except Exception as e:
    print(f"connection failed: {e}")