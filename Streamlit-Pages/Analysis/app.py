import streamlit as st
from huggingface_hub import Repository
import pandas as pd
import os

col1, col2 = st.columns(2)

with col1:
    teacher_code = st.text_input("Ogretmen kodu:",key=12)
with col2:
    exam_code = st.text_input("Sınav Kodu:",key=13,value=10)


exam_code = int(exam_code)
teacher_code = str(teacher_code)
DATA_FILENAME = f"{teacher_code}.csv"
DATA_FILENAME = str(DATA_FILENAME)

DATASET_REPO_URL = "https://huggingface.co/datasets/mertbozkurt/school_data"
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
#@st.cache

def convert_df_to_csv(df):
  return df.to_csv().encode('utf-8')


def screen_analysis_main():
    
    if st.button("Ogretmen koduna gore oku",key=26):
        try:
            repo, repo_df = pull_read()
            repo.git_pull()
            filtered_df = repo_df[(repo_df['sinav_kodu'] == exam_code)]#& (repo_df['not'] > 70)
            
            st.dataframe(filtered_df)
     
            st.download_button(label="Yukaridaki CSV Dosyasini indir",data=convert_df_to_csv(filtered_df),
                               file_name='result.csv',mime='text/csv',)   
            filtered_df["notu"] = filtered_df["notu"].astype(int)
            not_ortalamasi = filtered_df["notu"].mean()
            
            st.write("Sinifin not ortalamasi:",not_ortalamasi)
            numbers_list = filtered_df['yanlis_sorulari'].str.split(',', expand=True).stack().reset_index(drop=True)
            numbers_list = numbers_list.astype(int)
            freq = numbers_list.value_counts()
            freq = freq.sort_index()
            
            list1= []
            list2= []
            for i in range(1,21):
                try:
                    list1.append(i)
                    list2.append([freq[i]])
                except KeyError:
                    
                    list2.append(0)
           
            dict_data = {}
            for i in range(len(list1)):
                dict_data[list1[i]] = list2[i]

            df = pd.DataFrame(dict_data)
            
            st.subheader("Yanlis yapilan sorularin grafkisel gosterimi")
            st.bar_chart(df.T,width=0)
                  
        except FileNotFoundError :
            st.write("Yanlis ogretmen kodu")
        
#python -m streamlit run app.py
if __name__ == "__main__":
    screen_analysis_main()
