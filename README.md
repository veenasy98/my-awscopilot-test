# FastAPI Demo Service

A simple FastAPI application ready for deployment on AWS ECS using Copilot.

## Local Development

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   uvicorn app.main:app --reload
   ```

3. Access the API documentation at http://localhost:8000/docs

## Docker Build

Build the Docker image:
```
docker build -t fastapi-service .
```

Run the container locally:
```
docker run -p 8000:8000 fastapi-service
```

## AWS Copilot Deployment

1. Install AWS Copilot CLI: https://aws.github.io/copilot-cli/

2. Initialize a new application (first time only):
   ```
   copilot app init fastapi-demo
   ```

3. Deploy the service:
   ```
   copilot init --app fastapi-demo --name fastapi-service --type "Load Balanced Web Service" --dockerfile ./Dockerfile
   copilot env init --name test --profile default --app fastapi-demo
   copilot deploy --name fastapi-service --env test
   ```

4. To update the service after changes:
   ```
   copilot deploy --name fastapi-service --env test
   ```

## API Endpoints

- `GET /`: Welcome message
- `GET /health`: Health check endpoint
- `POST /items/`: Create a new item
- `GET /items/`: List all items
- `GET /items/{item_id}`: Get a specific item
- `PUT /items/{item_id}`: Update an item
- `DELETE /items/{item_id}`: Delete an item
