# Frog Jump


## Description
    Help the frog get to the other side of a river.

### Installing

```
pip install -r requirement.txt

```

### Executing program


```
    export FLASK_APP=app
    flask run
```

## Docker Run


```
   docker build -t frog_flask .
```

```
   docker-compose up
```

## HOW IT WORK
* Get a list from post method body, then validate datatype of it.
* Validate range of value from 1 to 100000
* If len of leaves array < river size, the frog can't jump to another river side
* Convert list to dictionary, get only min value  ( time ) in each position ( key ), 
and return max value ( Latest leaf fall time ) in this time list.
* The keys list of result dictionary is the leaves positions in the river, if it not equal the riversize, the frog can't jump to another river side
* If the number of keys in dictionary equal riverside, then get the max value. It the time when latest leaf  falls.

## Using API Post
```
curl --location --request POST 'http://localhost:5000/' \
--header 'Content-Type: application/json' \
--data-raw '{
            "leaves_pos": [5, 4, 4, 7, 4, 1, 9, 1, 1, 5, 6, 2, 7, 10, 2, 8, 7, 8, 7, 8, 6, 6, 9, 4, 8, 2, 8, 9, 7, 6, 9,
                           4, 6, 3, 10, 9, 7, 2, 7, 2, 5, 7, 6, 9, 5, 1, 10, 4, 9, 3, 3, 10, 8, 6, 1, 9, 8, 3, 7, 10,
                           10, 2, 8, 10, 9, 1, 2, 7, 6, 8, 3, 7, 3, 10, 2, 5, 1, 5, 7, 6, 4, 4, 4, 1, 6, 6, 6, 1, 3, 5,
                           1, 4, 8, 6, 7, 3, 4, 1, 7, 3],
            "river_size": 10
        }'
```

* sample response
```
{
    "time_to_jump": 33,
    "message": "The frog can start to jump at 33 seconds"
}
```
