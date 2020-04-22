## API for accessing Covid-19 Data from NYC Health 

<p align="center">
  <img width="360" height="200" src="https://i.imgur.com/8QizuMn.png">
</p>

### Usage
* Each .csv file in https://github.com/nychealth/coronavirus-data exists as the same name in a route.
* ie. boro.csv exists as /boro
* If the value is 0, it might be because it was a NaN/Null

### Routes
* `/boro`
* `/by-age`
* `/by-sex`
* `/case-hosp-death`
* `/probable-confirmed-dod`
* `/summary`
* `/tests-by-zcta`

#### Display boro
##### Definition

`GET /boro`

##### Response
```
[
{
BOROUGH_GROUP: "The Bronx",
COVID_CASE_COUNT: 31130,
COVID_CASE_RATE: 2115.28
},
{
BOROUGH_GROUP: "Brooklyn",
COVID_CASE_COUNT: 36699,
COVID_CASE_RATE: 1352.06
},
{
BOROUGH_GROUP: "Manhattan",
COVID_CASE_COUNT: 17495,
COVID_CASE_RATE: 927
},
{
BOROUGH_GROUP: "Queens",
COVID_CASE_COUNT: 42637,
COVID_CASE_RATE: 1700.58
},
{
BOROUGH_GROUP: "Staten Island",
COVID_CASE_COUNT: 10405,
COVID_CASE_RATE: 2075.01
},
{
BOROUGH_GROUP: "Citywide",
COVID_CASE_COUNT: 138435,
COVID_CASE_RATE: 0
}
]
```