import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        return result['encoding']

if __name__ == "__main__":
    file_path = "recommendations/data/data.csv"
    file_encoding = detect_encoding(file_path)
    print(f"Dosyanın encoding'i: {file_encoding}")
