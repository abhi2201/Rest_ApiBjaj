from flask import Flask , render_template , request
from flask import send_file

app = Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return render_template('app.html')

@app.route('/bfhl', methods=['POST', 'GET'])
def bfhl():
	error=None
	if request.method== 'POST':
		arr =  request.form.get('array')
		print(arr)

		odd=[]
		even=[]

		li = list(arr.split(" "))
		print(li)
		isSuccess = "true"
		final=[]
		flag=0
		for i in li:
			try:
				x=int(i)
				if x%2==0:
					even.append(x)
				else:
					odd.append(x)
			except:
				flag=1
				isSuccess="false"
				break

		print(final)


		name = "abhishek_singh_22011998"
		if flag == 0:
			return render_template("submit.html",isSuccess=isSuccess, name=name, odd_string = '"odd":', even_string = '"even":', odd = odd, even=even)
		else:
			return render_template("submit.html",isSuccess=isSuccess, name=name, odd_string = "", even_string = "", odd = "", even="") 

if __name__ == "__main__":
    app.run(debug=True)