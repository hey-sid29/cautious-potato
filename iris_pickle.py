from logging import exception
import pickle
import requests
class Pickling_Iris:
    def download_iris(url):
        my_file="Iris_copy.data"
        file=open(my_file,"w")
        try:
            req=requests.get(url=url)
            print(req.status_code)
        except exception as e:
            print(e)
        file.write(req.text)
        file.close()
    def pickling_iris(file):
        f=open(file)
        iris_file=f.read()
        iris_list=iris_file.split("\n")
        list_of_list=[]
        for items in iris_list:
            iris_list2=items.split(",")
            list_of_list.append(iris_list2)


        file_pkl="Iris.pkl"
        fileobj=open(file_pkl,"wb")
        pickle.dump(list_of_list,fileobj)
    def unpickling_iris():
        file_pkl="Iris.pkl"
        file_obj=open(file_pkl,"rb")
        iris_data=pickle.load(file_obj)
        print(iris_data)
    if __name__=='__main__':
        url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
        download_iris(url)
        pickling_iris("Iris_copy.data")
        unpickling_iris()
