from flask import Flask, render_template, request;
from flask_cors import CORS, cross_origin;

import secrets;
import joblib;
import os;
from flask_bootstrap import Bootstrap;

# Khởi tạo Flask Server Backend
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['TEMPLATES_AUTO_RELOAD'] = True


# Apply Flask CORS
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# ----------- Vi du -----------------------------------------------------------------------
@app.route('/home')
def index():
    username = 'Dorami chan'
    return render_template('app.html', username = username)

# ----------- Form ---------------------------------------------------------------------------

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class MyForm(FlaskForm):
    parents = StringField('Parents')
    has_nurs = StringField('Has Nurs')
    form = StringField('Form')
    children = StringField('Children')
    housing = StringField('Housing')
    finance = StringField('Finance')
    social = StringField('Social')
    health = StringField('Health')
    submit = SubmitField('Gửi Dữ Liệu')

@app.route('/form', methods=['GET', 'POST'])
@cross_origin(origins='*')
def train_():
    result = None
    form = MyForm()
    input_values = []
    # try:
    if form.validate_on_submit():
                # Thêm các giá trị từ biểu mẫu vào danh sách
                input_values.append(form.parents.data)
                input_values.append(form.has_nurs.data)
                input_values.append(form.form.data)
                input_values.append(form.children.data)
                input_values.append(form.housing.data)
                input_values.append(form.finance.data)
                input_values.append(form.social.data)
                input_values.append(form.health.data)

                input_values = [float(value) for value in input_values]

                print(type(input_values[-1]))

                # Nạp mô hình
                # Xác định đường dẫn tới tệp 'rf_model.pkl' trong thư mục cùng cấp
                model_path = os.path.join(os.path.dirname(__file__), 'model/rf_model.pkl')

                # Nạp mô hình từ đường dẫn
                rf_model = joblib.load(model_path)  # Thay 'joblib.load' bằng 'pickle.load' nếu bạn sử dụng thư viện pickle
                dudoan = rf_model.predict([input_values])
                if dudoan[0] == 1:
                      result = "not_recom"
                elif dudoan[0] == 2:
                      result = "recommended"
                elif dudoan[0] == 3:
                      result = "very_recom"
                elif dudoan[0] == 4:
                      result = "priority"
                elif dudoan[0] == 5:
                      result = "spec_prior"

            # Xử lý dữ liệu ở đây (ví dụ: tính toán kết quả)
            # Đoạn mã xử lý và gán kết quả vào biến result

    return render_template('form.html', form=form, result=result)
    
    # except FileNotFoundError:
    #     return "Mô hình không tồn tại. Vui lòng chạy mã huấn luyện trước."


#  --------------- VD: Add, minus -----------------------------------------------------------------------
# @app.route('/add', methods=['POST'])
# @cross_origin(origins='*')
# def add_process():
#       a = int(request.args.get('a'))
#       b = int(request.args.get('b'))
#       kq = a + b
#       return "Kết quả là: " + str(kq)

# @app.route('/minus', methods=['GET', 'POSR'])
# @cross_origin(origins='*')
# def minus_process():
#       return "Hàm trừ."

# @app.route('/viethoa', methods=['POST'])
# @cross_origin(origins='*')
# def viethoa_process():
#       a = request.form.get("nhapchuoi")
#       a_upper = a.upper()      
#       return a_upper



# Start Backend
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8888)

