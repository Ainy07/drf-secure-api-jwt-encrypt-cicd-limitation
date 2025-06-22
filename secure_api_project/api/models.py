from django.db import models
from cryptography.fernet import Fernet
import base64
import os

key = base64.urlsafe_b64encode(os.urandom(32))
cipher = Fernet(key)

class SecureData(models.Model):
    encrypted_text = models.BinaryField()

    def save_encrypted(self, text):
        encrypted = cipher.encrypt(text.encode())
        self.encrypted_text = encrypted
        self.save()

    def get_decrypted(self):
        return cipher.decrypt(self.encrypted_text).decode()
