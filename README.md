# Decomp-Parsing-Service

Decomp-Parsing-Service is a Python module that transforms abstract static analysis results into intermediate representations that can be used to suggest a decomposition of a monolithic application into microservices.

## Description

The Parsing Service interacts with the static analysis tools that generate abstract representations in the form of TypeData, methodData and invocationData. This service transforms these results into more detailed representations that can be used by monolith to microservices decomposition approaches. 

This service is a part of a research project that aims to provide a standarized framework for analyzing monolithic applications, decomposing them into microservices, visualizing the decompositions, evaluating the decompositions and refactoring the monolith.

Currently, the following representations are implemented:
- Call Dependency Matrix: a matrix that represents the call dependencies between the methods or classes of the application.
- Interaction Matrix: a matrix that represents all interactions between the classes of the application (calls, inheritance, field usage, return type, etc.).
- Bag of Words: a matrix that represents the frequency of the words in the code snippets of the methods or classes of the application.
- TF-IDF: a matrix that represents the Term Frequency - Inverse Document Frequency (TF-IDF) values of the words in the code snippets of the methods or classes of the application.

## Getting Started

### Dependencies

The Python module requires the following dependencies:
* Python 3.10 or higher
* Java (Optional for running the Java analysis service as Jar file):
  * JRE 11 or higher
* Docker (Optional for running the parser or analysis service in Docker containers):


### Installing

First, clone the repository to your local machine:
```
  git clone https://github.com/khaledsellami/decomp-parsing-service.git
```
Then, install the required dependencies or build the parsing module:
To install the dependencies only, you can run the following command:
```
  cd ./decomp-parsing-service
  pip install -r requirements.txt
```

To build the parsing module, you can run the following command:

```
  cd ./decomp-parsing-service
  pip install .
```

### Starting the analysis service
The parsing service depends on the analysis service. As a prerequisite, you need to run the analysis service, generate its Jar file or provide static analysis results of your project that were previously generated with the analysis service.

If you wish to run the analysis service, you can follow the instructions in the [analysis service repository](https://github.com/khaledsellami/decomp-java-analysis-service).

### Executing program

The are three ways to interact with the parsing service:

#### 1. Using the main script

You can run the main script to parse the source code of a monolithic application and generate the intermediate representations.
```
  python main.py parse your_app_name --data /path/or/link/to/source/code --output /path/to/output
```
The program will save the intermediate representations (by default in parquet format) in "/path/to/output/your_app_name".

#### 2. Using the parser as a module
If you installed the module, you can use the parser as a module in your Python code.
```python
from decparsing import DataHandler, select_client

app_name = 'your_app_name'
data_path = '/path/or/link/to/source/code'
# Select the analysis client that will be used to interface with 
# the analysis service (for example with gRPC or as Java subprocess)
analysis_client = select_client(app_name, data_path)

# Create the data handler that will be used to parse the source code 
# and generate the intermediate representations
parser = DataHandler(analysis_client, output_path='/path/to/output')

# Get the call dependency matrix at the class level
call_dependency_matrix = parser.get_data("calls", level="class")[1]
# Get the TFIDF matrix at the method level
tfidf_matrix = parser.get_data("tfidf", level="method")[1]
# Generate and save all of the intermediate representations at the class level
parser.load_all("class")
```

#### 3. Using the parser gRPC server

You can run the gRPC server that will serve the parsing service.
```
  python main.py start
  # or simply
  python main.py
```
Afterward, you can build your own gRPC client with the programming language of your choice to interact with the parsing service through port 50500. The gRPC server interface is defined in the `protos/parse/v2/parsing.proto` file.


### Help

If you wish to get more information about the available options in the main script, you can run the following command:
```
  python main.py parse --help
```

In addition, you can get more information about the data exposed by the parser service by inspecting the `protos/parse/v2/parsing.proto` file.

## Roadmap
* Improve the documentation of this module
* Integrate additional programming languages from the analysis service:
  * C#

## Authors

Khaled Sellami - [khaledsellami](https://github.com/khaledsellami) - khaled.sellami.1@ulaval.ca

## Version History

* 1.5.3
    * Initial Documented Release

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.