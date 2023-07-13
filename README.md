[![mini-etl-apache-beam](https://github.com/olahsymbo/mini-etl-apache-beam/actions/workflows/etl-ci.yaml/badge.svg?branch=main)](https://github.com/olahsymbo/mini-etl-apache-beam/actions/workflows/etl-ci.yaml)

# Apache Beam ETL Pipeline

This repository contains an example ETL (Extract, Transform, Load) pipeline implemented using Apache Beam in Python. The pipeline is designed to process customer data.

## Prerequisites

- Python 3.x
- Apache Beam library (pip install apache-beam)
- Pipeline Structure

### The ETL pipeline consists of the following steps:

- Extraction: Reading customer data from a text file.
- Transformation: Applying various transformations on the extracted data, including converting date to days, weekdays, hour, minute, and second, standardizing gender values, and mapping age to categories.
- Loading: Writing the transformed data to an output text file.

### Usage

Clone the repository: 

```
git clone https://github.com/olahsymbo/mini-etl-apache-beam.git
```

### Install the required dependencies:

```
pip install apache-beam
```

### Place your input data file in the repository's root directory.

Modify the data_source and data_destination variables in the etl_pipeline function in main.py to specify the filenames for your input and output data.

### Run the ETL pipeline:

```
python pipeline/customer_pipeline.py
```

The transformed data will be written to the specified output file.

## Customization

You can customize the pipeline by modifying the following components:

- **Transformation Logic:** Update the transform_function in `pipeline/customer_pipeline.py` to include your specific data processing logic.
- **Additional Transformations:** Extend the pipeline by adding more transformations based on your requirements.
- **Input Data Format:** Adjust the reading logic in etl_pipeline to handle your specific input file format (e.g., delimiter, encoding).
- **Output Data Sink:** Modify the writing logic in etl_pipeline to use a different output sink, such as a database or cloud storage.
