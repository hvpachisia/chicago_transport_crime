# Chicago Transport & Crime: An in-depth analysis

## Introduction
Welcome to the Chicago Transport and Crime Analysis repository. This project brings together three comprehensive studies that analyze various aspects of transport and crime in Chicago. Each study is designed to showcase different technical skills and tools, ranging from big data processing and machine learning to data visualization and interactive application development.

## Projects Overview

1. UChicago Lyft Program Analysis

- **Objective**: To evaluate the impact of UChicago's free Lyft program on student travel behavior.
- **Technologies Used**: GCP, PySpark, Big Data, Python.
- **Key Skills**: Big data processing, exploratory data analysis (EDA), supervised and unsupervised machine learning.

2. Chicago Crime Analysis

- **Objective**: To analyze crime data across Chicago.

- **Technologies Used**: PySpark, AWS.

- **Key Skills**: Big data processing, cloud computing.

3. Visualizing University of Chicago Crime and Campus Transportation

- **Objective**: To scrutinize crime in Hyde Park and campus transits.

- **Technologies Used**: R, Data Visualization, RShiny.

- **Key Skills**: R programming, data visualization, interactive application development.


## Repository Structure
The repository is organized to reflect the various stages of data analysis and skills demonstrated across the projects. Below is an overview of the main directories and their contents:

- ``data_collection/``: Scripts and tools for collecting and processing raw data for all projects.
- ``eda/``: Exploratory data analysis notebooks and scripts.
- ``ml/``: Machine learning models and scripts for both supervised and unsupervised learning.
- ``data_viz/``: Data visualization scripts and RShiny applications.
- ``final_outputs/``: Final reports, summaries, and key visualizations from each project.

# Detailed Project Descriptions

## The UChicago Lyft Ride Smart Program: Effects on Ridesharing

### Business/Research Question

How much did UChicago’s Lyft Ride Program impact ridesharing in Hyde Park and is it worth continuing?

