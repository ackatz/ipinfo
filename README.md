[![Deploy to Fly](https://github.com/ackatz/ipinfo/actions/workflows/cd.yaml/badge.svg)](https://github.com/ackatz/ipinfo/actions/workflows/cd.yaml)

# ipinfo

Tiny FastAPI app for getting your ip / country / city info

https://ipinfo.fly.dev

Example `curl`:

```
curl ipinfo.fly.dev
```

Example Response

```
{"client":{"ip":"1.2.3.4","port":48212,"location":{"country":"United States","city":"Los Angeles","latitude":69.6907,"longitude":-420.8173}}}
```
