import concurrent.futures
import requests
import multiprocessing

def downloadFile(url, name):
  print(f"Started Downloading {name}")
  response = requests.get(url)
  open(f"files/file{name}.jpg", "wb").write(response.content)
  print(f"Finished Downloading {name}")
 


url = "https://picsum.photos/2000/3000"

if __name__ == '__main__':

    for i in range(5):
        downloadFile(url, i)
        p = multiprocessing.Process(target=downloadFile, args=[url, i])
        p.start()
       
       


# with concurrent.futures.ProcessPoolExecutor() as executor:
#   l1 = [url for i in range(60)]
#   l2 = [i for i in range(60)]
#   results = executor.map(downloadFile, l1, l2)
#   for r in results:
#     print(r)