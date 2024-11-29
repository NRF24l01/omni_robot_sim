from requests import post, get
from json import dumps, loads
from logger import Logger


class Uploader:
    def __init__(self, logger: Logger, host: str="localhost", port: int=4040):
        self.logger = logger
        self.host = host
        self.port = port
        
        self.path = None
        self.filename = None
    
    def set_path(self, path):
        self.path = path
    
    def set_host(self, host: str):
        po = host.split(":")
        if len(po) == 1:
            self.host = po[0]
            self.port = 4040
        else:
            self.host = po[0]
            self.port = po[1]
    
    def test_connection(self) -> bool:
        request = get(f"{self.host}:{self.port}/api/get_ok")
        
        if request.status_code != 200:
            return False
        else: 
            if request.json["result"] == "ok":
                return True
            else:
                raise NotImplementedError

    def _generate_request_body(self):
        if self.path and self.filename:
            request = {}
            request["path"] = self.path
            request["filename"] = self.filename
            return request
        else:
            return False
    
    def is_name_avalible(self, name):
        request = get(f"{self.host}:{self.port}/api/is_name_avalible", params={"name": name})
        
        if request.status_code == 200:
            return request.json["result"]["is_avalible"]
        else:
            return False
        