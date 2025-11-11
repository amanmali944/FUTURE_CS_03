from flask import Flask, render_template, request, send_file, redirect, url_for, flash
from werkzeug.utils import secure_filename
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from dotenv import load_dotenv
import os

# Load AES key from .env
load_dotenv()
print("[debug] Starting app.py")
aes_key_env = os.getenv("AES_KEY")
if not aes_key_env:
    raise RuntimeError("AES_KEY not set in environment (.env missing or AES_KEY not defined)")
AES_KEY = aes_key_env.encode()
if len(AES_KEY) not in (16, 24, 32):
    raise RuntimeError(f"AES_KEY must be 16/24/32 bytes long, got length={len(AES_KEY)}")

app = Flask(__name__)
app.secret_key = "your_secret_key"
UPLOAD_FOLDER = "uploads"
DECRYPT_FOLDER = "decrypted"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DECRYPT_FOLDER, exist_ok=True)

# AES encryption/decryption helper
def encrypt_file(file_data):
    cipher = AES.new(AES_KEY, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(file_data, AES.block_size))
    return cipher.iv + ct_bytes

def decrypt_file(enc_data):
    iv = enc_data[:16]
    cipher = AES.new(AES_KEY, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc_data[16:]), AES.block_size)

@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash("No file selected")
        return redirect(url_for('index'))
    file = request.files['file']
    if file.filename == '':
        flash("No file chosen")
        return redirect(url_for('index'))

    filename = secure_filename(file.filename)
    file_data = file.read()
    encrypted_data = encrypt_file(file_data)

    with open(os.path.join(UPLOAD_FOLDER, filename + ".enc"), 'wb') as f:
        f.write(encrypted_data)

    flash(f"File '{filename}' uploaded and encrypted successfully!")
    return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_file(filename):
    enc_path = os.path.join(UPLOAD_FOLDER, filename)
    with open(enc_path, 'rb') as f:
        enc_data = f.read()
    decrypted_data = decrypt_file(enc_data)

    temp_path = os.path.join(DECRYPT_FOLDER, filename.replace(".enc", ""))
    with open(temp_path, 'wb') as f:
        f.write(decrypted_data)

    return send_file(temp_path, as_attachment=True)

if __name__ == "__main__":
    print("[debug] Calling app.run(debug=True, use_reloader=False)")
    app.run(debug=True, use_reloader=False)
