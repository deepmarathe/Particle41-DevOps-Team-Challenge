# Particle41-DevOps-Team-Challenge
My submission repository for the Particle41 DevOps Team Challenge.


#### How to Run SimpleTimeService, Task1
You only need Docker installed as a part of the prerequisites.

##Step 1: Pull the app

docker pull drax23/task1simpletimeservice


##Step 2: Run the app
docker run -p 8000:8000 drax23/task1simpletimeservice


##Step 3: Open in browser
http://localhost:8000


You will see something like:

{
  "timestamp": "2025-06-23T15:45:12.123456",
  "ip": "127.0.0.1"
}


Thats it!!
