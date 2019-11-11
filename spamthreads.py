from threading import Thread
from time import sleep

# BOTH classes SpamThread and SpamThreadsDaddy are threads,
# AND SpamThread is created to hold list of SpamThread objects


class SpamThread(Thread):
    def __init__(self, phone, client, spam_iterations=1):
        Thread.__init__(self)
        self.phone = phone
        self.spam_iterations = spam_iterations
        self.client = client
        self.spam_on = True

    def run(self):
        self.spam_on = True
        from time import sleep

        for i in range(self.spam_iterations):
            if not self.spam_on:
                break
            print('spam {} {}'.format(i, self.phone))
            sleep(1)

        self.spam_on = False


class SpamThreadsDaddy(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.spam_threads = []

    def add_thread(self, thread):
        self.spam_threads.append(thread)

    def run(self):
        while True:
            stopped_threads = filter(lambda x: not x.spam_on, self.spam_threads)
            for stopped in stopped_threads:
                print(stopped.spam_on)
                print('removed stopped thread')
                self.spam_threads.remove(stopped)
            sleep(1)

    def is_spamming(self, client, phone):
        spamming = False
        for thr in self.spam_threads:
            if thr.client == client and thr.phone == phone:
                spamming = True
        return spamming

    def stop_spam(self, client):
        for thr in self.spam_threads:
            if thr.client == client:
                thr.spam_on = False
