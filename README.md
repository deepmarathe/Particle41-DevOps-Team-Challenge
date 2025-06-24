
# Particle41-DevOps-Team-Challenge

My submission repository for the Particle41 DevOps Team Challenge Task1.

---

## How to Run SimpleTimeService (Task 1)

You only need Docker installed as a prerequisite.

### Step 1: Pull the app

```bash
docker pull drax23/task1simpletimeservice
```

### Step 2: Run the app

```bash
docker run -p 8000:8000 drax23/task1simpletimeservice
```

### Step 3: Open in your browser

Visit: [http://localhost:8000](http://localhost:8000)

You will see something like:

```json
{
  "timestamp": "2025-06-23T15:45:12.123456",
  "ip": "127.0.0.1"
}
```

---

That’s it!