![image](https://github.com/abejburton/bdp-rideshare/assets/30920386/67041b2d-2d5b-4f96-91fd-444b23d2c28b)

### Data
Raw Datasets:
1. [Transport Network Providers Ridesharing Dataset](https://data.cityofchicago.org/Transportation/Transportation-Network-Providers-Trips-2018-2022-/m6dm-c72p): each row is one ride from 2018-2023 (84.8 GB)
2. Daily Weather (1 GB)

Processed Dataset:
1. In program Dataset (rides in Hyde Park, Woodlawn, Kenwood): 10 GB
2. Other parts of Chicago: 74 GB

### Project Architecture
![image](https://github.com/abejburton/bdp-rideshare/assets/30920386/7d378c06-82ee-4e48-a593-2e1e63cdb904)

## Findings

### Unsupervised ML (clustering)
![image](https://github.com/abejburton/bdp-rideshare/assets/30920386/2d053141-5312-4c0c-ae0f-54f1dcc1ff11)
- The program did not affect where people were calling rideshares from in Hyde Park.
- On average, trip duration increased post-program
- On average, number of trips increased post-program
- On average, fare  increased post-program
- More late-night trips were taken post-program
- Marked increase in the proportion of rides taken at the end of month

### Supervised ML (linear regression with elastic net)
Showcase the impact of the Lyft program on daily ridership counts within the program area (Hyde Park, Kenwood, Woodlawn) by predicting how behavior would have been without the program (predict counter-factual)

![image](https://github.com/abejburton/bdp-rideshare/assets/30920386/def04be5-a3a8-402d-8c87-ed336d158771)

- There was a clear increase in ridership counts after the program was implemented
- Usage increase breaks down to about 4 rides per student per month

### Conclusion
- More rides are taken later in the evening supporting a safety-motivated hypothesis for Lyft usage
- Lyft Ride Smart amplify student habits - similar destinations to campus, shopping, and apartments with higher frequency and more trips taken at night
- Rides are not for superfluous spending - they facilitate necessary student trips in a wider range of times with increased safety. This is clarified with our clustering analysis

## Analysis Crime in Chicago

### Overview

The goal of this project is to analyze reported incidents of crime in the City of Chicago from 2001 to the present, utilizing a comprehensive dataset that contains over 10 million rows and 22 columns. This data, sourced from the Chicago Police Department's CLEAR (Citizen Law Enforcement Analysis and Reporting) system, includes information such as incident type, location (at the block level), and date of occurrence. Through this project, I aim to understand crime patterns, trends, and correlations, which can help in effective resource allocation, policy-making, and enhancing community resilience.

### The social science problem

Crime is a complex social phenomenon that affects the quality of life and economic development of communities. Understanding crime patterns is crucial for law enforcement and community organizations to effectively combat and prevent crime. This project focuses on identifying trends and hotspots of crime in Chicago, exploring socio-economic factors that may influence crime rates, and evaluating the impact of external factors like the COVID-19 pandemic on criminal activities. The insights gained can inform targeted interventions and public safety strategies, making them more data-driven and efficient.

### Why large-scale computing methods?
The volume, variety, and complexity of crime data necessitate the use of scalable computing methods. Traditional data processing tools are insufficient for handling datasets of this magnitude with the required speed and efficiency. Large-scale computing methods allow for the management and analysis of big data in a way that is both time-efficient and computationally feasible. These methods enabled me to perform extensive data cleaning, integration, exploratory data analysis (EDA), and complex model training across the crimes dataset which was too big for my laptop RAM to handle, making it a good use case for large-scale computing.

### Large scale methods employed

#### Data integration and management
I used PySpark, an interface for Apache Spark, which allows for fast cluster computing and is particularly adept at processing large datasets. The initial stage involved using a Python script to upload multiple datasets into an AWS S3 bucket. These datasets included:

1. Crime data from the Chicago Police Department
2. Socio-economic indicators such as poverty and income levels
3. COVID-19 case data by community area
4. Community names

This integration allows for a holistic analysis that considers various potential influences on crime rates. I also created a teardown script to delete the data following the completion of the analysis.

#### Exploratory Data Analysis (EDA)
After cleaning and integrating the data, I conducted extensive EDA using PySpark to explore trends over time, differences between community areas, and the prevalence of different types of crimes. Notably:

- Crime rates have generally decreased over time, with significant drops during the COVID-19 pandemic.
 ![image](https://github.com/macs30123-s24/final-project-chicago-crime/assets/30920386/9705e63e-27ea-486b-ac4e-d64fcb2eb946)

- Theft and battery are the most common crime types.
![image](https://github.com/macs30123-s24/final-project-chicago-crime/assets/30920386/33de08e6-a0a6-466c-a950-ed2485bc6033)

- Areas like Austin show higher crime rates, which prompts a deeper examination of regional disparities.
![image](https://github.com/macs30123-s24/final-project-chicago-crime/assets/30920386/5892ae10-d2e0-4c58-833e-082fe2bc0abe)

#### COVID-19 Impact Analysis

I then wanted to understand the effects of the COVID-19 pandemic on crime rates in Chicago. The integration of COVID-19 case data allowed for this exploration of how the pandemic influenced crime dynamics across different community areas and crime types. I found that there was a sharp decline in overall crime rates during the early stages of the pandemic, likely due to lockdown measures and reduced public presence. However, the impact varied by type of crime:

![image](https://github.com/macs30123-s24/final-project-chicago-crime/assets/30920386/5afd843b-6c27-489b-b172-eb5bac48d050)

We can see a clear effect of COVID-19 on monthly trends in the 10 top crime types (by count) in Chicago. All crimes in general plummet initially. We see a clear fall in 'Theft' as the largest crime type upon the onset of COVID-19 as people would be in lockdown. As time goes on, it rises again and by 2022 is getting back to the levels of pre-COVID times. Interestingly, narcotics also saw a rapid fall on the set of the pandemic due to the lockdown and don't seem to have recovered to pre-Covid levels. Battery, as expected, falls initially but then sees a quick jump back up to its pre-Covid levels. Interestingly, criminal damage follows pretty much the same pattern before and after COVID.

![image](https://github.com/macs30123-s24/final-project-chicago-crime/assets/30920386/96fca4af-f48f-41f8-8f0b-2a2bd85a871c)

We see a very clear relationship between number of crimes and COVID cases in each neighborhood. If the number of crimes increases, the number of cases seems to increase as well.

This aspect of the analysis highlights the importance of considering public health crises in crime trend analysis and the potential for these methods to inform responses to future emergencies. 
#### Machine Learning Models

The models were created in PySpark partitioning the data into 15 partitions in an EMR cluster. 

##### 0. Feature Engineering
I conducted extensive feature engineering on factors I thought could affect crime rates such as getting month, the hour of the day, season, the yearly change in crime rate based on community, duration since previous crime at the block level, etc. 

##### 1. Predicting Crime Type
Research question: How can various environmental, temporal, and community-related factors be used to predict the primary type of crime in a given location, and what insights does this provide into the patterns of criminal activity in urban environments like Chicago? I used a random Forest Classifier for this Crime Type Prediction. This model predicted the primary type of crime based on environmental, temporal, and community-related factors, achieving weighted precision and recall of 82%, and an F1 score of 81%. Significant features included the description of the crime and geographic location. 
 
##### 2. Predicting Arrests
Research Question: What factors predict the likelihood of an arrest during a crime? I used a random forest classifier for this prediction. This model predicted the likelihood of an arrest, achieving an accuracy of 87%. It highlighted the importance of the location and type of crime, along with socio-economic conditions. 

##### 3. Predicting Change in Yearly Crime Rate

Research Question: Can socio-economic indicators and crime history predict the yearly crime rate change in a community? I used linear regression for this prediction. The predicted changes in crime rates used socio-economic and historical crime data, showing moderate accuracy (18.7%) but also indicating the need for more comprehensive data to improve predictions. 

#### Conclusion

The use of PySpark and AWS EMR (Elastic MapReduce) cluster with 15 partitions ensured that the analysis was scalable and efficient. This setup allowed for the processing of large volumes of data across multiple nodes, significantly reducing processing time and facilitating more complex analyses without performance degradation. The application of large-scale computing methods to social science research problems like crime analysis offers a powerful tool for uncovering insights that can drive public policy and community interventions. By leveraging high-performance computing environments and sophisticated data analysis techniques, this project demonstrates how big data can be harnessed to address critical societal challenges effectively.

## Rides to Safety: Scrutinizing Crime in Hyde Park and Campus Transits

### Project Description

This project aims to analyze and understand the safety concerns and effectiveness of transportation options provided by the University of Chicago in the Hyde Park neighborhood. The neighborhood has a reputation of being unsafe due to prevalent criminal activities. The University of Chicago has taken extensive measures to enhance student safety, including establishing one of America's largest private security forces and initiating safety-oriented transportation services such as the UGO shuttle service and the UChicago Free Lyft Program. Despite these initiatives, the area has seen a worrying rise in crime, including several student fatalities and numerous robberies. This project seeks to investigate the changes in crime rates over time in Hyde Park and critically evaluate the effectiveness of the university's safety transportation services in reducing outdoor crime.

The investigation in this project is twofold. Firstly, it examines the historical trend of crime rates in Hyde Park, providing insights into how criminal activities have evolved over time. This includes a detailed analysis of different types of crimes, identifying temporal trends, daily peaks, and specific locations prone to criminal incidents. Secondly, the project evaluates the university's safety transit options, questioning their effectiveness in enhancing student safety. The analysis is based on the hypothesis that these transit options may not be significantly improving safety. To facilitate a comprehensive and interactive exploration of the data, the project includes an RShiny article and a standalone Shiny application. These outputs allow users to engage with the data, explore geographical hotspots of crime, and possibly unearth further insights into the dynamics of crime and safety in Hyde Park.

Final Article: https://harshpachisia.shinyapps.io/uchicago-crime-notebook/

Shiny Application: https://harshpachisia.shinyapps.io/uchicago-crimes-story/

### Instructions for running the project

#### Packages and Data needed

Install the packages below using the `install.packages()` command and then run the following code below. 
```{r}
library(viridis) 
library(tidyverse)
library(ggrepel)
library(shinythemes)
library(shiny)
library(leaflet)
library(leaflet.extras)
library(RColorBrewer)
library(sf)
library(ggplot2)
library(lubridate)
library(dplyr)
library(tidyr)
library(gridExtra)
library(grid)
library(leaflet.extras)
library(rsconnect)
```

All data sets needed to replicate the analysis are provided in the `data_collection` folder in the repository. For updated data for future analysis of crime, please check out the [Chicago Data Portal for crime.](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/about_data)