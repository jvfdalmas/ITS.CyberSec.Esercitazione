from multiprocessing import Process
import time

def sleepy():

    print("sono nella funzione")
    time.sleep(1)
    print("sto uscento dalla funzione")



# if __name__ == "__main__":
#     tic = time.time()

#     sleepy()
#     target=sleepy()
    
#     toc = time.time()

#     time_elapsed = toc - tic
#     print(f"{time_elapsed=}")



# if __name__ == "__main__":
#     tic = time.time()

#     t1 = Process(target=sleepy())
#     t2 = Process(target=sleepy())
#     t1.start()
#     t2.start()
    
#     toc = time.time()

#     time_elapsed = toc - tic
#     print(f"{time_elapsed=}")



if __name__ == "__main__":
    tic = time.time()

    t1 = Process(target=sleepy())
    t2 = Process(target=sleepy())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    toc = time.time()

    time_elapsed = toc - tic
    print(f"{time_elapsed=}")