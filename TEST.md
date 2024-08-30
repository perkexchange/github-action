# Local testing

## Build the container

```
docker build --tag ga-docker .`
```

## Run the container

```
docker run --net="host" --env-file test.env ga-docker
```

### Sample environment file

```
INPUT_APITOKEN=XXXXXXXXXXXX
INPUT_ORDERID=
INPUT_CURRENCY=USD
INPUT_AMOUNT=1.25
INPUT_SERVER=https://perk.exchange
```
