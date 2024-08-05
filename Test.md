#Binning API to render to render range buckets and color using a binning algorithm using size dynamically

#Install flask dependencies
> pip3 install -r requirements.txt

> cd BinningAPI

> python3 src/app.py

# API usage

curl -X GET 'http://localhost:5000/binning?bin_size=5&min_val=0&max_val=10000'


# Success Response
{
  "buckets_color": [200, 400, 600, 800, 1000],
  "range_buckets": [
    [1, 2000],
    [2001, 4000],
    [4001, 6000],
    [6001, 8000],
    [8001, 10000]
  ]
}

# Error Response

{
  "error": "min_val must be less than max_val"
}
