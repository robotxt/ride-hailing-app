# Ride Hailing

### Create environment variables:

Copy .env.template to .env

```bash
cp .env.template .env
```

### Run docker compose

```docker
docker-compose up --build
```

### Create test data
This will create users (admin, rider, driver). This also create a data for Ride and Ride Event. Ride latitude and longitude are base in US

#### Using makefile

```makefile
make seed
```

#### Using manage command 

```python
python wingz/manage.py seed
```


### API Endpoints

#### List of Events API
```
POST: http://localhost:8000/api/v1/login/
```
Payload:
```
{
    "email": "admin@example.com",
    "password": "Password101"
}
```

#### Ride API
Retrieve all rides
```
GET: http://localhost:8000/api/v1/ride/
```

Retrieve all paginate
```
GET: http://localhost:8000/api/v1/ride/?page=2
```

Sort Rides by pickup_time
```
GET: http://localhost:8000/api/v1/ride/?sort-pickup-time=asc
```

Sort Rides by distance
```
GET: http://localhost:8000/api/v1/ride/?latitude=41.84364&longitude=-87.71255
```

