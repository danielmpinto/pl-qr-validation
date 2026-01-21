import json
import time
import cv2
import hashlib
import base64
from pyzbar.pyzbar import decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# load essential files
FILES = {
    "seed": "/grade/serverFilesCourse/seed.txt",
    "img":  "/grade/student/qrcode.jpg"
}

# set the tolerance (seconds)
tolerance = 60 

# decrypts and checks if it`s a valid QR code
def grade():
    seed = open(FILES["seed"]).read().strip()
    key = hashlib.sha256(seed.encode()).digest()
    cipher = AES.new(key, AES.MODE_ECB)

    img = cv2.imread(FILES["img"])
    bruteqr = decode(img)
    try:
        payloadqr = bruteqr[0].data.decode('utf-8')
        brutedata = base64.b64decode(payloadqr)
        decryptedqr = unpad(cipher.decrypt(brutedata), AES.block_size)
        decryptedqrstring = decryptedqr.decode('utf-8')
        
        timestamp = decryptedqrstring
        
        try:
            timestamp_qr = int(timestamp)
        except ValueError:
             return {"score": 0.0, "message": f"Invalid QR Code {decifrado_str}"}

        now = int(time.time())
        difference = now - timestamp_qr
        
        print(f"DEBUG time: Server={now}, QR={timestamp_qr},  Diff={difference}s", flush=True)

        if difference > tolerance:
            return {
                "score": 0.0, 
                "message": f"Expired QR Code. Delayed {difference} seconds (tolerance is {tolerance}s)."
            }
        
    except ValueError:
        return {"score": 0.0, "message": "The Seed is different."}
    except Exception as e:
        return {"score": 0.0, "message": f"Error while processing the QR Code {str(e)}"}
    return {
        "score": 1.0, 
        "message": f"Success."
    }

if __name__ == "__main__":
    result = grade()

    with open('/grade/results/results.json', 'w') as f:
        json.dump(result, f)







