# Cyber Security Internship – Task 3  
## Secure File Sharing System using Flask and AES Encryption  

---

### Basic Information
- **Name:** Aman Mali  
- **Task:** Secure File Sharing System  
- **Internship:** Future Interns – Cybersecurity (2025)  
- **Tools / Framework:** Python Flask, PyCryptodome  
- **Date of Completion:** November 2025  

---

### Overview
This project involves creating a **secure web application** that enables users to upload and download files safely.  
To ensure **data confidentiality**, all files are encrypted before storage and decrypted upon download using the **AES (Advanced Encryption Standard)** algorithm.  

The main objective of this system is to simulate a **real-world secure file transfer mechanism** often used in corporate, legal, or healthcare environments where sensitive data must remain protected.

---

### ⚙️ Tools & Technologies Used
| Component | Description |
|------------|-------------|
| **Python Flask** | Backend framework handling routes, uploads, and downloads |
| **PyCryptodome** | Implements AES encryption/decryption |
| **dotenv** | Manages AES key securely via environment variables |
| **Werkzeug** | Secures filenames during upload |
| **HTML / CSS** | Frontend UI design |
| **VS Code** | Development environment |
| **Git & GitHub** | Version control and repository management |

---

### System Architecture & Workflow
1. **User uploads a file** via the Flask web interface.  
2. The file is immediately **encrypted using AES (CBC mode)**.  
3. The **encrypted file (.enc)** is stored securely in the `uploads/` folder.  
4. When a user requests to download, the file is **decrypted in memory**.  
5. The **original file** is returned securely to the user.  
6. AES key is stored in a `.env` file, preventing exposure in source code.  

---

### 🔐 Encryption Details
- **Algorithm:** AES (Advanced Encryption Standard)  
- **Mode:** CBC (Cipher Block Chaining)  
- **Key Size:** 128-bit (16 bytes)  
- **Padding:** PKCS7  
- **Initialization Vector (IV):** Randomly generated and prepended to ciphertext  

**Key Management**
- AES key is stored securely in a `.env` file (not uploaded to GitHub).  
  Example:
  ```bash
  AES_KEY=1234567890123456
