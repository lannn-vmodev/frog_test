import time
from dataclasses import dataclass
from typing import List

from flask import Flask
from flask_pydantic import validate
from pydantic import BaseModel

app = Flask(__name__)


@dataclass
class Config:
    FLASK_PYDANTIC_VALIDATION_ERROR_STATUS_CODE: int = 422


app.config.from_object(Config)

# validate the data type using pydantic

class RequestBodyModel(BaseModel):
    leaves_pos: List[int]
    river_size: int


class ResponseModel(BaseModel):
    time_to_jump: int
    message: str


def convert_list_to_dictionary(leaves_pos: list):
    ''' 
    convert list to dictionary, get only min value  ( time ) in each position ( key ), 
    and return max value ( Latest leaf fall time ) in this time list.
    '''
    data = {}
    last_pos_time = 0
    for f_time, pos in enumerate(leaves_pos):
        cur_min_time = data.get(pos, None)
        if not cur_min_time or f_time < cur_min_time:
            data[pos] = f_time
            if f_time > last_pos_time:
                last_pos_time = f_time
    return data, last_pos_time


@app.route('/', methods=["POST"])
@validate()
def solution(body: RequestBodyModel):
    start_time = time.time()
    leaves_pos = body.leaves_pos
    river_size = body.river_size
    # validate the data value
    if len(leaves_pos) < 1 or len(leaves_pos) > 100000 or river_size > 100000 or river_size < 1:
        return ResponseModel(time_to_jump=-1, message="The value mush in range 1 to 100000"), 400
    if river_size > len(leaves_pos):
        return ResponseModel(time_to_jump=-1, message="The frog can't jump to another river side")
    
    data, time_to_jump = convert_list_to_dictionary(leaves_pos)
    
    if len(data) < river_size:
        time_to_jump = -1
        message = "The frog can't jump to another river side"
    else:
        message = f"The frog can start to jump at {time_to_jump} seconds"
        
    print('time', time.time() - start_time)
    return ResponseModel(time_to_jump=time_to_jump, message=message)


if __name__ == '__main__':
    app.run()
