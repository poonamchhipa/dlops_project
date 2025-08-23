from src.cnnClassifier.constants import *
from src.cnnClassifier.utils.common import read_yaml, create_directories
from src.cnnClassifier.entity.config_entity import DataIngestionConfig
from src.cnnClassifier.entity.config_entity import PrepareBaseModelConfig
from src.cnnClassifier.entity.config_entity import PrepareCallbacksConfig
from pathlib import Path
import os


class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config['artifacts_root']])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config['data_ingestion']
        create_directories([config['root_dir']])

        return DataIngestionConfig(
            root_dir=Path(config['root_dir']),
            source_URL=config['source_URL'],
            local_data_file=Path(config['local_data_file']),
            unzip_dir=Path(config['unzip_dir'])
        )
    

    def get_prepare_base_model_config(self):
        config = self.config['prepare_base_model'] 
        params = self.params 
        create_directories([config['root_dir']]) 

        return PrepareBaseModelConfig(
            root_dir= Path(config['root_dir']),
            base_model_path=Path(config['base_model_path']),
            updated_base_model_path=Path(config['updated_base_model_path']),
            params_image_size=params['IMAGE_SIZE'],
            params_learning_rate=params['LEARNING_RATE'],
            params_include_top=params['INCLUDE_TOP'],
            params_weights=params['WEIGHTS'],
            params_classes=params['CLASSES'] 
        )
    

    def get_prepare_callback_config(self) -> PrepareCallbacksConfig:
        config = self.config['prepare_callbacks']
        model_ckpt_dir = os.path.dirname(config['checkpoint_model_filepath'])

        create_directories([
            Path(model_ckpt_dir),
            Path(config['tensorboard_root_log_dir'])
        ])

        return PrepareCallbacksConfig(
            root_dir=Path(config['root_dir']),
            tensorboard_root_log_dir=Path(config['tensorboard_root_log_dir']),
            checkpoint_model_filepath=Path(config['checkpoint_model_filepath'])
        )