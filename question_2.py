from flask import Flask, request


app = Flask(__name__)

"""
注册
1. 邮箱注册
涉及 api
    a. email_validity_checks：验证邮箱有效性，是否合法邮箱，是否已经被注册
    b. password_validity_checks：验证密码有效性，是否合乎强度要求
    c. signup_check/username：验证用户名有效性，是否已经注册
    d. email/code：发送邮箱验证码
    e. signup：注册


2. 手机短信验证
手机注册时，输入手机号与短信验证码即可。如果用户已经存在，登录成功；
如果此手机号未注册，创建新用户，新用户初始用户名为 gen_id(timestamp)，登录成功
涉及api
    a. phone_validity_checks：验证手机号合法性
    b. phone/code：发送短信验证码
    c. session?type=phone_login：注册登录


登录
1. 邮箱/用户名/手机号 + 密码 登录
涉及api：
    a. session?type=login：登录

2. 手机短信验证：同上

"""
@app.route('/email_validity_checks', methods=['POST'])
def email_validity_checks():
    """
    value
    """
    data = request.form.to_dict()
    pass


@app.route('/email/code', methods=['POST'])
def send_email_code():
    """
    value
    """
    data = request.form.to_dict()
    pass


@app.route('/password_validity_checks', methods=['POST'])
def password_validity_checks():
    """
    value
    """
    data = request.form.to_dict()
    pass


@app.route('/signup_check/username', methods=['POST'])
def signup_check_username():
    """
    value
    """
    data = request.form.to_dict()
    pass


@app.route('phone_validity_checks', methods=['POST'])
def phone_validity_checks():
    """
    value
    """
    data = request.form.to_dict()
    pass


@app.route('phone/code', methods=['POST'])
def send_phone_code():
    """
    value
    """
    data = request.form.to_dict()
    pass


@app.route('/signup', methods=['POST'])
def signup():
    """
    name、email、password、timestamp
    """
    data = request.form.to_dict()
    pass


@app.route('/session', methods=['POST'])
def login():
    """
    type：
        login：user、password、code、timestamp
        phone_login：phone、code、timestamp
    """
    data = request.form.to_dict()
    if request.args.get('type') == 'login':
        pass
    elif request.args.get('type') == 'phone_login':
        pass


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5002)
