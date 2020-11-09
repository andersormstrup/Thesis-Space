def on_created(self, event):
    file_size = -1
    while file_size != os.path.getsize(event.src_path):
        file_size = os.path.getsize(event.src_path)
        time.sleep(1)

    self.process(event)