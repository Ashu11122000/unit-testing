# Unit Testing in Python using Pytest & UV

## Task Overview

This task demonstrates the implementation of Unit Testing in Python using the powerful pytest framework, along with modern dependency management using uv.

Unit testing ensures that individual components (functions or methods) of an application work correctly in isolation, improving code reliability and maintainability.

---

## Concepts Covered

### 1. Unit Testing

* Process of testing individual components (a function, a method, or a class) of a code.
* Helps detect bugs early -> find errors before production.
* Improves code quality and maintainability -> forces better design.
* Documentation -> tests explains how code works.
* Automation -> runs tests anytime.

---

### 2. Test Case

A single test scenario

```python
def test_login():
    assert login("user", "pass") == True
```

---

### 3. Assertions

* Assertions are used to validate expected results. 
* Check expected vs actual results.

```python
assert add(2, 3) == 5
assert add(2, 2) != 5
assert isinstance(add(2, 3), int)
assert add(5, 5) > 0
```

---

### 3. Test Runner
* Tools that runs tests like pytest.

---

### 4. Fixtures

Reusable setup logic for tests.

```python
@pytest.fixture
def sample_numbers():
    return (10, 5)
```

---

### 4. Mocking
Replacing real dependencies with fake ones for avoiding DB calls, avoiding api calls and faster tests.

---

### 5. Isolation
Each test should not depends on others and runs independently.

---

### 6. Types of Testing
1. Unit Testing: Tests single function/module
2. Integration Testing: Test multiple components together.
3. End-to-End Testing: Test full systems.

---

### 7. Parametrized Tests

* Allows to run the same test with multiple inputs automatically. 
* Instead of writing multiple tests functions, always use one test + multiple data sets/

```python
@pytest.mark.parametrize("a,b,result", [
    (1, 2, 3),
    (2, 3, 5),
])
```

---

### 5. Exception Testing

* Testing whether code raises the correct error.
* Validate error handling.

```python
with pytest.raises(ValueError):
    divide(10, 0)
```

---

### 6. Edge Case Testing

Inputs that are rare, extreme and unexpected.

Testing unusual scenarios:

* Empty inputs: Testing behavior when no data is provided.
    -> Break Logic
    -> Cause Crashes
    -> Returns unexpected results

```python
def test_empty_list():
    assert sum([]) == 0
```

* Invalid data types: Testing wrong or unexpected data types.
    User or API can send:
    -> Wrong data types
    -> Corrupted data
    -> Unexpected formats

```python
def test_invalid_types():
    with pytest.raises(TypeError):
        add("a", 2)    # Raises error here, adding (string + int)    
```

* Large inputs: Testing extreme or large values.
    -> Overflow
    -> Performance issues
    -> Memory crashes

```python
def test_large_numbers():
    assert add(10**9, 10**9) == 2 * 10**9
```

---

### 7. Test Coverage

* Measures how much of code is executed during tests.
* Passing tests != full tested codes.
* It uses pytest-cov tool which is basically a plugin of pytest and measures how much of code is actually tested.

```bash
uv run pytest --cov=app
```

```output
Name            Stmts    Miss    Cover
app/main.py       50       5      90%
```

* stmts - total lines
* Miss - Not Executed
* Cover - % tested
---

### 8. Flow of unit testing
Write Code -> Write Tests -> Run Tests -> Fix -> Repeat

## Setup & Installation

---

### 1. Initialize Project

```bash
uv init unit-testing
cd unit-testing
```

---

### 2. Create Virtual Environment

```bash
uv venv
```

Activate:

```bash
.venv\Scripts\activate   # Windows
```

---

### 3. Install Dependencies

```bash
uv add pytest pytest-cov
```

---

## Running Tests

```bash
uv run pytest
```

Verbose mode:

```bash
uv run pytest -v
```

Run with coverage:

```bash
uv run pytest --cov=app
```

---

## Project Structure

```bash
unit-testing/
│
├── app/
│   ├── __init__.py
│   └── math_utils.py
│
├── tests/
│   ├── __pycache__/
│   └── test_math_utils.py
│
├── .venv/
├── .pytest_cache/
├── .coverage
├── pyproject.toml
├── uv.lock
├── README.md
```

---

## Git Commands

### Initialize Git

```bash
git init
```

---

### Add Files

```bash
git add .
```

---

### Commit

```bash
git commit -m "Initial commit - Unit Testing with pytest and uv"
```

---

### Add Remote

```bash
git remote add origin https://github.com/Ashu11122000/unit-testing.git
```

---

### Push Code

```bash
git branch -M main
git push -u origin main
```

---

## Key Learnings

* Writing clean and modular test cases
* Using pytest for efficient testing
* Implementing fixtures and parametrized tests
* Handling exceptions in tests
* Measuring code coverage
* Managing dependencies using uv

---

## Future Enhancements

* Add CI/CD pipeline (GitHub Actions)
* Add FastAPI endpoint testing
* Mock database/API calls
* Improve coverage reporting

---


