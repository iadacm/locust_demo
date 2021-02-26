# locustfile.py

'''
执行顺序：
Locust setup → 
  TaskSet setup → 
  TaskSet on_start → 
  TaskSet task1, 2, 3... → 
  TaskSet on_stop → 
  TaskSet teardown → 
Locust teardown
'''


from locust import HttpUser, TaskSet, task
from locust.exception import RescheduleTask


class UserBehavior(TaskSet):
    @task
    def sleep(self):
        url = "/sleep"
        self.client.get(url)
        #print('visit url: %s' % url)

    @task
    def sleep2(self):
        url = "/sleep2"
        self.client.get(url)
        #print('visit url: %s' % url)


class WebsiteUser(HttpUser):
    # task_set = UserBehavior
    tasks = [UserBehavior]
    min_wait = 0  # ms
    max_wait = 1


# locust --web-host 127.0.0.1 --host=http://localhost:8888
'''
作者：PegasusWang
链接：https://zhuanlan.zhihu.com/p/46147994
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
