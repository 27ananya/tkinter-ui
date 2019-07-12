import json
class Copy:
    def __init__(self,filename):
        file=open(filename,"r")
        self.data=json.load(file)
    def get_data(self):
        list1=[]
        for x in self.data["category_data"]:
            list1.append(x["name"])
        return list1
    def get_category(self,name):
        list1=[]
        for a in self.data["category_data"]:
            if a ["name"].lower()==name.lower():
                list1=a["list"]
        return list1


