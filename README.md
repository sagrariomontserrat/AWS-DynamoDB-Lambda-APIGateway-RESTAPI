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
17. Click on **Deploy**

## 🌐 API Gateway
1. In the search bar at the top of the AWS Management Console, type API Gateway and select **API Gateway from the dropdown**.


   










