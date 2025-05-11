from flask import Flask, session, render_template, request, redirect, url_for, make_response
import hmac, hashlib, secrets

used_tokens = set()

with open('./static/seed.txt', 'r') as f:
    SEED = bytes.fromhex(f.read().strip())

def lcg_params(seed: bytes, session_id: str):
    m = 2147483693
    raw_a = hmac.new(seed, (session_id + "a").encode(), hashlib.sha256).digest()
    a = (int.from_bytes(raw_a[:8], 'big') % (m - 1)) + 1
    raw_c = hmac.new(seed, (session_id + "c").encode(), hashlib.sha256).digest()
    c = (int.from_bytes(raw_c[:8], 'big') % (m - 1)) + 1
    return m, a, c

def generate_round_digits(seed: bytes, session_id: str, round_index: int):
    LCG_M, LCG_A, LCG_C = lcg_params(seed, session_id)

    h0 = hmac.new(seed, session_id.encode(), hashlib.sha256).digest()
    state = int.from_bytes(h0, 'big') % LCG_M

    for _ in range(DIGITS_PER_ROUND * round_index):
        state = (LCG_A * state + LCG_C) % LCG_M

    digits = []
    for _ in range(DIGITS_PER_ROUND):
        state = (LCG_A * state + LCG_C) % LCG_M
        digits.append(state % 10)

    return digits

def reset_rng():
    session.clear()
    session['session_id'] = secrets.token_hex(16)
    session['round'] = 0

TOTAL_ROUNDS = 10
DIGITS_PER_ROUND = 7
FLAG = "TsukuCTF25{Tr4d1on4l_P4th_Trav3rs4l}"

app = Flask(__name__)
app.secret_key = secrets.token_bytes(16)

@app.route('/')
def index():
    reset_rng()
    return render_template('index.html')

@app.route('/flash')
def flash():
    session_id = session.get('session_id')
    if not session_id:
        return redirect(url_for('index'))

    r = session.get('round', 0)
    if r >= TOTAL_ROUNDS:
        return redirect(url_for('result'))

    digits = generate_round_digits(SEED, session_id, r)

    session['round'] = r + 1

    visible = (session['round'] <= 3) or (session['round'] > 7)
    return render_template('flash.html', round=session['round'], total=TOTAL_ROUNDS, digits=digits, visible=visible)

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        if not session.get('session_id') or session.get('round', 0) < TOTAL_ROUNDS:
            return redirect(url_for('flash'))
        token = secrets.token_hex(16)
        session['result_token'] = token
        used_tokens.add(token)
        return render_template('result.html', token=token)

    form_token = request.form.get('token', '')
    if ('result_token' not in session or form_token != session['result_token']
            or form_token not in used_tokens):
        return redirect(url_for('index'))
    used_tokens.remove(form_token)

    ans_str = request.form.get('answer', '').strip()
    if not ans_str.isdigit():
        return redirect(url_for('index'))
    ans = int(ans_str)

    session_id = session.get('session_id')
    correct_sum = 0
    for round_index in range(TOTAL_ROUNDS):
        digits = generate_round_digits(SEED, session_id, round_index)
        number = int(''.join(map(str, digits)))
        correct_sum += number

    session.clear()
    resp = make_response(
        render_template('result.html', submitted=ans, correct=correct_sum,
                        success=(ans == correct_sum), FLAG=FLAG if ans == correct_sum else None)
    )
    cookie_name = app.config.get('SESSION_COOKIE_NAME', 'session')
    resp.set_cookie(cookie_name, '', expires=0)
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
