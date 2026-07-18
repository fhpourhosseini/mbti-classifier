from pipeline.pipeline import Pipeline

def main():
    data = Pipeline("data/16P.csv").run()
    return data

if __name__=="__main__":
    result = main()
    print(f"Pipeline completed: {len(result)} records processed")