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
 
<h2>Overview</h2>
<p align="justify">
Some times back, I built an <a href="https://github.com/Oyebamiji-Micheal/End-to-End-Customer-Churn-Prediction-using-MLflow-and-DVC">end to end machine learning project</a> that predicts customer churn using a dataset from <a href="https://www.kaggle.com/datasets/shubhammeshram579/bank-customer-churn-prediction">Kaggle</a>. The project was built using MLflow for model tracking and experiment management, DVC for data versioning, and Flask for serving the model. In this repository, I will be deploying the model to Heroku using Docker for containerization and GitHub Actions for continuous integration and deployment.</p><br>

