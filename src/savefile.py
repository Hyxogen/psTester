import json
from typing import List, Union

from testresult import TestResult


def parse_run(run: dict):
    ret = []
    for (key, val) in run.items():
        low = int(key.split("-")[0])
        hi = int(key.split("-")[1])
        ret.append(TestResult(range(low, hi), val['results'], val['success_count']))
    return ret


def create_entry(result: TestResult) -> dict:
    return {"results": result.results, "success_count": result.success_count}


def get_range_str(num_range: range) -> str:
    return "{}-{}".format(num_range.start, num_range.stop)

class SaveFile:
    def __init__(self, path: str):
        self.path = path
        self.jsonobj = json.load(open(path, 'r'))

    def get_range_info(self, num_range: range) -> Union[dict, None]:
        name = get_range_str(num_range)
        if name in self.jsonobj:
            return self.jsonobj[name]
        return None

    def get_range_entries(self, num_range: range) -> Union[dict, None]:
        range_info = self.get_range_info(num_range)
        if not range_info:
            return None
        return range_info["entries"]

    def get_best_index(self, num_range: range) -> int:
        range_inf = self.get_range_info(num_range)
        if not range_inf:
            return -1
        return int(range_inf["best"])

    def get_best_entry(self, num_range: range) -> Union[dict, None]:
        best_index = self.get_best_index(num_range)
        if best_index == -1:
            return None
        entries = self.get_range_entries(num_range)
        return entries[best_index]

    def get_best(self, num_range: range) -> Union[TestResult, None]:
        best_entry = self.get_best_entry(num_range)
        if not best_entry:
            return None
        return TestResult(num_range, best_entry["results"], best_entry["success_count"])

    def create_and_add_range(self, num_range: range) -> dict:
        range_info = {
            "best": -1,
            "count": -1,
            "entries": []
        }
        self.jsonobj[get_range_str(num_range)] = range_info
        return range_info

    def add_result(self, result: TestResult, new_best: bool = False):
        range_info = self.get_range_info(result.num_range)
        if not range_info:
            range_info = self.create_and_add_range(result.num_range)
        count = range_info["count"]
        entry = create_entry(result)
        range_info["entries"].append(entry)
        if new_best:
            range_info["best"] = count + 1;
        range_info["count"] += 1

    def save_file(self):
        file = open(self.path, "w")
        file.write(json.dumps(self.jsonobj))
