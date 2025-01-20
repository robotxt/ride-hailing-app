# Ride Hailing


## Requirements:

**Python:** ^3.10

**Django:** 5.1.5

**Docker**

**Poetry**: Dependency Management Tool ([https://python-poetry.org/docs/](https://python-poetry.org/docs/))

**PostGIS**: Geographic object support for PostgreSQL ([https://docs.djangoproject.com/en/5.1/ref/contrib/gis/install/postgis/](https://docs.djangoproject.com/en/5.1/ref/contrib/gis/install/postgis/))


## Development

Copy .env.template to .env

```bash
cp .env.template .env
```

Run docker compose

```docker
docker-compose up --build
```

Open: [http://localhost:8000](http://localhost:8000)

## Create test data
This will create users (admin, rider, driver). This also create a data for Ride and Ride Event. Ride latitude and longitude are base in US

#### Using makefile

```makefile
make seed
```

#### Using manage command 

```python
python wingz/manage.py seed
```


## API Endpoints

### Login API
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
Login will return Token to be used in Header.


### Ride API

Requires authentication token in header:
```
{
    "Authorization": "Token <token>"
}
```

#### Endpoints:

Retrieve all rides
```
GET: http://localhost:8000/api/v1/ride/
```

Retrieve all with pagination
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

