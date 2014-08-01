from locust import HttpLocust, TaskSet

def version(l):
    l.client.get("/alpha/version")

def list_jobs(l):
    l.client.get("/alpha/jobs/paas-aurora/mkrastev")

def restart_job(l):
    l.client.put("/alpha/jobs/paas-aurora/mkrastev/devel/rhel59_world2/restart")

def cancel_update_job(l):
    l.client.delete("/alpha/jobs/paas-aurora/mkrastev/devel/rhel59_world2/update")

class UserBehavior(TaskSet):
    tasks = {
        version:		1,
        list_jobs:		100,
#        restart_job:		10,
#        cancel_update_job:	20
    }

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait=1000
    max_wait=3000