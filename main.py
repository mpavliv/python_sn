import watchdog.events
import watchdog.observers
import time
import server
import read_from_1c as rfc


class Handler(watchdog.events.PatternMatchingEventHandler):
	def __init__(self):
		# Set the patterns for PatternMatchingEventHandler
		watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['SC16112.dbf'],
															ignore_directories=True, case_sensitive=False)

	def on_modified(self, event):
		print("Watchdog received modified event - % s." % event.src_path)
		data = rfc.read_data()
		server.send_request(data)
		# Event is modified, you can process it now


if __name__ == "__main__":
	src_path = "D:/Base1C/"
	event_handler = Handler()
	observer = watchdog.observers.Observer()
	observer.schedule(event_handler, path=src_path, recursive=True)
	observer.start()
	try:
		while True:
			time.sleep(10000)
	except KeyboardInterrupt:
		observer.stop()
	observer.join()
