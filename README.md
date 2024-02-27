# TensorQA test

## How to run tests:

- Clone the repository and go to it on the command line:

```
git clone git@github.com:We1der/TensorQA.git
```

- Create and activate a virtual environmen:

```
python3 -m venv env
```

* for Linux/macOS

    ```
    source env/bin/activate
    ```

* for windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

- Install dependencies from file requirements.txt:

```
pip install -r requirements.txt
```

- Run pytest:

```
pytest
```