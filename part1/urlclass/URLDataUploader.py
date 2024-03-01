import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import snowflake.connector
from model_orm import URLOrm, Base
from models import URLClass
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class URLDataUploader:
    def __init__(self, csv_path, snowflake_config):
        self.csv_path = csv_path
        self.snowflake_config = snowflake_config
        self.ensure_snowflake_setup()
        self.engine = create_engine(self._get_snowflake_connection_string())
        Base.metadata.create_all(self.engine)

    def ensure_snowflake_setup(self):
        conn = snowflake.connector.connect(
            user=self.snowflake_config['user'],
            password=self.snowflake_config['password'],
            account=self.snowflake_config['account']
        )
        cursor = conn.cursor()
        cursor.execute(f"CREATE WAREHOUSE IF NOT EXISTS {self.snowflake_config['warehouse']}")
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.snowflake_config['database']}")
        cursor.execute(f"USE DATABASE {self.snowflake_config['database']}")
        cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {self.snowflake_config['schema']}")
        cursor.close()
        conn.close()

    def _get_snowflake_connection_string(self):
        return f"snowflake://{self.snowflake_config['user']}:{self.snowflake_config['password']}@{self.snowflake_config['account']}/{self.snowflake_config['database']}/{self.snowflake_config['schema']}?warehouse={self.snowflake_config['warehouse']}"

    def read_csv(self):
        return pd.read_csv(self.csv_path)

    def create_orm_instances(self, df):
        orm_instances = []
        for _, row in df.iterrows():
            orm_instance = URLOrm(
                name_of_the_topic=row['Name of the topic'],
                year=row['Year'],
                level=row['Level'],
                topics=row['Topics'],
                learning_outcomes=row['Learning Outcomes Section'],
                introduction=row['Introduction'],
                summary=row['Summary Bullets'],
                link_to_the_pdf_file=row['Link to the PDF File'],
                link_to_the_summary_page=row['Link to the Summary Page']
            )
            orm_instances.append(orm_instance)
        return orm_instances

    def upload_to_snowflake(self, orm_instances):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.bulk_save_objects(orm_instances)
        session.commit()

    def process_data(self):
        df = self.read_csv()
        # Replace NaN values with None for compatibility with Snowflake
        df = df.where(pd.notnull(df), None)
        
        # Stripping "Curriculum" from the 'Curriculum' column values
        df['Year'] = df['Year'].str.replace('Curriculum', '').str.strip()
        
        # Stripping "CFA Program" from the 'Level' column values
        df['Level'] = df['Level'].str.replace('CFA Program', '').str.strip()
        orm_instances = self.create_orm_instances(df)
        self.upload_to_snowflake(orm_instances)

snowflake_config = {
    'user': os.getenv('SNOWFLAKE_USER'),
    'password': os.getenv('SNOWFLAKE_PASSWORD'),
    'account': os.getenv('SNOWFLAKE_ACCOUNT'),
    'warehouse': os.getenv('SNOWFLAKE_WAREHOUSE'),
    'database': os.getenv('SNOWFLAKE_DATABASE'),
    'schema': os.getenv('SNOWFLAKE_SCHEMA')
}

csv_path = '../resources/cfa_url/cfa_list_input.csv'
uploader = URLDataUploader(csv_path, snowflake_config)
uploader.process_data()
