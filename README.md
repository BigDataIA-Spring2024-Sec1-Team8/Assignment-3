# Assignment-3

## Project Description
This project bridges the foundational aspects of data schema design and the advanced methodologies of data transformation and analysis and is structured into two primary components. The Part1 will focus on creating Python classes to accurately represent and validate the structure of web pages and PDF documents, emphasizing data integrity and adherence to predefined standards. This step ensures the preparation of "clean" data, crucial for any analytical tasks that follow. The Part 2 will focus on leveraging DBT (Data Build Tool) and Snowflake for data transformation, which is to manage and execute data workflows efficiently. By creating a summary table that encapsulates key data metrics, we analyze and derive meaningful insights from the data. 

**Link to Repository of Part 2** : https://github.com/BigDataIA-Spring2024-Sec1-Team8/Assignment3-partb

## Project Resources
- Google Codelab - https://codelabs-preview.appspot.com/?file_id=1VZa2oD8pQvpc_y3ThVcDGuVyKk5gXutSJlcjZf9seag#0
- URL Jupyter Notebook - https://github.com/BigDataIA-Spring2024-Sec1-Team8/Assignment-3/blob/main/part1/urlclass/URLDataUploader.ipynb
- MetaData Jupyter Notebook - https://github.com/BigDataIA-Spring2024-Sec1-Team8/Assignment-3/blob/main/part1/pdfclass/MetaDataLoader.ipynb
- XMLContent Jupyter Notebook  - https://github.com/BigDataIA-Spring2024-Sec1-Team8/Assignment-3/blob/main/part1/pdfclass/XMLContentLoader.ipynb

## Tech Stack
SQLAlchemy | Snowflake | Pydantic | Pytest | DBT

## Architecture Diagram

![image](https://github.com/BigDataIA-Spring2024-Sec1-Team8/Assignment-3/assets/114782541/4b32e6a1-76e6-45a9-b8b0-6c61c9b48681)

The architectural diagram illustrates a data processing pipeline where a CSV file is read and its contents are extracted as metadata and content from XML files. These contents are then transformed and validated in Python using ORM and Pydantic before being tested with Pytest. Finally, the data is stored in Snowflake via SQLAlchemy, completing the workflow from data extraction to storage.

**Part2 - In DBT:**

![image](https://github.com/BigDataIA-Spring2024-Sec1-Team8/Assignment-3/assets/114782541/b311d2b8-7454-4615-9b88-910ae105fcbc)

To summarize, we initiated the project by setting up accounts on Snowflake and dbt Cloud. In Snowflake, we prepared a new Worksheet and imported sample data into a newly created database. We then integrated dbt Cloud with Snowflake, allowing us to use dbt for efficient data transformation, where we converted tested SQL queries into reusable models. We ensured data integrity through dbt's testing features and automated the transformation process by scheduling regular dbt jobs.

## Repository Structure
**For Part 1:**

![image](https://github.com/BigDataIA-Spring2024-Sec1-Team8/Assignment-3/assets/114782541/949b9ce0-24a7-4733-be9a-0b40b99ed5fd)

## Contributions
- Sai Durga Mahesh Bandaru - 33.3%
- Sri Poojitha Mandali - 33.3%
- Shivani Gulgani - 33.3%
  
WE ATTEST THAT WE HAVEN’T USED ANY OTHER STUDENTS’ WORK IN OUR ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK
