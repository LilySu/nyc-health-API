## API for accessing Covid-19 Data from NYC Health 

### Usage
All responses will have the form

```
{
    "data": "Mixed type holding the content of the response",
    "message": "Description"
}
```

Subsequent response definitions will only detail the expected value of 
the data field

##### List all devices
###### Definition

`GET /devices`

###### Response

* `200 OK` on success

```
[
    {
        "identifier": "boro",
        "header_name": "AGE_GROUP",
    },
    {
        "identifier": "by-age",
        "header_name": "COVID_CASE_RATE",
    }
]
```

##### Registering a new device
###### Definition

`POST /devices`

###### Arguments

* `"identifier":string` a globally unique identifier for this device
* `"name":string `a friendly name for this device
* `"controller_gateway":string` the IP address of the device's controller
If a device with the given identifier already exists, the existing 
device will be overwritten.

###### Response

* `201 Created` on success
```
{
        "identifier": "by-age",
        "header_name": "COVID_CASE_RATE",
}
```
* Lookup details
`GET /feature/<identifier>`

###### Response

* `404 Not Found` if the device does not exist
* `200 OK` on success
```
{
        "identifier": "by-age",
        "header_name": "COVID_CASE_RATE",
}
```