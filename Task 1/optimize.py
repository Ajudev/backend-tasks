from datetime import datetime, timedelta
import time
import uuid
import random
from concurrent import futures
from collections import deque


class OrdersManager:
    __orders = deque()
    __orders_processed = 0
    __last_printed_log = datetime.now()

    def __init__(self) -> None:
        self.__generate_fake_orders(quantity=1_000)

    def __generate_fake_orders(self, quantity):
        self.__orders = deque(maxlen=quantity)
        self.__log(f"Generating fake orders")

        for x in range(quantity):
            self.__orders.append((uuid.uuid4(), x))
        self.__log(f"{self.__orders.maxlen} generated...")

    def __log(self, message):
        print(f"{datetime.now()} > {message}")

    def __fake_save_on_db(self, order):
        id, number = order

        self.__log(
            message=f"Order [{id}] {number} was successfully prosecuted."
        )
        self.__orders_processed += 1
        if datetime.now() > self.__last_printed_log:
            self.__last_printed_log = datetime.now() + timedelta(microseconds=1000)
            self.__log(
                message=f"Total orders executed: {self.__orders_processed}/{self.__orders.maxlen}"
            )
        time.sleep(random.uniform(0, 1))

    def process_orders(self):
        with futures.ThreadPoolExecutor(max_workers=1000) as executor:
            executor.map(self.__fake_save_on_db, self.__orders)


#
#
# ---
orders_manager = OrdersManager()

start_time = time.perf_counter()

orders_manager.process_orders()

delay = time.perf_counter() - start_time

print(f"{datetime.now()} > Execution Time: {delay} seconds...")