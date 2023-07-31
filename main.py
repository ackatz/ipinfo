from fastapi import FastAPI, Request
import geoip2.database

app = FastAPI(redoc_url=None, docs_url=None, openapi_url=None)
reader = None

@app.on_event("startup")
async def startup_event():
    global reader
    reader = geoip2.database.Reader('/app/GeoLite2-City.mmdb')  # adjust this path to your database file

@app.on_event("shutdown")
async def shutdown_event():
    global reader
    if reader is not None:
        reader.close()

@app.get("/")
async def get_request_info(request: Request):

    try:

        x_forwarded_for = request.headers.get("X-Forwarded-For")
        if x_forwarded_for:
            # Take the first IP from X-Forwarded-For, which is the original client IP
            ip_address = x_forwarded_for.split(",")[0]
        else:
            ip_address = request.client.host
        response = reader.city(ip_address)
        return {
            "client": {
                "ip": ip_address,
                "port": request.client.port,
                "location": {
                    "country": response.country.name,
                    "city": response.city.name,
                    "latitude": response.location.latitude,
                    "longitude": response.location.longitude,
                }
            }
        }

    except geoip2.errors.AddressNotFoundError:
        return {"error": f"{ip_address} Address not found"}

    except Exception as e:
        return {"error": "Invalid request"}
