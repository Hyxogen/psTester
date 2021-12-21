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


class SaveFile:
    def __init__(self, path: str):
        self.path = path
        self.jsonobj = json.load(open(path, 'r'))

    def set_best_run(self, index: int):
        self.jsonobj['best'] = index

    def get_best_run_index(self) -> int:
        return self.jsonobj['best']

    def get_best_run(self) -> Union[List[TestResult], None]:
        best_index = self.get_best_run_index()
        if best_index == -1:
            return None
        return parse_run(self.jsonobj["{}".format(best_index)])

    def get_count(self) -> int:
        return self.jsonobj['count']

    def add_test_result(self, index: int, result: TestResult):
        x = {"results": result.results, "success_count": result.success_count}
        obj = self.jsonobj["{}".format(index)]
        lo = result.num_range.start
        hi = result.num_range.stop
        obj["{}-{}".format(lo, hi)] = x

    def add_run(self, run: List[TestResult]):
        count = self.get_count()
        for result in run:
            self.add_test_result(count + 1, result)
        self.jsonobj["count"] = count + 1

    def save_file(self):
        file = open(self.path, "w")
        file.write(json.dumps(self.jsonobj))
