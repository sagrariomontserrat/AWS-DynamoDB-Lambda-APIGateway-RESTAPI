# RESTAPI (CRUD) - AWS Lambda, API Gateway, DynamoDB
## 🗃️Setup DynamoDB Table
1. Sign in to the AWS Management Console and open the **Amazon console**.
2. The starting point of this section is the Amazon Web Services Management Console, as shown below:
![Picture1](https://github.com/user-attachments/assets/27eaa43c-1848-4165-8738-940609928f54)
3. Go to **DynamoDB** in AWS Console, navigate to DynamoDB and click on **Create table.**
![Picture2](https://github.com/user-attachments/assets/52a6fe73-5385-4732-86ac-191358abec3f)
4. Write a **table name** "users" to identify your table.
5. **Partition key:** "user_id" (type: String).
6. Leave everything else as default and click **Create table**.
![Picture3](https://github.com/user-attachments/assets/64e9fdc3-b0df-4153-9df0-77476629a003)
7. In the left navigation pane, choose **Tables** and look for your table's name in the list of tables. If it is listed, then your table has been created successfully.
![Picture4](https://github.com/user-attachments/assets/f079b71d-d03a-46c4-8548-bd5b72ba690e)

## ƛ Lambda 
1. In the search bar at the top of the AWS Management Console, type Lambda and select **Lambda from the dropdown**.
2. On the **Lambda page** click the **Create function** button.
3. You'll have a few options. Choose **Author form scratch**
4. Choose a **name** for your Lambda function.
5. Choose the **runtime** for your function.
6. Choose **Create a new role with basic Lambda permissions**
![Picture5](https://github.com/user-attachments/assets/e296135b-7bb1-4fcd-b7e7-a3ad423981d3)
7. After filling out the required information, click the **Create function**.
8. Once you're on the details page of your Lambda function, click on the **Configuration tab** at the top.
9. On the left navigation pane click on **Permissions**.
10. Click on **Role name**
![Picture6](https://github.com/user-attachments/assets/b9996781-76ca-4a9e-9495-7a867bf21947)
11. Click the **Add permissions** button in the IAM role section.
12. Select **Attach policies** option.
13. Select the services and actions you want to allow **(CloudWatchLogsFullAccess, AmazonDynamoDBFullAccess)**.
14. Click Review policy and then **Add permissions** to apply it.
![Picture7](https://github.com/user-attachments/assets/336280f4-3825-4cc6-8464-c09b336aeab2)
15. On the left navigation pane click on **Code**.
16. You’ll write the Python code that allows you to perform CRUD operations on DynamoDB.
![Picture9](https://github.com/user-attachments/assets/d4d68e80-81e2-4fee-af85-8f68d4688794)
17. Click on **Deploy**.

## 🌐 API Gateway
1. In the search bar at the top of the AWS Management Console, type API Gateway and select **API Gateway from the dropdown**.
2. Choose **Create API**.
3. Choose an API type. **(RESTAPI)**.
![Picture10](https://github.com/user-attachments/assets/a8d175dd-4604-4126-be82-23cea82e23e0)
4. Choose **New API**.
5. Give the API name.
6. Set the **Endpoint type** to **Regional**.
7. Click **Create API**.
![Picture11](https://github.com/user-attachments/assets/42c13d76-e838-40e6-9486-e934b42c35bb)
8. Now that your API is created, you can add resources and methods.
9. The root resource (/) is the base path for your API. You can create methods here.  **(GET, POST, PUT, DELETE)**.
10. In the **Resources section** of your API, click on **Create Resource.**
11. Set the **Resource Name** to users and the Resource Path to /users.
12. Click **Create Resource.**
![Picture12](https://github.com/user-attachments/assets/ff49f76f-9628-4408-b548-770c9b758ccc)
13. Create Methods for /users.
14. Select the /users resource.
15. Choose **Create Method** and select **GET** from the dropdown.
16. Choose **Lambda Function** as the integration type.
17. Enable **Lambda Proxy Integration.**
18. Enter the name of your Lambda function and click **Save.**
![Picture13](https://github.com/user-attachments/assets/88370a95-465a-43bd-9a4f-c9f8fb13e75c)
19. Select the /users resource.
20. Click on **Create Method** and select **POST.**
21. Choose **Lambda Function** as the integration type.
22. Enable **Lambda Proxy Integration.**
23. Enter the name of your Lambda function and click **Save.**
![Picture14](https://github.com/user-attachments/assets/738a2a45-f2e4-40aa-b856-dd37eff00ce7)
24. Next, we create the /users/{user_id} resource to handle specific users.
25. Select the /users resource.
26. Click on **Create Resource.**
27. Set the Resource Name to user_id and the Resource Path to /users/{user_id}.
28. Click **Create Resource.*
29. Create Methods for /users/{user_id}.
-- GET Method for /users/{user_id}:
-- Select the /users/{user_id} resource.
-- Click on **Create Method** and **choose GET.**
-- Choose **Lambda Function** as the integration type.
-- Enable **Lambda Proxy Integration.**
-- Enter the name of your Lambda function and click **Save.**

DELETE Method for /users/{user_id}:

Select the /users/{user_id} resource.

Click on Actions > Create Method and choose DELETE.

Choose Lambda Function as the integration type.

Enable Lambda Proxy Integration.

Enter the name of your Lambda function and click Save.

OPTIONS Method for /users/{user_id}:

Select the /users/{user_id} resource.

Click on Actions > Create Method and choose OPTIONS.

Choose Mock Integration for CORS pre-flight.

Click Save.

PUT Method for /users/{user_id}:

Select the /users/{user_id} resource.

Click on Actions > Create Method and choose PUT.

Choose Lambda Function as the integration type.

Enable Lambda Proxy Integration.

Enter the name of your Lambda function and click Save.







   










