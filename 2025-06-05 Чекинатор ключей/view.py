from app import app
from flask import render_template, request, send_file
from cypher import generate_rsa_keys, encrypt_rsa, decrypt_rsa
from io import BytesIO
import zipfile


@app.route('/login')
def login():
    author = '1149817'
    return author

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cypher', methods=['POST'])
def cypher():
    text = request.form.get('text', '').encode('utf-8')
    priv_key, pub_key = generate_rsa_keys()
    encrypted = encrypt_rsa(text, pub_key)

    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as zf:
        zf.writestr('secret', encrypted)
        zf.writestr('key', priv_key)
    zip_buffer.seek(0)

    return send_file(
        zip_buffer,
        mimetype='application/zip',
        as_attachment=True,
        download_name='rsa_encrypted.zip'
    )

@app.route('/decypher', methods=['GET', 'POST'])
def decypher():
    if request.method == 'GET':
        return render_template('decrypt.html')

    key_file = request.files['key']
    secret_file = request.files['secret']

    private_key_pem = key_file.read()
    encrypted_data = secret_file.read()

    # import base64
    # print(f"Encrypted data: {base64.b64encode(encrypted_data).decode('utf-8')}")
    # print(f"Private key: {private_key_pem.decode('utf-8')}")

    try:
        decrypted_text = decrypt_rsa(encrypted_data, private_key_pem)
        return decrypted_text
    except Exception as e:
        raise e

'''
It isn't just RSA, it is RSA/ECB/OAEP

Message:
PX7jUDl54hE8PzIi2ve4FoBogMYmshVSlS9GK+RkmxXErFoX0A55YVZKuMWjFd/xSFkfzvQhi0Fi3b0IsiU6KaoG0+05cs1mITj1XZfHBSkv5fWHKwlQEeLbGIXOeny8fprpzbXxOhyIAMsw5SKsKW6wcxdQsgRXC8L6JMIWXCHnHwyIhN/XOSCo5e0zr5lWMWkpIewp1gMvHTx0brF6nW54Liri9tuB5GUZEf0iYqfrgyG0Bk9O51U5UX6KGQ3Nyo2+uuo/S3Nlt7inY3xm77hPR6OIr4DXRpVCJS97CesZDu9DFnnkGLRdlTyCPi5YctBsMZyqCz53vYBrgGiNAg==

Private key:
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAuKCRusSoAIP8IWvlsyEgcTgvI56TMdFlDOzAEdRzmqIRmCcM
P5q4/aYmv3HJDsTn19e1jrh7xGlSUEfnjyRopojmODpzUDB8Ul59p39sXhgpFUgb
ClTPjKPvf2yYtDvGLNNK/3XmfvFP9UjKfADGrm9+GZjNCUUafNOzWtQHnxf2C9u6
Ws0JIkolneQy/zMDuCNYm0H9nt7RzfnYOq//z2Kn1F9FE6fRl6KqdJxnrX60BieT
Mt7MU6aGOvOZe/0JgSA/6C9k2G4J7K4q/zcqQIQe9vnZmKFGaFushm+fDjdT8zgi
mo18PuxNfAzyajobweoFxVXMXA44lQrARpbKQQIDAQABAoIBACo9glnquE015S94
UhtDjvqYUiCiHSceszHb0K3Dn5dXURMwi9rZeU1/AAp46/kXD7wQPBelGZv8RLrd
WJslR1QiqhlfNha4oRjvSWxS+OYmPPADiTw53ypcL2VF4UILEvIafWQpA00zxIln
1/u66bnrBDyy+uYOC1tXzAcRz5SUMMaNRfHuPB9swdSsnT2wRwjvqpRUX/yKZb2C
t3z+IbPRqeApzx+GsMjn9Ps9UyHQyk6pTt7qf51UhPT3kD8284PSahHzs2OmTphE
SJSetl/WPeOX177rG6DNh0Ry/9bHiO7RBMr+3Kwy/QwfAXT+9woZ0Rp781AKPAA3
EM/ow8kCgYEA8hZ3tiZ+dBMYoOxvM9HdeZwebwNo9bJT+O5WIdEvWc9/FzCKm6yi
cuNWU5z6fqR+RJA3jBYq9oXAwSEAK/8ZU8/hhg7HYSoQTaHNFugQlUgsJPgiFbhS
HtAu7uQ/TM4xkDs4Y2CB3TMWyggzYVfkbomQvq7XunthlfbLMv8M9acCgYEAwzzB
z0pCqf9M0IJcWBc3EWnLR9bDrwYT6IxzGrTwkgZAR4AEEedQfO5nWfah+OTgIVd8
LM57hImRLtRIOmQCkO/fLz2HeZoNyxF/TRm5S2h4y+ZdMFBmMc5P6TSbQ8aJyB4i
LH8y7hzPlbPFqouVXDSLNtQpN9CqymRIWCFNDdcCgYAFydG88jitz9MT7fNOuuLf
yILVxrAYx9XIKvK2RkkqjZKNXGTECiGsO5FR2HwI0SgPvZ8GY3VNha8xLvfRFX1m
ip7q1Kmhwh63rHm55XyYBSzBCYnPGSQlhnbI0X5N+NQojbHwdltEjbcqx31rA237
0qA6XvXbiJ2xtz/ujTijGwKBgFFUrRQSRmUU4kX2GEvmF92cKb+aetgdewuj/otA
lvrtubdPX+KpbsEse0dh06WgirG5BRSRS6kxuZY9fn08jkkcc+f1BMumXlqaxmIy
9hqwwamHJIjs5TWYUXe/n3KDcYA49Vl9/5Rr0hn10sEx9p17kgbcKPOEbLF1RyHX
dYbvAoGANJtBBePgmZSl+BvXSJ8PpEH+qwdxGQlof0IOSNYdvT+eW0P6KiK5nNo0
RS1qccontBudaN/rw04hlgxB/5bpQdX1+cQcqsK0jpmiH9uXNZ/o2tk0M721Dhrf
YkyYfPU3ENcS9Mx6Q5LJWOo5AZQSmwFHv8aIkLTaMQWAiFmrH4A=
-----END RSA PRIVATE KEY-----

'''
