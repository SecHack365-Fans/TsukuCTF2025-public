import base64
from Crypto.Hash import SHAKE128
from kyber_py.ml_kem import ML_KEM_768
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = "A" * 262 + """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
xUg="""

key = base64.b64decode(key)

ciphertext = bytes.fromhex("9956e487373793da71f9e70ea79a13a471bf7d512cb8b438c61532984a5309ed6ab6e663b615ff05b0ce792584db86dd82ca63092db11bd86b231daeb6fe5bd9e81c9dc27fcf84e71b843c2f7ed9048c9f2abd44e1244b8f9abf52b04651d4e4bbb40cd075b66b7ecf5bbd67082d9451c66cc5ffb9416b79db1eeece91173d0d11232d3e2ae3d59a50018b29553d6d2393ac4224a1fd94fa2a5e3d7d03b426ab7280385532724e19be44fc8bcdd4ea75853fd738163826e9a5359c6d5760c0e5de5907fa2b32256363114b3b4a785ea13e7273fbd8ffec00633523983e1bf9e3eab1b4cc86e9c22d104e3bc747a8179e70161ed21bdff6372324d0f726cea443b0f268e0df7f233efb2f51969115f00ba4af5ca69f0c1c65ca85cbad582d3ceb3c829615c1396808eb0da192560343f7c8bb5b71fca15b6c3bdcc5ea416148f569bb4d46f170f267356a91d4b6c1aa53fab54a788a549eedb7e349b332c417ea0000766bcb00150e02a0eb18b0f997be1badbbb62980ba4ae434c44560e01c75459e99799afaa07fcb880d619ccd19b98b1d1ac1b748ca89db0b019ddaccd21007ffc6965fe33434c91d91d64df237affd68133de514870159a8ef2a044d97ee1bc3b124bd3533aee83fc335b926b290e4d34c834a19ef80732f920783342e4f81721bde62e92334aaa67300ca301e1ccda61177e984d29629d2abc110bb90129697cceaedd268d121e34122952db4fce7af54dd0cffbcdd8ba63f4fe7c9d6d2244fcdbebe29a8b4e55384cd9b561a563a5f45a4f71cbbee5ec25b9fbcb47b112da7571cc3d021af31049b69f182b4ba7f230259a045c2b08bad89419ae37b1590ff405194f4b987d33e61435a40ffc1a9f9d9f0f5e9915ddbc5b7f0e4cc72d188c6c12593b38d96f98e7d4dfbcada0202a2b32226f9e111cc22c73a7d55e154d05115beab3b700fe62dbda9f86b5d8a4f5a758e4b913c3f96f11bc8768df25a851b0c817140d76cf75e5b045677b74208202c1827e66f4b81d5cd3fb93cc71dc7704f744dd278fd765959206fa0bb0b844db07ee040bc8d5563b797c8ecffb545e8c22dec89973f482ac6a29757cf5d51d2abe8f5abf074df8dac19a8d3b5804fe82a90694ba44a730ae12be00ff3dbfb1a55c3bda2bd93421dfd9f72025cf79bd8d6c5f8ff6d93895fd9743621eb141c00550a63b48f483ba5a67dd2b2ceeb4c126979a73433812a328405ee8402cc40b0b57cb8fd2c01496be77206a460cec5bca75a4d447665e0f150776b6966c3965bab258df823dba65fd9def5501623e88bc2e7cf4036792b4904a4932595a813f7c8e2b6e108d64e49d7ba5ea2949a40b2373596aec716375c2b5387e670cfe944db49b8e2eea00237216634c57a17fc1eb968158ebc502a599399a59a8eed3e11b9e02a12c3616b818d6c3d9d081d730d2ef62ee9b7337b995308c8b58baac95b38db76b9ea653f624b4d3e9ee1db51bc0204cc553763589d5a861510489141c71424c538592e8f7c75a55103a353")
encrypted_flag = bytes.fromhex("bed3b7d98a1058fe7059c15bffac13205a39bc22263ef9110b5bde66f10c847fbe2eae728a1a427d99bbee0b48c9fd76")


