Here's a polished and professional version of your READMEtask2.md, suitable for submission:

---

# Task 2: Deploying Infrastructure with Terraform

## Step 1: Log in to AWS

Before running the Terraform module, ensure you are authenticated with your AWS account.

Open your terminal (Command Prompt, PowerShell, or similar) and run:

```bash
aws configure
```

You will be prompted for the following:

- **AWS Access Key ID:**        `<enter your access key>`
- **AWS Secret Access Key:**    `<enter your secret key>`
- **Default region name:**      `us-east-1`
- **Default output format:**    `json`



To verify your credentials, run:

```bash
aws sts get-caller-identity
```

You should see your AWS account details.

---

## Step 2: Deploy the Infrastructure

Initialize and deploy the Terraform configuration with the following commands:

```bash
terraform init
terraform apply
```

When prompted to confirm the action, type:

```bash
yes
```

Terraform will perform the following actions:

- Create the networking resources
- Provision an EC2-based ECS cluster
- Pull your Docker image from Docker Hub
- Expose the service via an AWS Load Balancer

---

## Step 3: Access the Deployed Application

Once the deployment is complete, Terraform will output the URL for your application, similar to:

```
alb_url = task1-lb-xxxxxx.us-east-1.elb.amazonaws.com
```

Copy this URL and open it in your browser. You should see a confirmation that your containerized application is running successfully.

---

Let me know if you want this refined further or need it tailored for a specific audience!
