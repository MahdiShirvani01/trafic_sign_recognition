# download_data.py
import gdown
import os

def download_data():
    # Create data directory
    os.makedirs('data', exist_ok=True)
    
    # Download files using gdown
    gdown.download('https://drive.google.com/file/d/1-D8y7b2YXr5v9jiwvyQg_zwwhLubfCIB/view?usp=drive_link', 'data/test.p', quiet=False)
    gdown.download('https://drive.google.com/file/d/1ykq97xxkRozJNCB1aEVraPu9heE1A1Mq/view?usp=drive_link', 'data/valid.p', quiet=False)
    gdown.download('https://drive.google.com/file/d/1D4b2L_TtTdSfzc5OomfJnI226Qz9mK1U/view?usp=drive_link', 'data/train.p', quiet=False)

if __name__ == "__main__":
    download_data()
    
