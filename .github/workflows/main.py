name: Python CI

on:
  - push
  - pull_request

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        # we want to test our package on several versions of Python
        python-version: [3.8, 3.9]
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
        # make depends on poetry
      - name: Install dependencies
        run: |
          pip install poetry
          make install
      - name: Run linter and pytest
        run: |
          make check
      - name: Test & publish code coverage
        uses: paambaati/codeclimate-action@v5.0.0
        if: github.ref_name == 'main'
        env:
          CC_TEST_REPORTER_ID: ${{ secrets.CC_TEST_REPORTER_ID }}
        with:
          coverageCommand: make test-coverage
          debug: true
