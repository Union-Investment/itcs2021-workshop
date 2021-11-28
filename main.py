from fastapi import FastAPI, HTTPException
from typing import Optional
from csv import reader


app = FastAPI()

indices = []


@app.get("/indices/{date}")
async def read_item(date: str, index: str = "DAX", show_all_indices: Optional[bool] = False):
  if date not in fake_items_db:
        raise HTTPException(status_code=404, detail="Date not found")
  else:
    result = {"date": date}
    if show_all_indices:
      for i in indices:
        result.update({i: fake_items_db[date][i]})
    else:
      result.update({index: fake_items_db[date][index]})
    return result
# get method to specific filters

@app.post("/post")
async def add_entry(date: str, dax: int, sp500: int):
  fake_items_db.update({date : {"DAX" : dax, "SP500" : sp500}})
  return {date: fake_items_db[date]}
  # upload new csv => update dictionary

def add_entries_to_dict(fake_items_db, filename):
  file = open('./' + filename, encoding='UTF8')
  csv_reader = reader(file)

  for line_no, line in enumerate(csv_reader, 0):
    if (line_no == 0):
      new_indices = line[1:]
      for index in new_indices:
        indices.append(index) if index not in indices else indices
        #todo: check order of line[0] and indices
    else:
      fake_items_db.update({line[0]: {}})
      for index_no, index in enumerate(indices, 0):
        fake_items_db[line[0]].update({index: line[index_no + 1]})

  file.close()

  return fake_items_db

fake_items_db = dict()
fake_items_db = add_entries_to_dict(fake_items_db=fake_items_db, filename="indices.csv")
