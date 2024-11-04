from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Tunggu antara 1 hingga 5 detik sebelum request selanjutnya

    @task
    def get_users(self):
        self.client.get("/users")
    
    @task
    def get_user_by_id(self):
        user_id = 1  # ID contoh
        self.client.get(f"/users/{user_id}")
    
    @task
    def get_posts(self):
        self.client.get("/posts")
    
    @task
    def get_post_by_id(self):
        post_id = 1  # ID contoh
        self.client.get(f"/posts/{post_id}")
    
    @task
    def get_comments(self):
        self.client.get("/comments")
    
    @task
    def get_comment_by_id(self):
        comment_id = 1  # ID contoh
        self.client.get(f"/comments/{comment_id}")
    
    @task
    def get_todos(self):
        self.client.get("/todos")
    
    @task
    def get_todo_by_id(self):
        todo_id = 1  # ID contoh
        self.client.get(f"/todos/{todo_id}")