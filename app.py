from flask import Flask, render_template, jsonify,request

app = Flask(__name__)


# 기본 index
@app.route('/')
def home():
   return render_template('index.html')

# API
@app.route('/api/list', methods=['POST'])
def show_recommend():
   # ajax 데이터 받아오기
   data_dic = {
      'cpu': request.form['Cpu'],
      'gpu': request.form['Gpu'],
      'purpose': request.form['Purpose'],
      'ssd': request.form['Ssd'],
      'Hdd': request.form['Hdd'],
      'price': request.form['Price'],
               }
   print(data_dic)
   return jsonify({'result': 'success', 'msg': 'list 연결되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)