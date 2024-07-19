# The UChicago Lyft Ride Smart Program: Effects on Ridesharing
By Harsh Vardhan Pachisia, Abe Burton, Ridhi Purohit, and Rohit Kandala

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



