import json
import uuid
import logging
import os
import glob
import pandas as pd

# Some Issues to be addressed are:

# Folder paths are hard coded.
# Schemas.json path is also hard coded.
# Modularization with reusability.


def get_columns(ds):
    schemas_file_path=os.environ.setdefault('SCHEMAS_FILE_PATH', 'data/retail_db/schemas.json')
    with open(schemas_file_path) as fp:
        schemas = json.load(fp)
    try:
        schema = schemas.get(ds)
        if not schema:
            raise KeyError
        cols = sorted(schema, key=lambda s: s['column_position'])
        columns = [col['column_name'] for col in cols]
        return columns
    except KeyError:
        logging.error(f'Schema not found for {ds}')
        raise

def process_file(src_base_dir,ds,tgt_base_dir):
     for file in glob.glob(f'{src_base_dir}/{ds}/part*'):
        try:
            df = pd.read_csv(file, names=get_columns(ds))
            os.makedirs(f'{tgt_base_dir}/{ds}', exist_ok=True)
            df.to_json(
                f'{tgt_base_dir}/{ds}/{str(uuid.uuid1())}.json',
                orient='records',
                lines=True
             )
            logging.info(f'Number of records processed for {os.path.split(file)[1]} in {ds} is {df.shape[0]}')
        except KeyError:
            raise  

def main():
    src_base_dir=os.environ['SRC_BASE_DIR']
    tgt_base_dir=os.environ['TGT_BASE_DIR']
    log_file_path=os.environ['LOG_FILE_PATH']
    logging.basicConfig(
        filename=log_file_path,
        level=logging.INFO, 
        format='%(levelname)s %(asctime)s %(message)s',
        datefmt='%Y-%m-%d %I:%M:%S %p'
    )

    datasets=os.environ.get('DATASETS') # orders,order_items
    logging.info('File Format Conversion: Started')
    if not datasets:
        for path in glob.glob(f'{src_base_dir}/*'):
            if os.path.isdir(path):
                process_file(src_base_dir, os.path.split(path)[1], tgt_base_dir)
    else:
        dirs=datasets.split(',') #['orders', 'order_items']  
        for ds in dirs:
            try:
                process_file(src_base_dir, ds, tgt_base_dir)
            except Exception as e:
                logging.error(f'File Format Conversion for {ds} is not successful')              
    logging.info('File Format Conversion: Successful')

if __name__ == '__main__':
    main()

# Exercise: Similar program file for nyse-converter
# update app.py with core logic of File-Format-Conversion for nyse data
# Make sure to validate to see if it is working as per the expectations or not
# Changes are committed and pushed to remote repository


# Exercise: Make changes to nyse-converter to use environment variables.
# SRC_DIR: `data/nyse_all/nyse_data`
# TGT_DIR: `data/nyse_all/nyse_json`
# Make sure to run and validate the code after making changes using environment variables.
# Make sure to commit and push the changes to remote git repository.
