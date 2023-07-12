import os
import sys

HOME = "/Users/mini-etl"
sys.path.append(HOME)

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from utils.date_utils import DateTransformer
from utils.demograph_utils import GenderTransformer, AgeTransformer


data_dir_list = ['raw', 'consolidated', 'product']

if not os.path.exists(os.path.join(HOME, 'data')):
    os.mkdir(os.path.join(HOME, 'data'))

for data_dir in data_dir_list:
    data_path = os.path.join(os.path.join(HOME, 'data'), data_dir)
    os.mkdir(data_path)


def etl_pipeline(data_source, data_destination):
    pipeline_opt: PipelineOptions = PipelineOptions()

    with beam.Pipeline(options=pipeline_opt) as p:
        extract_data = (
                p
                | 'ReadInput' >> beam.io.ReadFromText(data_source, skip_header_lines=1)
        )

        transform_data = (
                extract_data
                | 'TransformData' >> beam.Map(transformation_function)
        )

        (
                transform_data
                | 'WriteOutput' >> beam.io.WriteToCsv(data_destination)
        )


def transformation_function(data) -> str:
    fields = data.split(',')
    print(fields)
    date = fields[1]
    date_obj: DateTransformer = DateTransformer(date)

    days: int = date_obj.convert_to_days()
    weekdays: int = date_obj.convert_to_weekdays()
    hours: int = date_obj.convert_to_hours()
    minutes: int = date_obj.convert_to_minutes()
    seconds: int = date_obj.convert_to_sec()

    gender_obj: GenderTransformer = GenderTransformer(fields[2])
    gender: str = gender_obj.std_gender()

    age_obj: AgeTransformer = AgeTransformer(fields[3])
    age: str = age_obj.std_age()

    transformed_data: str = f"{days}, {weekdays}, {hours}, {minutes}, {seconds}, {gender}, {age}"
    return transformed_data


source = "data/raw/customer.txt"
dest = "data/consolidated/customer.txt"
etl_pipeline(data_source=source, data_destination=dest)
