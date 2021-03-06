- [PyTest](#pytest)
  - [Installation](#installation)
  - [Use](#use)
  - [Naming convention](#naming-convention)
  - [Test storage](#test-storage)
  - [Testing](#testing)


# PyTest
PyWrangle uses the pytest module. Pytest is a light framework that scales well for more complex function testing. 

## Installation
Pytest can be installed with pip
```
python -m pip install -U pytest
```

## Use
Pytest is run through the cmd. Navigate to the directory and run:
```
python -m pytest
```


## Naming convention
Pytest uses files that include test_*.py and *_test.py in their names. Per convention, all tests are prefixed with:
> test_*.py

Additionally, test functions must also follow the "test_" nomenclature to be collected by pytest.


## Test storage
Tests are stored outside of the application code. This has the following benefits:
- Tests are not included in package deployment, keeping the library lightweight.
- Central location for all tests.
- Tests can be run against a pip installed package.

## Testing
To run all tests, navigate to the cloned repository directory; the parent dir `pywrangle_lib` :
```
├── API_token.txt
├── CONTRIBUTING.md
├── Documentation.md
├── HISTORY.md
├── LICENSE
├── README.md
├── build
├── creds.pypirc
├── dist
├── pywrangle
├── pywrangle.egg-info
├── setup.py
├── tests
│   ├── Testing_Documentation.md
│   └── test_case.py
└── todo_logs.md
```
and run the pytest command:
```
pytest tests
```

