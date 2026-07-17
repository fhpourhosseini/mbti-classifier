from pipeline.extract import extract

class Pipeline:
    def __init__(self, filepath):
        self.filepath = filepath

    def run(self):
        return list(extract(self.filepath))
    
    def __repr__(self):
        return f"Pipeline(filepath={self.filepath})"
    
        