n = 256
q = 3329
k = 3

def sampleNTT(B):
    ctx = SHAKE128.new()
    ctx.update(B)
    j = 0
    a = []
    while j < 256:
        C = ctx.read(3)
        d1 = C[0] + 256 * (C[1] % 16)
        d2 = (C[1] // 16) + 16 * C[2]
        if d1 < q:
            a.append(d1)
            j += 1
        if d2 < q and j < 256:
            a.append(d2)
            j += 1
    return a

def BitsToBytes(b):
    B = []
    for i in range(len(b) // 8):
        x = 0
        for j in range(8):
            x += b[i * 8 + j] << j
        B.append(x)
    return bytes(B)

def BytesToBits(B):
    b = []
    for i in range(len(B)):
        for j in range(8):
            b.append((B[i] >> j) & 1)
    return b

def ByteEncode(F):
    b = []
    for i in range(256):
        x = F[i]
        for j in range(12):
            b.append((x >> j) & 1)
    B = BitsToBytes(b)
    return B

def ByteDecode(B):
    b = BytesToBits(B)
    F = []
    for i in range(256):
        x = 0
        for j in range(12):
            x += b[i * 12 + j] << j
        assert x < q
        F.append(x)
    return F

def bitrev(i):
    bin_i = bin(i & (2**7 - 1))[2:].zfill(7)
    return int(bin_i[::-1], 2)

def inv_NTT(f):
    i = 127
    l = 2
    while l <= 128:
        s = 0
        while s < 256:
            zeta = pow(17, bitrev(i), q)
            i = i - 1
            for j in range(s,s + l):
                t = f[j]
                f[j] = t + f[j + l]
                f[j + l] = zeta * (f[j + l] - t)
            s += 2 * l
        l *= 2
    for i in range(256):
        f[i] = (f[i] * 3303) % q
    return f

s_enc = key[98:1250]
t_enc = key[1250:2402]
rho = key[2402:2434]

A = [[0] * k for _ in range(k)]
for i in range(k):
    for j in range(k):
        A[i][j] = sampleNTT(rho + bytes([j, i]))


s = [ByteDecode(s_enc[0:384]), ByteDecode(s_enc[384:768]), ByteDecode(s_enc[768:1152])]

X = 66

for i in range(X):
    s[0][i] = 0

t = [ByteDecode(t_enc[0:384]), ByteDecode(t_enc[384:768]), ByteDecode(t_enc[768:1152])]

PR.<x> = PolynomialRing(GF(q))
R.<z> = PR.quotient_ring(x^n + 1)

for i in range(k):
    for j in range(k):
        A[i][j] = R(inv_NTT(A[i][j]))

for i in range(k):
    s[i] = R(inv_NTT(s[i]))
    t[i] = R(inv_NTT(t[i]))

A = matrix(R, A)
s = vector(R, s)
t = vector(R, t)

Y = 132
C = 30000

M = matrix(ZZ,Y + X+1,Y + X+1)

for i in range(X):
    a = [0] * 256
    a[i] = 1
    a = R(inv_NTT(a))
    a = vector(R, [a,0,0])
    M[i,:Y] = C * vector(ZZ,(A * a)[0].list()[:Y])

M[:X,Y:Y+X] = identity_matrix(ZZ,X,X)
M[X:Y+X,:Y] = C * q * identity_matrix(ZZ,Y,Y)
M[Y+X,:Y] = C * vector(ZZ, (A * s - t)[0].list()[:Y])
M[Y+X,Y+X] = C * 10000

M = M.LLL()


s0 = ByteDecode(s_enc[0:384])

for i in range(X):
    s0[i] = int(M[-1,Y + i]) % q

dk = ByteEncode(s0) + key[98 + 384:]

shared_secret = ML_KEM_768.decaps(dk, ciphertext)

flag = unpad(AES.new(shared_secret, AES.MODE_ECB).decrypt(encrypted_flag), 16)
print(flag.decode())