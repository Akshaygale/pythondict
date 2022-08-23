from cProfile import run
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>This is Fibonacci Example</p>"

@app.route("/fibonacci/<int:num>")
def Fibonacci(num):
    First_val = 0
    Second_val = 1
    for n in range(0, num):
            if(n <= 1):
                next = n
            else:
                next = First_val + Second_val
                First_val = Second_val
                Second_val = next 
                data1={
                    "fibb":next
                }             
                return data1
            # print(next)



if __name__=="__main__":
    app.run(debug=True)

