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
