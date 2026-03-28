from locust import HttpUser, task, between
from bs4 import BeautifulSoup
import random

class SnapViewUser(HttpUser):
    wait_time = between(1, 3)
    
    def on_start(self):
        self.client.get("/login/")
        response = self.client.get("/login/")
        soup = BeautifulSoup(response.text, 'html.parser')
        csrf = soup.find('input', {'name': 'csrfmiddlewaretoken'})
        csrf_token = csrf['value'] if csrf else ''
        
        self.client.post("/login/", {
            "username": "valami",
            "password": "Semmi2002.",
            "csrfmiddlewaretoken": csrf_token
        }, headers={"Referer": f"{self.host}/login/"})
    
    @task(3)
    def view_home(self):
        self.client.get("/")
    
    @task(2)
    def view_photo(self):
        self.client.get("/photo/1/")
    
    @task(1)
    def view_upload_page(self):
        self.client.get("/upload/")
    
    @task(1)
    def sort_by_name(self):
        self.client.get("/?sort=name")
    
    @task(1)
    def sort_by_date(self):
        self.client.get("/?sort=date")