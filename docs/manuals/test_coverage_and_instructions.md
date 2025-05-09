# Test Coverage and Instructions

## Current Status
No unit or integration tests are currently implemented in the `tests/` folder. There is no automated test coverage report at this time.

## How to Add Tests
- Create test files in the `tests/` directory, following the structure:
  - `test_<module>.py` for Python modules.
- Use `pytest` for writing and running tests.

## Running Tests
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   pip install pytest coverage
   ```
2. Run all tests:
   ```sh
   pytest tests/
   ```
3. Generate a coverage report:
   ```sh
   coverage run -m pytest tests/
   coverage report
   coverage html  # For HTML report
   ```

## Manual Test Instructions
- Manual test cases should be documented here as they are developed.

## Future Work
- Add unit and integration tests for all modules.
- Update this document with test case descriptions and coverage results.
