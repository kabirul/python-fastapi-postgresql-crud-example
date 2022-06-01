# Install the required packages
   `python -m pip install -r requirements.txt`

#If everything completes should be available on [notes](http://localhost:8000/api/blogs)
#Docs are generated on [docs](http://localhost:8000/docs)

## Tests

Tests are available using pytest
Run them using `pytest .` while in the root directory (/python-fastapi-postgresql-curd-example)

## Documentation
Open API Documentation is provided by [Redoc](http://localhost:8000/redoc)

# Start the app using Uvicorn
 `uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000`
 or 'uvicorn app.main:app --reload'
