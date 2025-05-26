import os

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'data', 'uploads')

def process_uploaded_files(files):
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    file_paths = []
    for file in files:
        if file.filename == "":
            continue
        save_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(save_path)
        file_paths.append(save_path)
    return file_paths
