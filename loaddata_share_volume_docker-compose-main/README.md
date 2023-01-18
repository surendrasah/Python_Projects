# dataload_and_apigetrequest
Please use the below steps to load the data and run the flask program

docker build  -t osmwebapi .

docker run -p 5000:5000 osmwebapi

This flask api will run:

Running on http://172.17.0.2:5000

go to the browser and run the below:
http://172.17.0.2:5000/row/82a69eb5b7f8166a

[50.66396595000001, 7.15051185, null, "Bonn", 53177.0, "66", "DE", 82.8, null, null, 0.0, 44.0, 39.4, 116292019.0, 1.0, "way", 0.7310513447432763, 5.334963325183375, 0.0, null, 0.0, null, 6.0, 293.6, 0.0, null, 0.0, null, 4.0, 207.8, 113433.9, 0.0, null, null, 0.0, null, null, null, 3.0, 399.5, 0.0, null, 2.0, 1.0, 0.0, 0.0, 0.0, null, 1.0, 255.5, 0.0, null, 1.0, 221.8, 2.0, 293.4, 0.0, null, 1.0, 313.1, 0.0, null, 0.0, null, 2.0, 211.5, 7.0, 78.6, 1.0, 272.8, "82a69eb5b7f8166a", 0.4779727458953858, 1.4903185367584229, 0.0005040168762207, 0.0722262859344482, 2.041021585464477, "Weißdornweg", null]


or use the terminal and run the below.

curl http://172.17.0.2:5000/row/82a69eb5b7f8166a
