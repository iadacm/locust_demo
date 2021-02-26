# locust_demo
how to use locust?

0. locust installed

1. run the server:
  python server.py
  
2. run locust
  locust --web-host 127.0.0.1 --host=http://localhost:8888
  
  (or, run in command mode)
  locust --web-host 127.0.0.1 -f locustfile.py -u 10 -r 2 -t 2 --headless

3. open locust control web
   http://localhost:8089
  run the test
