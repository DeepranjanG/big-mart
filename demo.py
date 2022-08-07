from store.pipeline.pipeline import Pipeline
from store.exception import StoreException
from store.logger import logging
from store.config.configuration import Configuartion
from store.component.data_transformation import DataTransformation
import os
def main():
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuartion(config_file_path=config_path))
        pipeline.start()
        logging.info("main function execution completed.")
     

    except Exception as e:
        logging.error(f"{e}")
        raise StoreException(e, sys) from e
        print(e)



if __name__=="__main__":
    main()

