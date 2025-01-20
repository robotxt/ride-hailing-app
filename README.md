# Ride Hailing


## Requirements:

**Python:** ^3.11

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

## Run test

```makefile
make test
```

## Run lint

```makefile
make lint
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

## SQL Statement for the report
This is extracted from a django query.
```
SELECT 
    (EXTRACT(YEAR FROM "app_rideevent"."created_at" AT TIME ZONE 'UTC')::varchar || 
     '-' || 
     EXTRACT(MONTH FROM "app_rideevent"."created_at" AT TIME ZONE 'UTC')::varchar) AS "date",
    (COALESCE("app_user"."first_name", '') || ' ' || COALESCE("app_user"."last_name", '')) AS "driver",
    COUNT("app_rideevent"."ride_id") AS "trip_count"
FROM "app_rideevent"
INNER JOIN "app_ride" 
    ON "app_rideevent"."ride_id" = "app_ride"."id"
INNER JOIN "app_user" 
    ON "app_ride"."driver_id" = "app_user"."id"
WHERE 
    "app_rideevent"."description" = 'Status changed to pickup'
    AND (
        (SELECT U0."created_at" 
         FROM "app_rideevent" U0 
         INNER JOIN "app_ride" U1 
             ON U0."ride_id" = U1."id"
         WHERE 
             U0."description" = 'Status changed to dropoff' 
             AND U1."driver_id" = "app_ride"."driver_id"
             AND U0."ride_id" = "app_rideevent"."ride_id"
         LIMIT 1
        ) - "app_rideevent"."created_at"
    ) > INTERVAL '1 hour'
GROUP BY 
    EXTRACT(YEAR FROM "app_rideevent"."created_at" AT TIME ZONE 'UTC'),
    EXTRACT(MONTH FROM "app_rideevent"."created_at" AT TIME ZONE 'UTC'),
    "app_ride"."driver_id",
    "app_user"."first_name",
    "app_user"."last_name"
ORDER BY 
    EXTRACT(MONTH FROM "app_rideevent"."created_at" AT TIME ZONE 'UTC') ASC, 
    "app_ride"."driver_id" ASC;
```