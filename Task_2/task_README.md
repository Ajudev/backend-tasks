# Libraries and Services use test

## Proposed Architecture

- The proposed architecture involves using redis for caching data, flask for creating api service, MySQL database for storing order data.

- Flask service will expose a GET method api endpoint which will allow users to fetch order data from MySQL DB. The api endpoint will return back a paginated response to reduce response time. Each api call will return back with 10 order entries in the response.

- The api service will initially hit the redis cache to check if the api response has been cached earlier. If the response has been cached the api will fetch the data stored in the redis cache. Otherwise it will fetch the data from the DB and cache the response for the page the user is requesting for.

- API response will be cached for 1 hour but this duration can be changed as per the business requirement. This will ensure that we don't store a lot of data in redis memory. We can also modify what needs to be stored in cache as per business requirement.

- Caching data will help in serving customers data quickly since we don't have to query the db everytime a request is being made by a customer to view order data.

- I have used redis since redis is an in memory cache server which will store the response within the servers RAM. This ensures that the application using redis will have exceptional performance for read and write operations.

- Redis can serve frequently requested items at sub-millisecond response times, and allows to easily scale for higher loads without growing the costlier backend.

## Code Setup

- Please ensure you have docker installed and docker-compose plugin installed as well to run the application.
- Execute run.sh file when you have made sure the above dependencies are installed in your system.
- After executing the run.sh file you can use the following link to access the 99th page of orders data
  - ` http://localhost:5001/orders/99`

## Future Enhancements

- I have not handled a scenario where we expire the cache if there is any modification to the database due to time constraints. This is something I can work on if I get more time.
