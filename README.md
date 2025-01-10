*NAME:* SAMPANGI NAGAVARDHAN 
*COMPANY:* CODTECH IT SOLUTIONS  
*ID:* CT08DS540
*DOMAIN:* Cyber Security and Ethical Hacking  
*DURATION:* December 2024 to January 2025  
## **Task 1: File Integrity Checker**

## **Task 4: Advanced Encryption Tool**

### **Description**
A Python tool to encrypt and decrypt files using AES-256 encryption.

### **Features**
- AES-256 encryption for robust security.
- Password-based key derivation using PBKDF2.
- Supports file encryption and decryption.

### **Requirements**
- Python 3.x
- `cryptography` library

### **Setup**
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install cryptography
   ```

### **Usage**
1. **Encrypt File**:
   ```bash
   python encryption_tool.py --encrypt "file.txt" --password "securepassword"
   ```
2. **Decrypt File**:
   ```bash
   python encryption_tool.py --decrypt "file.txt.enc" --password "securepassword"
   ```

### **Example**
```bash
python encryption_tool.py --encrypt "document.pdf" --password "mysecurekey"
python encryption_tool.py --decrypt "document.pdf.enc" --password "mysecurekey"
```

---

### **General Notes**
- All scripts include logging and error handling for robust functionality.
- Follow security best practices when using these tools.
- Only use tools in environments where you have permission to do so.
