import os
from huggingface_hub import Repository
import pandas as pd

DATASET_REPO_URL = "https://huggingface.co/datasets/mertbozkurt/school_data"
DATA_FILENAME = "untitled.csv"
DATA_FILE = os.path.join("data", DATA_FILENAME)
HF_TOKEN = "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"

def pull_read():
    
    repo = Repository(
        local_dir="data", clone_from=DATASET_REPO_URL, use_auth_token=HF_TOKEN
        )
    
    with open(DATA_FILE) as csvfile:
        df = pd.read_csv(csvfile) 
        df = pd.DataFrame(df)
    
    return repo, df

#sinav_kodu,ogrenci_no,notu1,yanlis_sorulari1,notu2,yanlis_sorulari2,notu3,yanlis_sorulari3
def make_new_data(sinav_kodu,ogrenci_no,notu1,yanlis_sorulari1,notu2,yanlis_sorulari2,notu3,yanlis_sorulari3):
    yeni_satir = {"sinav_kodu": sinav_kodu, 
              "ogrenci_no": ogrenci_no, 
              "notu1": notu1, 
             "yanlis_sorulari1": yanlis_sorulari1,
             "notu2": notu2, 
             "yanlis_sorulari2": yanlis_sorulari2,
             "notu3": notu3, 
             "yanlis_sorulari3": yanlis_sorulari3,
             }
    new_data = pd.DataFrame([yeni_satir])
    return new_data
    
def update(new_data, ex_df):
    updated_df = pd.concat([ex_df, new_data])
    return updated_df
    
def save_and_push(dataFrame,repo,fileName):
    dataFrame.to_csv(fileName,index=False)
    commit_url = repo.push_to_hub()
    return commit_url

"""repo, repo_df = pull_read()
new_data = make_new_data(12,151718,56,80,"2,3,5")
updated_df = update(new_data,repo_df)
save_and_push(updated_df,repo)"""