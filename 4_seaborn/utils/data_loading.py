def load_dataset(dataset_name):
    import seaborn as sns
    import pandas as pd

    if dataset_name not in sns.get_dataset_names():
        raise ValueError(f"Dataset '{dataset_name}' not found in seaborn's dataset library.")

    return sns.load_dataset(dataset_name)

def load_csv(file_path):
    import pandas as pd

    return pd.read_csv(file_path)

def load_excel(file_path):
    import pandas as pd

    return pd.read_excel(file_path)

def load_json(file_path):
    import pandas as pd

    return pd.read_json(file_path)