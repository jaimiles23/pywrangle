- [PyTest](#pytest)
  - [Installation](#installation)
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


## Naming convention
Pytest uses files that include test_* and *_test in their names. Per convention, all tests are prefixed with:
> test_*


## Test storage
Tests are stored outside of the application code. This has the following benefits:
- Central location for all tests.
- Tests to be run against a pip installed package.

## Testing
To run all tests, navigate to the cloned repository directory; the parent dir :
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
pytest
```

