#!/bin/bash

PROJECT_ID="msca-bdp-student-ap"
DATASET_NAME="chicago_rideshare"
BUCKET_NAME="msca-bdp-student-gcs"
FOLDER_PATH="bdp-rideshare-project/rideshare/processed_data"

# Specify the folder names containing multiple CSV files
FOLDERS=("program_area_2020.csv" 
         "program_area_time_rides_2018.csv" 
         "program_area_time_rides_2019.csv" 
         "program_area_time_rides_2021.csv" 
         "program_area_time_rides_2022.csv"
         "rides_2018.csv"
         "rides_2019.csv"
         "rides_2020.csv"
         "rides_2021.csv"
         "rides_2022.csv")

# Load data into BigQuery for the specified folder
load_into_bigquery() {
    local TABLE_NAME="$1"
    local FOLDER_NAME="$2"
    
    # Construct the GCS file path for CSV files within the folder
    GCS_FOLDER_PATH="gs://$BUCKET_NAME/$FOLDER_PATH/$FOLDER_NAME/*.csv"
    echo "GCS Folder Path: $GCS_FOLDER_PATH"
    
    # Append all CSV files from the folder into the BigQuery table 
    bq load --autodetect --source_format=CSV --noreplace "$PROJECT_ID:$DATASET_NAME.$TABLE_NAME" "$GCS_FOLDER_PATH"
}

# Load data into BigQuery
for FOLDER in "${FOLDERS[@]}"; do
    TABLE=$(basename "$FOLDER" .csv)
    load_into_bigquery "$TABLE" "$FOLDER"
done
