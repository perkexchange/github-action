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
INPUT_CAMPAIGNSECRET=XXXXXXXXXXXX
INPUT_USERID=131
INPUT_PLATFORM=twitter
INPUT_AMOUNT=1
INPUT_SERVER=https://perk.exchange
```
