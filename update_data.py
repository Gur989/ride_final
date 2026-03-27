from feature_engineering import process_data

def run_pipeline():
    file_path = "data/new_rider_share10.csv"

    print("Running automation...")

    process_data(file_path)

    print("Data updated successfully!")

if __name__ == "__main__":
    run_pipeline()
