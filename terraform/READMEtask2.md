???? Step 1: Login to AWS
Before running the Terraform module, you will need to log in to your AWS account.

In your command prompt or CMD, enter:

bash
Copy
Proofread
aws configure
You'll be asked for:

pgsql
Copy
Rework
AWS Access Key ID:        <enter your access key>
AWS Secret Access Key:    <enter your secret key here>
Default region name:      us-east-1
Default output format:    json
✅ Done! You are now signed in to AWS.

You can check that it did work by running:

bash
Duplicate
Rephrase
aws sts get-caller-identity
This should show your AWS account details.

⚙️ Step 2: Deploy Infrastructure
Now deploy all using these two commands:

bash
Copy
Rephrase
terraform init
terraform apply
When it asks to confirm, type:

bash
Duplicate
Revise
yes This will:

Network and build

Launch EC2-based ECS cluster

Pull your Docker image from Docker Hub

Expose it with a Load Balancer

???? Step 3: Check the Output

Once ready, Terraform will provide a web URL:

bash

Copy Proofread alb_url = task1-lb-xxxxxx.us-east-1.elb.amazonaws.com Copy that URL and enter it into your browser. ✅ You will see something like: This indicates that your container is running flawlessly on AWS!
