# Ultra-Marathon Data Analysis Project

## Overview
This project analyzes ultra-marathon race data from the "TWO_CENTURIES_OF_UM_RACES.csv" dataset, focusing specifically on 50km and 50-mile races in the USA during 2020. The analysis explores various aspects of ultra-marathon running including gender differences, age performance patterns, and seasonal variations in performance.

## Table of Contents
- [Requirements](#requirements)
- [Dataset](#dataset)
- [Data Preparation](#data-preparation)
- [Analysis Features](#analysis-features)
- [Key Findings](#key-findings)
- [Usage](#usage)
- [Future Improvements](#future-improvements)

## Requirements
This project requires the following Python libraries:
- pandas
- seaborn

You can install these dependencies using pip:
```
pip install pandas seaborn
```

## Dataset
The analysis uses the "TWO_CENTURIES_OF_UM_RACES.csv" dataset, which contains comprehensive information about ultra-marathon races across two centuries.

**Dataset Link**: [Ultra-Marathon Dataset](https://drive.google.com/file/d/1gc9zNhSXjrP7IYL0u35hv2-agTm46Esx/view?usp=drive_link)

**Note**: The dataset is quite large and may require sufficient disk space and memory for processing.

The dataset includes:
- Race details (year, dates, name, distance, number of finishers)
- Athlete information (performance time, gender, average speed, ID, birth year)
- Geographic data (race locations)

## Data Preparation
The data preparation process includes the following steps:

1. **Data Filtering**
   - Filtered for only USA races (extracted from event names)
   - Selected only 50km and 50-mile races
   - Limited to 2020 race year

2. **Data Cleaning**
   - Removed "(USA)" from event names
   - Calculated athlete age from birth year
   - Removed "h" from athlete performance times
   - Dropped unnecessary columns (athlete club, country, age category, birth year)
   - Handled missing values
   - Checked and removed duplicates
   - Reset index

3. **Data Transformation**
   - Converted athlete age to integer type
   - Converted average speed to float type
   - Renamed columns for clarity
   - Reordered columns for better readability
   - Extracted race month from dates
   - Created season categories based on race months

## Analysis Features
The project includes several analytical approaches:

1. **Distribution Analysis**
   - Distribution of race lengths
   - Gender distribution across race types
   - Speed distribution in 50-mile races

2. **Comparative Analysis**
   - Gender differences in average speed across race types
   - Violin plots showing speed distribution by gender and race length

3. **Age Analysis**
   - Performance trends by age using regression plots
   - Best performing age groups (with minimum 20 races)
   - Worst performing age groups (with minimum 10 races)

4. **Seasonal Analysis**
   - Performance differences across seasons
   - Seasonal performance patterns specific to 50-mile races

## Key Findings
- There are distinct speed differences between male and female ultra-runners
- Peak performance age ranges were identified for 50-mile races
- Seasonal variations affect runner performance, with certain seasons showing better average speeds
- The relationship between age and speed follows expected patterns with a peak performance window

## Usage
To run this analysis:

1. Ensure you have the required libraries installed
2. Download the dataset from the provided Google Drive link
3. Due to the large size of the dataset, ensure you have sufficient memory allocated for processing
4. Place the "TWO_CENTURIES_OF_UM_RACES.csv" file in the same directory as the script
5. Run the Python script: `python ultra-marathon_running.py`

## Future Improvements
Potential enhancements to this analysis could include:
- Extending the analysis to multiple years to identify trends over time
- Including geographic analysis to identify fastest courses
- Analyzing individual runner progression across multiple races
- Incorporating weather data to assess its impact on performance
- Creating interactive visualizations for more dynamic exploration
- Implementing more efficient data handling techniques for the large dataset

---
*This project was created to analyze ultra-marathon race data and identify patterns in runner performance based on gender, age, and seasonal factors.*
