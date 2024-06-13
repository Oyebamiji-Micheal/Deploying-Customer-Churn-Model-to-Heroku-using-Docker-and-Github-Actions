<h1 align="center">Deploying Customer Churn Model to Heroku using Docker and Github Actions</h1>

<div align="center">

[![Language](https://img.shields.io/badge/Python-darkblue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Framework](https://img.shields.io/badge/sklearn-darkorange.svg?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/stable/index.html)
![build](https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat)
[![ML Tool](https://img.shields.io/badge/Heroku-945DD6.svg?style=flat&logo=iterative&logoColor=white)](https://www.heroku.com/)
[![ML Tool](https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![ML Tool](https://img.shields.io/badge/GitHub_Actions-2088FF.svg?style=flat&logo=github&logoColor=white)](https://docs.github.com/en/actions)

</div>

<p align="center">This repository contains the code and workflows for deploying a machine learning model that predicts customer churn, using Docker for containerization and GitHub Actions for continuous integration and deployment to Heroku</p>

<br />

<img src="images/application-interface.jpg" width="580" height="679">
 
You can view the deployed application here: <a href="https://customer-churn-551d7373243e.herokuapp.com">https://customer-churn-551d7373243e.herokuapp.com</a> <br/>
Note: This application is hosted on a student account. It will stop working when I exhaust my credits 😑

<h2>Overview</h2>
<p align="justify">
A few weeks ago, I built an <a href="https://github.com/Oyebamiji-Micheal/End-to-End-Customer-Churn-Prediction-using-MLflow-and-DVC">end to end machine learning project</a> that predicts customer churn using a dataset from <a href="https://www.kaggle.com/datasets/shubhammeshram579/bank-customer-churn-prediction">Kaggle</a>. The project was built using MLflow for model tracking and experiment management, DVC for data versioning, and Flask for serving the model. In this repository, I will be deploying the model to Heroku using Docker for containerization and GitHub Actions for continuous integration and deployment.</p>

<a id="customer_churn"></a>
<h2>Customer Churn and What it's all about</h2>
<p align="justify">
Customer churn refers to the phenomenon where customers stop doing business with a company or stop using its products or services. It is a critical metric for businesses, especially in industries with subscription-based models or recurring revenue streams.</p>

<img src="images/churn-image.jpg">

<p align="justify">Identifying customers who are likely to churn can help businesses take proactive measures to retain them, thereby reducing revenue loss and improving customer satisfaction.
</p>

<a id="data"></a>
<h2>Dataset</h2>
<p align="justify">
The dataset used for this project is obtained from <a href="https://www.kaggle.com/datasets/shubhammeshram579/bank-customer-churn-prediction">Kaggle</a>. It contains the following attributes:
</p>

- Customer ID: A unique identifier for each customer
- Surname: The customer's surname or last name
- Credit Score: A numerical value representing the customer's credit score
- Geography: The country where the customer resides (France, Spain, or Germany)
- Gender: The customer's gender (Male or Female)
- Age: The customer's age
- Tenure: The number of years the customer has been with the bank
- Balance: The customer's account balance
- NumOfProducts: The number of bank products the customer uses (e.g., savings account, credit card)
- HasCrCard: Whether the customer has a credit card (1 = yes, 0 = no)
- IsActiveMember: Whether the customer is an active member (1 = yes, 0 = no)
- EstimatedSalary: The estimated salary of the customer
- Exited: Whether the customer has churned (1 = yes, 0 = no)


<img src="images/prediction-result.jpg">