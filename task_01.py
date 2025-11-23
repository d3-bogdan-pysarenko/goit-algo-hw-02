import time
from queue import Queue


class MyRequestProcesor:
    def __init__(self):
        self.queue = Queue()
        self.request_id = 0

    def generate_request(self):
        """Generates new request and adds it to the queue"""
        self.request_id += 1
        request = f"Request #{self.request_id}"
        print(f"[CREATE] Created: {request}")
        self.queue.put(request)

    def process_request(self):
        """Processes the request if it is inthe queue"""
        if not self.queue.empty():
            request = self.queue.get()
            print(f"[PROCESS] Processing: {request}")
            time.sleep(0.5)  # processing imitation
        else:
            print("[INFO] Queue is empty — there is nothing to process")


def main():
    processor = MyRequestProcesor()

    print("Requests processing system is launched and working! Press 'Ctrl+C' to exit\n")

    try:
        while True:
            processor.generate_request()
            processor.process_request()
            time.sleep(1)   # waiting between cycles
    except KeyboardInterrupt:
        print("\nSystem is stopped by user!")


if __name__ == "__main__":
    main()
