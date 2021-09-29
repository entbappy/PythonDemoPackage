from src.utils.all_utils import read_yaml, create_directory
# import argparse
import pandas as pd
import os
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s] %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename= os.path.join(log_dir,"running_logs.log"),level=logging.INFO, format=logging_str, filemode="a")


def get_data(config_path):
    """This function save the data from remote

    Args:
        config_path (str): [description]
    """

    config = read_yaml(config_path)

    remote_data_path = config['data_source']
    df = pd.read_csv(remote_data_path , sep= ";")
    
    #Saving dataset in local to artifacts
    #create path to directory: artifacts/raw_local_dir/data.csv
    artifacts_dir = config['artifacts']['artifacts_dir']
    raw_local_dir = config['artifacts']['raw_local_dir']
    raw_local_file = config['artifacts']['raw_local_file']

    raw_local_dir_path = os.path.join(artifacts_dir, raw_local_dir)
    
    create_directory(dirs=[raw_local_dir_path])

    raw_local_file_path = os.path.join(raw_local_dir_path, raw_local_file)
    
    df.to_csv(raw_local_file_path, sep=',', index = False)
    logging.info(f"Data Saved to {raw_local_dir_path}")



# if __name__ == '__main__':
#     args = argparse.ArgumentParser()
#     args.add_argument("--config", "-c", default="config/config.yaml")
#     parsed_args = args.parse_args()
    
#     # Calling get_data function
#     try:
#         get_data(config_path = parsed_args.config)
#         logging.info("Execution Successful!")
#     except Exception as e:
#         logging.exception(e)
#         raise e
        