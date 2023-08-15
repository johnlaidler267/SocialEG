import time
import sys
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def __init__(self, script_to_run):
        self.script_to_run = "gui.py"
        self.process = None

    def on_any_event(self, event):
        if event.is_directory:
            return

        self.restart_script()

    def restart_script(self):
        print("Restarting script... {}".format(self.script_to_run))
        if self.process:
            self.process.kill()
            self.process.wait()

        self.process = subprocess.Popen(["python3", self.script_to_run])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python watch_and_restart.py <script_to_watch>")
        sys.exit(1)

    script_to_watch = sys.argv[1]
    event_handler = MyHandler(script_to_watch)

    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=False)
    observer.start()

    print(f"Watching {script_to_watch} for changes...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
