from time import time
from multiprocessing import Pool

def factorize(*numbers) -> list:
    try:
        dividers=[[divider for divider in range(1, number + 1)
                if number % divider == 0] for number in numbers]
        # print(dividers)
        return dividers
    except NotImplementedError: 
        raise NotImplementedError()


if __name__ == '__main__':
    number_list = [128, 255, 99999, 10651060]
    process_counter = 1
    
    while process_counter < 5:
        start = time()
        print(start)

        with Pool(processes = process_counter) as pool:
            pool.map_async(factorize, number_list)
            pool.close()
            pool.join()

        process_counter += 1
        print(process_counter)

        finish = time()

        print("Time:", finish - start)

    a, b, c, d  = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
