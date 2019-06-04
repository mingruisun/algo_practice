import time

class program_run_time():

    def __init__(self):
        self.start_time = 0

    def reset_start_time(self):
        self.start_time = time.time()

    def report_total_runtime(self, label):
        runtime = round(time.time() - self.start_time, 7)
        print("Total run time of {} is {}".format(label, runtime))


if __name__ == "__main__":
    logging_time = program_run_time()
    logging_time.reset_start_time()
    logging_time.report_total_runtime("test")