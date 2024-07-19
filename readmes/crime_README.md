# final-project-chicago-crime
By Harsh Vardhan Pachisia

May 2024

## Overview

The goal of this project is to analyze reported incidents of crime in the City of Chicago from 2001 to the present, utilizing a comprehensive dataset that contains over 10 million rows and 22 columns. This data, sourced from the Chicago Police Department's CLEAR (Citizen Law Enforcement Analysis and Reporting) system, includes information such as incident type, location (at the block level), and date of occurrence. Through this project, I aim to understand crime patterns, trends, and correlations, which can help in effective resource allocation, policy-making, and enhancing community resilience.

## The social science problem

Crime is a complex social phenomenon that affects the quality of life and economic development of communities. Understanding crime patterns is crucial for law enforcement and community organizations to effectively combat and prevent crime. This project focuses on identifying trends and hotspots of crime in Chicago, exploring socio-economic factors that may influence crime rates, and evaluating the impact of external factors like the COVID-19 pandemic on criminal activities. The insights gained can inform targeted interventions and public safety strategies, making them more data-driven and efficient.

## Why large-scale computing methods?
The volume, variety, and complexity of crime data necessitate the use of scalable computing methods. Traditional data processing tools are insufficient for handling datasets of this magnitude with the required speed and efficiency. Large-scale computing methods allow for the management and analysis of big data in a way that is both time-efficient and computationally feasible. These methods enabled me to perform extensive data cleaning, integration, exploratory data analysis (EDA), and complex model training across the crimes dataset which was too big for my laptop RAM to handle, making it a good use case for large-scale computing.

## Large scale methods employed

