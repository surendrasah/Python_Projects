"""
Creating a flask api to retrieve the minimum number of machine operators MO required to help SO

"""


#Using flask to make an API
from flask import Flask,jsonify, request
import minimummachineoperators

#creating a Flask app
app = Flask(__name__)

#inputs
input1={
    "machines": [15, 10],
    "C": 12,
    "P":5
}


input2={
    "machines": [11,15,13],
    "C": 9,
    "P":5
}

input3={
    "machines": [61, 10],
    "C": 50,
    "P":5
}

input4={
    "machines": [40,10],
    "C": 10,
    "P":5
}


#type curl http://127.0.0.1:5000/input1 or input2 to see output

@app.route('/', methods = ['GET'])
def home():
    if(request.method == 'GET'):
        data = "use curl http://127.0.0.1:5000/input1 to see output"
        return jsonify({'data': data})


# function that will run when the endpoint input1 is hit.
@app.route('/input1', methods = ['GET'])
def machineoperators1():
    return jsonify({'machines':minimummachineoperators.machineoperators(input1['machines'],input1['C'],input1['P'])})



# function that will run when the endpoint input2 is hit.
@app.route("/input2", methods=["GET"])
def machineoperators2():
    return jsonify({'machines':minimummachineoperators.machineoperators(input2['machines'],input2['C'],input2['P'])})


# function that will run when the endpoint input3 is hit.
@app.route("/input3", methods=["GET"])
def machineoperators3():
    input=input3
    return jsonify({'machines':minimummachineoperators.machineoperators(input['machines'],input['C'],input['P'])})

# function that will run when the endpoint input3 is hit.
@app.route("/input4", methods=["GET"])
def machineoperators4():
    input=input4
    return jsonify({'machines':minimummachineoperators.machineoperators(input['machines'],input['C'],input['P'])})



@app.route("/post/input", methods=["POST"])
def machineoperators5():
    data= request.get_json()
    machines=data['machines']
    C=data['C']
    P=data['P']
    return jsonify({'machines':minimummachineoperators.machineoperators(machines,C,P)})


# main function
if __name__ == '__main__':
    app.run(debug = True)