### Data integration and management
I used PySpark, an interface for Apache Spark, which allows for fast cluster computing and is particularly adept at processing large datasets. The initial stage involved using a Python script to upload multiple datasets into an AWS S3 bucket, which is stored [here](https://github.com/macs30123-s24/final-project-chicago-crime/blob/main/data_collection/launch_and_upload.py). These datasets included:

1. Crime data from the Chicago Police Department
2. Socio-economic indicators such as poverty and income levels
3. COVID-19 case data by community area
4. Community names

This integration allows for a holistic analysis that considers various potential influences on crime rates. I also created a teardown script stored [here](https://github.com/macs30123-s24/final-project-chicago-crime/blob/main/data_collection/teardown.py) to delete the data following the completion of the analysis.

### Exploratory Data Analysis (EDA)
After cleaning and integrating the data, I conducted extensive EDA using PySpark to explore trends over time, differences between community areas, and the prevalence of different types of crimes, stored [here](https://github.com/macs30123-s24/final-project-chicago-crime/blob/main/eda/crimes_eda.ipynb) Notably:

- Crime rates have generally decreased over time, with significant drops during the COVID-19 pandemic.
 ![image](https://github.com/macs30123-s24/final-project-chicago-crime/assets/30920386/9705e63e-27ea-486b-ac4e-d64fcb2eb946)

- Theft and battery are the most common crime types.
![image](https://github.com/macs30123-s24/final-project-chicago-crime/assets/30920386/33de08e6-a0a6-466c-a950-ed2485bc6033)

- Areas like Austin show higher crime rates, which prompts a deeper examination of regional disparities.
![image](https://github.com/macs30123-s24/final-project-chicago-crime/assets/30920386/5892ae10-d2e0-4c58-833e-082fe2bc0abe)

### COVID-19 Impact Analysis

I then wanted to understand the effects of the COVID-19 pandemic on crime rates in Chicago. The integration of COVID-19 case data allowed for this exploration of how the pandemic influenced crime dynamics across different community areas and crime types. I found that there was a sharp decline in overall crime rates during the early stages of the pandemic, likely due to lockdown measures and reduced public presence. However, the impact varied by type of crime:

![image](https://github.com/macs30123-s24/final-project-chicago-crime/assets/30920386/5afd843b-6c27-489b-b172-eb5bac48d050)

We can see a clear effect of COVID-19 on monthly trends in the 10 top crime types (by count) in Chicago. All crimes in general plummet initially. We see a clear fall in 'Theft' as the largest crime type upon the onset of COVID-19 as people would be in lockdown. As time goes on, it rises again and by 2022 is getting back to the levels of pre-COVID times. Interestingly, narcotics also saw a rapid fall on the set of the pandemic due to the lockdown and don't seem to have recovered to pre-Covid levels. Battery, as expected, falls initially but then sees a quick jump back up to its pre-Covid levels. Interestingly, criminal damage follows pretty much the same pattern before and after COVID.

![image](https://github.com/macs30123-s24/final-project-chicago-crime/assets/30920386/96fca4af-f48f-41f8-8f0b-2a2bd85a871c)

We see a very clear relationship between number of crimes and COVID cases in each neighborhood. If the number of crimes increases, the number of cases seems to increase as well.

This aspect of the analysis highlights the importance of considering public health crises in crime trend analysis and the potential for these methods to inform responses to future emergencies. The notebook is stored [here](https://github.com/macs30123-s24/final-project-chicago-crime/blob/main/eda/impact_of_covid_on_crime.ipynb).

### Machine Learning Models

The models were created in PySpark partitioning the data into 15 partitions in an EMR cluster. 

#### 0. Feature Engineering
I conducted extensive feature engineering on factors I thought could affect crime rates such as getting month, the hour of the day, season, the yearly change in crime rate based on community, duration since previous crime at the block level, etc. The PySpark notebook for this is stored [here](https://github.com/macs30123-s24/final-project-chicago-crime/blob/main/ml_models/feature_engineering_0.ipynb).

#### 1. Predicting Crime Type
Research question: How can various environmental, temporal, and community-related factors be used to predict the primary type of crime in a given location, and what insights does this provide into the patterns of criminal activity in urban environments like Chicago? I used a random Forest Classifier for this Crime Type Prediction. This model predicted the primary type of crime based on environmental, temporal, and community-related factors, achieving weighted precision and recall of 82%, and an F1 score of 81%. Significant features included the description of the crime and geographic location. The PySpark notebook for this is stored [here](https://github.com/macs30123-s24/final-project-chicago-crime/blob/main/ml_models/ml_model_1_primarytype.ipynb).
 
#### 2. Predicting Arrests
Research Question: What factors predict the likelihood of an arrest during a crime? I used a random forest classifier for this prediction. This model predicted the likelihood of an arrest, achieving an accuracy of 87%. It highlighted the importance of the location and type of crime, along with socio-economic conditions. The PySpark notebook for this is stored [here](https://github.com/macs30123-s24/final-project-chicago-crime/blob/main/ml_models/ml_model_2_arrest.ipynb).

#### 3. Predicting Change in Yearly Crime Rate

Research Question: Can socio-economic indicators and crime history predict the yearly crime rate change in a community? I used linear regression for this prediction. The predicted changes in crime rates used socio-economic and historical crime data, showing moderate accuracy (18.7%) but also indicating the need for more comprehensive data to improve predictions. The PySpark notebook for this is stored [here](https://github.com/macs30123-s24/final-project-chicago-crime/blob/main/ml_models/ml_model_3_crime_rate.ipynb).

### Conclusion

The use of PySpark and AWS EMR (Elastic MapReduce) cluster with 15 partitions ensured that the analysis was scalable and efficient. This setup allowed for the processing of large volumes of data across multiple nodes, significantly reducing processing time and facilitating more complex analyses without performance degradation. The application of large-scale computing methods to social science research problems like crime analysis offers a powerful tool for uncovering insights that can drive public policy and community interventions. By leveraging high-performance computing environments and sophisticated data analysis techniques, this project demonstrates how big data can be harnessed to address critical societal challenges effectively.
